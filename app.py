import youtube_dl
import easyocr

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

with ydl:
    result = ydl.extract_info(
           'http://www.youtube.com/watch?v=pJQQpuSc6Qw'
    )

if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result['entries'][0]
else:
    # Just a video
    video = result

print(video)
video_url = video['webpage_url']
print(video_url)

import cv2
vidcap = cv2.VideoCapture('test.mkv')
success,image = vidcap.read()
count = 0
text = []
reader = easyocr.Reader(['en'])
while success:
    if count % 100 == 0:
        
        cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
        print('performing ocr') 
        result = reader.readtext(f'frame{count}.jpg')
        for r in result:
            if r[2] > 0.01:
                print(r[1])
        text.append(result)
    success,image = vidcap.read()
    count += 1

