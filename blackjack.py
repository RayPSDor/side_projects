#random.randint(1,10) - generates random # between 1 and 10
#random.shuffle(x) - shuffles variables in x
import random, os, time, sys

#Initializing Classes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Card(object):

    cardVal = {
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
        'Six': 6,
        'Seven': 7,
        'Eight': 8,
        'Nine': 9,
        'Ten': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10,
        'Ace': 11
    }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show_card(self):
        print '%s of %s' %(self.value, self.suit)

    def card_value(self):
        return self.cardVal[self.value]

class Deck(object):

    values = {
        1: 'Ace',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Jack',
        12: 'Queen',
        13: 'King'
    }

    def __init__(self):
        self.cards = []

    def build(self):
        for suit in ['Clubs', 'Spades', 'Hearts', 'Diamonds']:
            for val in self.values:
                #appends Card() objects to list
                self.cards.append(Card(self.values[val], suit))

    # def show_deck(self):
    #     #loops through elements in self.cards
    #     for i in self.cards:
    #         #i represents Card() objects within self.cards list,
    #         #so to access suits and values we must use i.show_card()
    #         #defined in Card() class
    #         i.show_card()

    def shuffle(self):
        return random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

class Player(object):

    def __init__(self, deck, name):
        self.deck = deck
        self.hand = []

    def draw(self):
        self.hand.append(self.deck.draw_card())

    def show_hand(self):
        for card in self.hand:
            card.show_card()

    # def hand_value(self):
    #     score = 0
    #     for card in self.hand:
    #         score += card.card_value()
    #     return score

class Dealer(Player):
    pass

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

os.system('clear')
print 'RayDor\'s BlackJack|'
print '__________________|\n'
time.sleep(.3)

#initializing deck
deck = Deck()
deck.build()
deck.shuffle()

#initializing player
name = raw_input('Enter Player Name: ')
os.system('clear')
player = Player(deck, name)

#initializing dealer
dealer = Dealer(deck, 'house')

#starting game
def play_blackjack():

    #clearing board
    os.system('clear')
    del player.hand[:]
    del dealer.hand[:]

    playerScore = 0
    dealerScore = 0
    aceClause = False
    aceClause2 = False
    print 'Dealing Starting Hand'
    print '.....................'
    time.sleep(.5)


    while True:
        if len(player.hand) < 2 and len(dealer.hand) < 2:
            player.draw()
            playerScore += player.hand[-1].card_value()
            dealer.draw()
            dealerScore += dealer.hand[-1].card_value()
            player.draw()
            if playerScore > 10 and player.hand[-1].value == 'Ace':
                playerScore += 1
                aceClause = True
            else:
                playerScore += player.hand[-1].card_value()
            dealer.draw()
            if dealerScore > 10 and dealer.hand[-1].value == 'Ace':
                dealerScore += 1
                aceClause2 = True
            else:
                dealerScore += dealer.hand[-1].card_value()
            print '%s\'s Hand' %name
            player.show_hand()
            print '\n%s\'s Score:' %name ,playerScore
            print '\nDealer\'s Hand:'
            dealer.hand[0].show_card()
            print '(Facedown Card)\n'
            print 'Dealer\'s Score:',dealer.hand[0].card_value(),'\n'
            if playerScore == 21:
                time.sleep(1)
                print 'Blackjack! Dealer Must Tie or You Win!'
                time.sleep(1.5)
                break
        else:
            choice = raw_input('1. Hit\n2. Stand\n>> ')
            if choice == '1':
                time.sleep(.5)
                print '\n',
                #print '\n'
                #os.system('clear')
                player.draw()
                print '%s\'s Hand:' %name
                player.show_hand()
                if playerScore > 10 and player.hand[-1].value == 'Ace':
                    playerScore += 1
                    aceClause = True
                else:
                    playerScore += player.hand[-1].card_value()
                for i in player.hand:
                    if i.value == 'Ace' and playerScore > 21 and aceClause == False:
                        playerScore -= 10
                        aceClause = True
                print '\n%s\'s Score:' %name,playerScore
                print '\nDealer\'s Hand:'
                dealer.hand[0].show_card()
                print '(Facedown Card)\n'
                print 'Dealer\'s Score:',dealer.hand[0].card_value(),'\n'
                if playerScore == 21:
                    time.sleep(1)
                    print 'Blackjack! Dealer Must Tie or %s wins!' %name
                    time.sleep(1)
                    break
                if playerScore > 21:
                    time.sleep(1)
                    print 'BUST! Dealer Wins :('
                    time.sleep(1)
                    play = raw_input('\nPlay Again? (y/n): ')
                    if play == 'y':
                        play_blackjack()
                    else:
                        sys.exit(0)
            else:
                time.sleep(.5)
                break

    # print '\n%s\'s Hand:' %name
    # player.show_hand()
    # print '\nScore:',playerScore
    print '\nDealer Hand:'
    dealer.show_hand()
    print '\nDealer\'s Score:',dealerScore,
    print '\n'
    time.sleep(1.5)

    while True:
        if playerScore == 21 and dealerScore == 21:
            print '\'Tis a stalemate'
            time.sleep(1)
            play = raw_input('\nPlay Again? (y/n): ')
            if play == 'y':
                play_blackjack()
            else:
                sys.exit(0)

        # if dealerScore == 21 and playerScore < 21:
        #     print 'Dealer Got Blackjack. :('
        #     time.sleep(1)
        #     play = raw_input('\nPlay Again? (y/n): ')
        #     if play == 'y':
        #         play_blackjack()
        #     else:
        #         sys.exit(0)

        if dealerScore <= playerScore:
            dealer.draw()
            print 'Dealer\'s Hand:'
            dealer.show_hand()
            if dealerScore > 10 and dealer.hand[-1].value == 'Ace':
                dealerScore += 1
                aceClause2 = True
            else:
                dealerScore += dealer.hand[-1].card_value()
            for i in dealer.hand:
                if i.value == 'Ace' and dealerScore > 21 and aceClause2 == False:
                    dealerScore -= 10
                    aceClause2 = True
            print '\nDealer\'s Score:',dealerScore,
            print '\n'
            time.sleep(1.5)

        if dealerScore > 21:
            print 'Dealer Busted! %s wins!' %name
            time.sleep(1)
            play = raw_input('\nPlay Again? (y/n): ')
            if play == 'y':
                play_blackjack()
            else:
                sys.exit(0)

        if playerScore < dealerScore:
            print 'Dealer Wins :('
            play = raw_input('\nPlay Again? (y/n): ')
            if play == 'y':
                play_blackjack()
            else:
                sys.exit(0)

play_blackjack()
