import json

with open('techniques.json', 'r') as techniques_file:
  techniques_data = techniques_file.read()

techniques_objects = json.loads(techniques_data)
N = len(techniques_objects) #number of techniques
print(f"Number of techniques: {N}")

i = 1
for technique in techniques_objects:
  print(f"{i}. {technique['id']}")
  i = i + 1
  for command in technique['commands']:
    print(command)
