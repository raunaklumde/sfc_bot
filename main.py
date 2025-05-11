import discord
import os # default module
from dotenv import load_dotenv
from random import randint
from faction_data import save_faction_name
from pathlib import Path
import json
from kos_list import save_kos_user
from ally_factions import save_ally_factions


load_dotenv() # load all the variables from the env file
bot = discord.Bot(intents=discord.Intents.all())


@bot.event
async def on_ready():

    print(f"{bot.user} is ready and online!")

@bot.event
async def on_member_join(member):

    await member.send(f'Welcome to the server, {member.mention}!')

@bot.slash_command(name="print_enemy_factions", description = "Prints a list of enemy factions.", guild_ids = [1147726964048805938,1342131167175901286])
async def print_enemy(ctx):

    file_path = Path("factions.txt")
    neat_path = file_path.read_text().splitlines()
    formatted_lines = '\n'.join(f"-{line}"for line in neat_path)

    embed = discord.Embed(title="Enemy Factions", description = formatted_lines,color = discord.Colour.dark_gold(),)
    embed.set_thumbnail(url="https://i.postimg.cc/Jznf7tRw/isignia.webp")
    embed.set_footer(text="Created by SbPat")

    await ctx.respond("Here's the list of enemy factions in a list.", embed=embed)


@bot.slash_command(name="add_kos_user", description = "Add a user to the KOS list.", guild_ids = [1147726964048805938,1342131167175901286])
async def add_kos(ctx):
    await ctx.respond('Enter the ROBLOX username of the user.')
    rblx_id = await bot.wait_for('message', check=lambda message: message.author == ctx.author)

    save_kos_user(rblx_id.content)

    await ctx.respond(f"✅ {rblx_id.content} has been added to the list.")

@bot.slash_command(name = "add_allied_faction", description = "Adds an allied faction to the database.")
async def add_allied_faction(ctx: discord.ApplicationContext, fac_name: Option(str, "Name of the faction"), invitelink: Option(str, "Invite link of the faction")):
    save_ally_factions(fac_name, invitelink)

    await ctx.respond(f"{fac_name} has been added!")
    

@bot.slash_command(name="add_enemy_faction", description ="Adds an enemy faction to the DBMS", guild_ids = [1147726964048805938,1342131167175901286])
async def add_enemy_faction(ctx):


    '''A command to add an enemy faction to the Faction database'''
    await ctx.respond('Enter the faction name.')
    new_fac = await bot.wait_for('message',check=lambda message: message.author == ctx.author)

    save_faction_name(new_fac.content)

    await ctx.respond(f"✅`{new_fac.content}`has been added to the list.")

@bot.slash_command(name="print_ally_facs", description = "Gives a neatly formatted embed of ally facs.", guild_ids = [1147726964048805938,1342131167175901286])
async def ally_factions(ctx:discord.ApplicationContext):
    ally_path = Path("allied_factions.txt")

    lines  = ally_path.read_text(encoding="utf-8").splitlines()
    formatted_lines = []

    for line in lines:
        if " | " in line:
            fac_name, link = line.split(" | ", 1)
            formatted_lines.append(f"- **{fac_name.strip()}** → {link.strip()}")
    
    formatted_list = '\n'.join(formatted_lines)

    embed = discord.Embedmbed(title = "Allied factions", description = formatted_list, color = discord.Colour.dark_gold(),)
    embed.set_thumbnail(url="https://i.postimg.cc/Jznf7tRw/isignia.webp")
    embed.set_footer(text="Created by SbPat")
    
    await ctx.respond("Here's a neatly formatted list of ally factions.", embed=embed)



@bot.slash_command(name ="print_kos_users", description = "Gives a neatly formatted embed of users to KOS.",guild_ids = [1147726964048805938,1342131167175901286])   
async def print_kos_users(ctx):

    kos_path = Path("kosusers.txt")
    neat_kos_path = kos_path.read_text().splitlines()
    kos_path_formatted = '\n'.join(f"-{kos}" for kos in neat_kos_path)

    embed = discord.Embed(title="Enemy Users", description=kos_path_formatted,color = discord.Colour.dark_gold(),)
    embed.set_thumbnail(url="https://i.postimg.cc/Jznf7tRw/isignia.webp")
    embed.set_footer(text="Created by SbPat")

    await ctx.respond("Here's a neatly formatted list of the users to kill on sight.", embed=embed)


bot.run(os.getenv('TOKEN')) # run the bot with the token