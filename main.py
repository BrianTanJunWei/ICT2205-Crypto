import hashlib
import random

#takes the nonce, server seed, and client seed as inputs, concatenates them into a string,
# computes an SHA-512 hash and
# returns the resulting digest in hexadecimal format.
def get_nonce(nonce, status):
    if status == True:
        nonce == 0
    else:
        nonce += 1
        status = False

    return nonce, status

def get_roll_hash(nonce, server_seed, client_seed):
    message = str(nonce) + ":" + str(server_seed)
    hmac = hashlib.sha256(message.encode('utf-8'))
    hmac.update(client_seed.encode('utf-8'))
    return hmac.hexdigest()

def get_roll(hash_str): #result
    # takes the first 7
    sub_hash = hash_str[:7]
    #convert them into int & mod them, result to be in 0 to 100%
    num = int(sub_hash, 16)
    roll = (num % 10000)
    return 100.0 if roll == 0 else float(roll) / 100.0

def generate_server_seed(server_seed):
        if server_seed == "GoingToBeChanged":
            server_seed = str(random.getrandbits(512)) #will be hidden from player until he decides to reveal
        server_seed = hashlib.sha256(server_seed.encode('utf-8')).hexdigest()
        return server_seed

def generate_client_seed(client_seed, changeSeed):
    if changeSeed == "No need change":
        if client_seed == "GoingToBeChanged":
            client_seed = str(random.getrandbits(512))
        client_seed = hashlib.sha256(client_seed.encode('utf-8')).hexdigest()
        print("This is the client seed: " + client_seed)
        changeSeed = "Wait Until User Change"
    return client_seed, changeSeed

def get_roll_and_seeds(nonce, server_seed, client_seed):
    hash_str = get_roll_hash(nonce, server_seed, client_seed)
    roll = get_roll(hash_str)

    return roll, server_seed, client_seed

def verify_roll(verifyClientSeed,verifyServerSeed,verifyNonce): #makus implement this plz thanks, let user ownself input all the value
    hash_str = get_roll_hash(verifyNonce, verifyServerSeed, verifyClientSeed)
    result = "ToBeChanged"
    roll = get_roll(hash_str)
    print(f'\nRoll is {roll}')
    if roll <= 50:
        print("The result of the coin flip is heads!")
    if roll > 50:
        print("The result of the coin flip is tails!")