class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col = ord(coordinates[0]) - 96
        row = int(coordinates[1])

        print(row,col)

        if col % 2 == 0:
            if row % 2 == 0:
                return False
            else:
                return True
        else:
            if row % 2 == 0:
                return True
            else:
                return False