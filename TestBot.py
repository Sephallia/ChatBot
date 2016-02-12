from __future__ import print_function
import discord
import time
import os, sys
import json
import urllib.request as ur
import requests
from PIL import Image


client = discord.Client()
user = discord.User()
message = discord.Message()

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
            msg = "You're not link2110!".format(message)
            await client.send_message(message.channel, msg)
#list of commands here
    if message.content.startswith("!lolibothelp"):
        msg = "`!hello - greets you`\n`!testcommand - test`"
        await client.send_message(message.channel, msg)

#test message deletion here (use 2 second sleep)
    if message.content.startswith("!deletetest"):

        if str(message.author.id) == "97097796372414464":
            msg = "!play test"
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play test2"
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play test3"
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play test4"
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play test5"
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play test6"
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play test7"
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play test8"
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)
            msg = "!play test9"
            msg_obj = await client.send_message(message.channel, msg)
            time.sleep(2)
            await client.delete_message(msg_obj)

    #Get images to cut/paste together
    if message.content.startswith("!imagetest1"):
        img1 = os.path.join("H:\Documents\PyCharmProjects\ChatBot\Images","796RoundUmi.png")
        img2 = os.path.join("H:\Documents\PyCharmProjects\ChatBot\Images","795RoundEli.png")
        img5 = os.path.join("H:\Documents\PyCharmProjects\ChatBot\Images","797RoundNozomi.png")
        img6 = os.path.join("H:\Documents\PyCharmProjects\ChatBot\Images","797RoundHanayo.png")
        img7 = os.path.join("H:\Documents\PyCharmProjects\ChatBot\Images","795RoundNico.png")
        img4 = os.path.join("H:\Documents\PyCharmProjects\ChatBot\Images","test.png")
        img3 = Image.new("RGBA", (640,128))
        img3.paste(Image.open(img1), (0,0))
        img3.paste(Image.open(img2),(129,0))
        img3.paste(Image.open(img5),(257,0))
        img3.paste(Image.open(img6),(385,0))
        img3.paste(Image.open(img7),(513,0))
        img3.save(img4)
        await client.send_file(message.channel, img4)

    #larger image test
    if message.content.startswith("!imagetest2"):
        image1 = os.path.join("H:\Documents\PyCharmProjects\ChatBot\Images","796Umi.png")
        image2 = os.path.join("H:\Documents\PyCharmProjects\ChatBot\Images","795Eli.png")
        image3 = os.path.join("H:\Documents\PyCharmProjects\ChatBot\Images","797Nozomi.png")
        image4 = os.path.join("H:\Documents\PyCharmProjects\ChatBot\Images","798Hanayo.png")
        image5 = os.path.join("H:\Documents\PyCharmProjects\ChatBot\Images","799Nico.png")
        image7 = os.path.join("H:\Documents\PyCharmProjects\ChatBot\Images","test1.png")
        image6 = Image.new("RGBA",(2560,720))
        image6.paste(Image.open(image1),(0,0))
        image6.paste(Image.open(image2),(513,0))
        image6.paste(Image.open(image3),(1025,0))
        image6.paste(Image.open(image4),(1537,0))
        image6.paste(Image.open(image5),(2049,0))
        image6.save(image7)
        await client.send_file(message.channel, image7)

    #get JSON to display and parse (try something with classes next time)
    #if message.content.startswith("!jsontest"):
        import requests
        data = requests.get('http://schoolido.lu/api/cards/799/').json()
        print(data)
        #id = "799"
        #url = "http://schoolido.lu/api/cards/" + id + "/"
        response = ur.urlopen("http://schoolido.lu/api/cards/799/")
        #testing = json.loads(response)
        #print ('"id":', testing['id']['name']['attribute']['rarity'])

    if message.content.startswith("!testimg"):
        import requests
        import shutil
        data = requests.get("http://schoolido.lu/api/cards/799/").json()
        imgsave = "C:\\Users\pwu\Pictures\Python"
        cardsave = requests.get(data["card_image"], stream=True)
        with open((os.path.join(imgsave, "card.png")),"wb") as out_file:
            shutil.copyfileobj(cardsave.raw, out_file)
        roundsave = requests.get(data["round_card_image"], stream=True)
        with open((os.path.join(imgsave, "round.png")),"wb") as out_file:
            shutil.copyfileobj(roundsave.raw, out_file)
        imagesend = os.path.join(imgsave,"merged.png")
        imagemake = Image.new("RGBA",(512,848))
        imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(0,0))
        imagemake.paste(Image.open(os.path.join(imgsave,"round.png")),(0,720))
        imagemake.save(imagesend)
        imageresize = Image.open(imagesend)
        imageresize.thumbnail((258,360))
        imageresize.save(imagesend)
        await client.send_file(message.channel, imagesend)

    if message.content.startswith("!fortest"):
        import requests
        import shutil
        import random
        imagemake = Image.new("RGBA",(5632,848))
        for x in range (0,3):
            id = random.randrange(1,799,1)
            data = requests.get("http://schoolido.lu/api/cards/" + str(id)).json()
            imgsave = "C:\\Users\pwu\Pictures\Python"
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
            if x == 0:
                imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(0,0))
                imagemake.paste(Image.open(os.path.join(imgsave,"round.png")),(0,720))
            elif x == 1:
                imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(513,0))
                imagemake.paste(Image.open(os.path.join(imgsave,"round.png")),(513,720))
            elif x == 2:
                imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(1025,0))
                imagemake.paste(Image.open(os.path.join(imgsave,"round.png")),(1025,720))
            # elif x == 3:
            #     imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(1537,0))
            #     imagemake.paste(Image.open(os.path.join(imgsave,"round.png")),(1537,720))
            # elif x == 4:
            #     imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(2049,0))
            #     imagemake.paste(Image.open(os.path.join(imgsave,"round.png")),(2049,720))
            # elif x == 5:
            #     imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(2561,0))
            #     imagemake.paste(Image.open(os.path.join(imgsave,"round.png")),(2561,720))
            # elif x == 6:
            #     imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(3073,0))
            #     imagemake.paste(Image.open(os.path.join(imgsave,"round.png")),(3073,720))
            # elif x == 7:
            #     imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(3585,0))
            #     imagemake.paste(Image.open(os.path.join(imgsave,"round.png")),(3585,720))
            # elif x == 8:
            #     imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(4097,0))
            #     imagemake.paste(Image.open(os.path.join(imgsave,"round.png")),(4097,720))
            # elif x == 9:
            #     imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(4609,0))
            #     imagemake.paste(Image.open(os.path.join(imgsave,"round.png")),(4609,720))
            # elif x == 10:
            #     imagemake.paste(Image.open(os.path.join(imgsave,"card.png")),(5121,0))
            #     imagemake.paste(Image.open(os.path.join(imgsave,"round.png")),(5121,720))
            #     imagemake.save(imagesend)
            #     imageresize = Image.open(imagesend)
            #     imageresize.thumbnail((1800,848))
                imageresize.save(imagesend)
            else:
                print(x)
        await client.send_file(message.channel, imagesend)

#flter by card rarity: http://schoolido.lu/api/cards/?rarity=UR

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)

client.run('link2115@hotmail.com', 'link2113')
