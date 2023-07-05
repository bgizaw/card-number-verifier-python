def main():
    card_number = int(input("Card Number : "))
    # turn user input into list with each digit as an index
    card_number_list = list(map(int, list(str(card_number))))
    ver = verification(card_number_list)
    if ver:
        print(bank_name(card_number_list))
    else:
        print("INVALID")


# use the luhn algorithm to verify the card number
def verification(card_number_list):
    reverse = list(reversed(card_number_list))
    every_other = reverse[1::2]
    remaining = reverse[::2]
    doubled = [i * 2 for i in every_other]
    summation = 0
    subtractor = 0

    for i in doubled:
        if i >= 10:
            digits = list(map(int, list(str(i))))
            summation += sum(digits)
            subtractor += i

    summation += sum(doubled)-subtractor
    final_sum = summation + sum(remaining)
    mod = final_sum % 10
    ver = False

    if mod == 0:
        ver = True
    return ver


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
    else:
        other = "other"
        return other



main()
