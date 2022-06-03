# -*- coding: utf-8 -*-
#Programmer: 易弘翔
#Date: 2022/06/03
#機器人主程式
#pip install discord.py
#pip install youtube-dl
 
 
 
import discord                       #導入discord套件
from discord.ext import commands     #導入discord套件中的commands模組
import json                          #導入json套件
import os                            #導入os套件

with open('setting.json','r', encoding='utf8') as jfile:     #將setting.json檔用utf8編碼讀取
    jdata = json.load(jfile)                                 #定義jdata為setting.json檔案中的資料

intents = discord.Intents.all()                              #discord套件中的權限全開

bot = commands.Bot(command_prefix=jdata['BOT_PREFIX'],intents = intents)  #定義discord bot中指令的起始符號

@bot.event                                            #設定discord的活動模組
async def on_ready():                                 #定義on_ready狀態(BOT啟動時)
    print(">>Bot is online<<")                        #當啟動時列印(>>Bot is online<<)

@bot.command()                                        #設定discord的指令模組
async def load(ctx,extension):                        #定義load指令
    bot.load_extension(f'cmds.{extension}')           #讀取cmd資料夾下特定檔案的指令
    await ctx.send(f'Loaded {extension} done')        #列印讀取檔案成功

@bot.command()                                        #設定discord的指令模組
async def unload(ctx,extension):                      #定義unload指令
    bot.unload_extension(f'cmds.{extension}')         #卸除cmd資料夾下特定檔案的指令
    await ctx.send(f'Unloaded {extension} done')      #列印卸除檔案成功

@bot.command()                                        #設定discord的指令模組
async def reload(ctx,extension):                      #定義reload指令
    bot.reload_extension(f'cmds.{extension}')         #重新讀取cmd資料夾下特定檔案的指令
    await ctx.send(f'Reloaded {extension} done')      #列印重新讀取檔案成功

for filename in os.listdir('./cmds'):                    #利用os模組讀取cmd模組的名字
    if filename.endswith('.py'):                         #如果檔案結尾為.py
            bot.load_extension(f'cmds.{filename[:-3]}')  #載入檔案

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])                              #discord api 的tokon
