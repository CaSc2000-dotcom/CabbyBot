# NOTE: Last updated 2018. Functionality may not work as indended. 

# CabbyBot: The Pythonforengineers Minigame Bot

CabbyBot is a simple, game-oriented **Reddit bot** designed to monitor the **r/pythonforengineers** subreddit and respond to user commands with fun minigames like dice rolls and Rock, Paper, Scissors.

Note: I made this when I was 17 and just getting into coding in general

---

## Features

* **Game Commands:** Responds to commands for rolling a die, flipping a coin, and playing Rock, Paper, Scissors.
* **Persistent State:** Uses a local file (`comments_replied_to.txt`) to track comments it has already replied to, preventing spam and duplicate responses.
* **Simple PRAW Implementation:** Streams new comments from the specified subreddit for real-time interaction.

---

## Available Commands

Users can trigger the bot by starting a comment with one of the following commands (case-insensitive):

| Command | Action | Example Usage |
| :--- | :--- | :--- |
| **`!CabbyBotHelp`** | Displays a list of all available commands. | `!cabbybothelp` |
| **`!RollTheDice`** | Rolls a 6-sided die and returns the result. | `!rollthedice` |
| **`!FlipTheCoin`** | Flips a coin and returns either "heads" or "tails". | `!flipthecoin` |
| **`!RPS [choice]`** | Plays Rock, Paper, Scissors against the bot. | `!rps rock`, `!rps paper`, `!rps scissors` |

---

## Setup and Installation

### Prerequisites

1.  **Python 3.x**
2.  A registered **Reddit Bot Account** with API access (Client ID, Client Secret).

### Step 1: Install Dependencies

This project relies on the **PRAW** (Python Reddit API Wrapper) library.

```bash
pip install praw
```

### Step 2: Configure PRAW

You must set up a PRAW configuration file (praw.ini) in the same directory as the script, or in the standard PRAW location. This file securely stores your bot's credentials.

The bot is configured to look for the profile named bot1 (as seen in the code: reddit = praw.Reddit('bot1')).

praw.ini Example:

```ini
[bot1]
client_id=YOUR_CLIENT_ID
client_secret=YOUR_CLIENT_SECRET
password=YOUR_BOT_PASSWORD
username=YOUR_BOT_USERNAME
user_agent=CabbyBot minigame bot v1.0 by /u/YOUR_REDDIT_USERNAME
```

### Step 3: Run the Bot

Execute the Python script. The script will prompt you before starting its main loop.

```bash
python your_script_name.py
```

The bot will start streaming comments and will create the comments_replied_to.txt file automatically on its first run.

---

## Project Structure

`your_script_name.py` (e.g., `cabby_bot.py`): The main bot logic and functions.

`praw.ini`: Configuration file containing Reddit API credentials.

`comments_replied_to.txt`: Stores IDs of comments the bot has replied to for persistence.

## Bot Logic Overview
The bot operates within the `start()` function:

1. It iterates through the stream of new comments in the r/pythonforengineers subreddit.

2. It checks if the `comment.id` is already in the `comments_replied_to` list.

3. It uses regular expressions (`re.match`) to check for the supported commands at the beginning of the comment body.

4. If a command is found:

  - It generates a random result (dice, coin, or RPS choice).

  - It replies to the comment with the result.

  - It appends the comment ID to the reply list and writes the updated list to the text file.
