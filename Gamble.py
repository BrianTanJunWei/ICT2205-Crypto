import hashlib
import random


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


# Example usage
player_seed = "mysecretseed"
server_seed = "supersecureseed"
result, combined_seed = flip_coin(player_seed, server_seed)
print("Result:", result)
print("Combined seed:", combined_seed)
verified = verify_result(player_seed, server_seed, result, combined_seed)
print("Result verified:", verified)
