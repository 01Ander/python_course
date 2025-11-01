numbers = []
length = 5


def get_stats(data_list):
    return {
        "max_num": max(data_list),
        "min_num": min(data_list),
        "average_num": sum(data_list)/len(data_list)
    }


for _ in range(length):
    while True:
        try:
            data = int(input("Enter the number "))
            numbers.append(data)
            break
        except ValueError:
            print("That's not a valid number")


stats = get_stats(numbers)
print(f'The complete list: {numbers}')
print(f'The maximum number is: {stats["max_num"]}')
print(f'The minimum number is: {stats["min_num"]}')
print(f'The average is {stats["average_num"]}')
