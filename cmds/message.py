# -*- coding: utf-8 -*-
#Programmer: 易弘翔
#Date: 2022/06/05
#機器人回應類別指令

import discord                          #導入discord套件
from discord.ext import commands        #導入discord套件中的commands模組
from core.classes import Cog_Extension  #導入core資料夾中的Cog_Extension指令
import random                           #導入隨機套件

class Message(Cog_Extension):              #定義Message類別

    @commands.Cog.listener()               #設定discord的指令模組
    async def on_message(self, msg):       #定義讀取到的訊息      

        if msg.content.startswith("要不要"):       #如果訊息開頭是"要不要"
            rc = random.choice(['要','不要'])      #定義rc隨機為為要,不要
            await msg.channel.send(rc)             #回傳rc
        
        if msg.content.endswith("好不好"):         #如果訊息結尾是好不好
            rc = random.choice(['好','不好'])      #定義rc隨機為好,不好
            await msg.channel.send(rc)             #回傳rc

        if msg.content == "早安" and msg.author != self.bot.user:     #如果訊息為早安    
            await msg.channel.send("早安")                            #回傳早安
        
        if msg.content == "午安" and msg.author != self.bot.user:     #如果訊息為午安
            await msg.channel.send("午安")                            #回傳午安
        
        if msg.content == "晚安" and msg.author != self.bot.user:     #如果訊息為晚安
            await msg.channel.send("晚安")                            #回傳晚安
        
def setup(bot):                         #設定cog中讀取的程式類別為Message
    bot.add_cog(Message(bot))