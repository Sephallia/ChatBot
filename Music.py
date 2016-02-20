import discord
import asyncio

message = discord.Message()
client = discord.Client()

async def hearttoheart(channel):
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/01.%20HEART%20to%20HEART%21.mp3"
        msg_obj = await client.send_message(channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)
        msg = "!play https://dl.dropboxusercontent.com/u/24168007/ShareX/2016/01/LoveLive%20Music/02.%20%E5%B5%90%E3%81%AE%E3%81%AA%E3%81%8B%E3%81%AE%E6%81%8B%E3%81%A0%E3%81%8B%E3%82%89%28muse%29.mp3"
        msg_obj = await client.send_message(message.channel, msg)
        asyncio.sleep(3)
        await client.delete_message(msg_obj)
        return
