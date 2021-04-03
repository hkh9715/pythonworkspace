# reference : https://python-explorer.tistory.com/11
# pip install pytube3

from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)


# download english and korean captions
print(yt.captions)
caption1 = yt.captions.get_by_language_code('en')
caption2 = yt.captions.get_by_language_code('ko')

# xml format
# print(caption.xml_captions)
# srt format
# print(caption.generate_srt_captions())

caption1.download(yt.title, output_path = 'smallproject3_youtubecaptionfiltering')
caption2.download(yt.title, output_path = 'smallproject3_youtubecaptionfiltering')
