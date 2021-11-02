naam = input("Hallo wat is jou naam?\n>")

def start():

  antwoord = input("\n" + naam + " je woont in een land en de nieuwe dictator kom t je land binnen wat doe je?\nA) Ik wacht het af en doe er niks tegen,\nB) Je maakt plannen om te vluchten,\nC) Ik wil terug vechten.\n> ").lower()

  if "a" in antwoord:
    Executie()
  elif "b" in antwoord:
    Vraag1B()
  elif "c" in antwoord:
    Vraag1C()
  else:
    start("Kom op zo lastig is het niet.")

def Vraag1C():

  answer = input("\nHoe wil je terugvechten?\nA) Net zoals in vietnam,\nB) Door een mes te pakken en ze neer te steken,\nC) Ik wil toch niet vechten\n>")
  if answer == "a":
    Vraag1CA()
  elif answer == "b":
    insert()
  elif answer == "C":
    insert()
  else:
    Vraag1C()

def Vraag1CA():

  answer = input("\nA) Je word gevonden door een resistence fighter hij verteld je dat ze geurilla tactics gebruiken, Ga je met ze mee?\nA) Ja,\nB) Nee\n>")
  if answer == "ja":
    insert()
  elif answer == "nee":
    insert()
  else:
    Vraag1CA()


def Vraag1CAA():

  answer = input("\nDe rebellen geven jou een biertje en een AK ze sturen je in een truck naar een van hun kampen, een paar dagen later kom je op het kamp aan je ziet dat er een 9.000.000 euro bounty op de rebellen staan wat doe je?\nA) Niks ik ben trouw aan mijn nieuwe broeders,\nB) Met zo veel geld kan ik makkelijker weg,\nC) Laten zien aan de leiders van de rebellen\n>")
  if answer == "a":
    input()
  elif answer == "b":
    input()
  elif answer == "c":
    insert()
  else:
    Vraag1CAA()


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
  answer = input("\nHoe ga je naar " + plek + " vluchten?\nA) Ik heb me bedacht ik wil toch mijn huis niet verlaten,\nB) Je pakt de auto en rijd richting de grens,\n>")
  if answer == "a":
    Executie()
  elif answer == "b":
    AutoStart()
  else:
    Vraag1B("Kom op man / vrouw!")


def AutoStart():

  answer = input("\nJe word gezien door een aantal militairen ze vragen je om je vervoers bewijs wat doe je?\nA) Je rijd snel door,\nB) Ik geef me over,\nC) Je maakt een praatje met de soldaten,\n>")
  if answer == "a":
    AutoStartA()
  elif answer == "b":
    GoodEnding1()
  elif answer == "c":
    Auto1C()
  else:
    AutoStart("Kom op man / vrouw!")


def Auto1C():

  answer = input("\nJe praat met de soldaten en je komt er achter dat je veel met ze gemeen heb en ze nodigen je uit naar een feestje. wat zeg je?\nA) Prima,\nB) nee sorry ik moet door mischien de volgende keer,\nC) Rot op.")
  if answer == "a":
    Feestje()
  elif answer == "b":
    Nee()
  elif answer == "c":
    AutoStartAB()
  else:
    Auto1C()


def Nee():

  print("De dictator respecteerd je keuze en geeft je een penthouse. je leeft de rest van je leven in comfort.")


def Feestje():

  answer = input("\nJe gaat naar een feestje hier kom je dictator tegen hij mag je en offert een rank tussen zijn officiers wat zeg je?\nA) Ja natuurlijk,\nB) Nee sorry\n>")
  if answer == "a":
    SealTeam6()
  elif answer == "b":
    Leider()
  else:
    Feestje()


def Leider():

  print("De dictator respecteerd je keuze en geeft je een penthouse. je leeft de rest van je leven in comfort.")


def SealTeam6():

  print("A) na een aantal jaar als een officier word je vermoord door seal team 6.")


def GoodEnding1():

  answer = input("\nZe nemen je gevangen en de na 2 jaar word je gevonden door nederlandse soldaten\nDe soldaten sturen je naar nederland om informatie te geven aan de overheid.\nA) Geef je ze antwoord?\nB) IK ZWIJG.")
  if answer == "a":
    GoodEnding1A()
  elif answer == "b":
    GoodEnding1B()
  else:
    GoodEnding1()


