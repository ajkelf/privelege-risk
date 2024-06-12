import json

with open('techniques.json', 'r') as techniques_file:
  techniques_data = techniques_file.read()

techniques_objects = json.loads(techniques_data)
_N = len(techniques_objects) #number of techniques
print(f"N = {_N}, number of techniques to be used")

_MAT = [] #techniques with commands as elements, number of MAT is N

i = 1
for technique in techniques_objects:
  print(f"{i}. {technique['id']}")
  i = i + 1
  
  commands = []
  for command in technique['commands']:
    commands.append(command)
    print(command)

  _MAT.append(commands)

print("MATid arrays assigned:")
print(_MAT)

#source commands
CL1 = []
CL1.append(["du -h --max-depth=1 | sort -hr",0])
CL1.append(["cd postmaster/",0])
CL1.append(["ls -l",0])

CL2 = []
CL2.append(["passwd root",0])
CL2.append(["vi /etc/ssh/sshd_config ",0])
CL2.append(["systemctl restart sshd",0])

