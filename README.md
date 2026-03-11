# 🎮 Interactive Tic Tac Toe Discord Bot Command for python!

Welcome to the **Interactive Tic Tac Toe Discord Bot Command**, a fully interactive mini-game built for Discord bots. This command allows **two users** to play the classic game of Tic Tac Toe directly in Discord using **buttons**. Instead of typing moves or coordinates, players simply **click the buttons on a 3×3 grid**, and the board updates immediately. This makes the game **fast, intuitive, and fun**, perfect for friends, communities, or social servers.

The command is designed to be **flexible**: it can be attached to any command group or used as a standalone slash command. It works in **Discord servers, direct messages (DMs), and group DMs**, so you can play anywhere, anytime.

---

## 🔹 Features

This Tic Tac Toe command includes a variety of features to ensure smooth gameplay:

- **Two-Player Gameplay** – Only two human players can participate in each game.  
- **Interactive Buttons** – Players click buttons to place their markers (❌ for Player 1, 🔴 for Player 2).  
- **Random First Turn** – The bot randomly selects which player starts first for fairness.  
- **Real-Time Board Updates** – After each move, the board updates instantly without cluttering the channel.  
- **Win Detection** – Automatically checks for rows, columns, and diagonals to determine a winner.  
- **Draw Detection** – Detects if all cells are filled without a winner and announces a draw.  
- **Turn Validation** – Prevents players from making a move out of turn.  
- **Spectator Protection** – Other users cannot interfere with the game.  
- **Bot Prevention** – Bots cannot participate as players.  
- **Timeout Handling** – If players are inactive for too long, the game expires and disables the board.  
- **Command Cooldowns** – Prevents spamming to keep the server experience smooth.  
- **Error Handling** – Invalid moves and unexpected errors are handled gracefully.  

---

## 🔹 How to Execute This Command

1. **Import Required Modules**

```python
import discord
from discord import app_commands
from discord.ui import View, Button
import random
```
---

2. **Requried Versions**
```python
python 3.11+
discord.py (pip) 2.6+
```

---

3. **Define the Command**
you can use this group blow and can add more commands (max 25) in 1 group only 
```python

game_group = app_commands.Group(name="game", description="Fun game commands")

@game_group.command(name="tictactoe",description="....")
async def tictactoe(interaction: discord.Interaction, player2: discord.User):
.....
.....
# now rigester the slash command,use blow code

bot.tree.add_command(game_group)

# if you want this command to appear or work in Dms or Group Dms, you need to use this conext right next the the # @game_group.command(....
# or
# @bot.tree.command(....
# blow is the example to use the allowes contexests to make the command appear and work in Dms and group Dms so that your friends can enjoy 🤑

@bot.tree.command(name="tictactoe", description="....")
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True) #important here use this
async def tictactoe
.....


```
- like this I have used the command but you can also do something like:
```python
@game_group.command
# remove this and add this blow instead of @game_group.command add this
@bot.tree.command(..
# this will create a direct command
```
---

4. **Player Verification**

- The bot checks that player2 is not a bot.
- It ensures that player1 and player2 are different users.

---

5. **Randomm Turn Selection**

- The bot randomly picks the first player using random.sample([player1, player2], 2).

- A variable turn keeps track of whose turn it is.

---

6. **Board Initialization**

- The board is created as a 3×3 grid:
```python
board = [[" " for _ in range(3)] for _ in range(3)]
```
---

🔹 Contribution

Pull requests are welcome

Report issues or request features via GitHub Issues

Add more game commands under the same group or as separate commands

---

🔹 License 

This project is open-source under the MIT License. You are free to use, modify, and distribute it.


---

🚀 Enjoy playing Tic Tac Toe with your friends directly in Dms or Group Dms,don't forget to check and use allword contextes to make them appear and work in Dms and Group Dms 🤑

---

