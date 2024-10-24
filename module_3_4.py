def single_root_words(root_words, *other_words):
    same_words = []
    for i in other_words:
        if i.lower() in root_words.lower() or root_words.lower() in i.lower():
            same_words.append(i)
    return same_words

print(single_root_words('Яблоко', 'Око', 'Молоко', 'Блок', 'Топор'))