# Actions that will be replaced by gui
# All possible commands from gui

# start game as single player client + hosting

import nertz

def start_game():
    return nertz.Player("testing", 123) #todo: add in server status

# draw next 3 cards and print cards     
def draw(game):
    game.stock_deck.draw()
    game.show()

# move card has 6 possibilities:
# 1. stock to tableau
# 2. stock to foundation
# 3. reserve to tableau
# 4. reserve to foundation
# 5. tableau to tableau
# 6. tableau to foundation
# move card from waste to tableau (1-4) or foundation (0)
def move_stock(game, num):
    if num == 0:
        game.stock_deck.move(game.foundation_local)
    else:
        game.stock_deck.move(game.tableau_deck[num-1])
    game.show()

def move_reserve(game, num):
    if num == 0:
        game.reserve_deck.move(game.foundation_local)
    else:
        game.reserve_deck.move(game.tableau_deck[num-1])
    game.show()

def move_tableau(game, tableau_num, num):
    if num == 0:
        game.tableau_deck[tableau_num-1].move(game.foundation_local)
    else:
        game.tableau_deck[tableau_num-1].move(game.tableau_deck[num-1])
    game.show()
    
def move(game, type, dest):
    if type == "r" or type == "n" or type == "N":
        move_reserve(game, dest)
    elif type == "1T" or type == 1:
        move_tableau(game, 1, dest)
    elif type == "2T" or type == 2:
        move_tableau(game, 2, dest)
    elif type == "3T" or type == 3:
        move_tableau(game, 3, dest)
    elif type == "4T" or type == 4:
        move_tableau(game, 4, dest)
    elif type == 's' or type == 'S' or type == 'stock':
        move_stock(game, dest)

