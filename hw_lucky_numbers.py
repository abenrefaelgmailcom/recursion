import random


def get_lucky_numbers(amount: int) -> tuple[int]:
    # create empty list to collect numbers
    numbers = []

    # loop amount times
    for _ in range(amount):
        # generate random number between 1 and 100
        num = random.randint(1, 100)

        # add number to list
        numbers.append(num)

    # convert list to tuple and return
    return tuple(numbers)


def input_until_lucky(lucky_numbers: tuple) -> int:
    # counter for number of attempts
    attempts = 0

    while True:
        try:
            # ask user for number
            user_input = int(input("Enter a number: "))

            # increase attempts
            attempts += 1

            # check if number is lucky
            if user_input in lucky_numbers:
                print("You guessed a lucky number!")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    # return number of attempts
    return attempts


# -------------------------
# Example run
# -------------------------

lucky = get_lucky_numbers(3)

print("Lucky numbers:", lucky)

tries = input_until_lucky(lucky)

print("Attempts:", tries)
