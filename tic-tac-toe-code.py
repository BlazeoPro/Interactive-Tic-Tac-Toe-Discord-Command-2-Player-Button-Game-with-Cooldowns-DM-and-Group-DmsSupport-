# important notes:
# I uses "game" group, you can use @bot.tree.command instead,because this command is in my game group and I have many other commands for game group.
# you can use your custom group or use @bot.tree.command 
# using @bot.tree.command is my suggestion 
# replace @game_group.command with @bot.tree.command and test it. 
# it's your choice to put group.

# ==============================
# 🎮 TIC TAC TOE COMMAND BLOW
# ==============================
@game_group.command(name="tictactoe", description="Start a Tic Tac Toe game between 2 users")
@app_commands.describe(player2="Second player")
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.checks.cooldown(1, 3.2)
async def tictactoe(interaction: discord.Interaction, player2: discord.User):

    player1 = interaction.user

    if player2.bot:
        return await interaction.response.send_message(
            "<a:red_alert:1469365774895284284> **Bots cannot play!** <a:red_alert:1469365774895284284>",
            ephemeral=True
        )

    if player1 == player2:
        return await interaction.response.send_message(
            "<a:red_alert:1469365774895284284> **Select two different players!** <a:red_alert:1469365774895284284>",
            ephemeral=True
        )

    first_player, second_player = random.sample([player1, player2], 2)
    turn = first_player

    board = [[" " for _ in range(3)] for _ in range(3)]


    def check_winner():

        for i in range(3):

            if board[i][0] != " " and board[i][0] == board[i][1] == board[i][2]:
                return board[i][0]

            if board[0][i] != " " and board[0][i] == board[1][i] == board[2][i]:
                return board[0][i]

        if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]

        if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]

        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            return "Draw"

        return None


    # ==============================
    # 🎛️ BOARD VIEW BLOW
    # ==============================
    class TicTacToeView(View):

        def __init__(self):
            super().__init__(timeout=300)
            self.message = None

        async def on_timeout(self):

            for b in self.children:
                b.disabled = True

            embed.description = f"{player1.mention} ❌ vs {player2.mention} 🔴\n\n⏳ **Game expired due to inactivity!**"

            try:
                if self.message:
                    await self.message.edit(embed=embed, view=self)
            except Exception:
                pass


    def get_board_view():

        view = TicTacToeView()

        for i in range(3):
            for j in range(3):

                label = board[i][j] if board[i][j] != " " else "\u200b"

                button = Button(
                    label=label,
                    style=discord.ButtonStyle.secondary,
                    row=i,
                    custom_id=f"{i}-{j}"
                )

                async def button_callback(btn_interaction: discord.Interaction, row=i, col=j):

                    nonlocal turn, board, view

                    if btn_interaction.user not in (player1, player2):
                        return await btn_interaction.response.send_message(
                            "<a:red_alert:1469365774895284284> **You are not part of this game!**",
                            ephemeral=True
                        )

                    if btn_interaction.user != turn:
                        return await btn_interaction.response.send_message(
                            "<a:red_alert:1469365774895284284> **It's not your turn right now!** <a:red_alert:1469365774895284284>",
                            ephemeral=True
                        )

                    if board[row][col] != " ":
                        return await btn_interaction.response.send_message(
                            "<a:red_alert:1469365774895284284> **Cell already taken!** <a:red_alert:1469365774895284284>",
                            ephemeral=True
                        )

                    marker = "❌" if turn == player1 else "🔴"
                    board[row][col] = marker

                    winner = check_winner()

                    if winner:

                        for b in view.children:
                            r, c = map(int, b.custom_id.split("-"))
                            b.label = board[r][c] if board[r][c] != " " else "\u200b"
                            b.disabled = True

                        if winner == "Draw":
                            desc = f"{player1.mention} ❌ vs {player2.mention} 🔴\n\n🤝 **It's a draw!**"
                        else:
                            desc = f"{player1.mention} ❌ vs {player2.mention} 🔴\n\n🏆 **{turn.mention} ({marker}) wins!** <a:party_blob:1469365774895284284>"

                        embed.description = desc

                        await btn_interaction.response.edit_message(embed=embed, view=view)

                        view.stop()

                        if winner == "Draw":
                            await btn_interaction.followup.send(
                                f"{player1.mention} {player2.mention}\n🤝 **The TicTacToe match ended in a draw!**"
                            )
                        else:
                            await btn_interaction.followup.send(
                                f"{player1.mention} {player2.mention}\n🏆 **{turn.mention} won the TicTacToe match!**"
                            )

                        return

                    turn = second_player if turn == first_player else first_player

                    for b in view.children:

                        r, c = map(int, b.custom_id.split("-"))
                        b.label = board[r][c] if board[r][c] != " " else "\u200b"

                        if board[r][c] != " ":
                            b.disabled = True

                    embed.description = f"{player1.mention} ❌ vs {player2.mention} 🔴\n\n🎯 **{turn.mention}'s turn!**"

                    await btn_interaction.response.edit_message(embed=embed, view=view)

                button.callback = button_callback
                view.add_item(button)

        return view


    embed = discord.Embed(
        title="<a:rainbow_flame:1469205311956193331> **🎮 Tic Tac Toe** <a:rainbow_flame:1469205311956193331>",
        description=f"{player1.mention} ❌ vs {player2.mention} 🔴\n\n🎯 **{turn.mention} starts first!**",
        color=discord.Color.blurple()
    )

    view = get_board_view()

    await interaction.response.send_message(
        content=f"{player1.mention} {player2.mention}",
        embed=embed,
        view=view
    )

    view.message = await interaction.original_response()


# ==============================
# ⚠️ ERROR HANDLER BlOW
# ==============================
@tictactoe.error
async def tictactoe_error(interaction: discord.Interaction, error):

    if isinstance(error, app_commands.CommandOnCooldown):
        message = "<a:red_alert:1469365774895284284> **Slow down! Try again in a few seconds.** <a:red_alert:1469365774895284284>"
    else:
        message = "<a:red_alert:1469365774895284284> **Something went wrong while starting the game.** <a:red_alert:1469365774895284284>"
        print("TicTacToe Error:", error)

    try:
        await interaction.response.send_message(message, ephemeral=True)
    except discord.InteractionResponded:
        await interaction.followup.send(message, ephemeral=True)
