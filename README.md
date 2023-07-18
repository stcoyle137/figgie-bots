# Design Plans/Checklist (TODOs)

Setup API:

	- Make a api using the flask_restful library for connection to bots
 
		- Trades(Bids, Puts, Out, etcs)
  
		- Connection to game (unique player id, entering the game, etc)
  
		- Get the Book
  
    - Rate limiting (can only make x number of trades in y seconds)
    
  -Provide brief documentation (Possibly not need if template is create)


Good start for the API section: https://www.geeksforgeeks.org/python-build-a-rest-api-using-flask/


Setup Backend Market:

  - Store the current book and round history
    
  - Update the market with player input
    
      - Possibly Multi-threaded to prevent overwhelming the market
        
  - Settle the prize


Some simple code has been written for the market so far. My design plan is to seperate the book/market from the players using Object Oriented Programming but feel free to change as you wish


Template for bots/Parent class development:

  - Create a wrapper class to handle the API calls so bot makers can quick do development


This should be quick once we have the API working and is just to make lives easier in the future.

# Practices
Try to comment code for any funking business and include a doc string for functions. I'm not the best example, but it will make a team project go smoother if some amount of comments/consistence is used.

Use snake_case for functions and CamelCase for classes please
