phonebook = {}

while True:
  name = input("Enter the name: ")
  number = input("Enter the number: ")
  phonebook[name] = number
  if input("Type \'x\' to quit ") == 'x':
    break

print(phonebook)

n1 = input("Who are you going to call?")
print(f"Calling {n1} via number {phonebook[n1]}")


song = '''
Humpty Dumpty sat on the wall
Humpty Dumpty had a great, great fall and
All the king's horses and all the king's men
Couldn't put Humpty together again
Humpty Dumpty and Betty Louise
Stole a Sony and some Camembert cheese
And she said "Humpty baby
Take me to the river
Cause I like the way it runs
Take me to the river
You know I like the way it runs"
He said "ah, ooh, everything's going my way"
He said "maybe it's my lucky day"
I said "anything you want I can give"
She said "I want to take your picture, mm, just for me"
He said "anything"
She said "up there baby get on the wall babe"
Humpty Dumpty sat on the wall
'''

l = song.lower().replace("\"", "").replace("'", "").replace(",", "").split()

words_hd = {}

# for word in l:
#   if word in words_hd:
#     words_hd[word] += 1
#   else:
#     words_hd[word] = 1

for i in l:
  words_hd[i] = words_hd.get(i,0) + 1

print(dict(sorted(words_hd.items(), key = lambda x:-x[1])).keys())