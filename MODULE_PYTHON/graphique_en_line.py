import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.title("Graphique en line")
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.annotate('Peak', xy=(4, 30), xytext=(3, 28),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
