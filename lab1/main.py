import math


# Find The greatest common divisor of multiple numbers read from the console.
def ex1():
    numbers = [int(x) for x in input().split()]
    div = numbers[0]
    for x in numbers[1:]:
        div = math.gcd(div, x)
    print(div)


# Write a script that calculates how many vowels are in a string.
def ex2():
    string = input().lower()
    no_vowels = 0
    for x in string:
        if x in 'aeiou':
            no_vowels += 1
    print(no_vowels)


# Write a script that receives two strings and prints the number of occurrences of the first string in the second.
def ex3(first, second):
    print(second.count(first))


# Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
def ex4(string):
    result = string[0].lower()
    for x in string[1:]:
        if 'A' <= x <= 'Z':
            result += "_" + x.lower()
        else:
            result += x
    print(result)


# Given a square matrix of characters, write a script that prints the string obtained by going through the matrix in
# spiral order (as in the example): firs      1  2  3  4    =>   first_python_lab n_lt      12 13 14 5 oba_      11
# 16 15 6 htyp      10 9  8  7
# matrix = [
#         ['f', 'i', 'r', 's'],
#         ['n', '_', 'l', 't'],
#         ['o', 'b', 'a', '_'],
#         ['h', 't', 'y', 'p']
#     ]
def ex5(matrix):
    string = ""
    n = len(matrix)
    cycles = (n + 1) // 2
    for c in range(cycles):
        for i in range(c, n - c):
            string += matrix[c][i]
        for i in range(c + 1, n - c):
            string += matrix[i][n - c - 1]
        for i in range(n - c - 2, c - 1, -1):
            string += matrix[n - c - 1][i]
        for i in range(n - c - 2, c, -1):
            string += matrix[i][c]
    print(string)


# Write a function that validates if a number is a palindrome.
def ex6(string):
    if string == string[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")


# Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function
# will return 123, or if the text is "abc123abc" the function will extract 123). The function will extract only the
# first number that is found.
def ex7(string):
    index = 0
    nr = 0
    while string[index] < '0' or string[index] > '9':
        index += 1
    while index < len(string) and '0' <= string[index] <= '9':
        nr = nr * 10 + int(string[index])
        index = index + 1
    print(nr)


# Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format
# is 00011000, meaning 2 bits with value "1"
def ex8(number):
    if number == 0:
        print(0)
        return
    bits1 = 0
    while number >= 1:
        bits1 += (number & 1)
        number >>= 1
    print(bits1)


# Write a functions that determine the most common letter in a string. For example if the string is "an apple is not a
# tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered.
# Casing should not be considered "A" and "a" represent the same character.
def ex9(string):
    string = string.lower()
    freq = {}
    for x in string:
        if 'a' <= x <= 'z':
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

    print(max(freq, key=freq.get))


# Write a function that counts how many words exists in a text. A text is considered to be form out of words that are
# separated by only ONE space. For example: "I have Python exam" has 4 words.
def ex10(string):
    print(len(string.split()))


if __name__ == '__main__':
    pass
