# -*- coding: utf-8 -*-
#Programmer: 易弘翔
#Date: 2022/06/04
#定義機器人的文件


import discord                       #導入discord套件
from discord.ext import commands     #導入discord套件中的commands模組

class Cog_Extension(commands.Cog):  #定義機器人本身
    def __init__(self, bot):
        self.bot = bot