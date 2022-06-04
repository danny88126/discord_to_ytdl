# -*- coding: utf-8 -*-
#Programmer: 易弘翔
#Date: 2022/06/04
#機器人回應類別指令


import discord                          #導入discord套件
from discord.ext import commands        #導入discord套件中的commands模組
from core.classes import Cog_Extension  #導入core資料夾中的Cog_Extension指令
import random                           #導入隨機套件

class Message(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):

        if msg.content.startswith("要不要"):
            rc = random.choice(['要','不要'])
            await msg.channel.send(rc)
        
        if msg.content.endswith("好不好"):
            rc = random.choice(['好','不好'])
            await msg.channel.send(rc)

        if msg.content == "早安" and msg.author != self.bot.user:
            await msg.channel.send("早安")
        
        if msg.content == "午安" and msg.author != self.bot.user:
            await msg.channel.send("午安")
        
        if msg.content == "晚安" and msg.author != self.bot.user:
            await msg.channel.send("晚安")
        

def setup(bot):
    bot.add_cog(Message(bot))