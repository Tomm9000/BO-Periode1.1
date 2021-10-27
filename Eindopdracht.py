naam = input("Hallo wat is jou naam?\n>")

def start():

  print("\n" + naam + " je woont in een land en de nieuwe dictator kom t je land binnen wat doe je? ")
  print("\nA) Ik wacht het af en doe er niks tegen,")
  print("\nB) Je maakt plannen om te vluchten,")
  print("\nC) Ik wil terug vechten.\n")
  
  antwoord = input(">").lower()

  if "a" in antwoord:

    Executie()
  elif "b" in antwoord:

    Vraag1B()
  elif "c" in antwoord:

    Vraag1C()
  else:

    game_over("Kom op zo lastig is het niet.")


def game_over(reason):

  print("\n" + reason)
  print("Game Over!")

  Opnieuw()

def Opnieuw():
  print("\nWil je opnieuw proberen? (y or n)")
  

  answer = input(">").lower()

  if "y" in answer:
    start()
  else:
    exit()

def Executie():

  print("\nJe zei een verkeerd woord en werd gexecuteerd.")

def Vraag1B():

  plek = input("\nWaar wil je naartoe vluchten?\n>")
  print("\nHoe ga je naar " + plek + " vluchten?\n>")
  print("\nA) Ik heb me bedacht ik wil toch mijn huis niet verlaten,")
  print("\nB) Je pakt de auto en rijd richting de grens,")

  answer = input(">")
  
  if answer == "a":

    Executie()
  elif answer == "b":

    AutoStart()

  else:

    game_over("Kom op man / vrouw!")

def AutoStart():

  print("\nJe word gezien door een aantal militairen ze vragen je om je vervoers bewijs wat doe je?")
  print("\nA) Je rijd snel door,")
  print("\nB) Ik geef me over,")
  print("\nC) Je maakt een praatje met de soldaten,")

  answer = input(">")
  
  if answer == "a":

    AutoStartA()
  elif answer == "b":

    print("\n")
    Insert()
  elif answer == "c":

    print("\n")
    Insert()
  else:

    game_over("Kom op man / vrouw!")

def AutoStartA():

  print("\nDe soldaten schieten richting en je word in je schouder en motor geschoten, Je ziet een grot wat doe je?")
  print("\nA) Ik ren naar de grot,")
  print("\nB) Ik blijf zitten,")
  print("\nC) Ik blijf rijden,")

  answer = input(">")
  
  if answer == "a":

    Grot()
  elif answer == "b":

    print("\n")
    Insert()
  elif answer == "c":

    print("\n")
    Insert()
  else:

    game_over("Kom op man / vrouw!")

def Grot():

  print("\nGelukig voor jou zagen de soldaten je niet, ze schelden je uit en gooien een grenaat naar je auto.")
  print("\nJe bloedt wat ga je daar aan doen?")

  answer = input(">")
  
  if answer == "a":

    insert()
  elif answer == "b":

    print("\n")
    Insert()
  elif answer == "c":

    print("\n")
    Insert()
  else:

    game_over("Kom op man / vrouw!")


def template():

  print("\n")

  answer = input(">")
  
  if answer == "a":

    insert()
  elif answer == "b":

    print("\n")
    Insert()
  elif answer == "c":

    print("\n")
    Insert()
  else:

    game_over("Kom op man / vrouw!")

start()