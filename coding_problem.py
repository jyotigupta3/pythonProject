import string


def reverse_each_word(sentence):
    words = sentence.split(" ")
    rev_word = []

    for word in words:
        l = []
        for char in word:
            if char in string.punctuation:
                l.append(char)
            else:
                l.insert(0, char)
        word = "".join(l)
        rev_word.append(word)

    return " ".join(rev_word)


def main(sentence):
    test_str = sentence
    assert reverse_each_word(test_str) == "gnirtS; eb2 desrever..."
    return 0


if __name__ == "__main__":
    main(sentence="String; 2be reversed...")
