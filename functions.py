# name = input("What's your name?")


# def greet(name):
#     print(f'Hello, {name}!')


# greet(name)


# >>>>>>>>>>First Version<<<<<<<<<<<<<<<<<

# number_input = int(input('Enter the number '))


# def check_number(num):
#     if num > 0:
#         print('The number is positive')
#     elif num < 0:
#         print('The number is negative')
#     else:
#         print('The number is zero')


# check_number(number_input)


number_input = float(input('Enter the number '))


def check_number(num):
    if num > 0:
        message = "positive"
    elif num < 0:
        message = "negative"
    else:
        message = "zero"
    return message


status = check_number(number_input)
print(f'The number is {status}')
