# Nertz! card game, rules based on julie's variant
# Author: Ying Wu working w/Michael Chen
# Last updated: Jan 2014

# todo: activity log for rollback
# make private/public variables and function names
#   http://stackoverflow.com/questions/70528/why-are-pythons-private-methods-not-actually-private
#   http://www.diveintopython.net/object_oriented_framework/private_functions.html
# follow style guide more closely
#   http://www.python.org/dev/peps/pep-0008/
# maybe clean up some self vs class stuff
#   http://stackoverflow.com/questions/12031571/self-variable-in-python-vs-class-variable
# handling no possible movie scenario
# remember to exit and re-import when testing
#
# resources:
# http://www.tutorialspoint.com/python/python_functions.htm
# http://www.diveintopython.net/object_oriented_framework/defining_classes.html
# http://docs.python.org/3/tutorial/classes.html
# http://docs.python.org/2/tutorial/classes.html
# http://www.joelonsoftware.com/articles/Unicode.html
# http://docs.python.org/2/tutorial/modules.html

# convert numerical format to cards
# cards will be stored as follows:
# Clubs     1-K = 0-12
# Diamonds  1-K = 13-25
# Hearts    1-K = 26-38
# Spades    1-K = 39-51
# use card%13 to get card (0-9 is 1-10, 10 is J, 11 is Q, 12 is K)
# use card/13 to get suit (0 = clubs, 1 = diamonds, 2 = hearts, 3 = spades)
def get_card(num) : 
    
    suitchar = "_"
    numchar = "0"
    cardnum = num%13
    cardsuit = num/13
    
    if cardsuit > 3 or cardsuit < 0 :
        raise Exception("Invalid card suit")
    if cardnum > 12 or cardnum < 0 :
        raise Exception("Invalid card number")        
     
    # todo: catch unicode for windows
    # http://stackoverflow.com/questions/6725249/how-to-print-a-unicode-string-in-python-in-windows-cmd
    # if sys.platform == "win32": 
    
    # http://unicode-table.com/en/sets/suits-of-the-cards/
    if cardsuit == 0 : # clubs
        suitchar = u"\u2663" # u2667
    elif cardsuit == 1 : # diamonds
        suitchar = u"\u2662" # u2666
    elif cardsuit == 2 : # hearts
        suitchar = u"\u2661" # u2665
    elif cardsuit == 3 : # spades
        suitchar = u"\u2660" # u2664
        
    if cardnum == 0 :
        numchar = 'A'
    elif cardnum == 9 :
        numchar = 'T'
    elif cardnum == 10 :
        numchar = 'J'
    elif cardnum == 11 :
        numchar = 'Q'
    elif cardnum == 12 :
        numchar = 'K'
    else :
        numchar = str(cardnum+1)
        
    return numchar+suitchar

def shuffle_deck(seed = None) :
    # http://docs.python.org/2/library/random.html
    # alternative: http://code.activestate.com/recipes/272884-random-samples-without-replacement/
    
    import random
    if seed != None : random.seed(seed) #for testing 
    return random.sample(range(52), 52)
    
    '''
    # old way
    deck_clubs = random.sample(range(1, 13), 13 )
    deck_hearts = random.sample(range(1, 13), 13 )
    deck_diamonds = random.sample(range(1, 13), 13 )
    deck_spades = random.sample(range(1, 13), 13 )
    
    deck_hearts = deck_hearts + 20
    deck_diamonds = deck_diamonds + 40
    deck_spades = deck_spades + 60
    
    deck = zip(deck_clubs, deck_hearts, deck_diamonds, deck_spades)
    '''

class Reserve:

    def __init__(self, cards):
        self.deck = cards
    
    def show(self):
        print "-N\t"+get_card(self.deck[1]) + " --"*(len(self.deck)-1) + " | Cards left: " + str(len(self.deck))
        
    def move(self, dest_deck):
        if(dest_deck.add(self.deck[1])):
            self.deck.pop(1)
            return len(self.deck)
        else:
            raise Exception("Not a valid move")

