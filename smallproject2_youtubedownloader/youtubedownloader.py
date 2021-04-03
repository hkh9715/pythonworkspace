# pip install pytube3

from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)

#1 information
# print("Title: ", yt.title)
# print("Number of views: ", yt.views)
# print("Length of video: ", yt.length, "seconds")
# # print("Description: ", yt.description)
# print("Ratings: ", yt.rating)
# --------------------------------------------------------
# print(yt.streams)


#2 download video
# ys = yt.streams.get_highest_resolution()
# print("Downloading...")
# ys.download("")
# print("Download completed!")

#3 download only audio
# print(yt.streams.filter(only_audio=True))
# ys = yt.streams.get_by_itag("251")
# print("Downloading...")
# ys.download("audio")
# print("Download completed!")

#4 download korean captions
print(yt.captions)
caption = yt.captions.get_by_language_code('ko')
# xml format
# print(caption.xml_captions)
# srt format
# print(caption.generate_srt_captions())

caption.download(yt.title)
