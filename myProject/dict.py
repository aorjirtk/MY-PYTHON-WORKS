
def word_in_a_dictionary(word):
    result = {character for character in word}
    for key in result:
        if result[1] == result[key]:
            return result
word = 'winning'





