<div align="center">

# Credit Card Validator


**A simple Python program to validate credit card numbers using the Luhn algorithm and determine the associated bank.**


</div>

## Description

The **Credit Card Validator** is a Python program that validates credit card numbers using the Luhn algorithm and identifies the associated bank. It provides a reliable way to check the validity of a credit card and determine if it belongs to Visa, Amex, MasterCard, or another bank.

## Features

- Validates credit card numbers using the Luhn algorithm
- Identifies the associated bank (Visa, Amex, MasterCard, or Other)
- User-friendly command-line interface
- Fast and efficient algorithm

## Usage

1. Make sure you have Python 3.x installed on your machine.
2. Clone this repository or download the `credit_card_validator.py` file.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the following command to execute the program:

   ```shell
   python credit_card_validator.py

## Examples 
**[*You may also look through the example credit card numbers listed in this link to test the code*](https://developer.paypal.com/api/nvp-soap/payflow/integration-guide/test-transactions/#standard-test-cards)**

```shell
$ python credit_card_validator.py
Card Number: 1234567890123456
INVALID
```

```shell
$ python credit_card_validator.py
Card Number: 4111111111111111
Bank: Visa
