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

#server 13191751363066580391246424792365768454619389975528325025443195643009258367707808651043418920801515460908615720609101844463440533610809843465516619223283840
#client 11677750745121269248081345389030720550103105603233164809186336150519006691489811322930083942736075397631012714411723507639815986589889717006328141396563509
#result 20778