# -*- coding: utf-8 -*-
#Programmer: 易弘翔
#Date: 2022/06/04
#機器人youtube_dl類別指令


import discord                          #導入discord套件
from discord.ext import commands        #導入discord套件中的commands模組
from core.classes import Cog_Extension  #導入core資料夾中的Cog_Extension指令
import youtube_dl                       #導入youtube_dl套件

def get_video_info(youtube_url):              #定義各項youtube_dl所回傳的資料及字典的建立
    video_info = {}
    with youtube_dl.YoutubeDL() as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        video_info['ID'] = info.get('id')
        video_info['標題'] = info.get('title')
        video_info['影片縮圖'] = info.get('thumbnail')
        video_info['上傳者'] = info.get('uploader')
        video_info['上傳者網址'] = info.get('uploader_url')
        video_info['影片長度(秒)'] = str(info.get('duration'))
        video_info['觀看次數'] = str(info.get('view_count'))
        video_info['喜歡數'] = str(info.get('like_count'))
        video_info['描述'] = info.get('description')
        video_info['上傳日期'] = info.get('upload_date')
    return video_info       

class YtGet(Cog_Extension):              #定義YtGet類別

    @commands.command()                      #設定discord的指令模組
    async def yt_pic(self, ctx, *, msg):     #定義yt_pic指令,並把指令後的文字定義為URL
        await ctx.message.delete()           #將剛剛使用者的指令刪除
        video_info = get_video_info(msg)     #將剛剛的URL帶入get_video_info抓取影片資料
        await ctx.send(video_info['標題'] + "的縮圖是" + video_info['影片縮圖'])    #回傳影片標題及影片縮圖

    @commands.command()                      #設定discord的指令模組
    async def yt_likes(self, ctx, *, msg):   #定義yt_likes指令,並把指令後的文字定義為URL
        await ctx.message.delete()           #將剛剛使用者的指令刪除
        video_info = get_video_info(msg)     #將剛剛的URL帶入get_video_info抓取影片資料
        await ctx.send(video_info['標題'] + "的likes數為" + video_info['喜歡數'])    #回傳影片標題及影片喜歡數
    
    @commands.command()                      #設定discord的指令模組
    async def yt_author(self, ctx, *, msg):  #定義yt_author指令,並把指令後的文字定義為URL
        await ctx.message.delete()           #將剛剛使用者的指令刪除
        video_info = get_video_info(msg)     #將剛剛的URL帶入get_video_info抓取影片資料
        await ctx.send(video_info['標題'] + "的上傳者為" + video_info['上傳者'] + "\n" + video_info['上傳者網址'])    #回傳影片標題及影片上傳者

    @commands.command()                      #設定discord的指令模組
    async def yt_views(self, ctx, *, msg):   #定義yt_views指令,並把指令後的文字定義為URL
        await ctx.message.delete()           #將剛剛使用者的指令刪除
        video_info = get_video_info(msg)     #將剛剛的URL帶入get_video_info抓取影片資料
        await ctx.send(video_info['標題'] + "的觀看數為" + video_info['觀看次數'])    #回傳影片標題及影片觀看數
    
    @commands.command()                      #設定discord的指令模組
    async def yt_date(self, ctx, *, msg):    #定義yt_date指令,並把指令後的文字定義為URL
        await ctx.message.delete()           #將剛剛使用者的指令刪除
        video_info = get_video_info(msg)     #將剛剛的URL帶入get_video_info抓取影片資料
        await ctx.send(video_info['標題'] + "的上傳時間" + video_info['上傳日期'])    #回傳影片標題及影片上傳時間

    @commands.command()                      #設定discord的指令模組
    async def yt_txt(self, ctx, *, msg):     #定義yt_txt指令,並把指令後的文字定義為URL
        await ctx.message.delete()           #將剛剛使用者的指令刪除
        video_info = get_video_info(msg)     #將剛剛的URL帶入get_video_info抓取影片資料
        await ctx.send(video_info['標題'] + "的描述為\n" + video_info['描述'])    #回傳影片標題及影片敘述
    
    @commands.command()                      #設定discord的指令模組
    async def yt_time(self, ctx, *, msg):    #定義yt_time指令,並把指令後的文字定義為URL
        await ctx.message.delete()           #將剛剛使用者的指令刪除
        video_info = get_video_info(msg)     #將剛剛的URL帶入get_video_info抓取影片資料
        await ctx.send(video_info['標題'] + "的影片長度為" + video_info['影片長度(秒)'] + 's')    #回傳影片標題及影片長度(單位為秒)
        
def setup(bot):                      #設定cog中讀取的程式類別為YtGet
    bot.add_cog(YtGet(bot))
