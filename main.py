import random

first_cards = list()
ai_cards = list()
ai_total = 0
over=list()
over_total=0
hit = "hit"
amount = 2
for i in range(0, 2):
    card = random.randint(1, 11)
    first_cards.append(card)
print("your two cards are" + str(first_cards[0:2]))
while sum(ai_cards)-over_total < 13:
    card = random.randint(1, 11)
    ai_cards.append(card)
    card = random.randint(1, 11)
    if sum(ai_cards)> 21:
        over.append(card)
while True:
    hit = input("do you want to hit or stick\n>")
    if hit == "stick":
        break
    if hit == "hit":
        amount = amount + 1
        card = random.randint(0, 10)
        first_cards.append(card)
        print("your " + str(amount) + " cards are now " +
              str(first_cards[0:amount]))
    if sum(first_cards) > 21:
        print("you lose! your oppenent scored " + str(ai_total))
        print("your opponents score was " + ai_total)
        break

if sum(first_cards) > ai_total:
    print("you win, well done you scored " + str(sum(first_cards)) +
          " your oppenent scored " + str(ai_total))
else:
    print("you lose, bad luck you scored " + str(sum(first_cards)) +
          " your oppenent scored " + str(ai_total))
