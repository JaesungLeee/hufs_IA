# Q4.
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
#
# Then, the output should be:
# LETTERS 10
# DIGITS 3
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

question = input("Enter the sentence with letters and digits : ")
digit_count = 0
letter_count = 0

for i in question:
    if i.isdigit():
        digit_count += 1
    elif i.isalpha():
        letter_count += 1
    else:
        print("No need to count")

print("LETTERS ", letter_count)
print("DIGITS ", digit_count)