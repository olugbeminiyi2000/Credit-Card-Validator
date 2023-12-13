#ifndef CREDITCARD_H
#define CREDITCARD_H

/**
 * @file creditcard.h
 * @brief Header file for checking credit card validity using Luhn's Algorithm.
 */

long get_card_length(long card);
int get_count_outcome(int count);
int amex_first_digit(int count, long card);
int amex_second_digit(int count, long card);
int visa_master_first_digit(int count, long card);
int visa_master_second_digit(int count, long card);
int visa_first_digit(int count, long card);
int second_to_last(int count, long card);
int lasts(int count, long card);

#endif
