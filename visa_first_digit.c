#include "creditcard.h"

/**
 * @file visa_first_digit.c
 * @brief Implementation of the function to get the first digit of a Visa credit card number.
 */

/**
 * @brief Gets the first digit of a Visa credit card number.
 *
 * This function retrieves the first digit of the provided Visa credit card number.
 *
 * @param count The length of the credit card number.
 * @param card The Visa credit card number.
 * @return The first digit of the Visa credit card number.
 */
int visa_first_digit(int count, long card)
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
