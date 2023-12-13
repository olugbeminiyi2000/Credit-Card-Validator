#include "creditcard.h"

/**
 * @file amex_first_digit.c
 * @brief Implementation of the function to get the first digit of an American Express credit card number.
 */

/**
 * @brief Gets the first digit of an American Express credit card number.
 *
 * This function retrieves the first digit of the provided credit card number
 * when the card type is American Express.
 *
 * @param count The length of the credit card number.
 * @param card The credit card number.
 * @return The first digit of the American Express credit card number.
 */
int amex_first_digit(int count, long card)
{
    long test_length = card;
    long whole, remainder;
    int first;

    for (int i = count; i > 0; --i)
    {
        whole = test_length / 10;
        remainder = test_length % 10;
        test_length = whole;

        if (i != 1)
            continue;

        first = remainder;
    }

    return first;
}
