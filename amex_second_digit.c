#include "creditcard.h"

/**
 * @file amex_second_digit.c
 * @brief Implementation of the function to get the second digit of an American Express credit card number.
 */

/**
 * @brief Gets the second digit of an American Express credit card number.
 *
 * This function retrieves the second digit of the provided credit card number
 * when the card type is American Express.
 *
 * @param count The length of the credit card number.
 * @param card The credit card number.
 * @return The second digit of the American Express credit card number.
 */
int amex_second_digit(int count, long card)
{
    long test_length = card;
    long whole, remainder;
    int second;

    for (int i = count; i > 0; --i)
    {
        whole = test_length / 10;
        remainder = test_length % 10;
        test_length = whole;

        if (i != 2)
            continue;

        second = remainder;
    }

    return second;
}
