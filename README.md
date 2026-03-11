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
