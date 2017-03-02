import getpass

class HangMan():
    GAME_STEPS = 5
    DEFAULT_USER_LIVES = 5

    @classmethod
    def game_procces(cls):
        user_word = cls.ask_user_to_type_word()
        partly_visible_word = ['*'] * len(user_word)
        asterisks_list = cls.make_asterisks_from_word(user_word)
        asterisks_list = ''.join(asterisks_list)

        print('Word to guess: {}'.format(asterisks_list))

        for step in range(cls.GAME_STEPS):
            letters = cls.show_guessed_letters(user_word)

            # save all guessed letters and show it on next steps
            for i, symbol in enumerate(letters):
                if symbol != '*':
                    partly_visible_word[i] = partly_visible_word[i].replace(partly_visible_word[i], symbol)

            result = ''.join(partly_visible_word)

            if user_word == result:
                return print('You win the game!\nThis word is - {}'.format(user_word))
            elif step == cls.GAME_STEPS - 1:
                return print('You lose the game.')
            else:
                print('Word to guess: {}'.format(result))

    @classmethod
    def ask_user_to_type_word(cls):
        word = getpass.getpass(prompt='Type a word and press Enter: ')
        return word


    @classmethod
    def ask_user_to_type_letter(cls):
        next_letter = input('You have xxxx lives left - Letter? ')
        return next_letter


    @classmethod
    def make_list_from_word(cls, word):
        letters = []
        for letter in word:
            letters.append(letter)
        return letters


    @classmethod
    def make_asterisks_from_word(cls, word):
        asterisks = list(map(lambda letter: letter.replace(letter, '*'), word))
        return asterisks


    @classmethod
    def show_guessed_letters(cls, word):
        user_letter = cls.ask_user_to_type_letter()
        if user_letter in word:
            guessed_letters = cls.replace_asterisk_on_letter(word, user_letter)
            return guessed_letters
        else:
            return []


    @classmethod
    def replace_asterisk_on_letter(cls, word, next_letter):
        user_word_list = cls.make_list_from_word(word)
        asterisks_list = cls.make_asterisks_from_word(word)
        letter_positions = []

        # get letter position in word and replace asterisk on this letter
        for index, symbol in enumerate(user_word_list):
            if symbol == next_letter:
                letter_positions.append(index)

        for i in letter_positions:
            asterisks_list[i] = next_letter

        return asterisks_list


HangMan.game_procces()
