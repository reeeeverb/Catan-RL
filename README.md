## Catan RL
- Great game, gonna code it terribly then put some terrible AI on top of it

#### TO DO 
- implement roads
- harbors
- resource cards
- turns
- robber
- usage of development cards 
- interperson trading
- building
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
	- that is more than 

#### Fair Board Generation
- I stumbled upon [this article](https://www.boardgameanalysis.com/the-fair-catan-board-quest/) a while ago while looking for some balanced catan boards to play on with my roommates
- It had some interesting insights as to what a balanced board and doesn't have a lot of the solution but the article does contain a lot of the correct questions.
