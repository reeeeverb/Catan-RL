"It's amazing what we can do with computers these days." -- Wallace Wells

## Catan RL
- Great game, gonna code it terribly then put some terrible AI on top of it

#### TO DO 
- ~~implement roads~~
- ~~harbors~~
- ~~bank~~
- ~~turn tree~~
- ~~resource cards~~
- ~~turns~~
- ~~robber~~
- usage of development cards 
- bank and maritime trades
- interperson trading
- ~~building~~
- victory points tracker
- longest road and largest army cards

- finally, front end to make troubleshooting and playing against AI a little more doable

#### Notations
- Settlement and city locations are denoted by the number of the corner they sit on
	- it is 1D starting from top left as 0, there are 54 possibilities
	- internally determining neighbors is done by if you are on a row on the lower half of the board, your even numbered ones must look downward, and vice versa 
- Road locations are denoted by a single number
	- there are 72 possible road locations
	- starting from top left at 0
- Harbor locations are stuck in place as they are in the base game
	- 0 is the top left 
	- there are 9 total

#### Roads
- what a *pain*
- there are 72 possible road locations on a base catan game
	- that is in fact more than 54
```python
72 > 54 # True
```
- the numbering method is going to be the same as the settlements just 0-71 from the top left
- rather than individually numbering which edges contact which im just going to have each road label which two vertices can have roads from the same player build out of them.
- the fucking if statement I wrote for the roads might be the most abysmal thing I have ever written and that is saying something

#### Harbors
- actually a lot easier than I thought they would be
- only one person can own a harbor(because the 2 entrances(?) are within one vertex) so that simplified things a lot
- most of the issues will arise when I have to make the trading interface but cross that bridge

#### Resource Cards
- originally I was just going to add these into the board class but its already a bit large for my liking
	- plus I gave the development cards their own class and that just seems unfair
- Most of this shit was already established its just resource mgmt
	- although I got to use an embedded dict so thats... pretty cool
- honestly not having to fuck with the map and that stupid numbering system was such a needed break

#### Turn Tree
- data structure that is not really a tree but I like aliteration
- everytime a settlement or city is build check every tile it is touch and add the resource+number to the array
- should make dissing out resources on each turn a little faster
- GODDAMN IT I HAVE TO MAP THE VERTICES TO TILES
	- making a vertex map that is a 54 dimension array where each vertex lists its connecting tile(s)
		- do not care if this is wrong, call it an alternative rule set

#### Turns 
- thanks to the turns tree this should be super simple
- roll the two dice, add em up and look up through the turn tree

#### GUI 
- originally I was gonna procrastinate the front end til the very end of the project but at this point most of the things I am programming will be simplified by its existencefor troubleshooting purposes
- gonna use [pygame](pygame.org) because I am simply that guy
	- I have never used pygame before
- gotta do the little glowing effect whenever something needs to be placed
	- the chess.com arcade effect whenever you click on a piece yknow
- im actually having so much fun using pygame, might be the best library I have ever used
- corners are programmatically generated, implementing working with screen rather than numbers now

- show settlements on board
- do edge touch detection for road placement
	- kill me now
	- wasn't that bad, very similar to corner drawings
- rewrite at some point using [sprites](https://realpython.com/lessons/creating-sprites/)

#### Fair Board Generation
- I stumbled upon [this article](https://www.boardgameanalysis.com/the-fair-catan-board-quest/) a while ago while looking for some balanced catan boards to play on with my roommates
- It had some interesting insights as to what a balanced board and doesn't have a lot of solutions but the article does contain a lot of the correct questions.
- if I can get a pretty good catan ai up and running then figuring out what boards are balanced is very easy, just see which games last the longest and come closest to a draw


## Misc.
- I have just stumbled across perhaps the [most annoying Python behavior](https://stackoverflow.com/questions/7745562/appending-to-2d-lists-in-python) I have ever seen
	- why is there just some random C bullshit interjected into python 2D lists?
- This project is the reason why I [disabled the clock in ubuntu](https://extensions.gnome.org/extension/545/hide-top-bar/)
