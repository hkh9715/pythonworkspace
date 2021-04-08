# ---------------------reference---------------------
# https://stackoverflow.com/questions/2081836/how-to-read-specific-lines-from-a-file-by-line-number
# https://opentutorials.org/module/2980/17644
# https://python-explorer.tistory.com/11
# https://pythonq.com/so/python/1991078  for filename
# https://eehoeskrap.tistory.com/496  for filename
# pip install pytube3

from pytube import YouTube
import sys
import os

link = input("Enter the link: ")
yt = YouTube(link)


# download english and korean captions
# print(yt.captions)
language = ['en', 'ko']
caption1 = yt.captions.get_by_language_code(language[1])
# caption2 = yt.captions.get_by_language_code('ko')

# xml format
# print(caption.xml_captions)
# srt format (default)
# print(caption.generate_srt_captions())

captionfile1 = caption1.download(yt.title, output_path = 'smallproject3_youtubecaptionfiltering')
# file2 = caption2.download(yt.title, output_path = 'smallproject3_youtubecaptionfiltering')
rawname1 = os.path.splitext(captionfile1)[0]
filename1 =  '{0}.txt'.format(rawname1)
sys.stdout=open(filename1, 'w', encoding='UTF8')
f = open(captionfile1, 'r', encoding='UTF8')

lines = f.readlines()
numbers = [4*n+2 for n in range(200)]
for n in numbers:
    print(lines[n])

f.close()