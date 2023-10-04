import matplotlib.pyplot as plt

# Sample data as a list of tuples (x, y)
data = [(1, 10), (2, 16), (3, 8), (4, 14), (5, 12)]

# Extract x and y values using zip and unpacking
x, y = zip(*data)

# Create a line chart
plt.plot(x, y)

# Add labels and a title
plt.xlabel('Дни')
plt.ylabel('Количество товаров')
plt.title('Статистика парсинга')

# Display the chart
plt.show()
