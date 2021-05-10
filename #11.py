"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries
"""
import re


def get_string_with_prefix(list_of_strings, prefix):
    string = ' , '.join(list_of_strings)
    # using regular expressions for speed up here, see https://docs.python.org/3/howto/regex.html as a reference
    regex = re.compile(prefix + '\w*')
    return regex.findall(string)


if __name__ == '__main__':
    string_list = ['deer', 'dog', 'deal', 'de', 'horse']
    print(get_string_with_prefix(string_list, "de"))
