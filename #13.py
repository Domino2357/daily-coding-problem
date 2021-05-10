"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""


def longest_substring(max_distinct_char, input_string):
    if len(input_string) == 0:
        print("The string received is empty")
        return 0
    sub_string = ''
    max_length = 1
    number_of_distinct_chars = 0
    sub_string = ''
    for j in range(len(input_string)):
        offset = 0
        while number_of_distinct_chars <= max_distinct_char and j + offset < len(input_string):
            char = input_string[j + offset]
            if not character_in_substring(char, sub_string):
                number_of_distinct_chars += 1
            sub_string += char
            offset += 1
        if len(sub_string)-1 > max_length:
            max_length = len(sub_string)-1
        sub_string = ''
        number_of_distinct_chars = 0
    return max_length


def character_in_substring(character, input_string):
    for i in range(len(input_string)):
        if character == input_string[i]:
            return True
    return False


if __name__ == '__main__':
    print(longest_substring(2, "abcdeababababbbac"))
