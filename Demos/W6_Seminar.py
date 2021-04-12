def shop():
  items = {
    "Eggs":1.99,
    "Milk": 0.99,
    "Bread": 1.29,
    "Soup": 1.99,
    "Cake": 3.99,
    "Honey": 2.29,
    "Beer": 3.49
  }
  return items

def view_all(products = {}):
  for i in products:
    print(i)

def basket():
  basket = []
  while True:
    item = input("Enter item (or \"stop\"): ")
    if item == "stop":
      break
    else:
      print("Enter quantity: ")
      n = int(input())
      for i in range(n):
        basket.append(item)
  return basket

def till(basket = []):
  shoplist = shop()
  total = 0.0
  for item in basket:
    total += shoplist[item]
  return total

def update_price(item, new_price,products = {}):
  products[item] = new_price
  return products

def run():
  print("Welcome to our shop! Please have a look around and add items that you like")
  chosen_items = basket()
  while True:
    print("Are you ready to pay for your items?")
    if "yes" == input().lower():
      to_pay = till(chosen_items)
      print(f"Please pay £{to_pay:.2f} by cash or card")
      break
    else:
      chosen_items += basket()


view_all(shop())