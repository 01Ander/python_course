for d in range(5):
    print('Iteration', d)

count = 0
while count < 5:
    print("Count is:", count)
    count += 1


number = int(input('Enter a number: '))

for i in range(number):
    print(i+1)

count = 0
while count < number + 1:
    verification = count % 2
    if verification == 0:
        print(count)
    count += 1
