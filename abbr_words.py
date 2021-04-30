def starts_with_uppercase(word):
    return word and 'A' <= word[0] <= 'Z'


def abbr_words(s: str):
    words = s.split(' ')
    print(words)
    flag_map = [False] * len(words)
    # loop until second last since are checking current and next item
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]

        if starts_with_uppercase(word) and starts_with_uppercase(next_word):
            flag_map[i] = True
            flag_map[i + 1] = True

    result = ''
    needs_space = True
    for index, flag in enumerate(flag_map):
        if flag:
            result += (' ' if needs_space and index != 0 else '') + words[index][0]
            needs_space = False
        else:
            result += (' ' if index != 0 else '') + words[index]
            needs_space = True

    print(flag_map)

    return result


print(abbr_words('I live in the United States of America.'))
print('-' * 50)
print(abbr_words('I live in the United States America.'))
print('-' * 50)
print(abbr_words('Test tEST Test TEST'))
