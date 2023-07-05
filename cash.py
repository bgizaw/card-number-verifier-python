def main():
    loop = True
    # loop to keep asking user if they would like ot enter another card number
    while loop:
        card_number = int(input("Card Number : "))
        # turn user input into list with each digit as an index
        card_number_list = list(map(int, list(str(card_number))))
        ver = verification(card_number_list)
        # only print the bank name if the card is valid
        if ver:
            print(bank_name(card_number_list))
        else:
            print("INVALID")
        repeat = input("Would you like to enter another card?(y/n): ")
        if repeat.lower() == "y":
            loop = True
        else:
            loop = False


# use the luhn algorithm to verify the card number
def verification(card_number_list):
    # iterate through every other digit of card number starting from the end
    reverse = list(reversed(card_number_list))
    every_other = reverse[1::2]
    remaining = reverse[::2]
    # multiply every digit by two
    doubled = [i * 2 for i in every_other]
    summation = 0
    subtractor = 0

    # if any numbers in the list are above or equal to 10 (meaning they have more than 1 digit)
    # break them up into their digits so they can be added to the sum
    for i in doubled:
        if i >= 10:
            digits = list(map(int, list(str(i))))
            summation += sum(digits)
            # set this variable to the value of the number >= 10, so it can be subtracted from the final sum
            # this makes sure you can find the total of the digits rather than including integers that
            # are multiple digits
            subtractor += i

    summation += sum(doubled)-subtractor
    final_sum = summation + sum(remaining)
    mod = final_sum % 10
    ver = False

    if mod == 0:
        ver = True
    return ver


# use prerequisites to check which bank the card is from
def bank_name(card_number_list):
    length = len(card_number_list)
    if length in [13, 16] and card_number_list[0] == 4:
        visa = "Visa"
        return visa
    elif length == 15 and card_number_list[0:2] in ([3,4], [3,7]):
        amex = "Amex"
        return amex
    elif length == 16 and card_number_list[0:2] in ([5,1], [5,2], [5,3], [5,4], [5,5]):
        mastercard = "MasterCard"
        return mastercard
    # if the card is form a different bank, return "other"
    else:
        other = "other"
        return other


main()
