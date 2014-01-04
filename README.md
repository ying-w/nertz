# NERTZ!
A card game thats like multiplayer solitare. 

Quick project that I did after talking to an old family friend about it.

Project will be split into 3 parts:

## Coding the game (finished)

I will write the rules for the game in python while my friend writes a java version

## Coding server {work in progress}

Thinking of using event driven model, I started writing some code but I will 
probably have to change things up since client code must run in safari browser
on ipad

## UI

This is the hard part for us since neither of us have any experience with UI.
Our idea is that we will run our program inside a touch enabled browser and 
connect to external computer on lan that acts as a server.

# Example
```
$ python
Python 2.6.6 (r266:84292, Sep 15 2010, 16:22:56)
[GCC 4.4.5] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from nertzplayer import * #import functions into namespace
>>> game = start_game()
testing Score: 0 Cards remaining: 12
0F  | Finished: 0
-N 5♣ -- -- -- -- -- -- -- -- -- -- -- | Cards left: 12
1T T♣
2T A♣
3T 4♢
4T 4♣
-S J♣ K♠ 9♢
>>> move(game, 2, 0)
testing Score: 0 Cards remaining: 12
0F A♣ | Finished: 0
-N 5♣ -- -- -- -- -- -- -- -- -- -- -- | Cards left: 12
1T T♣
2T None!
3T 4♢
4T 4♣
-S J♣ K♠ 9♢
>>> move(game, 'n', 2)
testing Score: 0 Cards remaining: 11
0F A♣ | Finished: 0
-N 8♢ -- -- -- -- -- -- -- -- -- -- | Cards left: 11
1T T♣
2T 5♣
3T 4♢
4T 4♣
-S J♣ K♠ 9♢
>>> draw(game)
testing Score: 0 Cards remaining: 11
0F A♣ | Finished: 0
-N 8♢ -- -- -- -- -- -- -- -- -- -- | Cards left: 11
1T T♣
2T 5♣
3T 4♢
4T 4♣
-S 9♡ 3♡ 3♠
>>> move(game, 's', 1)
testing Score: 0 Cards remaining: 11
0F A♣ | Finished: 0
-N 8♢ -- -- -- -- -- -- -- -- -- -- | Cards left: 11
1T 9♡ T♣
2T 5♣
3T 4♢
4T 4♣
-S 3♡ 3♠ J♣
>>> draw(game)
testing Score: 0 Cards remaining: 11
0F A♣ | Finished: 0
-N 8♢ -- -- -- -- -- -- -- -- -- -- | Cards left: 11
1T 9♡ T♣
2T 5♣
3T 4♢
4T 4♣
-S K♡ T♢ Q♠
>>> draw(game)
testing Score: 0 Cards remaining: 11
0F A♣ | Finished: 0
-N 8♢ -- -- -- -- -- -- -- -- -- -- | Cards left: 11
1T 9♡ T♣
2T 5♣
3T 4♢
4T 4♣
-S 4♠ 7♡ 7♠
>>> draw(game)
testing Score: 0 Cards remaining: 11
0F A♣ | Finished: 0
-N 8♢ -- -- -- -- -- -- -- -- -- -- | Cards left: 11
1T 9♡ T♣
2T 5♣
3T 4♢
4T 4♣
-S 8♣ 5♢ J♠
>>> draw(game)
testing Score: 0 Cards remaining: 11
0F A♣ | Finished: 0
-N 8♢ -- -- -- -- -- -- -- -- -- -- | Cards left: 11
1T 9♡ T♣
2T 5♣
3T 4♢
4T 4♣
-S Q♣ 4♡ 9♠
>>> draw(game)
testing Score: 0 Cards remaining: 11
0F A♣ | Finished: 0
-N 8♢ -- -- -- -- -- -- -- -- -- -- | Cards left: 11
1T 9♡ T♣
2T 5♣
3T 4♢
4T 4♣
-S T♠ 2♠ A♠
>>> draw(game)
testing Score: 0 Cards remaining: 11
0F A♣ | Finished: 0
-N 8♢ -- -- -- -- -- -- -- -- -- -- | Cards left: 11
1T 9♡ T♣
2T 5♣
3T 4♢
4T 4♣
-S A♡ 8♡ 3♢
>>> move(game, 3, 2)
testing Score: 0 Cards remaining: 11
0F A♣ | Finished: 0
-N 8♢ -- -- -- -- -- -- -- -- -- -- | Cards left: 11
1T 9♡ T♣
2T 4♢ 5♣
3T None!
4T 4♣
-S A♡ 8♡ 3♢
>>> move(game, 's', 0)
testing Score: 0 Cards remaining: 11
0F A♣ A♡ | Finished: 0
-N 8♢ -- -- -- -- -- -- -- -- -- -- | Cards left: 11
1T 9♡ T♣
2T 4♢ 5♣
3T None!
4T 4♣
-S 8♡ 3♢ T♠
>>> draw(game)
testing Score: 0 Cards remaining: 11
0F A♣ A♡ | Finished: 0
-N 8♢ -- -- -- -- -- -- -- -- -- -- | Cards left: 11
1T 9♡ T♣
2T 4♢ 5♣
3T None!
4T 4♣
-S K♣ T♡ 9♣
>>> move(game, 's', 3)
testing Score: 0 Cards remaining: 11
0F A♣ A♡ | Finished: 0
-N 8♢ -- -- -- -- -- -- -- -- -- -- | Cards left: 11
1T 9♡ T♣
2T 4♢ 5♣
3T K♣
4T 4♣
-S T♡ 9♣ 8♡
>>> 
```