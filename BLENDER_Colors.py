file = open("gaga.csv", "w")
file.write("This is just irresponsible\nDon't you think?\nYessir!")
file.close()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

with open("gaga.csv") as g:
  for lines in g:
    if  "ust" in lines:
      print(lines, end = "")
    elif "sir" in lines:
      print(f"\033[92m{lines}\033[0m")

