import discord
import random
import os
import time

client = discord.Client()

MEMEPATH = r"D:\\Qi\\Fun\\Anime\\Reaction Gifs"
FORMATS = ("png", "gif", "jpg")

# Used to remember corn's last meme state
global normal_last 
normal_last = False

# Generates meme list statically, check that the formats are restricted
meme_list = [meme for meme in os.listdir(MEMEPATH) if meme[-3:] in FORMATS]
towel_meme_list = [towel_meme for towel_meme in meme_list if "towel" in towel_meme]

usage = ''' Hi! I am MemeBot created by Chezz and developed using discord.py.

***Commands:***
----------
!choose <choice1>,<choice2>,<choice3>,... : Choose 1 item from the choices
!meme [meme_name] : Generates a random meme, with an option to specify a particular meme
!towel_meme : Generates a random towel meme
!honk : THIS IS AGAINST THE RULES. YOU WILL GET BANNED.
!helpmeme : You already did this.
!listmemes: Prints a list of all memes possible
!ping : Will reply with "pong"
'''

async def printC(ch, msg):
    return await client.send_message(ch, msg)

def scout():
    num = random.random()

    if num < 0.01:
        out_msg = "UR"
    elif num < 0.1:
        out_msg = "SR"
    else:
        out_msg = "R"

    return out_msg


@client.event
async def on_message(message):

    global normal_last
    ch = message.channel

    msg = message.content.lower()

    ### CHOOSES FROM A LIST OF OPTIONS ###
    if msg.startswith("!choose"):
        cmd_split = msg.split()

        if len(cmd_split) != 2:
            await printC(ch, "Error! Input syntax '!choose <choice1>,<choice2>,<choice3>,...'")
        else:
            choices = cmd_split[1].split(",")
            await printC(ch, "I chose {0}!".format(random.choice(choices)))

    ### GENERATES A RANDOM MEME ###
    elif msg.startswith("!meme"):#,"!maymay"):
        msg_split = msg.split()

        if len(msg_split) == 1:
            meme = random.choice(meme_list)
            await client.send_file(ch, os.path.join(MEMEPATH, meme))
        elif len(msg_split) == 2:
            meme = msg_split[1]
            await client.send_file(ch, os.path.join(MEMEPATH, meme))
        else:
            await printC(ch, "Error! Input syntax '!meme [meme_name]'")

    ### GENERATES A RANDOM TOWEL MEME ###
    elif msg == "!towel_meme":
        meme = random.choice(towel_meme_list)
        await client.send_file(ch, os.path.join(MEMEPATH, meme))

    ### TELLS PEOPLE NOT TO HONK ###
    elif msg == "!honk":
        await client.send_file(ch, os.path.join(MEMEPATH, "dont_honk.jpg"))

    ### HELP MESSAGE ###
    elif msg == "!helpmeme":
        if not str(ch).startswith("Direct Message with"):
            await printC(ch, "{0.mention}, please check your direct message inbox for a list of instructions.".format(message.author))
        await client.send_message(message.author, usage)

    elif msg == "!listmemes":
        if not str(ch).startswith("Direct Message with"):
            await printC(ch, "{0.mention}, please check your direct message inbox for a list of memes.".format(message.author))
        await printC(message.author, "***The following comands can be used with !meme [meme_name] to show a specific meme.***")
        await printC(message.author, "-----------------------------------------------------------------------------------")
        await printC(message.author, "\n".join(meme_list))

    elif msg == "!testdel":
        outmsg = "Hi!\nThis is a multiline message.\nI will delete this message after 3 seconds!\n(P.S. link is noob)"
        outmsg_obj = await printC(ch, outmsg)
        time.sleep(3)
        await client.delete_message(outmsg_obj)

    elif msg == "!ping":
        await printC(ch, "pong")

    elif msg == "!noob_scout":
        result = scout()
        await printC(ch, "{0.mention}, you drew an {1}!".format(message.author, result))

    elif msg == "!noob_scout11":
        results = [scout() for _ in range(11)]
        results.sort()
        await printC(ch, "{0.mention}, you drew an {1}!".format(message.author, results))
        if "UR" in results:
            await printtC(ch, "{0.mention} got a UR!!".format(message.author))


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

