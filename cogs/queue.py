from discord.ext import commands
from discord import User, Embed
from util.checks import is_staff, is_allowed_in_channel
from obj.Queue import Queue

class QueueCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.queues = {}  # holds all queue objects identified by channel id


    @commands.command(name="join", aliases=['j'])
    @commands.check(is_allowed_in_channel)
    async def join(self, ctx):
        """ When a user joins a queue """

        if ctx.channel.id not in self.queues.keys():

            self.queues[ctx.channel.id] = Queue(ctx.channel.id)

        active_queue: Queue = self.queues[ctx.channel.id]

        if not active_queue.is_frozen():

            active_queue.add_player(ctx.author.id)

            embed = Embed(
                title=f"{ctx.channel.name} - {len(active_queue.get_players())} / {active_queue.get_max_players()}",
                description=f"{ctx.author.mention} has joined the queue!"
            )

            await ctx.channel.send(embed=embed)

        else:

            await ctx.channel.send("Queue is frozen!")


    @commands.command(name="leave", aliases=['l'])
    @commands.check(is_allowed_in_channel)
    async def leave(self, ctx):
        """ When a user leaves a queue """
        
        if not self.queue_exists(ctx.channel.id):

            await ctx.channel.send("No queue found!")
            return

        active_queue: Queue = self.queues[ctx.channel.id]

        if ctx.author.id in active_queue.get_players():

            active_queue.remove_player(ctx.author.id)
       
            embed = Embed(
                title=f"{ctx.channel.name} - {len(active_queue.get_players())} / {active_queue.get_max_players()}",
                description=f"{ctx.author.mention} has left the queue!"
            )

            await ctx.channel.send(embed=embed)


    #TODO: Do embed stuff
    @commands.command(name='queue', aliases=['q'])
    @commands.check(is_allowed_in_channel)
    async def queue(self, ctx):
        """ Sends an embed with queue info """

        if not self.queue_exists(ctx.channel.id):

            await ctx.channel.send("No queue found!")
            return

        active_queue: Queue = self.queues[ctx.channel.id]
        
        mention_str = ""

        # loop through player ids and append them to a string for mentions in discord embed
        for user_id in active_queue.get_players():

            mention_str += f"<@{user_id}>\n"

        embed = Embed(
                title=f"{ctx.channel.name} - {len(active_queue.get_players())} / {active_queue.get_max_players()}",
                description=mention_str
            )

        await ctx.channel.send(embed=embed)


    @commands.command(name='forcejoin')
    @commands.check(is_staff)
    async def forcejoin(self, ctx, user: User):
        """ Force adds a user to the queue """

        if ctx.channel.id not in self.queues.keys():

            self.queues[ctx.channel.id] = Queue(ctx.channel.id)

        active_queue: Queue = self.queues[ctx.channel.id]

        active_queue.add_player(user.id)

        embed = Embed(
                title=f"{ctx.channel.name} - {len(active_queue.get_players())} / {active_queue.get_max_players()}",
                description=f"{ctx.author.mention} has added {user.mention} to the queue!"
            )
        
        await ctx.channel.send(embed=embed)
    
   
    @commands.command(name='forceleave')
    @commands.check(is_staff)
    async def forceleave(self, ctx, user: User):
        """ Force removes a user from the queue """

        if not self.queue_exists(ctx.channel.id):

            await ctx.channel.send("No queue found!")
            return

        active_queue: Queue = self.queues[ctx.channel.id]

        if user.id in active_queue.get_players():

            active_queue.remove_player(user.id)

            embed = Embed(
                    title=f"{ctx.channel.name} - {len(active_queue.get_players())} / {active_queue.get_max_players()}",
                    description=f"{ctx.author.mention} has removed {user.mention} from the queue!"
                )
            
            await ctx.channel.send(embed=embed)
    

    @commands.command(name='freeze')
    @commands.check(is_staff)
    async def freeze(self, ctx):
        """ Freeze the queue to disallow new users joining """

        if not self.queue_exists(ctx.channel.id):

            await ctx.channel.send("No queue found!")
            return

        active_queue: Queue = self.queues[ctx.channel.id]

        active_queue.freeze()

        embed = Embed(
                    title=f"{ctx.channel.name} - {len(active_queue.get_players())} / {active_queue.get_max_players()}",
                    description=f"{ctx.author.mention} has frozen the queue!"
                )

        await ctx.channel.send(embed=embed)


    #TODO: Do embed stuff
    #TODO: Queue exists check
    @commands.command(name='unfreeze')
    @commands.check(is_staff)
    async def unfreeze(self, ctx):
        """ Unfreeze the queue to allow new users joining """

        if not self.queue_exists(ctx.channel.id):

            await ctx.channel.send("No queue found!")
            return

        active_queue: Queue = self.queues[ctx.channel.id]

        active_queue.unfreeze()

        embed = Embed(
                    title=f"{ctx.channel.name} - {len(active_queue.get_players())} / {active_queue.get_max_players()}",
                    description=f"{ctx.author.mention} has unfrozen the queue!"
                )

        await ctx.channel.send(embed=embed)


    @commands.command(name='clear', aliases=['c'])
    @commands.check(is_staff)
    async def clear(self, ctx):
        """ Unfreeze the queue to allow new users joining """

        if not self.queue_exists(ctx.channel.id):

            await ctx.channel.send("No queue found!")
            return

        active_queue: Queue = self.queues[ctx.channel.id]

        active_queue.clear()

        embed = Embed(
                    title=f"{ctx.channel.name}",
                    description=f"{ctx.author.mention} has cleared the queue!"
                )

        await ctx.channel.send(embed=embed)


    #TODO: Do embed stuff
    #TODO: Queue exists check
    @commands.command(name='size')
    @commands.check(is_staff)
    async def size(self, ctx, size: int):
        """ Unfreeze the queue to allow new users joining """

        if not self.queue_exists(ctx.channel.id):

            await ctx.channel.send("No queue found!")
            return

        active_queue: Queue = self.queues[ctx.channel.id]

        active_queue.set_max_players(size)

        embed = Embed(
                    title=f"{ctx.channel.name} - {len(active_queue.get_players())} / {active_queue.get_max_players()}",
                    description=f"{ctx.author.mention} has set the size of the queue to {size}"
                )

        await ctx.channel.send(embed=embed)


    def queue_exists(self, channel_id: int):
        """ return bool if queue id is in queues dict or not """
        if channel_id not in self.queues.keys():

            return False
        
        return True

def setup(bot):
    """ Used to set up cogs for the bot """
    bot.add_cog(QueueCog(bot))