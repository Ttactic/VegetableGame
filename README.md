# Vegetable Game

This is a simple, fun game made using **Pygame** where the player controls a character to collect various vegetables that appear randomly on the screen. The game runs for a set time limit, and the player's goal is to collect as many vegetables as possible before the time runs out. If the player reaches a score of 100 or more within the time limit, they win.

## Features

- **Player Movement**: The player can move using the arrow keys (Up, Down, Left, Right).
- **Random Vegetables**: Vegetables randomly appear on the screen for the player to collect.
- **Time Limit**: The game runs for a fixed duration (60 seconds).
- **Scoring**: Each vegetable collected increases the score.
- **Background Music**: Background music is played throughout the game.
- **Game Over and Restart**: After the time limit is up, the player can see the results (win/lose) and choose to restart the game or quit.

## Prerequisites

Make sure you have the following files in your project folder:
- **bg.jpg**: The background image for the game.
- **icon.jpg**: The icon used for the game window.
- **Asset/**: A folder containing vegetable images named `1.png`, `2.png`, ..., `47.png`.
- **Player.jpg**: The image of the player character.
- **background_music.mp3**: The background music for the game.

## Installation

1. Install Python and Pygame if you haven’t already:

```bash
pip install pygame
```

2. Download or create the required images and music file:
   - **bg.jpg**: Background image.
   - **icon.jpg**: Icon for the game window.
   - **Asset/**: A folder with vegetable images named `1.png` to `47.png`.
   - **Player.jpg**: The image of the player character.
   - **background_music.mp3**: Background music for the game.

3. Save the game code in a `.py` file, for example, `vegetable_game.py`.

4. Run the game:

```bash
python vegetable_game.py
```

## How to Play

- Use the **arrow keys** to move the player character around the screen.
- Collect vegetables by moving the player character over them.
- The score increases with every vegetable collected.
- The game ends when the time runs out.
- If the player achieves a score of 100 or more, they win. Otherwise, the game ends in failure.
- After the game is over, press **'R'** to restart or **'Q'** to quit.

## Code Breakdown

1. **Player Class**:
   - The player is represented by an image and starts at a fixed position on the screen.
   - The `move` method allows the player to move using the arrow keys.
   
2. **Vegetable Class**:
   - Vegetables are randomly chosen from a set of images and appear at random positions on the screen.
   - The `collide` method checks if the player character collides with the vegetable.
   
3. **Game Loop**:
   - The game runs inside a loop where the player’s position is updated based on key presses.
   - Vegetables are drawn on the screen and checked for collisions with the player.
   - If a vegetable is collected, it is replaced by a new vegetable.
   - The score and remaining time are displayed.
   - If time runs out, the game shows a game over message and allows the player to restart or quit.

4. **Music**:
   - Background music plays throughout the game at a low volume.

## Key Code Sections

- **Background and Setup**:
    ```python
    background_image = pygame.image.load("bg.jpg")
    bg = pygame.transform.scale(background_image, (screen_width, screen_height))
    ```

- **Player Movement**:
    ```python
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.v
        if keys[pygame.K_RIGHT] and self.x < screen_width - self.image.get_width():
            self.x += self.v
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.v
        if keys[pygame.K_DOWN] and self.y < screen_height - self.image.get_height():
            self.y += self.v
    ```

- **Collision Detection**:
    ```python
    def collide(self, player_rect):
        veg_rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        return player_rect.colliderect(veg_rect)
    ```

- **Game Over Screen**:
    ```python
    def display_game_over(message):
        game_over_font = pygame.font.SysFont(None, 60)
        restart_font = pygame.font.SysFont(None, 40)

        game_over_text = game_over_font.render(message, True, (255, 0, 0))
        restart_text = restart_font.render("Press 'R' to Play Again or 'Q' to Quit", True, (0, 0, 0))

        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 3))
        screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() // 2, screen_height // 2))
    ```

---

Enjoy playing the Vegetable Game!
