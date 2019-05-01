class GameResult():

    def __init__(self, humanHasWon, message):
        self.humanHasWon = humanHasWon
        self.message = message

    def __str__(self):
        lostOrWonString = "WOW! You win!" if self.humanHasWon else "Oh no, you lost!"
        return f'{lostOrWonString} \t {self.message}'
