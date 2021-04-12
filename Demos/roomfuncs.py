def room_area(w,l):
  return w*l

def room_name():
  print("What is the name of the room?")
  return input()

def price(name, area):
  if(name == "kitchen"):
    return 5*area
  elif name == "bedroom":
    return 3*area
  elif name == "bathroom":
    return 20*area
  else:
    return 7*area

def run():
  name = room_name()
  print("What is the width of the room?")
  w = float(input())
  print("What is the length of the room?")
  l = float(input())
  print(f"You should pay £{price(name,room_area(w,l)):.2f}")
