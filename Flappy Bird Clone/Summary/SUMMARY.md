# Summary

This project is a Flappy Bird style game built with Pygame. The bird falls due to gravity and flies upward when SPACE is pressed. Pipes move from right to left, and the score increases by 1 each time the bird passes a pipe. The game ends when the bird hits a pipe, the ground, or the top of the screen, and you can restart by pressing R.

Concepts: Pygame, Gravity, Collision, Game Loop.

## Main Points

- **Game loop:** every frame the program reads input, updates the bird and pipes, draws everything, and runs at 30 FPS.
- **Gravity and flap:** velocity increases by 1 each frame and the bird moves by that velocity. Pressing SPACE sets velocity to -10, so the bird moves up.
- **Pipes:** a new pipe with a random gap (150 px) is added every 90 frames. Pipes move left by 3 px per frame, and pipes that leave the screen are removed.
- **Score:** when a pipe has fully passed the bird, the score increases by 1. Each pipe is counted only once.
- **Collision and Game Over:** `Rect.colliderect()` checks the bird against the top and bottom pipes. The game also ends if the bird touches the ground or goes above the top of the screen.
- **Restart:** pressing R after Game Over resets the bird, pipes, score and timer.
- **Testing:** `test_cases.py` checks the main logic with normal input, boundary values, an invalid key and valid actions. All test cases gave the expected output.

## Difficulties Faced and How They Were Solved

1. **Making the movement feel right.** Gravity and flap speed were hard to balance. Too weak a flap and the bird fell too fast; too strong and it flew off the screen. After trying values, gravity +1 and flap -10 gave smooth and playable movement.
2. **Score increasing many times for one pipe.** The pipe stays behind the bird for many frames, so the score kept increasing. A `scored` flag for each pipe fixed this, so each pipe adds only 1.
3. **Collision with two pipes.** Each pipe has a top part and a bottom part, so both are checked with `colliderect()`. The ground and top of the screen are checked separately.
4. **Old pipes piling up.** Pipes that left the screen stayed in the list. They are now removed when their right edge goes past x = 0.
5. **Restart.** After Game Over, the old values stayed. A `new_game()` function now resets everything in one place.
6. **Testing a game window.** A game with a window is hard to test directly, so the logic (gravity, boundaries, key handling, scoring) was tested separately in `test_cases.py`.
7. **Installing Pygame.** The newest Python versions may not work with the standard `pygame` package, so `pygame-ce` was installed. It works with `import pygame` and needs no code change.
