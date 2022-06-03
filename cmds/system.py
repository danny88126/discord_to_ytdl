# -*- coding: utf-8 -*-
#Programmer: 易弘翔
#Date: 2022/06/03
#機器人COG系統主程式
#pip install discord.py
#pip install youtube-dl
 
import discord                          #導入discord套件
from discord.ext import commands        #導入discord套件中的commands模組
from core.classes import Cog_Extension  #導入core資料夾中的Cog_Extension指令

class System(Cog_Extension):            # 定義System類別

    @commands.command()                                          #設定discord的指令模組
    async def ping(self, ctx):                                   #定義ping指令
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')    #計算延遲並用ms印出
    
    @commands.command()               #設定discord的指令模組 
    async def version(self, ctx):     #定義version指令
        await ctx.send("v1.0")        #回傳版本號

def setup(bot):                       #設定cog中讀取的程式類別為System
    bot.add_cog(System(bot))