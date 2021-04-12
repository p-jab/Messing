#IMDB clone (ish)

def rate_a_movie(title):
  return float(input(f"What would you rate \"{title}\"?\n"))

def actors():
  real = input("Name:")
  role = input("Role:")
  return real,role

def rating(title, number_of_responses):
  sum = 0.0
  for i in range(number_of_responses):
    sum+=rate_a_movie(title)
  return sum/number_of_responses

def new_movie():
  movie = {}
  movie["Title"] = input("What is the title?\n")
  movie["Released"] = input("What year was it released?\n")
  movie["Genre"] = input("What genre is it?\n")
  movie["Duration"] = input("How long is it?\n")
  actor_list = []
  i = 0
  print("Provide details of all the actors. How many actors are in the cast?")
  n=int(input())
  while i < n:
     actor_list.append(actors())
     i+=1
  movie["Actors"] = actor_list
  movie["Rating"] = 10.0, 0
  return movie

def movie_search(database = {}):
  print("Search by: Title, Genre or Actor?")
  opt = input()
  movie ={}
  if opt.lower() == "title":
    t = input("Enter the title: ")
    if t in database:
      movie = database[t]
    else:
      print("The database does not contain any details of this movie :(")
  elif opt.lower() == "genre":
    g = input("Enter the genre: ")
    for details in database.values():
      if details["Genre"] == g:
        movie = details
  elif opt.lower() == "actor":
    a = input("Enter actor's name: ")
    for details in database.values():
      for actor in details["Actors"]:
        if actor[0] == a:
          movie = details
  return movie

def movie_print(movie = {}):
  print("*"*5 + " "*2 + "{}".format(movie["Title"])+ " "*2 + "*"*5, end = "\n\n")
  for i in movie.items():
    print(f"{i[0]} ---> {i[1]}")


def imdb():
  imdb = {}
  print("Welcome to da BEST movie database!\n\n")
  while True:
    print("\nChoose one of the options:\n1-Add a movie\n2-Search for a movie\n3-Show dull database\n5-Exit")
    option = int(input())
    if option == 5:
      break
    elif option == 1:
      m_title = input("What is the movie called?\n")
      imdb[m_title] = new_movie()
    elif option == 2:
      print(movie_search(imdb))
    elif option == 3:
      print(imdb)
    else:
      print("Invalid option. Try again. You noob.\n")

n = new_movie()
movie_print(n)


#ADD rating update to database!!!!!