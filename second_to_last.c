#include "creditcard.h"

/**
 * @file second_to_last.c
 * @brief Implementation of the function to calculate the sum of second-to-last digits in a credit card number.
 */

/**
 * @brief Calculates the sum of second-to-last digits in a credit card number.
 *
 * This function iterates through every second-to-last digit in the provided credit card number,
 * multiplies it by 2, and adds the result to the sum.
 *
 * @param count The length of the credit card number.
 * @param card The credit card number.
 * @return The sum of second-to-last digits in the credit card number.
 */
int second_to_last(int count, long card)
{
    int sum = 0;
    int two_product, first_value, second_value, remainder;
    long first_whole, second_whole;

    for (int i = count; i > 0; i -= 2)
    {
        first_whole = card / 10;
        remainder = first_whole % 10;
        second_whole = first_whole / 10;
        card = second_whole;

        // Multiply remainder by 2
        two_product = remainder * 2;

        if (two_product > 9)
        {
            first_value = two_product / 10;
            second_value = two_product % 10;
            sum += first_value + second_value;
        }
        else
        {
            sum += two_product;
        }
    }

    return sum;
}
