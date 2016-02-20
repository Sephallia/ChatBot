from __future__ import print_function
import discord
import os
import json
import requests
import aiohttp
import asyncio
from PIL import Image
import Music



client = discord.Client()
user = discord.User()
message = discord.Message()
scoutStats = {}

urcount = requests.get("http://schoolido.lu/api/cards/?is_promo=False&is_special=False&rarity=UR").json()
urcounttotal = urcount["count"]
srcount = requests.get("http://schoolido.lu/api/cards/?is_promo=False&is_special=False&rarity=SR").json()
srcounttotal = srcount["count"]
rcount = requests.get("http://schoolido.lu/api/cards/?is_promo=False&is_special=False&rarity=R").json()
rcounttotal = rcount["count"]

urlist = list()
srlist = list()
rlist = list()

dataur = requests.get("http://schoolido.lu/api/cards/?page=1&is_promo=False&is_special=False&page_size=100&rarity=UR").json()
for i in range(len(dataur["results"])):
    urlist.append(dataur["results"][i]["id"])
for x in range(1,5):
    datasr = requests.get("http://schoolido.lu/api/cards/?page=" + str(x) + "&is_promo=False&is_special=False&page_size=100&rarity=SR").json()
    for i in range(len(datasr["results"])):
        srlist.append(datasr["results"][i]["id"])
datar = requests.get("http://schoolido.lu/api/cards/?page=1&is_promo=False&is_special=False&page_size=100&rarity=R").json()
for i in range(len(datar["results"])):
    rlist.append(datar["results"][i]["id"])


@client.event
async def on_message(message):
    if message.author == client.user:
        return
#test bot response, also fun stuff
    if message.content.startswith("!hello"):
        if str(message.author.id) == "97097796372414464":
            msg = "Hello link Onii-chan!! :heart:"
            await client.send_message(message.channel, msg)
        else:
            msg = "Hello {0.author.mention} onii-sama!".format(message)
            await client.send_message(message.channel, msg)

#list of commands here
    if client.user in message.mentions:
        import time
        if message.author.id == "139966249248489472":
            return
        else:
            msg = "`Hi! I'm a bot made by link2110 to queue music and other things! Here are my commands:`\n`!hello - greets you`\n`!songhelp - list of songs to queue`\n`!scout11 - scouts 10+1 guaranteed SR/UR. May be slow, please wait.`\n`!textscout - Scouts 10+1 guaranteed SR/UR in text form`"
            await client.send_message(message.channel, msg)

#songlist
    if message.content.startswith("!songhelp"):
        msg = "`!hearttoheart - ueues Heart to Heart(full single)`\n`!waowao - Queues WAO-WAO Powerful Day!(full single)`\n`!omoide - Queues 思い出以上になりたくて(full single)`\n`!sakkaku - Queues 錯覚CROSSROADS(full single)`\n`!angelic - Queues Angelic Angel(full single)`\n`!sunnydaysong - Queues Sunny Day Song(full single)`\n`!yumenotobira - Queues Yume no Tobira(full single)`\n`!aqours - Queues 君のこころは輝いてるかい？(3songs)`\n`!imas1 - Queues some IM@S CG songs(5songs)`\n`!imas2 - Queues some different IM@S CG songs(5songs)`\n`!imas3 - Queues other IM@S songs(4songs)`\n`!imas4 - Queues still different IM@S songs(4songs)`\n`!itsudemo - Queues (✿◠‿◠) 〜ITSUDEMO (✿◠‿◠) 〜(1song)`\n`!psychicfire - Queues PSYCHIC FIRE(1song)`\n`!brainpower - Lists Brainpower!`\n`!shunjou - Queues 春情ロマンティック(1song)`\n`!korekara - Queues これから(1song)`\n`!bokuhika - Queues 僕たちはひとつの光(1song)`\n`!storminlover - Queues Storm in Lover(1song)`\n`!magnetic - Queues ずるいよMagnetic Today(1song)`\n`!feels - ;-; (3songs)`\n`!gochiusa1 - Queues some GochiUsa songs(4songs)`\n`!gochiusa2 - Queues some different GochiUsa songs(4songs)`\n`!railgun1 - Queues some Railgun music(4songs)`\n`!eriri1 - Queues some Eriri songs(3songs)`\n`!amaburi1 - Queues some AmaBuri songs(3songs)`\n`!oregairu1 - Queues OreGairu songs(4songs)`"
        await client.send_message(message.channel, msg)

