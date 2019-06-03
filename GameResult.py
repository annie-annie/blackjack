class GameResult():
    winText = "WOW! You win!"
    loseText = "Oh no, you lost!"
    winColour = 32
    loseColour = 31

    def __init__(self, humanHasWon, message):
        self.humanHasWon = humanHasWon
        self.message = message

    def __str__(self):
        lostOrWonString = self.winText if self.humanHasWon else self.loseText
        colour = self.winColour if self.humanHasWon else self.loseColour

        return self.colourConsoleText(
            f'{lostOrWonString} \t {self.message}',
            colour
        )

    def colourConsoleText(self, text, colour):
        return f"\033[1;{colour};40m {text} \n"
