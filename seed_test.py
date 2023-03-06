import random
import sys


def flip_coin(player1_seed, player2_seed, server_seed):
    combined_seed = player1_seed + player2_seed + server_seed
    print(combined_seed)
    random.seed(combined_seed)
    rand_num = random.random()

    result = "heads" if rand_num < 0.5 else "tails"

    return result, combined_seed

def verify_result(player1_seed, player2_seed, server_seed, result, combined_seed):
    # Combine player seed and server seed to generate the same unique seed used to generate the result
    expected_seed = player1_seed + player2_seed + server_seed

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


player1=random.randrange(sys.maxsize)
player2=random.randrange(sys.maxsize)

server=random.randrange(sys.maxsize)

result, combined_seed = flip_coin(player1, player2, server)
print("Result:", result)
print("Combined seed:", combined_seed)
verified = verify_result(player1, player2, server, result, combined_seed)
print("Result verified:", verified)
