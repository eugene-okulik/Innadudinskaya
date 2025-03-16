def print_words(text, number):
    for val in range(number):
        print(text, end='')
    else:
        print('')


words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for word in words.keys():
    print_words(word, words[word])
