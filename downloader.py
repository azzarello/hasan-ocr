import youtube_dl
import os
ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s', 'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]'})

video = 'https://www.twitch.tv/videos/891581744'

with ydl:
    result = ydl.extract_info(
           video
    )
