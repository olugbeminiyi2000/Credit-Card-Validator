#include "creditcard.h"
#include <cs50.h>
#include <stdio.h>

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
int main(void)
{
    long long int card;

    // Prompt the user for a credit card number.
    do
    {
        card = get_long("Number: ");
    }
    while (card < 0);

    // Get the length of the credit card number.
    int count = get_card_length(card);

    // Check if the length is valid.
    int outcome = get_count_outcome(count);
    if (outcome == 1)
    {
        printf("INVALID\n");
        return 0;
    }

    // Calculate the sum of second-to-last and last digits.
    int second_to_lasts = second_to_last(count, card);
    int last = lasts(count, card);
    int total_sum = second_to_lasts + last;

    // Check if the total sum is divisible by 10.
    if (total_sum % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    // Check the type of credit card and print the result.
    if (count == 15)
    {
        int amex_first = amex_first_digit(count, card);
        int amex_second = amex_second_digit(count, card);
        if (amex_first == 3 && (amex_second == 4 || amex_second == 7))
        {
            printf("AMEX\n");
        }
        else
        {
            printf("INVALID\n");
            return 0;
        }
    }
    else if (count == 16)
    {
        int visa_master = visa_master_first_digit(count, card);
        if (visa_master == 4)
        {
            printf("VISA\n");
        }
        else if (visa_master == 5)
        {
            int visa_master_second = visa_master_second_digit(count, card);
            if (visa_master_second != 1 && visa_master_second != 2 && visa_master_second != 3 && visa_master_second != 4 &&
                visa_master_second != 5)
            {
                printf("INVALID\n");
                return 0;
            }
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
            return 0;
        }
    }
    else
    {
        int visa_first = visa_first_digit(count, card);
        if (visa_first == 4)
        {
            printf("VISA\n");
        }
        return 0;
    }

    return 0;
}
