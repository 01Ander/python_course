numbers = []
length = 5


def get_stats(data_list):
    max_num = max(data_list)
    min_num = min(data_list)
    ave_num = sum(data_list)/len(data_list)
    return max_num, min_num, ave_num


for _ in range(length):
    while True:
        try:
            data = int(input("Enter the number "))
            numbers.append(data)
            break
        except ValueError:
            print("That's not a valid number")


max_stats, min_stats, ave_stats = get_stats(numbers)
print(f'The complete list: {numbers}')
print(f'The maximum number is: {max_stats}')
print(f'The minimum number is: {min_stats}')
print(f'The average is {ave_stats}')


# este es un ejemplo de tupla dentro de python
