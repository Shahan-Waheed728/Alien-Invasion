# Alien Invasion

A classic arcade-style Alien Invasion game built with Python and Pygame.

This project was developed as a practical Python and software engineering learning project. It started with basic player movement and gradually evolved into a complete game featuring alien fleets, shooting, collision detection, scoring, levels, high scores, player lives, game states, and dynamic difficulty.

The project also focuses on modular design and separation of responsibilities as the codebase grows.

---

## Features

### Player

- Move the spaceship left and right.
- Prevent the spaceship from moving outside the screen.
- Multiple player lives.
- Respawn the player after an alien collision.
- Reset the player's position when starting a new game.

### Shooting

- Fire bullets from the spaceship.
- Limit the number of active bullets.
- Remove bullets when they leave the screen.
- Detect bullet-alien collisions.
- Remove both bullets and aliens after a collision.

### Alien Fleet

- Generate multiple rows and columns of aliens.
- Dynamically calculate the number of aliens that fit on the screen.
- Move the entire fleet horizontally.
- Detect when the fleet reaches the screen edge.
- Drop the fleet and reverse its direction.
- Generate a new fleet after the current fleet is destroyed.

### Collision Detection

The game handles:

- Bullet vs. Alien collisions.
- Ship vs. Alien collisions.

Pygame sprite groups are used to manage objects and collision detection efficiently.

### Scoring

- Earn points by destroying aliens.
- Display the current score.
- Increase the score based on the current game level.
- Display the high score.

### High Score

- Maintain the highest score during the game session.
- Update the high score whenever the current score exceeds it.
- Preserve the high score when starting a new game.

### Levels

- Display the current game level.
- Advance to the next level after destroying an entire alien fleet.
- Increase the game difficulty with each new level.

### Dynamic Difficulty

The game becomes progressively more difficult as the player advances.

The following speeds increase between levels:

- Ship speed
- Alien speed
- Bullet speed

A gradual speed-up factor is used to keep the game challenging while remaining playable.

### Player Lives

- Display the number of remaining ships.
- Decrease the number of ships after a ship-alien collision.
- Create a new fleet after a collision.
- End the game when the player runs out of ships.

### Game State

- Game starts in an inactive state.
- Game starts only when the player presses the Play button.
- Play button disappears while the game is running.
- Mouse cursor is hidden during gameplay.
- Cursor reappears when the game ends.
- Starting a new game resets the appropriate game state.

---

## Project Structure

```text
Alien-Invasion/
│
├── alien_invasion.py
├── alien.py
├── bullet.py
├── game_functions.py
├── game_stats.py
├── scoreboard.py
├── settings.py
├── ship.py
│
├── images/
│   ├── alien.png
│   └── ship.png
│
├── .gitignore
└── README.md
