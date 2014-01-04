#!/usr/bin/env python
# Work in progress, see nertz.py for details

# When acting as nertz server this program will keep track of
# 1. total number of players
# 2. name of all players
# 3. score for all players
# 4. current global foundation
#
# Functions:
# 1. init (playernames)
# 2. declare winner
# 3. calculate and update score
# 4. track/update reserve
# 5. notify reserve updates
# 6. track/update foundation
# 7. notify foundation updates (and conflicts)
#
# Win conditions are by numnber of games and score
# server should store local copy
#
# Nertz game can start in 3 modes
# 1. host + player
# 2. player
# 3. host only

# guide
# http://ilab.cs.byu.edu/python/socketmodule.html
# other reading
# http://sourceforge.net/projects/eventdrivenpgm/files/
# http://www.pythonschool.net/eventdrivenprogramming

import select 
import socket 
import sys 
import threading 

class nertz_server:

    def __init__(self, port = 58692, numplayers):
        self.host = '' 
        self.port = port 
        self.backlog = 5 
        self.size = 1024 
        self.server = None 
        self.threads = [] 
        
        self.playernum = numplayers
        self.playernames = []
        self.playerscore = [] #2d list

        # command queue
    
    def add_player:
        # check if game started
    
    def start_game:
    
    def get_scores:

class nertz_client:

    def __init__(self):
    
    

# based on function from nertz.py
# keep track of what player the card came from
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

    
