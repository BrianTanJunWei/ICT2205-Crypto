import Gamble

nonce = input("Enter nonce: ")
server_seed = Gamble.generate_server_seed()
client_seed = Gamble.generate_client_seed()

roll, server_seed, client_seed = Gamble.get_roll_and_seeds(nonce, server_seed, client_seed)

print(f'Roll for nonce {nonce} is {roll}')

# Ask user if they want to verify the result
choice = input("Do you want to verify the roll? (y/n): ")
if choice.lower() == 'y':
    verified = Gamble.verify_roll(server_seed, client_seed, nonce, roll)
    if verified:
        print("Roll verified!")
    else:
        print("Roll verification failed!")