#include "creditcard.h"

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
long get_card_length(long card)
{
    long count = 0;
    long boolean = 1;
    long test_length = card;
    long whole, remainder;

    // Continue the loop as long as boolean is true (non-zero).
    while (boolean)
    {
        // Divide the test_length by 10 to get the quotient and remainder.
        whole = test_length / 10;
        remainder = test_length % 10;
        test_length = whole;
        boolean = whole;

        count++;
    }

    // Return the calculated length of the credit card number.
    return count;
}
