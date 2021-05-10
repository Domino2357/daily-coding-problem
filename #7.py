""""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""""


def encode_mapping(code):
    list_of_numbers = []
    for char in code:
        list_of_numbers.append(int(char))
    count = 1
    index = 0
    while index < len(list_of_numbers):
        length_of_1_or_2_sequence = 0
        if list_of_numbers[index] == 1 or list_of_numbers[index] == 2:
            length_of_1_or_2_sequence += 1
            while list_of_numbers[index + length_of_1_or_2_sequence] == 1 or list_of_numbers[
                index + length_of_1_or_2_sequence] == 2:
                length_of_1_or_2_sequence += 1
                if (index + length_of_1_or_2_sequence >= len(list_of_numbers)):
                    break
            # TODO still missing the edge case that the last number of the sequence is a 2 and its predecessor is >6, e.g.,
            # TODO 1129, then length_of_1_or_2_sequence shouldn't be increased
            count = count * fibonacci(length_of_1_or_2_sequence + 1)
            index = index + length_of_1_or_2_sequence
        index += 1
    return count


def fibonacci(n):
    if n == 2:
        return 2
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(encode_mapping("11211"))
