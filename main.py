#youtube video downloader
from pytube import YouTube

link = input("Enter your link here :")
youtube_1 = YouTube(link)

# print(youtube_1.thumbnail_url)

video = youtube_1.streams.all()
vid = list(enumerate(video))
for i in vid:
    print(i)
inp = int(input("Enter the video type you want :"))
video[inp].download()
print(youtube_1.title, "\n DOWNLOAD COMPLETED")
print("DOWNLOAD COMPLETED")
