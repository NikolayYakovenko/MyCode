import getpass

class HangMan():
    GAME_STEPS = 5

    @classmethod
    def promt_word(cls):
        user_word = getpass.getpass(prompt='Type a word and press Enter: ')
        partly_visible_word = ['*'] * len(user_word)
        asterisks_list = cls.make_asterisks_from_word(user_word)
        asterisks_list = ''.join(asterisks_list)
        lives_counter = 5

        print('Word to guess: {}'.format(asterisks_list))

        for step in range(cls.GAME_STEPS):
            letters = cls.promt_to_type_letter(user_word, lives_counter)

            for i, symbol in enumerate(letters):
                if symbol != '*':
                    partly_visible_word[i] = partly_visible_word[i].replace(partly_visible_word[i], symbol)

            result = ''.join(partly_visible_word)
            if user_word == result:
                print('You win the game!\nThis word is - {}'.format(user_word))
                return
            elif step == cls.GAME_STEPS - 1:
                return print('You lose the game.')
            else:
                print('Word to guess: {}'.format(result))


    @classmethod
    def list_from_word(cls, word):
        letters = []
        for letter in word:
            letters.append(letter)
        return letters


    @classmethod
    def promt_to_type_letter(cls, word, lives):
        next_letter = input('You have {} lives left - Letter? \n'.format(lives))

        if next_letter and next_letter in word:
            guessed_letters = cls.replace_asterisk_on_letter(word, next_letter)
            return guessed_letters
        else:
            return []


    @classmethod
    def replace_asterisk_on_letter(cls, word, next_letter):
        hidden_word = cls.list_from_word(word)
        asterisks_list = cls.make_asterisks_from_word(word)
        letter_positions = []

        for index, letter in enumerate(hidden_word):
            if letter == next_letter:
                letter_positions.append(index)

        for i in letter_positions:
            asterisks_list[i] = next_letter

        return asterisks_list


    @classmethod
    def make_asterisks_from_word(cls, word):
        asterisks = list(map(lambda letter: letter.replace(letter, '*'), word))
        return asterisks


HangMan.promt_word()
