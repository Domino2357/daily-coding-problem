"""
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction,
then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

"""
# assuming no complexity bounds; assuming words can be part of the string multiple times
# first thought: take all the words which are a prefix of the string; strip the prefix, do the same until the string is
# empty


def return_words(dictionary, word_bundle):
    if word_bundle == '':
        return []
    for word in dictionary:
        if starts_with(word_bundle, word):
            next_word = return_words(dictionary, word_bundle[len(word):])
            if next_word is not None:
                return [word] + next_word
            else:
                return None


# seems in python 3.7 there is no str.startswith(prefix)
def starts_with(word, prefix):
    if prefix == word[:len(prefix)]:
        return True
    else:
        return False


if __name__ == '__main__':
    print(return_words(['quick', 'brown', 'the', 'fox'], "thequickbrownfox"))
    print(return_words(['bed', 'bath', 'bedbath', 'and', 'beyond'], "bedbathandbeyond"))
    print(return_words(['hello', 'green', 'hopr'], "hellogreenhope"))