#list of stuff to do
    if message.content.startswith("!todo"):
        if str(message.author.id) == "97097796372414464":
            msg = "Code MusicBot auto restart command \n ~~Finish coding 10+1 scout sim~~ \n Figure out that queue thing after shuffle \n ~~make LewdLive MusicBot~~ \n ~~Subunit autoplaylitsts~~ \n Make !music command better \n twitch emotes \n add trivia \n ~~figure out async~~ \n log number of messages sent by users in channel i.e the way Eter does it \n save scout data \n change songs to their own module\ntags and stuff\nsend songlist in PM instead"
            await client.send_message(message.channel, msg)
        else:
            msg = "You're not my Onii-chan!"
            await client.send_message(message.channel, msg)

#Set some music, only if it is link2110 sending commands
    if message.content.startswith("!music"):
        import asyncio
        if str(message.author.id) == "97097796372414464":
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01.%20Angelic%20Angel.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            asyncio.sleep(3)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01.%20HEART%20to%20HEART%21.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            asyncio.sleep(3)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01.%20SUNNY%20DAY%20SONG.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            asyncio.sleep(3)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01.%20WAO-WAO%20Powerful%20day%21.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            asyncio.sleep(3)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01.%20%E6%80%9D%E3%81%84%E5%87%BA%E4%BB%A5%E4%B8%8A%E3%81%AB%E3%81%AA%E3%82%8A%E3%81%9F%E3%81%8F%E3%81%A6%28LilyWhite%29.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            asyncio.sleep(3)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/1%20%E9%8C%AF%E8%A6%9ACROSSROADS.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            asyncio.sleep(3)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02%20Happy%20maker%21.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            asyncio.sleep(3)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02.%20%EF%BC%9F%E2%86%90HEARTBEAT.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            asyncio.sleep(3)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02.%20Future%20style.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            asyncio.sleep(3)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02.%20Hello%2C%E6%98%9F%E3%82%92%E6%95%B0%E3%81%88%E3%81%A6.mp3"
            msg_obj = await client.send_message(message.channel, msg)
            asyncio.sleep(3)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02.%20NO%20EXIT%20ORION.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            asyncio.sleep(3)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02.%20%E5%B5%90%E3%81%AE%E3%81%AA%E3%81%8B%E3%81%AE%E6%81%8B%E3%81%A0%E3%81%8B%E3%82%89%28muse%29.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            asyncio.sleep(3)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02.%20%E6%98%A5%E6%83%85%E3%83%AD%E3%83%9E%E3%83%B3%E3%83%86%E3%82%A3%E3%83%83%E3%82%AF%28LilyWhite2%29.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            asyncio.sleep(3)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/2%20PSYCHIC%20FIRE.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            asyncio.sleep(3)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01%20%E5%90%9B%E3%81%AE%E3%81%93%E3%81%93%E3%82%8D%E3%81%AF%E8%BC%9D%E3%81%84%E3%81%A6%E3%82%8B%E3%81%8B%E3%81%84%EF%BC%9F%28Aqours%29.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            asyncio.sleep(3)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02%20%EF%BC%B3%EF%BD%94%EF%BD%85%EF%BD%90%EF%BC%81%EF%BC%BA%EF%BC%A5%EF%BC%B2%EF%BC%AF%E3%80%80%EF%BD%94%EF%BD%8F%E3%80%80%EF%BC%AF%EF%BC%AE%EF%BC%A5%28Aqours%29.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            asyncio.sleep(3)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/03%20%EF%BC%A1%EF%BD%91%EF%BD%8F%EF%BD%95%EF%BD%92%EF%BD%93%E2%98%86%EF%BC%A8%EF%BC%A5%EF%BC%B2%EF%BC%AF%EF%BC%A5%EF%BC%B3%28Aqours%29.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            asyncio.sleep(3)
            await client.delete_message(msg_obj)
#otherwise refuse
        else:
            msg = "You're not my Onii-chan!".format(message)
            await client.send_message(message.channel, msg)