class Tableau:

    def __init__(self, card, num):
        self.deck = [card]
        self.num = num # tableau number
    
    def add(self, card):
        if(len(self.deck) == 0):
            self.deck.append(card)
            return 1
        elif(card in self.next_card(self.deck[len(self.deck)-1])):
            self.deck.append(card)
            return len(self.deck) # all numbers greater than 0 are true
                             # http://docs.python.org/2/library/stdtypes.html#truth-value-testing
        else:
            raise Exception("Not a valid move")
            return 0
            
    def move(self, dest_deck): # could be extension of deck class
        if(dest_deck.add(self.deck[len(self.deck)-1])):
            self.deck.pop()
            return len(self.deck)
        else:
            raise Exception("Not a valid move")
            
    def show(self): #card on left will be bottom card
        if(len(self.deck) > 0) :
            # use list comprehension and also index backwards
            # http://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
            # http://stackoverflow.com/questions/4048964/printing-tab-separated-values-of-a-list
            print(self.num+"T\t"+' '.join([get_card(self.deck[i]) for i in range(len(self.deck)-1,-1,-1)]))
        else:
            print self.num+"T\tNone!"
    
    def next_card(self, card): # alternating suit of lower number
        cur_suit = card/13
        cur_num = card%13
        
        match = [-1, -1]
        
        if(cur_num == 0): # Aces
            raise Exception("Cannot add card to ace")
        
        if(cur_suit in [0,3]): # black
            match[0] = cur_num-1 + 13*1
            match[1] = cur_num-1 + 13*2
        elif(cur_suit in [1,2]): # red
            match[0] = cur_num-1
            match[1] = cur_num-1 + 13*3
        else:
            raise Exception("Invalid card suit")
        
        return match

# cards you draw from, waste deck is combined into this class
class Stock:
    
    def __init__(self, cards):
        self.deck = cards
        self.current = 2
        
    def draw(self):
        self.current += 3
        if self.current >= len(self.deck):
            print "END OF DECK!"
            self.current = 2
        if len(self.deck) < 3: #catch rare edge case
            self.current = len(self.deck)-1
        if len(self.deck) == 0: #catch rare edge case
            raise Exception("Deck is empty!")
    
    def move(self, dest_deck): # could be extension of deck class
        if(dest_deck.add(self.deck[self.current])):
            self.deck.pop(self.current)
            self.current -= 1
            if(self.current < 0): #edge case
                self.current = 2
            return len(self.deck)
        else:
            raise Exception("Not a valid move")
    
    def show(self):
        print("-S\t"+' '.join([nertz.get_card(deck[i]) for i in range(self.current, max(-1,self.current-3), -1)]))
    '''
        # does not account for case where current is < 2
        print("-S\t"+get_card(self.deck[self.current])+
            ' '+get_card(self.deck[self.current-1])+
            ' '+get_card(self.deck[self.current-2]))
    '''
    
# Only hold top card
class Foundation:

    def __init__(self):
        self.decks = []
        self.points = 0
        self.finished = 0 # fun stat
    
    def add(self, card):
        if(self.update(card)):
            self.points += 1
            return True
        else:
            raise Exception("Not a valid move")
            
    def update(self, card):
        if(card%13 == 0): # Aces
            #self.decks.append([card])
            self.decks.append(card)
            return len(self.decks)
        else: #search
            if(self.decks.count(card-1)):
                i = self.decks.index(card-1)
                self.decks[i] += 1
                if(card%13 == 12): #King
                    self.decks.pop(i)
                    self.finished += 1
                return True
            return False
    
    def show(self):
        print("0F\t"+' '.join([get_card(self.decks[i]) for i in range(len(self.decks))]) + 
            " | Finished: " + str(self.finished))

# player
class Player:
        
    def __init__(self, name = "nertz player", seed = None):
    
        self.name = name
        self.score = 0
        self.winner = []
        
        if(seed):
            self.deck = shuffle_deck(seed)
        else:
            self.deck = shuffle_deck()
        self.reserve_deck = Reserve(self.deck[0:12])
        self.stock_deck = Stock(self.deck[16:52])
        self.foundation_local = Foundation()
        
        # create 4 empty Tableaus
        self.tableau_deck = []
        self.tableau_deck.append(Tableau(self.deck[12], "1"))
        self.tableau_deck.append(Tableau(self.deck[13], "2"))
        self.tableau_deck.append(Tableau(self.deck[14], "3"))
        self.tableau_deck.append(Tableau(self.deck[15], "4"))
        
        self.show()

    def show(self):
        print self.name + "\tScore: " + str(self.score) + \
            "\tCards remaining: " + str(len(self.reserve_deck.deck))
        self.foundation_local.show()
        self.reserve_deck.show()
        for i in range(4): #len(self.tableau_deck)):
            self.tableau_deck[i].show()
        self.stock_deck.show()
    
    def game_over(win) :
        score += foundation_local.points - len(reserve_deck.deck)
        winner.append(win)
        return score
    
