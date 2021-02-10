import matplotlib.pyplot as plt
GB = [1, 2, 3, 4, 5, 6, 7]
plan1PRICE = [14, 28, 42, 56, 70, 84, 98]
plan2PRICE = [45, 45, 45, 45, 45, 45, 45]
plt.plot(GB, plan1PRICE, label = "Plan 1")
plt.plot(GB, plan2PRICE, label = "Plan 2")
plt.ylabel('Cost - $')
plt.xlabel('GigaBytes')
xIntersection = 45/14
plt.scatter(xIntersection, 45, color='black')
plt.legend()
plt.show()