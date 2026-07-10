# monte-carlo-stock-simulation
This is a Monte Carlo Stock Simulation considering stock prices over a trading year period (252 days) - created in python using NumPy and Matplotlib. 

# What it does:
- Using an intial stock price of 100 this simulates 50 possible paths of stock prices.
- A normal distribution (symmetrical probability distribution) is used to model each days price which is scaled by the previous price and a random daily return.
- A graph is produced containing the 50 different paths.
- The probability of the stock finsihing above the price 110 is calculated.
- A Geometric Brownian Motion (GBM) makes the calculations and develops the potential paths that the stock prices follow. 

# Parameters:
- Start price: 100
- Trading days: 252
- No. simulations: 50
- Daily return: 0.05%
- Daily volatility: 2%

# Result: 
![image_alt](https://github.com/Arch1e710/monte-carlo-stock-simulation/blob/092088f6d5ac1789e29e7a28ac9fd7241e99707b/monte%20carlo%20simulation.png)


                                                        
