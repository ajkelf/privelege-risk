import json

with open('techniques.json', 'r') as techniques_file:
  data = techniques_file.read()

objects = json.loads(data)

i = 1
for technique in objects:
  print(i + ". " + technique['id'])
  i = i + 1
  for command in technique['commands']:
    print(command)
