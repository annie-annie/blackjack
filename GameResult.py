class GameResult():

    def __init__(self, humanHasWon, message):
        self.humanHasWon = humanHasWon
        self.message = message

    def __str__(self):
        lostOrWonString = "WOW! You win!"
        if self.humanHasWon
        else "Oh no, you lost!"

        return self.colourConsoleText(
            f'{lostOrWonString} \t {self.message}', self.humanHasWon
        )

    def colourConsoleText(self, text, humanHasWon):
        colour = "32" if self.humanHasWon else "31"
        return f"\033[1;{colour};40m {text} \n"
