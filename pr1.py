import json

with open('techniques.json', 'r') as techniques_file:
  data = techniques_file.read()

objects = json.loads(data)

for technique in objects:
  print(technique['id'])
  for command in technique['commands']:
    print(command)
