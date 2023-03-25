import json

def convert_text_to_json(input_file, output_file):
    # Open the input file and read the lines
    with open(input_file, "r") as f:
        lines = f.readlines()

    # Create a list to hold the dictionaries
    data = []

    # Iterate over the lines and parse them into dictionaries
    for line in lines:
        # Parse the line into fields
        fields = line.strip().split("|")

        # Create a dictionary with the fields as keys and values
        d = {
            "Client Seed": fields[0],
            "Server Seed": fields[1]
            # Add more fields as needed
        }

        # Append the dictionary to the list
        data.append(d)

    # Write the list of dictionaries to the output file as JSON
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)
