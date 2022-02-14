import discord
from redbot.core import commands


class CounterCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.group()
    async def count(self, ctx):
        """Count your cogs/commands."""
        pass

    @commands.is_owner()
    @count.command()
    async def cogs(self, ctx):
        """Count your cogs."""

        cogs = len(self.bot.cogs)
        await ctx.send(f"I have `{cogs}` cogs loaded!")

    @commands.is_owner()
    @count.command()
    async def commands(self, ctx, cog: str = None):
        """
        Count your commands.
        
        You can also provide a cog name to see how many commands is in that cog.
        """
        if cog:
            if self.bot.get_cog(cog) != "NoneType":
                cmds = sum(1 for _ in self.bot.get_cog(cog).walk_commands())
                await ctx.send(f"I have `{cmds}` commands loaded on that cog!")
            else:
                await ctx.send("Please provide a valid cog name. (Example: `Core`)")
        else:
            cmds = len(self.bot.commands)
            await ctx.send(f"I have `{cmds}` commands loaded!")
