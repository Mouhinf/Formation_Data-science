import matplotlib.pyplot as plt

x = ['A', 'B', 'C', 'D', 'E']
y = [10, 20, 25, 30, 35]
plt.bar(x, y, color = "blue")
plt.title("Diagramme en barre")
plt.xlabel('x')
plt.ylabel('y')
plt.show()