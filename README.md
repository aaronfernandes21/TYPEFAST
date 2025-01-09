Here is the full `README.md` file that you can copy entirely:

```markdown
# Typing Speed Test Game

A simple **Typing Speed Test** game built using **Python** and **Pygame**. The game allows users to test their typing speed (Words Per Minute) and accuracy while typing a random sentence from a text file. The game also tracks the highest score (WPM) achieved and displays real-time results.

## Features

- **Typing Speed Test**: The player types a randomly chosen sentence, and the game calculates their typing speed in words per minute (WPM) and accuracy.
- **High Score**: The game tracks the highest typing speed (WPM) and saves it to a text file for future sessions.
- **Timer**: Displays the time taken to complete the typing test.
- **Real-time Accuracy Calculation**: Accuracy is calculated based on the number of correct characters typed.
- **Reset Functionality**: The game allows the user to restart the test and try again.

## Screenshots

![Game Screenshot](assets/SpeedTestGame.jpg)

## Requirements

- Python 3.x
- Pygame library

### Install Dependencies

Before running the game, you need to install the required dependencies. You can do this by running the following command:

```bash
pip install pygame
```

## How to Play

1. **Run the Game**:
   To start the game, run the following command in your terminal:

   ```bash
   python main.py
   ```

2. **Typing Test**:
   - A random sentence will appear on the screen.
   - Start typing the sentence in the input box at the bottom.
   - Your typing speed (WPM) and accuracy will be displayed once you hit **Enter**.
   - After completing the test, the game will show your results along with the high score.

3. **Reset Function**:
   - To restart the game, click on the **Reset** button on the screen.

4. **High Score**:
   - The highest typing speed achieved will be saved and displayed during the game.

## Game Flow

- The game starts by displaying the main screen with the background and a randomly selected challenge sentence.
- Once the user clicks on the typing area, the timer starts, and the user begins typing.
- After typing, the WPM (Words Per Minute) and accuracy are displayed, and the score is saved if it beats the previous high score.
- The user can reset the game and try again.

## Files

- **main.py**: The main Python script for running the game.
- **essay.txt**: A text file containing multiple lines of sentences, one of which is selected randomly as the typing challenge.
- **assets**:
  - `SpeedTestGame.jpg`: Background image for the main screen.
  - `ppt.jpg`: Background image for the typing area.
  - `icon.png`: Icon displayed when the game ends (reset button).
- **highscore.txt**: A text file to store the highest typing speed (WPM).



---

