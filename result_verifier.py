import main
import os
import json

if os.path.isfile('client-file.json'):
    print("The last 10 result is being displayed...\n")
    with open('client-file.json', 'r') as file:
            data = json.load(file)
    last_result = data[-10:]
    for line in last_result:
        main.verify_roll(line["Client Seed"],line["Server Seed"],line["Nounce"])
        print(f"Server seed: " +line["Client Seed"])
        print(f"Server seed: " +line["Server Seed"])
        print(f"Server seed: " +line["Nounce"])
        print(f"You have chosen: " + line["Client Answer"])
        print("\n")