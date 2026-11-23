# DAILY PYDLE :D

__Contents__
- [Answer Format](#answer-format)
- [Instructions for storing the answers](#instructions-for-storing-the-answers)
- [Folder Structure](#folder-structure)
- [Functions inside `pydle.py`](#functions-inside-pydlepy)
- [References/Materials](#references-or-materials)

## Answer Format
_On what format do you upload your answers?_ </br>

__Daily puzzles, should have 3 outputs:__
- __A .py file__: containing the code/answer
- __A README.md file__: containig the game result (named with the current date)
- __a png__: the image of your answer against the puzzle reference.


## Instructions for storing the answers
_How do i upload these outputs?_

__For uniformity and consistency, follow these steps:__

1. Answer the pydle for the day: https://pydle.net/
2. Create a folder named with the current date (`MM-DD-YYYY`). This is where you'll store the outputs for that current day.
3. Copy the code, and put inside a `{puzzle-name}.py` file
    - Add the imports
        ```
        import sys, os
        sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
        from pydle import *
        ```
    - Add the code/answer.
    - Call `show()` for rendering it locally through terminal.
4. Copy the results of the pydle (the message that appears once the puzzle is solved) and paste it in the README file named `MM-DD-YYYY`
5. Go to `pydle.py`, and update the `sq` dictionary under the function `show()` with new characters if needed (for local rendering in terminal).

## Folder Structure
```
.
├── pydle.py
├── _01_ArchivedPuzzles/
├── _02_OwnPatterns/
├── MM-DD-YYYY/
│   ├── MM-DD-YYYY.md
│   ├── {puzzle-name}.py
│   └── {PuzzleName}.png
├── MM-DD-YYYY
└── ...
```
> __01_ArchivedPuzzles:__ Where the past puzzles are stored (i just answered these puzzles archived from the past in pydle)
> __02_OwnPatterns:__ Where my very own created patterns are stored.
> __MM-DD-YYYY/:__ For example 11-23-2026 (folder) </br>
> __MM-DD-YYYY.md:__ For example 11-23-2026.md (md file) </br>
> __{puzzle-name}.py:__ For example rice-and-dumpling.py </br>
> __{PuzzleName}.png:__ For example RiceAndDumpling.py

## Functions inside `pydle.py`

__What is `show()`?__ </br>
This can be used for rendering or running the codes locally in terminal. This is called at the end of every `.py`  file. The `sq` dictionary needs to be updated everytime there are new attributes or colors  in the puzzles.

__What is `pydle()`?__</br>
The [pydle game](https://pydle.net/) has a built in function `pydle( x, y, Emoji, Color)`. The defined function in this file is made just so the everytime the function is called, it won't cause undefined error. That function is not the official function from the game, it is made for this repo only.

## References or Materials
- [Pydle](https://pydle.net/)
- [pydle-public repo by anyhotcountry](https://github.com/anyhotcountry/pydle-public)