import unicodedata


# created just so the pydle function won't cause an undefined error
SIZE = 5
grid = [[("", "black") for _ in range(SIZE)] for _ in range(SIZE)]

def pydle(x, y, emoji="", color="white"):
    if 0 <= x < SIZE and 0 <= y < SIZE:
        grid[y][x] = (emoji, color)

# call this function to display the grid in the console when ran locally
# UPDATE THE sq DICTIONARY TO MATCH YOUR COLORS
def show():
    sq = {"black": "⬛",
          "white": "⬜",
          "gray": "⬛",
          "zinc": "🔲",
          "slate": "🟦", 
          "red": "🟥",
          "maroon": "🟥",
          "green": "🟩",
          "orange": "🟧",
          "yellow": "🟨",
          "brown": "🟫",
          "blue": "🟦",}
    for row in grid:
        line = []
        for e, c in row:
            cell = e or sq.get(c, "?")
            wide = len(cell) > 1 or unicodedata.east_asian_width(cell) in "WF"
            line.append(cell if wide else cell + " ")
        print(" ".join(line))