import numpy as np
import matplotlib.pyplot as plt

start_price = 100
days = 252        # trading days in a year
simulations = 50  # number of price paths to simulate
daily_return = 0.0005    # average daily return
daily_volatility = 0.02  # daily volatility (standard deviation)


all_paths = []

for daily_price in range(simulations):
    day_price = [start_price]
    while len(day_price) < 252:
        change = day_price[-1] * (1 + daily_return + daily_volatility * np.random.normal())
        day_price.append(change)
    all_paths.append(day_price)


for path in all_paths:
    plt.plot(path, c = "blue", alpha = 0.3)
plt.title("Annual price paths")
plt.xlabel("days")
plt.ylabel("price")
plt.axhline(y = 110, c = "red", linestyle = "--")
plt.show()

gain = []
for path in all_paths:
    if path[-1] > 110:
        gain.append(path[-1])

prob = len(gain)*100/simulations
print(prob)

  

  