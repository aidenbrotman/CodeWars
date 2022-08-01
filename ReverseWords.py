def reverse_words(text):
    text_reverse = []
    for l in text.split():
        reversed_l = ''.join(reversed(l))
        text_reverse.append(reversed_l)
    return '  '.join(text_reverse) if '  ' in text else ' '.join(text_reverse)

reverse_words('double  spaced  words')
