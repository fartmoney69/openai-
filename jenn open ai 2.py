colors = []

# Append colors to the list using a while loop
while True:
    color = input("Enter a color (or type 'done' to stop): ")
    if color == 'done':
        break
    colors.append(color)

# Traverse the list and print each element using a for loop
for i in range(len(colors)):
    print(colors[i])
