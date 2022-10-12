import numpy as np
cardnumbers =["A","J","Q","K","2","3","4","5","6","7","8","9","10"]
signs=["Kupa","Karo","Maça","Sinek"]
deck=[]
for sign in signs:
  for cards in cardnumbers:
    deck.append(f"{sign} {cards}")
bank=5000
print("BLACKJACK")
def computerdraw(gamedeck,cmpicked,bet,bank):
  bank=bank
  bet = bet
  rn =np.random.randint(0,len(gamedeck),1)
  rn = np.asarray(rn).astype(int)
  cc = gamedeck[int(rn[0])]
  cmpicked.append(cc)
  gamedeck.pop(int(rn[0]))
  print(f"The computer has drawn {cmpicked[len(cmpicked)-1]}")
  if calculate(cmpicked) < 17:
    computerdraw(gamedeck,cmpicked,bet,bank)
  if calculate(cmpicked) >= 17:
    if calculate(cmpicked) == 21:
      print("the computer has blackjack")
    if calculate(cmpicked) > 21:
      print("the computer has bust")
      bank = bank+int(bet)
      game(bank)
    return calculate(cmpicked)
def calculate(userpicked):
  total = 0
  for i in userpicked:
    a = i.split()
    if a[1] == "J":
      total=total+10
    if a[1] == "K":
      total=total+10
    if a[1] == "Q":
      total=total+10
    if a[1] == "A":
      if total+11 > 21:
        total = total+1
      if total+11 <= 21:
        total = total+11
    if a[1] == "2":
      total = total+int(a[1])
    if a[1] == "3":
      total = total+int(a[1])
    if a[1] == "4":
      total = total+int(a[1])
    if a[1] == "5":
      total = total+int(a[1])
    if a[1] == "6":
      total = total+int(a[1])
    if a[1] == "7":
      total = total+int(a[1])
    if a[1] == "8":
      total = total+int(a[1])
    if a[1] == "9":
      total = total+int(a[1])
    if a[1] == "10":
      total = total+int(a[1])
  return total
while True:
  def game(bank):
    print(f"You have {bank} dollars.")
    bet = int(input("your bet: "))
    bank=bank
    
    if 2*int(bet) <= bank:
      chanceofdouble=True
    if 2*int(bet) > bank:
      chanceofdouble=False
    if int(bet) > bank:
      print("you don't have enough money!")
    else:
      bank = bank - int(bet)
      print(f"You have {bank} dollars left.")
      gamedeck = deck.copy()
      userpicked=[]
      cmpicked=[]

      rn =np.random.randint(0,len(gamedeck),1)
      rn = np.asarray(rn).astype(int)
      cc = gamedeck[int(rn[0])]
      userpicked.append(cc)
      gamedeck.pop(int(rn[0]))

      rn =np.random.randint(0,len(gamedeck),1)
      rn = np.asarray(rn).astype(int)
      cc = gamedeck[int(rn[0])]
      userpicked.append(cc)
      gamedeck.pop(int(rn[0]))

      print(f"you picked {userpicked}")
      #playerdraws
      while calculate(userpicked)<21:
        if chanceofdouble == True:
          hit = input("hit doubledown pass? (h/d/p): ")
          if hit == "h":
            rn =np.random.randint(0,len(gamedeck),1)
            rn = np.asarray(rn).astype(int)
            cc = gamedeck[int(rn[0])]
            userpicked.append(cc)
            gamedeck.pop(int(rn[0]))
            print(f"you picked {userpicked}")
            chanceofdouble= False
            if calculate(userpicked) == 21:
              print("blackjack!")
              bank=bank+int(bet)
              game(bank)
            if calculate(userpicked) > 21:
              print("you bust!")
              game(bank)
          if hit == "d":
            bank=bank-int(bet)
            bet = int(bet)*2
            rn =np.random.randint(0,len(gamedeck),1)
            rn = np.asarray(rn).astype(int)
            cc = gamedeck[int(rn[0])]
            userpicked.append(cc)
            gamedeck.pop(int(rn[0]))
            print(f"you picked {userpicked}")
            chanceofdouble=False
            if calculate(userpicked) == 21:
              print("you win!")
              bank = bank+int(bet)*2
              game(bank)
            if calculate(userpicked) > 21:
              print("bust!")
              game(bank)
            if computerdraw(gamedeck,cmpicked,2*int(bet),bank) > calculate(userpicked):
              print("you lose")
              game(bank)
            if computerdraw(gamedeck,cmpicked,2*int(bet),bank) < calculate(userpicked):
              print("you win")
              bank = bank+int(bet)*4
              game(bank)
            if computerdraw(gamedeck,cmpicked,2*int(bet),bank) == calculte(userpicked):
              print("draw")
              bank = bank+int(bet)*2
              game(bank)
          if hit == "p":
            if computerdraw(gamedeck,cmpicked,2*int(bet),bank) > calculate(userpicked):
              print("you lose")
              game(bank)
            if computerdraw(gamedeck,cmpicked,2*int(bet),bank) < calculate(userpicked):
              bank = bank+int(bet)*2
              print("you win")
              game(bank)
            if computerdraw(gamedeck,cmpicked,2*int(bet),bank) == calculte(userpicked):
              print("draw")
              bank = bank+int(bet)
              game(bank)
        if chanceofdouble == False:
          hit = input("hit or pass? (h/p): ")
          if hit == "h":
            rn =np.random.randint(0,len(deck),1)
            rn = np.asarray(rn).astype(int)
            cc = gamedeck[int(rn[0])]
            userpicked.append(cc)
            gamedeck.pop(int(rn[0]))
            print(f"you picked {userpicked}")
            if calculate(userpicked) == 21:
              print("you win!")
              bank = bank+int(bet)*2
              game(bank)
            if calculate(userpicked) > 21:
              print("bust!")
              game(bank)
          if hit == "p":
            if computerdraw(gamedeck,cmpicked,2*int(bet),bank) > calculate(userpicked):
              print("you lose")
              game(bank)
            if computerdraw(gamedeck,cmpicked,2*int(bet),bank) < calculate(userpicked):
              print("you win")
              bank = bank+int(bet)*2
              game(bank)
            if computerdraw(gamedeck,cmpicked,2*int(bet),bank) == calculte(userpicked):
              print("draw")
              bank = bank+int(bet)
              game(bank)
  game(bank)
