# card-number-verifier-python
reads a card number inputted by the user and returns if it is valid and from what bank the card is made (Amex, Mastercard, or Visa)

## Luhn Algorithm
<sub> **Most card numbers are made using an algorithm invented by Hans Peter Luhn of IBM. You can determine if any credit card number is syntactically valid using the following algorithm:**
1. Multiply every other digit by 2, starting with the second-to-last digit of the card number, then add all those products together
2. Add the previous sum to the sum of the digits remaining in the number that you did not multiply by 2
3. If the total you received after completing step 2 has a final digit of 0, then the card number is valid. In code, you can find the last digit by using the % (modulo) operator to find the modulo between your sum and 10 (sum % 10), which will return the remainder left over after you divide your sum by 10. Since only a number ending with the digit 0 would return a remainder of 0, if your modulo operation returns 0, then the card number is valid.</sub>
