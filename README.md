# LemonMarkets

!! currently under re-construction and not finsihed !!


Building my first algorithm based on the lemon-market API (https://www.lemon.markets/de-de)

Overview of the project:
1. helper.py:
   - contains several helper files and functions to make the API requests reusable
   - enables GET, PUT, POST requests and new token requests

2. .env
   - containing several environment variables, so they can be called in the helper.py file
   - included variables:
     - TOKEN_KEY, CLIENT_ID, CLIENT_SECRET, SPACE_UUID 
     - MIC, BASE_URL_TRADING, BASE_URL_DATA, AUTH_URL

3. Instruments.py
- two functions to get historical OHLC market data and to get the latest OHLC data

4. Order.py
- the order function can place, activate, and see all orders
- as these functionalities are all handled by the API, the function is defined as a sub-class of the ResquestHandler in the helper.py file

5. Token.py
- as the Tokens expires, a function is needed to request a new token

6. TradingVenue.py
- three functions checking if a trading venue is currently open, checking the general opening times for the next days, determining the seconds until the trading venue reopens
