#include "creditcard.h"

/**
 * @file lasts.c
 * @brief Implementation of the function to calculate the sum of last digits in a credit card number.
 */

/**
 * @brief Calculates the sum of last digits in a credit card number.
 *
 * This function iterates through every last digit in the provided credit card number,
 * and adds the result to the sum.
 *
 * @param count The length of the credit card number.
 * @param card The credit card number.
 * @return The sum of last digits in the credit card number.
 */
int lasts(int count, long card)
{
    int remainder;
    int sum = 0;
    long first_whole;

    for (int i = count; i > 0; i -= 2)
    {
        remainder = card % 10;
        first_whole = card / 100;
        card = first_whole;

        sum += remainder;
    }

    return sum;
}
