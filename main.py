import random
zahl=(random.randrange(1,10))
punkte=100
while True:
  raten=int(input("raten sie: "))
  if raten==zahl:
   print("gewonnen!")
   print("punkte=" + str(punkte))
   break
  elif raten<0:
   print("spiel beendet!")
   break
  else:
    print("falch, nochmal versuchen")
    punkte-=10
    if punkte==0:
      print("verloren!")
      break
      


