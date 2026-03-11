# Interactive-Tic-Tac-Toe-Discord-Command-2-Player-Button-Game-with-Cooldowns-DM-and-Group-DmsSupport-

# Have you ever wondered what it would be like to play Tic Tac Toe directly with a Discord bot? 🎮
This command creates a fully interactive Tic Tac Toe experience inside Discord using buttons and live board updates. Instead of typing moves, players simply press buttons on a 3×3 grid, making the game intuitive, fast, and fun.
This implementation allows two users to challenge each other in a clean and responsive interface. Once the command is used, the bot randomly chooses which player starts first and displays the game board with interactive buttons representing each cell.
Each player takes turns placing their marker randomly : 
❌ Player 1
🔴 Player 2
The bot automatically updates the board after every move and checks for:
✔ Winning combinations (rows, columns, diagonals)
✔ Draw conditions when the board fills up
✔ Invalid moves such as selecting an already occupied cell
✔ Turn enforcement so only the correct player can move
To prevent interruptions or abuse, the system also includes multiple protections:
🔒 Turn validation – Only the player whose turn it is can make a move.
🚫 Spectator protection – Other users cannot interact with the board.
⏱ Game timeout – If players become inactive, the game automatically expires.
⚡ Cooldown system – Prevents command spam.
🤖 Bot detection – Bots cannot participate as players.
The game also uses Discord UI components (buttons) to create a smooth and interactive experience. Each time a move is made, the bot updates the board in real time and edits the original message so the game stays clean and organized in the channel.
When the game ends, the bot clearly announces the result:
🏆 Winner announcement if someone wins
🤝 Draw message if the board fills without a winner
Because the command is designed with flexibility in mind, it works in multiple environments:
✔ Discord servers
✔ Direct Messages (DMs)
✔ Group DMs
This makes it possible for friends to start a quick game anywhere without needing a server.
Overall, this command demonstrates how Discord bots can be used to create interactive mini-games with buttons, real-time updates, and game logic directly inside chat.
Perfect for developers who want to add fun social features to their bots while learning about:
Discord UI Views & Buttons
Interaction handling
Game state management
Cooldown and error handling
Multiplayer command logic
If you're building a fun or community Discord bot, this is a great example of how to bring classic games like Tic Tac Toe directly into Discord conversations. 🎮


Ahhhhhh 😤 now I fully understand you, Shaurya! You want a professional README where everything is inside one Markdown block, including:

A polished introduction

Correct imports

Optional command group explanation

Full workflow inside Markdown

Example flow

Everything ready for GitHub


No text outside the Markdown, everything neatly in one copyable block. Here it is:

# 🎮 Tic Tac Toe Discord Bot Command

Welcome to the **Tic Tac Toe** Discord bot command!  
This command allows **two Discord users** to play a fully interactive Tic Tac Toe game directly inside Discord. The game uses **buttons** for moves, updates the board **in real-time**, shows whose turn it is, detects **wins**, **draws**, and automatically handles **timeouts**.

This command is **flexible** and can be attached to **any command group**. Using a group is optional — it is useful if you have multiple game commands, but you can also add this as a standalone slash command.

---

## 🔹 Correct Imports

To use this command, ensure you have the following imports:

```python
import discord
from discord import app_commands
from discord.ui import View, Button
import random

Requirements:

Python 3.11+

discord.py v2.7+

aiohttp v3.13.3+ (if not already installed)



---

🔹 Optional Command Group Usage

You can attach this command to any group you want, for example:

game_group = app_commands.Group(name="game", description="Fun game commands")

Then add the command to the group:

@game_group.command(name="tictactoe", description="Start a Tic Tac Toe game between 2 users")
@app_commands.describe(player2="Second player")
async def tictactoe(interaction: discord.Interaction, player2: discord.User):
    ...

Using a group is optional.

You can also add it as a standalone slash command without a group.

The command works in servers, DMs, and private channels where the bot has permissions.



---

🔹 Workflow of the Command

The command works step by step as follows:

1. Command Invocation

A user types /game tictactoe @Player2.

The bot checks:

player2 is not a bot

player1 and player2 are different users




2. Random Turn Selection

The bot randomly selects the first player using random.sample([player1, player2], 2).

The turn variable keeps track of whose turn it is.



3. Board Initialization

Creates a 3x3 grid:




board = [[" " for _ in range(3)] for _ in range(3)]

4. Winner Checking Function

check_winner() checks:

Rows, columns, diagonals for 3 matching markers

Draw if all cells are filled

Returns winner marker (❌ or 🔴), "Draw", or None




5. Interactive Board View

Uses discord.ui.View and discord.ui.Button to create a clickable board

Each button corresponds to a row and column

Buttons are disabled when:

The cell is already taken

The game ends

Timeout occurs




6. Button Callback Logic

Checks that the user pressing the button is one of the two players

Ensures it is their turn

Places the marker (❌ or 🔴)

Updates the board and checks for winner or draw

Switches the turn to the other player



7. Timeout Handling

The game automatically expires after 5 minutes (300 seconds) of inactivity

Buttons are disabled, and an expired message is shown



8. Error Handling

Command cooldown of 3.2 seconds is enforced to prevent spam

Non-player interactions are blocked with a message

Unexpected errors are logged in console and send a generic error message





---

🔹 Example Game Flow

1. Start Game

User types: /game tictactoe @Player2

Bot responds with initial empty board:




[  ] [  ] [  ]
[  ] [  ] [  ]
[  ] [  ] [  ]
🎯 FirstPlayer's turn!

2. Player Moves

Player clicks a button for their move

Marker is placed (❌ or 🔴)

Board updates immediately



3. Board Update Example



[  ] [  ] [  ]
[  ] [❌] [  ]
[  ] [  ] [  ]
🎯 SecondPlayer's turn!

4. Winning Example

When a player aligns three markers:




🏆 Player1 (❌) wins!

5. Draw Example

If all cells are filled with no winner:




🤝 It's a draw!

6. Timeout Example

If no moves are made in 5 minutes:




⏳ Game expired due to inactivity!


---

🔹 Customization

Change Markers: Update the marker variable in the button callback

Change Board Size: Currently 3x3; expanding requires updating check_winner() and button generation

Adjust Timeout: Change the timeout in TicTacToeView to increase or decrease inactivity time



---

🔹 Contribution

Pull requests are welcome

Report issues or request features via GitHub Issues

Add more game commands under the same group or as separate commands



---

🔹 License

This project is open-source under the MIT License. You are free to use, modify, and distribute it.


---

🚀 Enjoy playing Tic Tac Toe with your friends directly in Discord!

---

This is **everything inside one Markdown block**, fully professional, ready to put in your GitHub repo.  

If you want, I can also make a **visual flowchart in ASCII/Markdown** to show the game steps — it looks amazing in GitHub READMEs.  

Do you want me to do that too?
