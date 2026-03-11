@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
# guilds means servers,dms means direct messages, 
# private_channels means group Dms 

# If you have too many commands, you can use group and put your commands into group
# still wondering how to make the group subcommands appear in Dms and group Dms?
# don't worry! use this code blow!
class DMEnabledGroup(app_commands.Group):
    def __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            allowed_contexts=app_commands.AppCommandContext(
                guild=True, dm_channel=True, private_channel=True
            ),
            allowed_installs=app_commands.AppInstallationType(
                guild=True,
                user=True,  # REQUIRED FOR DMs
            ),
        )

# this class will enable the group subcommands appear and work in Dms and Group Dms.
# now use them in groups like this,blow example code:-
YourName_group = DMEnabledGroup(
    name="YourName",
    description="......"
)

# don't forgot to replace "YourName" with your group name in all small caps.

# now attach this command to the bot.tree.command by using this code

bot.tree.add_command(YourName_group)

# put the exact group name instead of "YourName"

# now let's take an example to use this group in code:-

@YourName_group.command(name="meme")
async def meme(interaction: discord.Interaction):
    await interaction.response.send_message("Here's a meme! or your name")

# like this replace "YourName" with your exact group name
# your ready and you can put 25 subcommands (max) to a group
