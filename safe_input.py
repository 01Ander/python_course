def check_number(num):
    if num > 0:
        message = "positive"
    elif num < 0:
        message = "negative"
    else:
        message = "zero"
    return message


while True:
    try:
        number_input = float(input('Enter the number '))
        status = check_number(number_input)
        print(f'The number is {status}')
        break
    except ValueError:
        print("That's not a valid number")
