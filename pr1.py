import json

with open('techniques.json', 'r') as techniques_file:
  data = techniques_file.read()

objects = json.loads(data)

print(objects)
