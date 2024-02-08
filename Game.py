import random

#auth
#P1


p1 = input('Enter player one name ')

#P2
p2 = input('Enter player two name ')

#CARDS
p1cards = [

]

p2cards = [

]

#Pickings
round = 1

#Deck

Deck = [
	
	[], [], [], [], [], [], [], [], [], [],
	[], [], [], [], [], [], [], [], [], [],
	[], [], [], [], [], [], [], [], [], []
	
]
	

#unique deck
UDeck = [

]

#cols and nums

while len(UDeck) < 30:
	for card in Deck:
	
		numberc = random.randint(1,10)
		letterc = random.choice('BYR')

		card = [numberc, letterc]

		#put unique cards in Udeck
		if card not in UDeck:
			UDeck.append(card)
		#if it is
		else:
			card.pop
			
#print(UDeck)
#input()
#print(len(UDeck))
#input()

#check for duplicates



#rules

print('These are the rules of the card game:')
input()
print('The players take one card each from the 30 card deck and compare them')
input()
print('Every card has a number and (1 - 10) a letter (B, Y or R) on it')
input()
print('B = black, Y = yellow and R = red')
input()
print('Red beats black, black beats yellow and yellow beats red')
input()
print('If the letters are the same, the card with the highest number wins')
input()
print('The winner of that round also gets both of the cards')
input()
print('This goes on until the deck is empty')
input()
print("At the end, I'll show you how many cards you each have, and the one with the most wins")
input()


#takes cards
def takecards():
	p1cards.append(UDeck[0])
	UDeck.pop(0)

	p2cards.append(UDeck[0])
	UDeck.pop(0)


#GAME

while len(UDeck) != 0:
	
	#shuffle cards
	random.shuffle(UDeck)


	print(f'Round {round}')

	input()

	#players take cards
	takecards()

	#game round cards
	p1card = p1cards[-1]
	p2card = p2cards[-1]

	#tell cards
	print(f'{p1} picked {p1card}')
	input()
	print(f'{p2} picked {p2card}')
	input()

	#decide winner

	#same letter
	if p1card[1] == p2card[1]:

		print('Same colour')
		input()

		#check higher number

		if p1card[0] > p2card[0]:
			
			print(f'{p1} wins round {round}')
			
			#take both cards
			p1cards.append(p2card)
			p2cards.pop(-1)

			


		else:
			print(f'{p2} wins round {round}')
			
			#take both cards
			p2cards.append(p1card)
			p1cards.pop(-1)	

			

	#black and red
	elif p1card[1] == 'R' and p2card[1] == 'B':
		
		print(f'{p1} wins round {round}')
		input()
		
		#take both cards
		p1cards.append(p2card)
		p2cards.pop(-1)

		


	elif p2card[1] == 'R' and p1card[1] == 'B':
		
		print(f'{p2} wins round {round}')
		input()
		
		#take both cards
		p2cards.append(p1card)
		p1cards.pop(-1)

		

	# yellow and red
	elif p1card[1] == 'Y' and p2card[1] == 'R' :
		
		print(f'{p1} wins round {round}')
		input()
		
		#take both cards
		p1cards.append(p2card)
		p2cards.pop(-1)

		

	elif p2card[1] == 'Y' and p1card[1] == 'R':
		
		print(f'{p2} wins round {round}')
		input()
		
		#take both cards
		p2cards.append(p1card)
		p1cards.pop(-1)

		

	#black and yellow
	elif p1card[1] == 'B' and p2card[1] == 'Y' :
		
		print(f'{p1} wins round {round}')
		input()
		
		#take both cards
		p1cards.append(p2card)
		p2cards.pop(-1)

		


	elif  p2card[1] =='B' and p1card[1] == 'Y':
		
		print(f'{p2} wins round {round}')
		input()
		
		#take both cards
		p2cards.append(p1card)
		p1cards.pop(-1)


	input()

	#increase
	round += 1

#say winner
def decidewinner():
	
	global p1cards
	global p2cards
	
	if len(p1cards)> len(p2cards):
		print(f'{p1} wins!')

	else:
		print(f'{p2} wins!')

print('GAME END')

print(f'{p1} cards:')
input()
print(len(p1cards))

input()

print(f'{p2} cards:')
input()
print(len(p2cards))
input()

decidewinner()