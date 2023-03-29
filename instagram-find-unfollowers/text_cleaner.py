def cleaner(text):
    word_list = text.split()

    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
            
        else:
            word_count[word] = 1

    last_words = []
    for word in word_list:
        if word_count[word] > 1:
            word_count[word] -= 1
        else:
            last_words.append(word)

    last_words_str = "\n".join(last_words)
    return last_words_str


def start(name):
    with open(name, "r",encoding="utf-8") as test:
        content = cleaner(test.read())
        test.close()

    with open(name, "w", encoding="utf-8") as test:
        test.write(content)
        test.close()
#start("zytest.txt")
#start("ztest.txt")