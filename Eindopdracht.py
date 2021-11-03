naam = input("Hallo wat is jou naam?\n>")




def Opnieuw():
  print("\nWil je opnieuw proberen? (y or n)")
  

  answer = input(">").lower()

  if "y" in answer:
    start()
  else:
    exit()




def game_over(reason):

  print("\n" + reason)
  print("Game Over!")

  Opnieuw()




def start():

  answer = input("\n" + naam + " je woont in een land en de nieuwe dictator kom t je land binnen wat doe je?\nA) Ik wacht het af en doe er niks tegen,\nB) Je maakt plannen om te vluchten,\nC) Ik wil terug vechten.\n> ").lower()

  if answer == "a":
    Executie()
  elif answer == "b":
    Vraag1B()
  elif answer == "c":
    Vraag1C()
  else:
    start("Kom op zo lastig is het niet.")




def Vraag1C():

  answer = input("\nHoe wil je terugvechten?\nA) Net zoals in vietnam,\nB) Door een mes te pakken en ze neer te steken,\nC) Ik wil toch niet vechten\n>")
  if answer == "a":
    Vraag1CA()
  elif answer == "b":
    Vraag1CB()
  elif answer == "C":
    Vraag1CC()
  else:
    Vraag1C()
    



def Vraag1CC():
  game_over("\neen A-10 warthog lost een bombing run en daarin ben jij gestorven.")




def Vraag1CB():

  game_over("\nJe rent op de soldaten af en je struikelt over een grenaat en breekt je nek.")




def Vraag1CA():

  answer = input("\nA) Je word gevonden door een resistence fighter hij verteld je dat ze geurilla tactics gebruiken, Ga je met ze mee?\nA) Ja,\nB) Nee\n>")
  if answer == "ja":
    Vraag1CAA()
  elif answer == "nee":
    Vraag1B()
  else:
    Vraag1CA("error")




def Vraag1CAA():

  answer = input("\nDe rebellen geven jou een biertje en een AK ze sturen je in een truck naar een van hun kampen, een paar dagen later kom je op het kamp aan je ziet dat er een 9.000.000 euro bounty op de rebellen staan wat doe je?\nA) Niks ik ben trouw aan mijn nieuwe broeders,\nB) Met zo veel geld kan ik makkelijker weg,\nC) Laten zien aan de leiders van de rebellen\n>")
  if answer == "a":
    nosnitch()
  elif answer == "b":
    Vraag1CAAB()
  elif answer == "c":
    goodsnitch()
  else:
    Vraag1CAA()




def Vraag1CAAB():

  game_over("\nJe belt het leger die zeiden dat ze zouden komen jij wacht op ze, Een aantal uur later komen ze aan alleen word jij geraakt door een van de tanks en je sterft.")




def goodsnitch():

  answer = input("\nJe praat met de leiders van de rebellen over de brochure ze geven je de optie om het land uit te komen en naar cuba te gaan doe je dat?\nA) Ja graag,\nB) Nee ik blijf en vecht,\nC) Is nederland ook een optie?\n>")
  if answer == "a":
    goodsnitcha()
  elif answer == "b":
    nosnitcha()
  elif answer == "c":
    goodsnitchC()




def goodsnitchC():

  answer = input("\nJa zeggen ze alleen wordt dit lastiger dan Cuba weet je het zeker?\nA) Ja,\nB) Nee\n>")
  if answer == "a":
    Nederland()
  elif answer == "b":
    Cuba()




def Nederland():

  answer = input("\nJe word op een transport gezet en je krijgt de instructies om stil te blijven, een aantal uur in de reis stop het transport je hoort een aantal schoten wat doe je?\nA) Ik kijk wat er aan de hand is,\nB) Ik luister naar de instructies,\nC) Ik ren weg\n>")
  if answer == "a":
    NederlandA()
  elif answer == "b":
    pass
  elif answer == "c":
    NederlandC()