def GoodEnding1B():

  answer = input("\nJe zwijgt maar dit maakt de nederlanders niet uit die denken dat je getraumatiseerd ben dus laten je. Je doet je inburgering Leer je nederlands\n Y/N?")
  if answer == "y":
    GoodEnding1BYes()
  elif answer == "n":
    GoodEnding1BNo()
  else:
    GoodEnding1B()


def GoodEnding1BNo():

  print("Leven in nederland is lastiger er word meer naar je gediscrimineerd maar je kan er mee leven.")


def GoodEnding1BYes():

  print("Je word goed ingeburgerd en je vind vrienden goede vrienden ze  helpen je door de lastige tijden je leven is goed hier. maar je mist thuis wel")


def GoodEnding1A():

  print("\nJe help ze en krijgt snellere unburgering na 3 jaar heb je een gezin en een succesvolle baan, Het was verassend hoe snel ik de taal heb geleerd")


def AutoStartA():

  answer = input("\nDe soldaten schieten richting en je word in je schouder en motor geschoten, Je ziet een grot wat doe je?\nA) Ik ren naar de grot,\nB) Ik blijf zitten,\nC) Ik blijf rijden,\n>")
  if answer == "a":
    Grot()
  elif answer == "b":
    AutoStartAB()
  elif answer == "c":
    AutoBoem()
  else:
    AutoStartA("Kom op man / vrouw!")


def AutoBoem():

  answer = input("\nJe komt ongeveer 2km verder tot de motorkap gaat roken wat doe je?\nA) Ik blijf rijden,\nB) Ik snap snel uit.\n>")
  if answer == "a":
    AutoBoemA()
  elif answer == "b":
    AutoBoemB()
  else:
    AutoBoem("Kom op man / vrouw!")


def AutoBoemB():

  game_over("Je komt niet snel genoeg uit de auto en hij explodeert")


def AutoBoemA():

  game_over("De auto explodeert")


def AutoStartAB():

  game_over("De soldaten lopen naar je raam en trekken je er uit, ze maken grappen over hoe dom je bent en schieten je daarna neer.")


def Grot():

  answer = input("\nGelukig voor jou zagen de soldaten je niet, ze schelden je uit en gooien een grenaat naar je auto.\nJe bloedt wat ga je daar aan doen?\nA) Ik probeer de kogel er uit te halen,\nB) Ik negeer het en ga verder,\nC) Ik blijf wachten in de grot.\n>")
  if answer == "a":
    GrotA()
  elif answer == "b":
    GrotB()
  elif answer == "c":
    GrotC()
  else:
    Grot("Kom op man / vrouw!")


def GrotA():

  game_over("Dit is niet een film de pijn word te veel en je sterft aan een hartaanval.")


def GrotB():

  game_over("Je loopt Hopelijk richting de grens maar na 48 uur sterf je aan de verwonding")


def GrotC():

  answer = input("\nJe blijft wachten maar na een tijdje begin je moe te worden wat doe je?\nA) Ik moet wakker blijven,\nB) Ik denk dat het goed is dat ik even ga liggen,C) Ik druk op de wond om wakker te blijven.\n>")
  if answer == "a":
    GrotCDeath1()
  elif answer == "b":
    GrotCDeath2()
  elif answer == "c":
    GrotCDeath3()
  else:
    game_over("Kom op man / vrouw!")


def GrotCDeath1():

  game_over("De pijn houd je 5 minuten wakker maar je hart kan het niet houden je sterft")


def GrotCDeath2():

  game_over("Je gaat slapen maar dit is permanent")


def GrotCDeath3():

  game_over("Je kan niet wakker blijven en sterft aan de verwonding.")


def template():

  print("\n")

  answer = input(">")
  
  if answer == "a":

    insert()
  elif answer == "b":

    Insert()
  elif answer == "c":

    Insert()
  else:

    game_over("Kom op man / vrouw!")

start()