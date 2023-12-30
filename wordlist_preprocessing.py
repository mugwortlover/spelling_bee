#preprocess wordlists for use in spelling bee solver

def main(wordlist_filename):
    with open(wordlist_filename, 'r') as wordlist:
        words = [word[:-1] for word in wordlist.readlines()]
    
    with open('preprocessed_words.txt', 'w') as new_wordlist:
        for word in words:
            if len(word) > 3:
                new_wordlist.write(word + '\n')

        print(words)


if __name__ == '__main__':
    filename = 'better_wordlist.txt'
    main(filename)