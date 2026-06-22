# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience


**The Game's Purpose**
This is a number-guessing game where the computer picks a secret number and you try to guess it. To help you along the way, the game gives you hints after each turn by telling you whether you need to guess higher or lower.

**Bugs Found**

* **Backwards Hints:** The game gave opposite hints, telling me to go lower when my guess was already too low.
* **Broken Turn Counter:** The counter went into negative numbers and still said I had attempts left even after the game was over.
* **Broken Reset Button:** Clicking the "New Game" button did absolutely nothing and wouldn't start a fresh round.
* **Inaccurate History Log:** The developer debug tool didn't accurately show the list of numbers and words I had previously typed in.

**Fixes Applied**

* **Fixed Hint Directions:** Swapped the logic inside the guess-checking function so that the high/low arrows point the right way.
* **Clamped the Counter:** Added a rule to ensure that the attempts left counter clamps cleanly at zero instead of dropping below it.
* **Fixed the New Game Button:** Programmed the button to reset the player's attempts back to zero, pick a brand new secret number, and force the app to reload fresh.
* **Corrected the State History:** Updated the history tracker so it saves every valid guess and invalid input into the page state accurately.


## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. **Launch the Game and Select Difficulty:** Start the game by launching the Streamlit app; by default, the game initializes to "Normal" difficulty with a range from 1 to 100, allowing up to 8 attempts.
2. **Make an Initial Low Guess:** Expand the "Developer Debug Info" tab to observe the secret number (for example: 42), then enter a low guess like `20` into the text box and click "Submit Guess". The app registers the first attempt, leaving 7 attempts remaining, and correctly flashes an upward-trending warning hint stating "Go HIGHER!".
3. **Make an Overcorrecting High Guess:** Enter a significantly higher number like `75` into the input field and hit the submit button again. The system logs the second attempt, leaving 6 attempts remaining, and now displays a downward-trending warning hint stating "Go LOWER!".
4. **Submit the Correct Secret Number:** Refine your guess by entering the exact secret number `42` into the input field and clicking the submit button for a third time. The turn tracker processes the interaction, and because the guess matches the secret value, the app instantly bursts with a celebratory screen animation of falling balloons.
5. **Review the Final Victory State:** The interface locks down further input and displays a final success message proclaiming: *"You won! The secret was 42. Final score: 60"*, confirming a completed, victorious game loop.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
