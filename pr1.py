import json
import re

def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0,size):
        list_of_objects.append( list() ) #different object reference each time
    return list_of_objects
#====def init_list_of_objects(size)

def calculate_d_command(cmd, _MAT, _A, _MATnames, debug = 0):
  cmd_for_analyze = str(cmd)
  if debug:
    print(f"======\nCommand for analyze: {cmd_for_analyze}")

  D = 0

  i = 0
  for mat in _MAT:
    i = i + 1

    ME = 0
    MP = 0
    S = 0
    F = 1

    for mat_cmd in mat:
      cmd_to_compare = mat_cmd["command"]

      cmd_conjuct = 0

      if cmd_for_analyze == cmd_to_compare:
        if debug:
          print(f"  compare with: {cmd_to_compare}")
          print(f"    exact match, MAT={_MATnames[i-1]}")
        cmd_conjuct = 1
        ME = 1

      if cmd_to_compare not in ["^","+","..","$"]:
        if re.search(cmd_to_compare, cmd_for_analyze):
          if debug:
            print(f"  compare with: {cmd_to_compare}")
            print(f"    regex pattern match, MAT={_MATnames[i-1]}")
          cmd_conjuct = 1
          MP = 1

      if cmd_conjuct == 1:
        if not cmd_to_compare in _A[i-1]:
          _A[i-1].append(cmd_to_compare)

    if len(_A[i-1])>0:
      S = len(_A[i-1])
      
    if len(_A[i-1]) == len(_MAT[i-1]):
      F = 2

    D = D + (ME + MP)*S*F
  
  if debug:
    print(f"D(cmd) = {D}")

  return D
#=======def calculate_d_command()


#======main

with open('techniques.json', 'r') as techniques_file:
  techniques_data = techniques_file.read()

techniques_objects = json.loads(techniques_data)
_N = len(techniques_objects) #number of techniques
print(f"N = {_N}, number of techniques to be used")

_MAT = init_list_of_objects(_N) #techniques with commands as elements, number of MAT is N
_A = init_list_of_objects(_N) #arrays for storage commands which equals exactly or by pattern with _MAT commands
_MATnames = list(range(_N))

i = 0
for technique in techniques_objects:
  i = i + 1
  _MATnames[i-1] = technique['id']
  commands = []
  for command in technique['commands']:
    commands.append(command)
  _MAT[i-1] = commands

#source commands=======COMMANDS-----#1
#with open('commands1.json', 'r') as commands1_file:
#  commands1_data = commands1_file.read()

#commands1_objects = json.loads(commands1_data)
#print(f"Commands #1 list number of commands = {len(commands1_objects)}")

#making analyze for commands in Commands list #1
#for cmd1 in commands1_objects:
#  cmd = cmd1["command"]
#  Dcmd = calculate_d_command(cmd, _MAT, _A, _MATnames, 0)
#  print(f"cmd={cmd}, Dcmd={Dcmd}")


#number of commands list collections
h = 5

for f in range(1,h+1):
  print(f"f={f}")
  with open('commands' + str(f) + '.json', 'r') as commands_file:
    commands_data = commands_file.read()

  commands_objects = json.loads(commands_data)
  print(f"Commands #{f} list number of commands = {len(commands_objects)}")

  #making analyze for commands in Commands list #1
  for cmd1 in commands_objects:
    cmd = cmd1["command"]
    Dcmd = calculate_d_command(cmd, _MAT, _A, _MATnames, 0)
    print(f"cmd={cmd}, Dcmd={Dcmd}")
