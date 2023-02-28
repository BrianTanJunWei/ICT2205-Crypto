import hashlib
import random
import main

# Return user input


def server_seed():
    #generate a random sha256 hash each time player rerun the code

    #can be a randomized hashed value or *see line 15
    # prehashServerseed = str(random.getrandbits(256))
    # print("This is a prehash value: " + prehashServerseed)

    prehashServerseed = "85943002341619080928654322842274335146257750056392232559940811297469147320250" #can either be a fixed hashed value
    print("This is a prehash value: " + prehashServerseed)

    #hashed serverseed
    server_seed = hashlib.sha256(prehashServerseed.encode('utf-8')).hexdigest()
    print("This is the server seed: " + server_seed)


    expected_server_seed = hashlib.sha256(prehashServerseed.encode('utf-8')).hexdigest()

# XOR the prehash and hashedserver to verify if user taper with it
    if int(server_seed, 16) ^ int(expected_server_seed, 16) != 0:
        return False
    else:
        print("Seed is not tapered with")

    #for testing purpose
    server_seed = "85943002341619080928654322842274335146257750056392232559940811297469147320250aa"

    if int(server_seed, 16) ^ int(expected_server_seed, 16) != 0:
        print("WTF BRO?")
    else:
        print("Seed is not tapered with")
    #test until here

def flip_coin(player_seed, server_seed):
    # Combine player seed and server seed to generate a unique seed for this round
    combined_seed = player_seed + server_seed

    # Generate a random number using the unique seed
    random.seed(combined_seed)
    rand_num = random.random()

    # Determine the result of the coin flip based on the random number
    result = "heads" if rand_num < 0.5 else "tails"

    # Return the result of the coin flip and the combined seed for verification
    return result, combined_seed


def verify_result(player_seed, server_seed, result, combined_seed):
    # Combine player seed and server seed to generate the same unique seed used to generate the result
    expected_seed = player_seed + server_seed

    # Generate a random number using the expected seed
    random.seed(expected_seed)
    rand_num = random.random()

    # Determine the expected result based on the random number
    expected_result = "heads" if rand_num < 0.5 else "tails"

    # Verify that the expected result matches the actual result
    if expected_result == result:
        # Verify that the combined seed matches the expected seed
        if combined_seed == expected_seed:
            return True
    return False



player_seed = "mysecretseed"

server_seed = str(server_seed())
result, combined_seed = flip_coin(player_seed, server_seed)
print("Result:", result)

print("Combined seed:", combined_seed)
verified = verify_result(player_seed, server_seed, result, combined_seed)
print("Result verified:", verified)



