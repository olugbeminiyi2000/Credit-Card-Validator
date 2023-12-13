#include "creditcard.h"

/**
 * @file get_count_outcome.c
 * @brief Implementation of the function to check the outcome of the credit card number length.
 */

/**
 * @brief Checks the outcome of the credit card number length.
 *
 * This function checks whether the provided credit card number length is valid.
 * It returns 1 if the length is not 13, 15, or 16; otherwise, it returns 0.
 *
 * @param count The length of the credit card number.
 * @return 1 if the length is not 13, 15, or 16; otherwise, 0.
 */
int get_count_outcome(int count)
{
    // Check if the count is not 13, 15, or 16.
    if (count != 13 && count != 15 && count != 16)
    {
        return 1;
    }

    return 0;
}
