# Flappy Bird Clone

**Name:** MANSI SAHU
**Class/Section:** M
**ERP / Roll Number:** RU-26-01854
**PS No.:** 54
**University:** Rungta International Skills University

---

## Project Description

A Flappy Bird style game built with Python and Pygame. The player controls a bird that must fly through gaps between moving pipes without touching them, the ground, or the top of the screen. The project also includes test cases that check the game logic.

## Features

- The bird falls because of gravity and flies up when SPACE is pressed.
- Pipes with a random gap move from right to left.
- Score increases by 1 each time the bird passes a pipe.
- Game Over when the bird hits a pipe, the ground, or the top of the screen.
- Press R after Game Over to restart.

## Libraries Required

- Python 3
- pygame-ce

```
pip install pygame-ce
```

pygame-ce is a maintained version of Pygame. It is used in the code with `import pygame`, so no code change is needed.

## Steps to Run

1. Install the library: `pip install pygame-ce`
2. Open the `Code` folder in a terminal.
3. Run:

```
python main.py
```

## Controls

| Key | Action |
|---|---|
| SPACE | Bird flaps upward |
| R | Restart after Game Over |

## Game Settings

Window 400x600, bird 30x30, pipe width 60, gap 150, pipe speed 3.

## Test Cases

The tests are in the `Test Case` folder. Run:

```
python test_cases.py
```

It checks gravity and movement, ground and top boundary, an invalid key, flap speed, and pipe scoring. Screenshots of the results are saved in the same folder.

## Project Files

| File | Purpose |
|---|---|
| `Code/main.py` | The game |
| `Test Case/test_cases.py` | Test cases for the game logic |
| `Test Case/game_over.png` | Game Over screenshot |
| `SUMMARY.md` | Short project summary |

PS No. 54 - Rungta International Skills University
