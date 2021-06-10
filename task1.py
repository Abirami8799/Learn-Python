import tamil

def all_tamil(word_in):
    if isinstance(word_in, list):
        word = word_in
    else:
        word = get_letters(word_in)
    return all([(letter in tamil_letters) for letter in word])

