import json

# Load JSON file
file_path = 'body_template.json'
with open(file_path, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()

file_contents = file_contents.replace('\n', '').replace(' ', '').replace('"', '\"')

# Print the contents of the file
print(file_contents)
