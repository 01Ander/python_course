numbers = []
length = 5


# como la variable del for no se usa en el loop se nombra _
for _ in range(length):
    while True:
        try:
            data = int(input("Enter the number "))
            numbers.append(data)
            break
        except ValueError:
            print("That's not a valid number")

print(f'The complete list: {numbers}')
print('The maximum number is: ', max(numbers))
print('The minimum number is: ', min(numbers))
average = sum(numbers)/length
print(f'The average is {average}')
