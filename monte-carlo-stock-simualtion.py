import numpy as np
import matplotlib.pyplot as plt

start_price = 100
days = 252        # trading days in a year
simulations = 50  # number of price paths to simulate
daily_return = 0.0005    # average daily return
daily_volatility = 0.02  # daily volatility (standard deviation)


all_paths = []

for daily_price in range(simulations): #Simulates stock price paths 50 times over 252 trading days using Monte Carlo
    day_price = [start_price]
    while len(day_price) < 252: #Each day's price is detirmined by the previous price scaled by random return
        change = day_price[-1] * (1 + daily_return + daily_volatility * np.random.normal()) #Simplified Geometric Brown Motion (GBM) calculating stock prices
        day_price.append(change)
    all_paths.append(day_price)


for path in all_paths: #plotting all of the different price paths
    plt.plot(path, c = "blue", alpha = 0.3)
plt.title("Annual price paths")
plt.xlabel("days")
plt.ylabel("price")
plt.axhline(y = 110, c = "red", linestyle = "--")
plt.show()


#Calculating the probability of the stock finishing abover 110 (10% more than the original price)
gain = []
for path in all_paths:
    if path[-1] > 110:
        gain.append(path[-1])

prob = len(gain)*100/simulations
print("Probability of finishing above a price of 110: " + str(prob) + "%")

  

  
