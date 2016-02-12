from __future__ import print_function
import discord
import os
import requests
from PIL import Image



client = discord.Client()
user = discord.User()
message = discord.Message()


# dataur = requests.get("http://schoolido.lu/api/cards/?page=1&page_size=1000&rarity=UR").json()
# urtotal = len(dataur["results"])
# datasr = requests.get("http://schoolido.lu/api/cards/?page=1&page_size=1000&rarity=SR").json()
# srtotal = len(datasr["results"])
# datar = requests.get("http://schoolido.lu/api/cards/?page=1&page_size=1000&rarity=R").json()
# rtotal = len(datar["results"])

# urcount = requests.get("http://schoolido.lu/api/cards/?rarity=UR").json()
# urcounttotal = urcount["count"]
# srcount = requests.get("http://schoolido.lu/api/cards/?rarity=SR").json()
# srcounttotal = srcount["count"]
# rcount = requests.get("http://schoolido.lu/api/cards/?rarity=R").json()
# rcounttotal = rcount["count"]
#
urlist = list()
srlist = list()
rlist = list()
for x in range(1,11):
    dataur = requests.get("http://schoolido.lu/api/cards/?page= " + str(x) + "page_size=100&rarity=UR").json()
    for i in range(len(dataur["results"])):
        urlist.append(dataur["results"][i]["id"])
for x in range(1,40):
    datasr = requests.get("http://schoolido.lu/api/cards/?page= " + str(x) + "page_size=100&rarity=SR").json()
    for i in range(len(datasr["results"])):
        srlist.append(datasr["results"][i]["id"])
for x in range(1,15):
    datar = requests.get("http://schoolido.lu/api/cards/?page= " + str(x) + "page_size=100&rarity=R").json()
    for i in range(len(datar["results"])):
        rlist.append(datar["results"][i]["id"])

@client.event
async def on_message(message):
    if message.author == client.user:
        return
#test bot response, also fun stuff
    if message.content.startswith("!hello"):
        msg = "Hello {0.author.mention} onii-sama!".format(message)
        await client.send_message(message.channel, msg)
#Set some music, only if it is link2110 sending commands
    if message.content.startswith("!music"):
        import time
        if str(message.author.id) == "97097796372414464":
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01.%20Angelic%20Angel.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01.%20HEART%20to%20HEART%21.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01.%20SUNNY%20DAY%20SONG.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01.%20WAO-WAO%20Powerful%20day%21.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01.%20%E6%80%9D%E3%81%84%E5%87%BA%E4%BB%A5%E4%B8%8A%E3%81%AB%E3%81%AA%E3%82%8A%E3%81%9F%E3%81%8F%E3%81%A6.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/1%20%E9%8C%AF%E8%A6%9ACROSSROADS.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02%20Happy%20maker%21.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02.%20%EF%BC%9F%E2%86%90HEARTBEAT.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02.%20Future%20style.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02.%20NO%20EXIT%20ORION.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02.%20%E5%B5%90%E3%81%AE%E3%81%AA%E3%81%8B%E3%81%AE%E6%81%8B%E3%81%A0%E3%81%8B%E3%82%89.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02.%20%E6%98%A5%E6%83%85%E3%83%AD%E3%83%9E%E3%83%B3%E3%83%86%E3%82%A3%E3%83%83%E3%82%AF.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/2%20PSYCHIC%20FIRE.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01%20%E5%90%9B%E3%81%AE%E3%81%93%E3%81%93%E3%82%8D%E3%81%AF%E8%BC%9D%E3%81%84%E3%81%A6%E3%82%8B%E3%81%8B%E3%81%84%EF%BC%9F.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02%20%EF%BC%B3%EF%BD%94%EF%BD%85%EF%BD%90%EF%BC%81%EF%BC%BA%EF%BC%A5%EF%BC%B2%EF%BC%AF%E3%80%80%EF%BD%94%EF%BD%8F%E3%80%80%EF%BC%AF%EF%BC%AE%EF%BC%A5.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/03%20%EF%BC%A1%EF%BD%91%EF%BD%8F%EF%BD%95%EF%BD%92%EF%BD%93%E2%98%86%EF%BC%A8%EF%BC%A5%EF%BC%B2%EF%BC%AF%EF%BC%A5%EF%BC%B3.mp3".format(message)
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
#otherwise refuse
        else:
            msg = "You're not my Onii-chan!".format(message)
            await client.send_message(message.channel, msg)
#list of commands here
    if message.content.startswith("!lolibothelp"):
        msg = "`!hello - greets you`\n`!testcommand - test`"
        await client.send_message(message.channel, msg)
#list of stuff to do
    if message.content.startswith("!todo"):
        if str(message.author.id) == "97097796372414464":
            msg = "'Code MusicBot auto restart command' \n 'Finish coding 10+1 scout sim' \n 'Figure out that queue thing after shuffle' \n '~~make LewdLive MusicBot~~' \n 'Subunit autoplaylitsts' \n 'Make !music command better"
            await client.send_message(message.channel, msg)
        else:
            msg = "You're not my Onii-chan!"
            await client.send_message(message.channel, msg)

