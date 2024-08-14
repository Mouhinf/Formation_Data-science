import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [10, 20, 25, 30]
y2 = [5, 15, 10, 20]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(x, y1, color='blue')
ax2.plot(x, y2, color='red')

ax1.set_title('Plot 1')
ax2.set_title('Plot 2')
plt.show()
