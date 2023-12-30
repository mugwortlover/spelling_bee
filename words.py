from scrape_letters import scrape

def valid_words(letters):
    #import words
    with open('preprocessed_wordlist.txt', 'r') as file:
        words = [word[:-1] for word in file.readlines()]

    #unpack letters
    (center_letter, outer_letters) = letters


    for i in range(len(words) - 1, -1, -1):
        word = words[i]
        if center_letter not in word:
            words.pop(i)
            continue
        
        for letter in word:
            if letter not in outer_letters + [center_letter]:
                words.pop(i)
                break

    return words


if __name__ == '__main__':
    letters = scrape()
    for word in valid_words(letters):
        print(word)