#if card is idolized, need to call card_idolized_image, or round_card_idolized_image
    if message.content.startswith("!jsontest"):
        import random
        id = random.randrange(1,799,1)
        url = "http://schoolido.lu/api/cards/" + str(id) + "/"
        data = requests.get(url).json()
        msg = data['id'], data['rarity'], data['attribute'], data['card_image'], data['card_idolized_image'], data['round_card_image'], data['round_card_idolized_image']
        await client.send_message(message.channel, msg)

    if message.content.startswith("!fortest"):
        if str(message.author.id) == "97097796372414464":
            import requests
            import shutil
            import random
            start = time.time()
            imagemake = Image.new("RGBA",(2048,2160))
            for x in range (0,11):
                id = random.randrange(1,799,1)
                data = requests.get("http://schoolido.lu/api/cards/" + str(id)).json()
                imgsave = "H:\Documents\PyCharmProjects\ChatBot\Images"
                if data["is_promo"] == False:
                    cardsave = requests.get(data["card_image"], stream=True)
                    with open((os.path.join(imgsave, "card.png")),"wb") as out_file:
                        shutil.copyfileobj(cardsave.raw, out_file)
                    roundsave = requests.get(data["round_card_image"], stream=True)
                    with open((os.path.join(imgsave, "round.png")),"wb") as out_file:
                        shutil.copyfileobj(roundsave.raw, out_file)
                elif data["is_promo"] == True:
                    cardsave = requests.get(data["card_idolized_image"], stream=True)
                    with open((os.path.join(imgsave, "card.png")),"wb") as out_file:
                        shutil.copyfileobj(cardsave.raw, out_file)
                    roundsave = requests.get(data["round_card_idolized_image"], stream=True)
                    with open((os.path.join(imgsave, "round.png")),"wb") as out_file:
                        shutil.copyfileobj(roundsave.raw, out_file)
                imagesend = os.path.join(imgsave,"merged.png")

                # Working elif code.

                if x == 0:
                    imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(0,0))
                elif x == 1:
                    imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(513,0))
                elif x == 2:
                    imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(1025,0))
                elif x == 3:
                    imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(1537,0))
                elif x == 4:
                    imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(0,721))
                elif x == 5:
                    imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(513,721))
                elif x == 6:
                    imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(1025,721))
                elif x == 7:
                    imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(1537,721))
                elif x == 8:
                    imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(0,1441))
                elif x == 9:
                    imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(513,1441))
                elif x == 10:
                    imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(1025,1441))
                    imagemake.save(imagesend)
                    await client.send_file(message.channel, imagesend)
                    print(time.time()-start)
        else:
            msg = "You're not my Onii-chan!"
            await client.send_message(message.channel, msg)

    if message.content.startswith("!dictest"):
        if str(message.author.id) == "97097796372414464":
            import requests
            import time
            start = time.time()
            # urcount = requests.get("http://schoolido.lu/api/cards/?rarity=UR").json()
            # urcounttotal = urcount["count"]
            # srcount = requests.get("http://schoolido.lu/api/cards/?rarity=SR").json()
            # srcounttotal = srcount["count"]
            # rcount = requests.get("http://schoolido.lu/api/cards/?rarity=R").json()
            # rcounttotal = rcount["count"]
            # urlist = list()
            # srlist = list()
            # rlist = list()
            # for x in range(1,3):
            #     dataur = requests.get("http://schoolido.lu/api/cards/?page= " + str(x) + "page_size=100&rarity=UR").json()
            #     for i in range(len(dataur["results"])):
            #         urlist.append(dataur["results"][i]["id"])
            # for x in range(1,5):
            #     datasr = requests.get("http://schoolido.lu/api/cards/?page= " + str(x) + "page_size=100&rarity=SR").json()
            #     for i in range(len(datasr["results"])):
            #         srlist.append(datasr["results"][i]["id"])
            # for x in range(1,3):
            #     datar = requests.get("http://schoolido.lu/api/cards/?page= " + str(x) + "page_size=100&rarity=R").json()
            #     for i in range(len(datar["results"])):
            #         rlist.append(datar["results"][i]["id"])
        else:
            msg = "You're not my Onii-chan!"
            await client.send_message(message.channel, msg)

    if message.content.startswith("!asynctest"):
        if str(message.author.id) == "97097796372414464":
            import requests
            import random
            import time
            start = time.time()
            # for x in range(3):
            #     id = dataur["results"][random.randint(0,len(results)-1)]["id"]
            #     print(id)
            #     print(time.time()-start)
        else:
            msg = "You're not my Onii-chan!"
            await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)

client.run('link21110@hotmail.com', 'link2113')
