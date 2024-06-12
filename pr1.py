import json
import re

def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0,size):
        list_of_objects.append( list() ) #different object reference each time
    return list_of_objects



with open('techniques.json', 'r') as techniques_file:
  techniques_data = techniques_file.read()

techniques_objects = json.loads(techniques_data)
_N = len(techniques_objects) #number of techniques
print(f"N = {_N}, number of techniques to be used")

_MAT = init_list_of_objects(_N) #techniques with commands as elements, number of MAT is N
_A = init_list_of_objects(_N) #arrays for storage commands which equals exactly or by pattern with _MAT commands

i = 0
for technique in techniques_objects:
  i = i + 1
#  print(f"{i}. {technique['id']}")
  commands = []
  for command in technique['commands']:
    commands.append(command)
#    print(command)

  _MAT[i-1] = commands

#print("MATid arrays assigned:")
#print(_MAT)

#source commands
CL1 = []
CL1.append(["du -h --max-depth=1 | sort -hr",0])
CL1.append(["cd postmaster/",0])
CL1.append(["ls -l",0])

CL2 = []
CL2.append(["passwd root",0])
CL2.append(["vi /etc/ssh/sshd_config ",0])
CL2.append(["systemctl restart sshd",0])

for cmd in CL1:
  print("Command for analyze:")
  cmd_for_analyze = cmd[0]
  print(cmd_for_analyze)

  i = 0
  for mat in _MAT:
    i = i + 1

    ME = 0
    MP = 0

    #print(mat)
    for mat_cmd in mat:
      cmd_to_compare = mat_cmd["command"]
      #print("compare with: " + cmd_to_compare)

      cmd_conjuct = 0

      if cmd_for_analyze == cmd_to_compare:
        print("compare with: " + cmd_to_compare)
        print("exact match")
        cmd_conjuct = 1
        ME = ME + 1

      if cmd_to_compare not in ["^","+","..","$"]:
        if re.search(cmd_to_compare, cmd_for_analyze):
          print("compare with: " + cmd_to_compare)
          print("regex pattern match")
          cmd_conjuct = 1
          MP = MP + 1

      if cmd_conjuct == 1:
        _A[i-1].append(cmd_for_analyze)

    if _A[i-1]:
      print(f"A[{i-1}]={_A[i-1]}")
    if ME>0 or MP>0:
      print(f"ME(id={i-1})={ME}, MP(id={i-1})={MP}")

#print(_A)