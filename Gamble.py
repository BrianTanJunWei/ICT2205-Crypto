import hashlib
import random
import main

# # Return user input
#
#
#
#
def server_seed():
    #generate a random sha256 hash each time player rerun the code

    #for testing purpose
    prehashServerseed = "85943002341619080928654322842274335146257750056392232559940811297469147320250" #can either be a fixed hashed value
    print("This is a prehash value: " + prehashServerseed)

    # can be a randomized hashed value or *see line 15
    # prehashServerseed = str(random.getrandbits(256))
    # print("This is a prehash value: " + prehashServerseed)

    #hashed serverseed
    server_seed = hashlib.sha256(prehashServerseed.encode('utf-8')).hexdigest()
    print("This is the server seed: " + server_seed)

    #This part is for user to check if the server seed had been modified, usually users will check the server seed online
    expected_server_seed = hashlib.sha256(prehashServerseed.encode('utf-8')).hexdigest()

    #for testing purpose
    #server_seed = "85943002341619080928654322842274335146257750056392232559940811297469147320250"

    # XOR the prehash and hashedserver to verify if user taper with it, this is best if we implement it online
    if int(server_seed, 16) ^ int(expected_server_seed, 16) != 0:
       print("Seed is tapered with")
    else:
        print("Seed is not tapered with")

    return server_seed
#     #test until here
#
#
# def flip_coin(player_seed, server_seed):
#     # Combine player seed and server seed to generate a unique seed for this round
#     combined_seed = player_seed + server_seed
#
#     # Generate a random number using the unique seed
#     random.seed(combined_seed)
#     rand_num = random.random()
#     print(rand_num)
#     # Determine the result of the coin flip based on the random number
#     result = "heads" if rand_num < 0.5 else "tails"
#
#     # Return the result of the coin flip and the combined seed for verification
#     return result, combined_seed
#
#
# def verify_result(player_seed, server_seed, result, combined_seed):
#
#
#     expected_seed = player_seed + server_seed
#     random.seed(expected_seed)
#     rand_num = random.random()
#
#     # Determine the expected result based on the random number
#     expected_result = "heads" if rand_num < 0.5 else "tails"
#
#     # Verify that the expected result matches the result from flip_coin()
#     if expected_result == result:
#         # Verify that the combined seed matches the expected seed (Player seed + server seed) if both condition are true, return true
#         if combined_seed == expected_seed:
#             return True
#     return False
#
#
# def client_seed():
#     #generate a random sha256 hash each time player rerun the code
#
#     # randomized hashed value
#     #prehashPlayerseed = str(random.getrandbits(256))
#     #print("This is a prehash user seed: " + prehashPlayerseed)
#
#
#     prehashPlayerseed = "d9550b6a19dd31dc774318cb70568d1ff6c0455417aab774ea38632f0448955b" #hard coded player seed
#     #hashed player seed
#     player_seed = hashlib.sha256(prehashPlayerseed.encode('utf-8')).hexdigest()
#     #print("This is the user seed: " + player_seed)
#
#
#     #This part is for user to check if the server seed had been modified, usually users will check the server seed online
#     expected_Player_seed = hashlib.sha256(prehashPlayerseed.encode('utf-8')).hexdigest()
#
#
#     # XOR the prehash and hashedserver to verify if user taper with it, this is best if we implement it online
#     if int(player_seed, 16) ^ int(expected_Player_seed, 16) != 0:
#        print("Player Seed is tapered with")
#     else:
#        print("Player Seed is not tapered with")
#        print(player_seed)
#        return player_seed
#
#
# server_seed = str(server_seed())
# player_seed = str(player_seed())
#
# result, combined_seed= flip_coin(player_seed, server_seed)
# print("Result:", result)
#
# print("Combined seed:", combined_seed)
#
# verified = verify_result(player_seed, server_seed, result, combined_seed)
# print("Result verified:", verified)
#


#make it so that the result will be in hmac-512(player_seed,server_seed + nonce)


# code number 2

import hashlib

def get_roll_hash(nonce, server_seed, client_seed):
    message = str(nonce) + str(server_seed)
    hmac = hashlib.sha512(message.encode('utf-8'))
    hmac.update(client_seed.encode('utf-8'))
    return hmac.hexdigest()

def get_roll(hash_str):
    sub_hash = hash_str[:7]
    num = int(sub_hash, 16)
    if num is None:
        raise ValueError('Invalid hash')
    roll = (num % 100000)
    return 100000 if roll == 0 else roll

def client_seed():
    choice = input("Enter '1' to use your own client seed or any other characters to generate a random one: ")
    if choice == '1':
        user_seed = input("Enter your client seed: ")
        # Hash the user input to generate the client seed
        client_seed = hashlib.sha256(user_seed.encode('utf-8')).hexdigest()
    else:
        # Generate a random client seed
        prehashClientseed = str(random.getrandbits(256))
        client_seed = hashlib.sha256(prehashClientseed.encode('utf-8')).hexdigest()
        print("This is the client seed: " + client_seed)


    return client_seed

nonce = '2'
server_seed = str(server_seed())
client_seed = str(client_seed())

hash_str = get_roll_hash(nonce, server_seed, client_seed)
roll = get_roll(hash_str)

print(f'Roll for nonce {nonce} is {roll}')