import random

a = random.randint(1,1000)
b = 0
while b != a:
    b = int(input("On va jouer au juste prix dis moi un chiffre : "))
    if b < a:
      print("c'est +")
    elif b > a:
      print("c'est - ")
    else:
      print("bien joué")
