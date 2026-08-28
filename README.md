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
```
## Module Responsibilities
| File | Responsibility |
|------|----------------|
| `alien_invasion.py` | Main program and game loop |
| `settings.py` | Game configuration and settings |
| `game_stats.py` | Dynamic game state and player statistics |
| `game_functions.py` | Game events, updates, collisions, and helper functions |
| `ship.py` | Player spaceship |
| `alien.py` | Alien behavior and movement |
| `bullet.py` | Bullet behavior |
| `scoreboard.py` | Score, high score, level, and remaining ships display |

The project is divided into separate modules so that each component has a clear responsibility instead of placing the entire game inside one file.

## Game Architecture

The main program coordinates the different components of the game.
```text
                    alien_invasion.py
                           |
                           v
                    Main Game Loop
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
          Events        Updates        Drawing
             |             |             |
             v             v             v
           Ship         Bullets      Scoreboard
                           |
                           v
                     Collisions
                           |
                +----------+----------+
                |                     |
                v                     v
             Aliens                 Score
                |                     |
                v                     v
           New Fleet              High Score
                |
                v
             New Level
```
## Alien Fleet Generation

The number of aliens is calculated based on the available screen space instead of using a fixed number.

The fleet is generated using nested loops:
```text
Outer loop
    |
    +-- Create each row
            |
            +-- Inner loop
                    |
                    +-- Create each alien
```
The available horizontal space determines the number of aliens in each row, while the available vertical space determines the number of rows.

This allows the fleet to adapt to the game screen dimensions.

## Collision and Fleet Progression

When a bullet hits an alien:
```text
Bullet + Alien
      |
      v
Collision Detection
      |
      +---- Remove Bullet
      |
      +---- Remove Alien
      |
      +---- Increase Score
      |
      +---- Check High Score
```
When the entire fleet is destroyed:
```text
Alien Fleet Destroyed
          |
          v
     Clear Bullets
          |
          v
     Increase Level
          |
          v
   Increase Game Speed
          |
          v
    Create New Fleet
```
## Ship Collision

When the player's ship collides with an alien:
```text
Ship + Alien Collision
          |
          v
     Short Pause
          |
          v
   Clear Aliens/Bullets
          |
          v
   Decrease Ship Count
          |
          v
    Create New Fleet
          |
          v
      Continue Game
```
If no ships remain, the game ends.

## Controls
| Input | Action |
|-------|--------|
| Left Arrow | Move ship left |
| Right Arrow | Move ship right |
| Space | Fire bullet |
| Mouse Click | Start the game using the Play button |
| Q | Exit the game |
| Close Window | Exit the game |

## Technologies Used
-Python
-Pygame
-Git
-GitHub
-Visual Studio Code

## Installation
### 1. Clone the Repository
   git clone <repository-url>
### 2. Navigate to the Project
   cd Alien-Invasion
### 3. Create a Virtual Environment
   python -m venv myaliengame
### 4. Activate the Virtual Environment
   On Windows:
myaliengame\Scripts\activate
### 5. Install Pygame
  pip install pygame
### 6. Run the Game
  python alien_invasion.py

## Learning Outcomes

This project helped develop practical understanding of the following concepts.

### Python
-Classes and objects
-Inheritance
-Instance attributes
-Methods
-Functions
-Modules
-Imports
-Nested loops
-Conditional logic
-Collections
-Floating-point movement
-Code refactoring
### Pygame
-Game loops
-Event handling
-Keyboard input
-Mouse input
-Sprites
-Sprite groups
-Collision detection
-Screen rendering
-Rectangles and coordinates
-Frame-rate control
###Software Engineering
A major focus of the project was learning how to structure a growing application.
Instead of placing everything in a single file, responsibilities were separated across different modules.

### For example:
```text
settings.py
    |
    +-- Configuration

game_stats.py
    |
    +-- Dynamic Game State

game_functions.py
    |
    +-- Game Logic

ship.py
    |
    +-- Player Behavior

alien.py
    |
    +-- Alien Behavior

bullet.py
    |
    +-- Bullet Behavior

scoreboard.py
    |
    +-- Game Information Display

alien_invasion.py
    |
    +-- Application Entry Point
```
This separation makes the project easier to understand, maintain, debug, and extend.

## Development Progression

The game was developed incrementally, with each milestone adding new functionality.

1.Create the game window
2.Create the player ship
3.mplement ship movement
4.Implement bullets
5.Create an alien
6.Create a complete alien fleet
7.Implement fleet movement
8.Implement bullet-alien collisions
9.Implement fleet respawning
10.Implement ship-alien collisions
11.Implement player lives
12.Add Play button and game state
13.Implement game reset
14.Implement dynamic difficulty
15.Implement scoring
16.Implement high score
17.Implement game levels
18.Display remaining ships

This incremental approach helped demonstrate how new features can be added to an existing codebase while continuously refactoring and improving its structure.

## Possible Future Improvements

The current version is complete as a learning project, but it could be extended with:

-Sound effects and background music
-Different types of aliens
-Special weapons
-Power-ups
-Pause functionality
-Difficulty selection
-Improved visual effects
-Persistent high scores
-Leaderboard system
-Improved user interface
-Project Purpose

The main purpose of this project was to strengthen Python programming and software engineering fundamentals through practical development.

Rather than only focusing on making the game work, the project provided experience with:

-Designing a game loop
-Managing application state
-Organizing a multi-module Python application
-Using object-oriented programming
-Managing multiple objects with sprite groups
-Implementing collision detection
-Refactoring code
-Managing dynamic game difficulty
-Using Git for incremental development
-Maintaining a project on GitHub

## Acknowledgment

This project was developed as a practical learning exercise inspired by the Alien Invasion project from Python Crash Course by Eric Matthes.

The project was developed incrementally with additional experimentation, debugging, refactoring, and feature development throughout the learning process.

## Author

### Shahan Waheed

### BS Software Engineering Student

This project is part of my journey toward becoming a professional software engineer by building practical projects and developing strong programming, architecture, and software engineering fundamentals.
