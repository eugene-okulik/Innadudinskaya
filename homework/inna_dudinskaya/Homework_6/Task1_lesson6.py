text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
words = text.split()
print(words)
fin_words = []
for word in words:
    if ',' in word:
        word = word[: word.index(',')] + 'ing' + ','
    elif '.' in word:
        word = word[: word.index('.')] + 'ing' + '.'
    else:
        word = word + 'ing'
    fin_words.append(word)
print(' '.join(fin_words))