#public music commands

        #Heart to Heart
    if message.content.startswith("!hearttoheart"):
        # import asyncio
        # msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01.%20HEART%20to%20HEART%21.mp3"
        # msg_obj = await client.send_message(message.channel, msg)
        # asyncio.sleep(3)
        # await client.delete_message(msg_obj)
        # msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02.%20%E5%B5%90%E3%81%AE%E3%81%AA%E3%81%8B%E3%81%AE%E6%81%8B%E3%81%A0%E3%81%8B%E3%82%89%28muse%29.mp3"
        # msg_obj = await client.send_message(message.channel, msg)
        # asyncio.sleep(3)
        # await client.delete_message(msg_obj)
        timessquare = message.channel
        await Music.hearttoheart(timessquare)

        #WAO-WAO Powerful Day
    if message.content.startswith("!waowao"):
        import asyncio
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01.%20WAO-WAO%20Powerful%20day%21.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02.%20NO%20EXIT%20ORION.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #LilyWhite Omoide Ijou ni Naritakute
    if message.content.startswith("!omoide"):
        import asyncio
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01.%20%E6%80%9D%E3%81%84%E5%87%BA%E4%BB%A5%E4%B8%8A%E3%81%AB%E3%81%AA%E3%82%8A%E3%81%9F%E3%81%8F%E3%81%A6%28LilyWhite%29.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02.%20%E6%98%A5%E6%83%85%E3%83%AD%E3%83%9E%E3%83%B3%E3%83%86%E3%82%A3%E3%83%83%E3%82%AF%28LilyWhite%29.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #Sakkaku Crossroads
    if message.content.startswith("!sakkaku"):
        import asyncio
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/1%20%E9%8C%AF%E8%A6%9ACROSSROADS.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/2%20PSYCHIC%20FIRE.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #Angelic Angel
    if message.content.startswith("!angelic"):
        import asyncio
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01.%20Angelic%20Angel.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02.%20Hello%2C%E6%98%9F%E3%82%92%E6%95%B0%E3%81%88%E3%81%A6.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #SunnyDaySong
    if message.content.startswith("!sunnydaysong"):
        import asyncio
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01.%20SUNNY%20DAY%20SONG.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02.%20%EF%BC%9F%E2%86%90HEARTBEAT.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #Yume no Tobira
    if message.content.startswith("!yumenotobira"):
        import asyncio
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01%20Yume%20no%20Tobira.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02%20SENTIMENTAL%20StepS.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #IM@S #1
    if message.content == ("!imas1"):
        import asyncio
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/IM%40S/iM%40S%201/01.%20Shine%21%21.m4a"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/IM%40S/iM%40S%201/02.%20Never%20say%20never%20%7EFor%20Anastasia%20rearrange%20MIX%7E.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/IM%40S/iM%40S%201/02.%20S%28mile%29ING%21%20%7EFor%20Rin%20rearranged%20MIX%7E.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/IM%40S/iM%40S%201/03.%20%23U30df%23U30c4%23U30dc%23U30b7%23U2606%23U2606%23U2605%20%7EFor%20Minami%20rearrange%20MIX%7E.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/IM%40S/iM%40S%201/03.%20%E6%82%B2%E3%81%97%E3%81%BF%E3%82%92%E3%82%84%E3%81%95%E3%81%97%E3%81%95%E3%81%AB%28im%40s1%29.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #IM@S #2
    if message.content == ("!imas2"):
        import asyncio
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/IM%40S/iM%40S%202/01%20Anzu%20no%20Uta.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/IM%40S/iM%40S%202/01%20GOIN_%21%21%21.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/IM%40S/iM%40S%202/01.%20Trancing%20Pulse.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/IM%40S/iM%40S%202/02.%20dokxswzi%20-LOVE%20LAIKA%20qfdjt-.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/IM%40S/iM%40S%202/06%20Memories.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #Istudemo (✿◠‿◠) 〜ITSUDEMO (✿◠‿◠) 〜
    if message.content.startswith("!itsudemo"):
        import asyncio
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01.%20%E6%B0%B8%E9%81%A0%E3%83%95%E3%83%AC%E3%83%B3%E3%82%BA%28Printemps%29.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(2)
        await client.delete_message(msg_obj)

        #Psychic Fire
    if message.content.startswith("!psychicfire"):
        import asyncio
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/2%20PSYCHIC%20FIRE.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #Brainpower
    if message.content.startswith("!brainpower"):
        import time
        msg = "https://www.youtube.com/watch?v=9R8aSKwTEMg"
        msg_obj = await client.send_message(message.channel, msg)
        time.sleep(5)
        await client.delete_message(msg_obj)

        #Shunjou Romantic
    if message.content.startswith("!shunjou"):
        import asyncio
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02.%20%E6%98%A5%E6%83%85%E3%83%AD%E3%83%9E%E3%83%B3%E3%83%86%E3%82%A3%E3%83%83%E3%82%AF%28LilyWhite2%29.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #Final Single
    if message.content.startswith("!finalsingle"):
        import asyncio
        msg = "!play https://www.youtube.com/watch?v=VilL2kOF8NU"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #CantoBoyz
    if message.content.startswith("!cantoboyz"):
        msg = "CANTONESE IS PUMPING\nCANTONESE IS PUMPING\nGENERATOR\nAUTOMATIC CANTO\nCANTO\nCANTO\nCANTODRIVE\nCANTOBUSTER\nCANTOPOWER\nCALL ME A CANTO\nCANTONESE\nDON'T U TRY IT\nDON'T U TRY IT\nCANTOVATOR\nCANTO MACHINE\nTHERES NO CANTOS\nTAKE CANTO\nCANTOPOWER\nLET THE CANTO KICK\nC-CCCCCCCCCCC AAAC-A-A-N-T-O CA-CCCCCCCCCCCC -AAN-C-A-N-T-O-O- N-NNN-NN-NNN AA AAN-A-N-T-N-C- CA-AAA-AA-AA-AA NNNNT-O-CAN-TOOO C-CCCCCCCCCCC AAAC-A-A-N-T-O CA-CCCCCCCCCCCC -AAN-C-A-N-T-O-O- N-NNN-NN-NNN AA AAN-A-N-T-N-C- CA-AAA-AA-AA-AA NNNNT-O-CAN-TOOO C-CCCCCCCCCCC AAAC-A-A-N-T-O CA-CCCCCCCCCCCC -AAN-C-A-N-T-O-O- N-NNN-NN-NNN AA AAN-A-N-T-N-C- CA-AAA-AA-AA-AA NNNNT-O-CAN-TOOO C-CCCCCCCCCCC AAAC-A-A-N-T-O CA-CCCCCCCCCCCC -AAN-C-A-N-T-O-O- N-NNN-NN-NNN AA AAN-A-N-T-N-C- CA-AAA-AA-AA-AA NNNNT-O-CAN-TOOO C-CCCCCCCCCCC AAAC-A-A-N-T-O CA-CCCCCCCCCCCC -AAN-C-A-N-T-O-O- N-NNN-NN-NNN AA AAN-A-N-T-N-C- CA-AAA-AA-AA-AA NNNNT-O-CAN-TOOO C-CCCCCCCCCCC AAAC-A-A-N-T-O CA-CCCCCCCCCCCC -AAN-C-A-N-T-O-O- N-NNN-NN-NNN AA AAN-A-N-T-N-C- CA-AAA-AA-AA-AA NNNNT-O-CAN-TOOO C-CCCCCCCCCCC AAAC-A-A-N-T-O CA-CCCCCCCCCCCC -AAN-C-A-N-T-O-O- N-NNN-NN-NNN AA AAN-A-N-T-N-C- CA-AAA-AA-AA-AA NNNNT-O-CAN-TOOO C-CCCCCCCCCCC AAAC-A-A-N-T-O CA-CCCCCCCCCCCC -AAN-C-A-N-T-O-O- N-NNN-NN-NNN AA AAN-A-N-T-N-C- CA-AAA-AA-AA-AA NNNNT-O-CAN-TOOO C-CCCCCCCCCCC AAAC-A-A-N-T-O CA-CCCCCCCCCCCC -AAN-C-A-N-T-O-O- N-NNN-NN-NNN AA AAN-A-N-T-N-C- CA-AAA-AA-AA-AA NNNNT-O-CAN-TOOO"
        await client.send_message(message.channel, msg)

        #Korekara
    if message.content.startswith("!korekara"):
        import asyncio
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/%E3%81%93%E3%82%8C%E3%81%8B%E3%82%89%28muse2%29.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #BokuTachi
    if message.content.startswith("!bokutachi"):
        import asyncio
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/BokuHika.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #Storm in Lover
    if message.content.startswith("!storminlover"):
        import asyncio
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/Storm_in_Lover.ogg"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #Magnetic
    if message.content.startswith("!magnetic"):
        import asyncio
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/Zurui_yo_Magnetic_today.ogg"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #Aqours
    if message.content.startswith("!aqours"):
        import asyncio
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01%20%E5%90%9B%E3%81%AE%E3%81%93%E3%81%93%E3%82%8D%E3%81%AF%E8%BC%9D%E3%81%84%E3%81%A6%E3%82%8B%E3%81%8B%E3%81%84%EF%BC%9F%28Aqours%29.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02%20%EF%BC%B3%EF%BD%94%EF%BD%85%EF%BD%90%EF%BC%81%EF%BC%BA%EF%BC%A5%EF%BC%B2%EF%BC%AF%E3%80%80%EF%BD%94%EF%BD%8F%E3%80%80%EF%BC%AF%EF%BC%AE%EF%BC%A5%28Aqours%29.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/03%20%EF%BC%A1%EF%BD%91%EF%BD%8F%EF%BD%95%EF%BD%92%EF%BD%93%E2%98%86%EF%BC%A8%EF%BC%A5%EF%BC%B2%EF%BC%AF%EF%BC%A5%EF%BC%B3%28Aqours%29.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #feels
    if message.content == "!feels":
        import asyncio
        msg = "!play https://www.youtube.com/watch?v=VilL2kOF8NU"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/%E3%81%93%E3%82%8C%E3%81%8B%E3%82%89%28muse2%29.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/BokuHika.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #GochiUsa1
    if message.content == "!gochiusa1":
        import asyncio
        msg = "!play https://www.dropbox.com/s/hb4ykqevzhu3l6k/01%20Daydream%20cafe.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/s/6r5yosvtc3x4m6r/01%20Poppin%20Jump%E2%99%AA.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/s/nruve2hsd9yqxb4/nopoi%21.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/s/r8nmibjbdbck9dx/01tokimekipoporon%E2%99%AA.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #GochiUsa2
    if message.content == "!gochiusa2":
        import asyncio
        msg = "!play https://www.dropbox.com/s/di1ljh0qi1uqago/nantonaku.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/s/5wnt4mteigbchjf/nikkori.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/s/khyz9uz5j6eyjeu/nopoichino.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/s/aeny1wtfwwyzba9/02%20Daydream%20caf%C3%A9%20~Chino%20Ver.~.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #Railgun
    if message.content == "!railgun1":
        import asyncio
        msg = "!play https://www.dropbox.com/s/z0pc5ll4nm8vc64/01.%20only%20my%20railgun.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/s/frv09zcfubeblw2/02.%20LEVEL5%20-judgelight-.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/s/m62l6jtwdhb50ar/05.%20future%20gazer.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/s/uggjeij64ugwvhp/12.%20sister%27s%20noise.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #imas3
    if message.content == ("!imas3"):
        import asyncio
        msg = "!play https://www.dropbox.com/sh/cdhhg2bnjvstgpz/AABuZkw3WPYWaIYkbUmnUDn_a/01%20-LEGNE-%20Adanasu%20Tsurugi%20Hikari%20no%20Shirabe.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/sh/cdhhg2bnjvstgpz/AAC7WLKebhki6g-CX6hyBAXQa/01%20Nation%20Blue.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/sh/cdhhg2bnjvstgpz/AABhz-OCJgwIYMPp_mkSkHpHa/todokeidoru.m4a?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/sh/cdhhg2bnjvstgpz/AABdfJ5yg9qdjcmEQ3ajIaYaa/yumeiro%20-LOVE%20LAIKA%20-.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #imas4
    if message.content == ("!imas4"):
        import asyncio
        msg = "!play https://www.dropbox.com/sh/hl5jktag3abpka2/AAARw5QWJEEgZjgwawvRauwUa/01%20Koi%20Kaze.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/sh/hl5jktag3abpka2/AAA06IzWVj-mkpo1rd5L9bOea/02.%20Nebula%20Sky.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/sh/hl5jktag3abpka2/AADPJV9b7wm1jw6yUEu8RsWaa/fdsfsdh-LOVE%20LAIKA-Rosenburg%20Engel-.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/sh/hl5jktag3abpka2/AAADra0drmOtpuz2sMmL1DHva/yuubaepresent.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #Eriri
    if message.content == ("!eriri1"):
        import asyncio
        msg = "!play https://www.dropbox.com/sh/dtfa68oyd08qzif/AAAeTDsD9xttV1ODp89YcjXua/Blooming%20Lily.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/sh/dtfa68oyd08qzif/AAB0ha9NwHxLGCCxdkBEoOcRa/LOVE%20iLLUSiON%20%28Eriri%20Solo%20Ver.%29.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/sh/dtfa68oyd08qzif/AABOQNJzcjzaZFgo5jj_Exqda/Yuuki%20no%20Kamisama.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #Oregairu1
    if message.content == ("!oregairu1"):
        import asyncio
        msg = "!play https://www.dropbox.com/sh/2xmhc5f8xz48qmg/AADOz0WP-QrSZqHR_4g68vkNa/02%20Kashiko%20Girl.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/sh/2xmhc5f8xz48qmg/AAAtaSnQD_qrYklJ1YyW8O8ma/07%20Happy%20End%20no%20Soba%20de.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/sh/2xmhc5f8xz48qmg/AAALcYhZUCWKg0C0JJUFftXVa/08%20Kimi%20ni%20Crescendo.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/sh/2xmhc5f8xz48qmg/AAAqnf-LXdlD6RL59oc6inHPa/09%20Honmono%20ga%20Hoshikereba.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        #Amaburi1
    if message.content == ("!amaburi1"):
        import asyncio
        msg = "!play https://www.dropbox.com/sh/zrcu7v4lk2of8wa/AAD1-l20TOZ8DesC9CvX6fE3a/01%20elementario.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/sh/zrcu7v4lk2of8wa/AACcSZ_N6gtQrp7UM9bl23y3a/01%20EXTRA%20MAGIC%20HOUR.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

        msg = "!play https://www.dropbox.com/sh/zrcu7v4lk2of8wa/AAArZ2SA-FNPQh_WQGYAJb33a/02%20sdklfdshfklFUN%21TASY.mp3?dl=0"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)

    if message.content.startswith("!gameupdate"):
        if message.author.id == ("97097796372414464"):
            await gameupdate("@lolibot for help")
            msg = "Okay link Onii-chan :heart:"
            await client.send_message(message.channel, msg)

    if message.content.startswith("!scout11"):
        # if str(message.author.id) == "97097796372414464":
            import aiohttp
            import asyncio
            import random
            import time
            start = time.time()
            imagemake = Image.new("RGBA",(2048,2160))
            imgsave = "H:\Documents\PyCharmProjects\ChatBot"
            imagesend = os.path.join(imgsave,"merged.png")
            imgmergedsend =os.path.join(imgsave,"merged2.png")
            siteurl = "http://schoolido.lu/api/cards/"
            notr = 0
            rare = 0
            sr = 0
            ur = 0
            with aiohttp.ClientSession() as session:
                for x in range(11):
                # draw 10 cards with the chances for R/SR/UR at 90/9/1%
                    if 0 <= x <= 9:
                        chance = random.randint(0,100)
                        if 0 <= chance <= 90:
                            cardid = rlist[random.randint(0,rcounttotal-1)]
                            print(cardid)
                            data = await get_url(siteurl + str(cardid))
                            cardurl = data["card_image"]
                            async with session.get(cardurl) as resp:
                                cardimg = await resp.read()
                                with open((os.path.join(imgsave, "card" + str(x) + ".png")), "wb") as f:
                                    f.write(cardimg)
                            rare += 1
                        if 91 <= chance <= 99:
                            cardid = srlist[random.randint(0,srcounttotal)]
                            print(cardid)
                            data = await get_url(siteurl + str(cardid))
                            cardurl = data["card_image"]
                            async with session.get(cardurl) as resp:
                                cardimg = await resp.read()
                                with open((os.path.join(imgsave, "card" + str(x) + ".png")), "wb") as f:
                                    f.write(cardimg)
                            notr += 1
                            sr += 1
                        if chance == 100:
                            cardid = urlist[random.randint(0,urcounttotal)]
                            print(cardid)
                            data = await get_url(siteurl + str(cardid))
                            cardurl = data["card_image"]
                            async with session.get(cardurl) as resp:
                                cardimg = await resp.read()
                                with open((os.path.join(imgsave, "card" + str(x) + ".png")), "wb") as f:
                                    f.write(cardimg)
                            notr += 1
                            ur += 1
                #if no SR/UR in first 10, then give 90/10% chance of SR/UR
                    elif notr == 0:
                        chance3 = random.randint(0,100)
                        if 0 <= chance3 <= 90:
                            cardid = srlist[random.randint(0,srcounttotal)]
                            print(cardid)
                            data = await get_url(siteurl + str(cardid))
                            cardurl = data["card_image"]
                            async with session.get(cardurl) as resp:
                                cardimg = await resp.read()
                                with open((os.path.join(imgsave, "card" + str(x) + ".png")), "wb") as f:
                                    f.write(cardimg)
                            sr += 1
                            notr = notr + 1
                        if 91 <= chance3 <= 100:
                            cardid = urlist[random.randint(0,urcounttotal)]
                            print(cardid)
                            data = await get_url(siteurl + str(cardid))
                            cardurl = data["card_image"]
                            async with session.get(cardurl) as resp:
                                cardimg = await resp.read()
                                with open((os.path.join(imgsave, "card" + str(x) + ".png")), "wb") as f:
                                    f.write(cardimg)
                            ur += 1
                #if at least 1 SR/UR in first 10, then draw normal chance for last card
                    elif notr > 0:
                        chance1 = random.randint(0,100)
                        if 0 <= chance1 <= 90:
                            cardid = rlist[random.randint(0,rcounttotal-1)]
                            print(cardid)
                            data = await get_url(siteurl + str(cardid))
                            cardurl = data["card_image"]
                            async with session.get(cardurl) as resp:
                                cardimg = await resp.read()
                                with open((os.path.join(imgsave, "card" + str(x) + ".png")), "wb") as f:
                                    f.write(cardimg)
                            rare += 1
                        if 91 <= chance1 <= 99:
                            cardid = srlist[random.randint(0,srcounttotal)]
                            print(cardid)
                            data = await get_url(siteurl + str(cardid))
                            cardurl = data["card_image"]
                            async with session.get(cardurl) as resp:
                                cardimg = await resp.read()
                                with open((os.path.join(imgsave, "card" + str(x) + ".png")), "wb") as f:
                                    f.write(cardimg)
                            sr += 1
                            notr = notr + 1
                        if chance1 == 100:
                            cardid = urlist[random.randint(0,urcounttotal)]
                            print(cardid)
                            data = await get_url(siteurl + str(cardid))
                            cardurl = data["card_image"]
                            async with session.get(cardurl) as resp:
                                cardimg = await resp.read()
                                with open((os.path.join(imgsave, "card" + str(x) + ".png")), "wb") as f:
                                    f.write(cardimg)
                            ur += 1
                        print(time.time()-start)
                    if x == 0:
                        imagemake.paste(Image.open(os.path.join(imgsave,"card0.png")),(0,0))
                    elif x == 1:
                        imagemake.paste(Image.open(os.path.join(imgsave,"card1.png")),(513,0))
                    elif x == 2:
                        imagemake.paste(Image.open(os.path.join(imgsave,"card2.png")),(1025,0))
                    elif x == 3:
                        imagemake.paste(Image.open(os.path.join(imgsave,"card3.png")),(1537,0))
                    elif x == 4:
                        imagemake.paste(Image.open(os.path.join(imgsave,"card4.png")),(0,721))
                    elif x == 5:
                        imagemake.paste(Image.open(os.path.join(imgsave,"card5.png")),(513,721))
                    elif x == 6:
                        imagemake.paste(Image.open(os.path.join(imgsave,"card6.png")),(1025,721))
                    elif x == 7:
                        imagemake.paste(Image.open(os.path.join(imgsave,"card7.png")),(1537,721))
                    elif x == 8:
                        imagemake.paste(Image.open(os.path.join(imgsave,"card8.png")),(0,1441))
                    elif x == 9:
                        imagemake.paste(Image.open(os.path.join(imgsave,"card9.png")),(513,1441))
                    elif x == 10:
                        imagemake.paste(Image.open(os.path.join(imgsave,"card10.png")),(1025,1441))
                        imagemake.save(imagesend)
                        imageresize = Image.open(imagesend)
                        imagesend = imageresize.resize((1024,1080))
                        imagesend.save(imgmergedsend)
                        print(time.time()-start)
                        currentAuthorStats = None
                        
                        if (message.author.id in scoutStats):
                            currentAuthorStats = scoutStats[message.author.id]
                            currentAuthorStats.update(rare, sr, ur)
                        else:
                            currentAuthorStats = Stat()
                            currentAuthorStats.update(rare, sr, ur)
                            scoutStats[message.author.id] = currentAuthorStats
                        
                        await client.send_file(message.channel, imgmergedsend, content= "{} scouted {}R's, {}SR's and {}UR's this scout.\nOver the course of {} scouts, {} has scouted {}R's, {}SR's and {}UR's ".format(message.author.mention, str(rare), str(sr), str(ur), str(currentAuthorStats.count), message.author.name, str(currentAuthorStats.r), str(currentAuthorStats.sr), str(currentAuthorStats.ur)))
                        # msg = "{} scouted {}R's, {}SR's and {}UR's".format(message.author.mention, str(rare), str(sr), str(ur))
                        # await client.send_message(message.channel, msg)
                        # msg = "{} scouted {}R's, {}SR's and {}UR's".format(message.author.mention, str(rare), str(sr), str(ur))
                        # await client.send_message(message.channel, msg)
                        print(time.time()-start)
                        print(notr)

        # else:
        #     msg = "You're not my Onii-chan!"
        #     await client.send_message(message.channel, msg)


    #working async download
    if message.content.startswith("!async2"):
        import aiohttp
        with aiohttp.ClientSession() as session:
            async with session.get("http://schoolido.lu/api/cards/788/") as resp:
                data = await resp.json()
                card = data["card_image"]
                async with session.get(card) as resp2:
                    test = await resp2.read()
                    with open("cardtest2.png", "wb") as f:
                        f.write(test)

    if message.content.startswith("!textscout"):
        import random
        rare = 0
        superrare = 0
        ultrarare = 0
        notrare = 0
        for x in range(11):
            chance = random.randint(0,100)
            if 0 <= x <= 9:
                if 0 <= chance <= 90:
                    rare += 1
                if 91 <= chance <= 99:
                    superrare += 1
                    notrare += 1
                if chance == 100:
                    ultrarare += 1
                    notrare += 1
            elif notrare == 0:
                chance2 = random.randint(0,100)
                if 0 <= chance2 <= 90:
                    superrare += 1
                if 91 <= chance2 <= 100:
                    ultrarare += 1
            elif notrare > 0:
                if 0 <= chance <= 90:
                    rare += 1
                if 91 <= chance <= 99:
                    superrare += 1
                    notrare += 1
                if chance == 100:
                    ultrarare += 1
                    notrare += 1
        msg = "You scouted " + str(rare) + " R's, " + str(superrare) + " SR's, and " + str(ultrarare) + " UR's."
        await client.send_message(message.channel, msg)
        id = message.author.id

    if message.content.startswith("!chance2test"):
        # if message.author.id == "97097796372414464":
            import random
            rare = 0
            superrare = 0
            ultrarare = 0
            notrare = 0
            for y in range (1000):
                for x in range(11):
                    chance = random.randint(0,100)
                    if 0 <= x <= 9:
                        if 0 <= chance <= 90:
                            rare += 1
                        if 91 <= chance <= 99:
                            superrare += 1
                            notrare += 1
                        if chance == 100:
                            ultrarare += 1
                            notrare += 1
                    elif notrare == 0:
                        chance2 = random.randint(0,100)
                        if 0 <= chance2 <= 90:
                            superrare += 1
                        if 91 <= chance2 <= 100:
                            ultrarare += 1
                    elif notrare > 0:
                        if 0 <= chance <= 90:
                            rare += 1
                        if 91 <= chance <= 99:
                            superrare += 1
                            notrare += 1
                        if chance == 100:
                            ultrarare += 1
                            notrare += 1
            rarepercent = (rare / 11000) * 100
            srpercent = (superrare / 11000) * 100
            urpercent = (ultrarare / 11000) * 100
            msg = "The percentage of your scouts is: " + str(rarepercent) + "% R's, " + str(srpercent) + "% SR's and " + str(urpercent) + "% UR's"
            await client.send_message(message.channel, msg)

        # else:
        #     msg = "You're not my Onii-chan!"
        #     await client.send_message(message.channel, msg)

    if message.content.startswith("!asynctest"):
        if message.author.id == "98528499408576512":
            msg = "Fuk you {0.author.mention}".format(message)
            await client.send_message(message.channel, msg)
        else:
            msg = "This command is dead, use !scout11"
            await client.send_message(message.channel, msg)

    if message.content.startswith("!speedtest1"):
        import random
        import aiohttp
        import time
        start = time.time()
        with aiohttp.ClientSession() as session:
            for x in range(11):
                cardid = rlist[random.randint(0,rcounttotal-1)]
                print(cardid)
                async with session.get("http://schoolido.lu/api/cards/" + str(cardid)) as resp:
                    data = await resp.json()
                    card = data["card_image"]
                    async with session.get(card) as resp2:
                        cardimg = await resp2.read()
                        with open("card" + str(x) + ".png", "wb") as f:
                            f.write(cardimg)
        print("Done!")
        print(time.time()-start)

    if message.content.startswith("!speedtest2"):
        import random
        import aiohttp
        import time
        start = time.time()
        siteurl = "http://schoolido.lu/api/cards/"
        with aiohttp.ClientSession() as session:
            for x in range(11):
                cardid = rlist[random.randint(0,rcounttotal-1)]
                data = await get_url(siteurl + str(cardid))
                cardurl = data["card_image"]
                print(cardurl)
                # async with session.get(cardurl) as resp:
                #     cardimg = await resp.read()
                #     with open("card" + str(x) + ".png", "wb") as f:
                #         f.write(cardimg)
            print(time.time()-start)


async def get_url(url):
    response = await aiohttp.request("GET", url)
    data = await response.json()
    return data

async def gameupdate(game):
    gamename = str(game)
    await client.change_status(game=discord.Game(name=gamename))
    return



#stats_dict = {id : Stat}

class Stat:
    def __init__(self):
        self.count = 0
        self.r = 0
        self.sr = 0
        self.ur = 0
    def update(self, rCount, srCount, urCount):
        self.count += 1
        self.r += rCount
        self.sr += srCount
        self.ur += urCount

#client.change_status(game=discord.Game(name="your custom game here"))
@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)

filepos = "H:\Documents\PyCharmProjects\ChatBot"
docs = open(os.path.join(filepos, "username.txt"))
credentials = json.load(docs)
client.run(credentials["username"], credentials["password"])
