import discord
from discord.ext import commands
from core.classes import Cog_Extension
import youtube_dl
from pprint import pprint

def get_video_info(youtube_url):
    video_info = {}

    with youtube_dl.YoutubeDL() as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        video_info['ID'] = info.get('id')
        video_info['標題'] = info.get('title')
        video_info['影片縮圖'] = info.get('thumbnail')
        video_info['上傳者'] = info.get('uploader')
        video_info['上傳者網址'] = info.get('uploader_url')
        video_info['影片長度(秒)'] = info.get('duration')
        video_info['觀看次數'] = info.get('view_count')
        video_info['留言數'] = info.get('comment_count')
        video_info['喜歡數'] = info.get('like_count')
        video_info['不喜歡數'] = info.get('dislike_count')
        video_info['平均評分'] = info.get('average_rating')
        video_info['描述'] = info.get('description')
        video_info['標籤'] = info.get('tags')
        video_info['網頁網址'] = info.get('webpage_url')
        video_info['上傳日期'] = info.get('upload_date')
    return video_info       

class System(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        
        if msg.content == "id" and msg.author != self.bot.user:        

            video_info = get_video_info('https://youtu.be/aHNWL7MBXoc')
            await msg.channel.send(video_info['ID'])

def setup(bot):
    bot.add_cog(System(bot))
