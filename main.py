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
    hmac = hashlib.sha512(message.encode('utf-8'))
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
        print("Server seed: " + server_seed)
        return server_seed

def generate_client_seed(client_seed, changeSeed):
    if changeSeed == "No need change":
        if client_seed == "GoingToBeChanged":
            client_seed = str(random.getrandbits(512))
        changeSeed = "Wait Until User Change"
    elif changeSeed == "User want to change":
        client_seed = input("Enter your client seed: ")

    print(f"Client seed: {client_seed}\n")
    return client_seed, changeSeed

def get_roll_and_seeds(nonce, server_seed, client_seed):
    hash_str = get_roll_hash(nonce, server_seed, client_seed)
    roll = get_roll(hash_str)

    return roll, server_seed, client_seed

def verify_roll(): #makus implement this plz thanks, let user ownself input all the value
    #Download text file containing all results.
    verifyClientSeed = input("Enter Client Seed: ")
    verifyServerSeed = input("Enter Server Seed: ")
    verifyNonce = input("Enter Nonce: ")
    hash_str = get_roll_hash(verifyNonce, verifyServerSeed, verifyClientSeed)
    roll = get_roll(hash_str)
    print(f'\nRoll is {roll}')
    if roll <= 50:
        print("The result of the coin flip is heads!\n")
    if roll > 50:
        print("The result of the coin flip is tails!\n")


#server 7568606721039477025273988730392623903635665727836223611337065207590923632826146818635086846148536304983960786723830486883238254666879353976103064727496648
#client 5495000861733297226453958943252942669778400366030278634093774521290896745526730452504126597379676013244581832661752423153143399549168041323497132898788987
#result 98.01

#only client, nonce & roll is shown to player unless he reveal then we show all



status = True
nonce = 0
changeSeed = "No need change"
client_seed = "GoingToBeChanged"
server_seed = "GoingToBeChanged"
gameOn = True
print("Welcome To Coin Flip!")
print("Heads for rolls <= 50")
print("Tails for rolls > 50\n")
while gameOn:
    print("Enter '1' To Start New Game")
    print("Enter '2' To Verify Roll")
    print("Enter '3' To Change Client Seed")
    print("Enter '4' To End The Program")
    #print("This is changeSeed: " + changeSeed)
    try:
        clientDecision = int(input())
        if clientDecision == 1:
            nonce = get_nonce(nonce, status)[0]
            server_seed = generate_server_seed(server_seed)
            client_seed, changeSeed = generate_client_seed(client_seed, changeSeed)
            roll, server_seed, client_seed = get_roll_and_seeds(nonce, server_seed, client_seed)
            print(f'\nRoll for nonce {nonce} is {roll}')
            status = False
            if roll <= 50:
                print("The result of the coin flip is heads!\n")
            if roll > 50:
                print("The result of the coin flip is tails!\n")
            #Append variables to text file
            # Need to store client seed, server seed, nonce, roll, result.
        elif clientDecision == 2:
            status = True
            #Print text file
            print("We somehow or rather need to print the text file for them")
            verify_roll()
            server_seed = "GoingToBeChanged"
        elif clientDecision == 3:
            changeSeed = "User want to change"
            client_seed = generate_client_seed(client_seed, changeSeed)[0]
            changeSeed = "User has changed"
        elif clientDecision == 4:
            gameOn = False
            #Print text file

    except ValueError:
        print("Invalid input, please enter a number!")
