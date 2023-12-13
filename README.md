# Credit Card Validator

This repository contains a C implementation of a Credit Card Validator program that checks the validity of credit card numbers using Luhn's Algorithm. The program prompts the user for a credit card number and reports whether it is a valid American Express, MasterCard, Visa card, or invalid.

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Implementation Details](#implementation-details)
- [Contributing](#contributing)
- [License](#license)

## Overview

Credit Card Validator implements Luhn's Algorithm to determine the syntactical validity of credit card numbers. It supports American Express (15-digit), MasterCard (16-digit), and Visa (13 or 16-digit) card numbers. The program performs checksum calculations and verifies the structure of credit card numbers.

## Usage

To use the Credit Card Validator, follow these steps:

1. Clone this repository:

```bash
git clone https://github.com/excel-asaph/credit-card-validator.git
cd credit-card-validator
```

2. Compile and run the program:

To compile the program, you can use the `gcc` compiler along with the provided Makefile. Follow these steps:

```bash
gcc -o creditcard_main creditcard_main.c get_card_length.c get_count_outcome.c amex_first_digit.c amex_second_digit.c visa_master_first_digit.c visa_master_second_digit.c visa_first_digit.c second_to_last.c lasts.c -lcs50
./creditcard_main
```

# File Descriptions

## `creditcard_main`

Main program file responsible for user input and validation result output.

## `get_card_length.c`

```c
/**
 * @file get_card_length.c
 * @brief Implementation of the function to get the length of a credit card number.
 */

/**
 * @brief Gets the length of the credit card number.
 *
 * This function calculates the length of the provided credit card number by iteratively
 * dividing it by 10 until the number becomes zero.
 *
 * @param card The credit card number.
 * @return The length of the credit card number.
 */
long get_card_length(long card);
```

## `get_count_outcome.c`

```c
/**
 * @file get_count_outcome.c
 * @brief Implementation of the function to determine the validity of a credit card number based on its length.
 */

/**
 * @brief Determines the validity of the credit card number based on its length.
 *
 * This function returns 1 if the length is not 13, 15, or 16, indicating an invalid length.
 *
 * @param count The length of the credit card number.
 * @return 1 if invalid, 0 if valid.
 */
int get_count_outcome(int count);
```

## `amex_first_digit.c`

```c
/**
 * @file amex_first_digit.c
 * @brief Implementation of the function to retrieve the first digit of an American Express credit card.
 */

/**
 * @brief Retrieves the first digit of an American Express credit card.
 *
 * @param count The length of the credit card number.
 * @param card The credit card number.
 * @return The first digit of the credit card.
 */
int amex_first_digit(int count, long card);
```

## `amex_second_digit.c`

```c
/**
 * @file amex_second_digit.c
 * @brief Implementation of the function to retrieve the second digit of an American Express credit card.
 */

/**
 * @brief Retrieves the second digit of an American Express credit card.
 *
 * @param count The length of the credit card number.
 * @param card The credit card number.
 * @return The second digit of the credit card.
 */
int amex_second_digit(int count, long card);
```

## `visa_master_first_digit.c`

```c
/**
 * @file visa_master_first_digit.c
 * @brief Implementation of the function to retrieve the first digit of a Visa or MasterCard.
 */

/**
 * @brief Retrieves the first digit of a Visa or MasterCard.
 *
 * @param count The length of the credit card number.
 * @param card The credit card number.
 * @return The first digit of the credit card.
 */
int visa_master_first_digit(int count, long card);
```

## `visa_master_second_digit.c`

```c
/**
 * @file visa_master_second_digit.c
 * @brief Implementation of the function to retrieve the second digit of a Visa or MasterCard.
 */

/**
 * @brief Retrieves the second digit of a Visa or MasterCard.
 *
 * @param count The length of the credit card number.
 * @param card The credit card number.
 * @return The second digit of the credit card.
 */
int visa_master_second_digit(int count, long card);
```

## `visa_first_digit.c`

```c
/**
 * @file visa_first_digit.c
 * @brief Implementation of the function to retrieve the first digit of a Visa credit card.
 */

/**
 * @brief Retrieves the first digit of a Visa credit card.
 *
 * @param count The length of the credit card number.
 * @param card The credit card number.
 * @return The first digit of the credit card.
 */
int visa_first_digit(int count, long card);
```

## `second_to_last.c`

```c
/**
 * @file second_to_last.c
 * @brief Implementation of the function to perform calculations on every other digit, starting from the second-to-last digit.
 */

/**
 * @brief Performs calculations on every other digit, starting from the second-to-last digit.
 *
 * @param count The length of the credit card number.
 * @param card The credit card number.
 * @return The sum of calculated values.
 */
int second_to_last(int count, long card);
```

## `lasts.c`

```c
/**
 * @file lasts.c
 * @brief Implementation of the function to perform calculations on the remaining digits.
 */

/**
 * @brief Performs calculations on the remaining digits.
 *
 * @param count The length of the credit card number.
 * @param card The credit card number.
 * @return The sum of calculated values.
 */
int lasts(int count, long card);
```

## `creditcard_main.c`

```c
/**
 * @file creditcard_main.c
 * @brief Main file for the Credit Card Validity Checking program.
 */

/**
 * @brief Main function to check the validity of a credit card number.
 *
 * This function prompts the user for a credit card number, performs various checks
 * using helper functions, and prints the type of the credit card if it's valid.
 *
 * @return 0 if the program executes successfully.
 */
int main(void);
```

# Implementation Details

The program utilizes Luhn's Algorithm, a process that involves the following steps:

1. Multiply every other digit by 2.
2. Sum the digits of those products.
3. Add the sum to the sum of the digits that weren't multiplied by 2.
4. Check if the total's last digit is 0.

# Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make your changes and commit them (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a pull request

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Note:** This project uses the CS50 library for input, credit to CS50 for the library.

