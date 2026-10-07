print("Water Jug Problem")
x = int(input("Enter X (0-4): "))
y = int(input("Enter Y (0-3): "))
steps = 0
while True:
    print("\nCurrent State:")
    print("X =", x)
    print("Y =", y)
    print("\nRules:")
    print("1. Fill Jug X")
    print("2. Fill Jug Y")
    print("3. Pour X into Y")
    print("4. Pour Y into X")
    print("5. Empty Jug X")
    print("6. Empty Jug Y")
    print("7. Pour Y into X until X is full")
    print("8. Pour X into Y until Y is full")
    print("9. Pour X into Y completely")
    print("10. Pour Y into X completely")
    rule = int(input("\nEnter the Rule No: "))
    if rule == 1:
        if x < 4:
            x = 4
            steps += 1
    elif rule == 2:
        if y < 3:
            y = 3
            steps += 1
    elif rule == 3:
        amount = min(x, 3 - y)
        x -= amount
        y += amount
        steps += 1
    elif rule == 4:
        amount = min(y, 4 - x)
        y -= amount
        x += amount
        steps += 1
    elif rule == 5:
        if x > 0:
            x = 0
            steps += 1
    elif rule == 6:
        if y > 0:
            y = 0
            steps += 1
    elif rule == 7:
        if x + y >= 4 and y > 0:
            y = y - (4 - x)
            x = 4
            steps += 1
    elif rule == 8:
        if x + y >= 3 and x > 0:
            x = x - (3 - y)
            y = 3
            steps += 1
    elif rule == 9:
        if x + y <= 4 and y > 0:
            x = x + y
            y = 0
            steps += 1
    elif rule == 10:
        if x + y <= 3 and x > 0:
            y = x + y
            x = 0
            steps += 1
    else:
        print("Invalid rule!")
        continue
    if x == 2:
        print("\nX =", x)
        print("Y =", y)
        print("The result is a Goal State.")
        print("Minimum/Total steps used:", steps)
        break