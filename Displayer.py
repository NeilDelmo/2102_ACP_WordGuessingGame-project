def show_execute(tries):
    stages = [
        """
                  ------
                  |    |
                  |    O
                  |   /|\\
                  |   / \\
                  |
               """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """,
        """
           ------
           |
           |
           |
           |
           |
        """,
        """
           |
           |
           |
           |
           |
           |
        """,
    ]
    return stages[tries]

def display_current_state(word, guessed_letters):
    current_state = ''.join(letter if letter in guessed_letters else '_' for letter in word)
    return current_state