def NederlandC():

  answer = input("\nJe rent weg van het conflict en komt in de wildernis wat doe je\nB) Ik ga terug,\nA) Ik probeer een auto te vinden\n>")
  if answer == "a":
    AutoStart("\nJe vind een auto en je rijdt richting de grens")
  elif answer == "b":
    nederlandB()
  else:
    NederlandC()




def nederlandB():

  answer = input("\nNa een tijdje schieten stopt het het transport begint weer te bewegen na een tijdje stop het transport op een vliegveld een man doet open en zegt dat je mee moet komen wat doe je?\nA) Ik blijf zitten,\nB) Ik loop mee.\n>")
  if answer == "a":
    Nederlaag()
  elif answer == "b":
    NederlandEnd()
  else:
    nederlandB()




def NederlandEnd():

  answer = input("\nJe loopt mee met de man naar het vliegtuig deze stijgt op na een reis van een aantal uur land je in nederland je word begroet door een aantal militairen omdat je onderdeel was van de rebellen krijg je sneller een inburgering en je krijgt de optie over waar je wil wonen.\nA) Urk,\nB) Den helder,\nC) Friesland\n>")
  if answer == "a":
    End()
  elif answer == "b":
    End()
  elif answer == "c":
    End()
  else:
    NederlandEnd()




def End():
  game_over("Het leven is lastig want je kan de taal niet zo goed maar je haalt het door")




def Nederlaag():
  game_over("\nDe man word boos en trekt je uit het transport")




def NederlandA():
  game_over("\nJe steekt je hoofd uit het transport je ziet soldaten ze richten hun wapen en schieten je dood.")




def goodsnitcha():

  answer = input("\nZe geven je twee opties van reizen,\nA) Land,\nB) Lucht?\n>")
  if answer == "a":
    land()
  elif answer == "b":
    Cuba()
  else:
    goodsnitcha()




def land():

  answer = input("\nOp een haven moet je kiezen tussen boten er zijn er twee een oude boot en een nieuwe boot welke kies je?\nA) De oude denk ik.\nB) De nieuwe boot natuurlijk\n>")

  if answer == "a":
    BootA()
  elif answer == "b":
    Cuba()
  else:
    land()




def Cuba():
  
  answer = input("\nJe vlucht naar cuba na 5 jaar heb je een leven op gang je heb vrienden een vrouw en kinderen. Wat doe je?\nA) Ik start een drugscartel,\nB) Ik moet terug naar mijn eigen land,\nC) Ik heb geluk gevonden ik hou het zo\n>")
  if answer == "a":
    CubaA()
  elif answer == "b":
    CubaB()
  elif answer == "c":
    CubaC()
  else:
    Cuba()




def CubaC():
  game_over("\nJe bent gelukkig en leid je leven met geluk je sterft op oude leeftijd met je kinderen en vrouw aan je zij")




def CubaB():
  game_over("\nJe gaat terug naar je land van afkomst hier word je opgepakt en opgesloten.")




def CubaA():

  game_over("\nJe start een succesvol drugs cartel todat je een olie mijn vind vol met olie de amerikaanse overheid stuurt een A-10 warthog naar jou toe om het te stelen helaas kom je om")




def BootA():

  game_over("De boot was te fragiel om te varen je komt om in de crash.")




def nosnitch():
  
  answer = input("\nJe snitcht niet op de rebellen, Wat doe je met de foto?\nA) Niks ik laat het liggen,\nB) Ik verscheur hem\nC) Ik laat het zien aan de leiders.\n>")
  if answer == "a":
    nosnitcha()
  elif answer == "b":
   nosnitchb()
  elif answer == "c":
    goodsnitch()
  else:
    nosnitch()




def nosnitchb():

  game_over("iemand belt het leger die zeiden dat ze zouden komen jij wacht op ze, Een aantal uur later komen ze aan alleen word jij geraakt door een van de tanks en je sterft.")




def nosnitcha():

  game_over("je vecht de rest van de tijd met de dictator totdat je uiteindelijk wint.")




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

  game_over("Je loopt Hopelijk richting de grens")
  Vraag1CA()




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




start()