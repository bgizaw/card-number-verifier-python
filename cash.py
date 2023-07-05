def main():
    cardNumber = int(input("Card Number :"))
    cardNumberList = list(map(int, list(str(cardNumber))))
    checker(cardNumberList)
    

def checker(cardNumberList):
    everyOther = cardNumberList[::2]
    upEveryOther = cardNumberList[1::2]
    reverse = list(reversed(everyOther))
    doubledReverse = [i*2 for i in reverse]
    summation = 0
    subtractor = 0
    for i in doubledReverse:
        if i>=10:
            digits = list(map(int, list(str(i))))
            summation += sum(digits)
            subtractor += i
    summation += sum(doubledReverse)-subtractor
    finalSum = summation + (sum(upEveryOther))
    print(finalSum)


    



        
    
    



    


main()