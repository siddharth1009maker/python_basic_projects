def replace_word():
    word = "Hi , my name is Siddharth"
    word_to_replace = input("Enter the word you want to replace: ")
    word_replacement = input("Enter the word with which you want to replace: ")
    new_word = word.replace(word_to_replace, word_replacement)
    print(new_word)


replace_word()
