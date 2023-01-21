from pytube import Channel, YouTube
from mega import Mega
import os
from os import listdir

mega = Mega()
m = mega.login('EMAIL_HERE', 'PASSWORD_HERE') # Enter email and password
path = "PATH_HERE" # Path to where videos will be downloaded
folder_name = "MEGA_FOLDER_NAME_HERE" # Mega folder name
c = Channel('https://www.youtube.com/@rA9k') # Channel link


download_type = input("Backup whole channel or a single video? (channel, video): ").lower()

if download_type == "channel":

    # Download all videos of a channel
    print(f'Downloading videos by: {c.channel_name}')

    for video in c.videos:
        video.streams.get_highest_resolution().download(path)
    print("Download Complete!")

    # Get the files
    dir_list = os.listdir(path)
    size = len(dir_list)
    print("\n", "Number of Files: ", size)
    # print(dir_list)

    # Mega Upload
    print("\n", "Starting Upload...")
    count = 0

    while count < size:
        filename = f"{path}/{dir_list[count]}"
        Folder = mega.find(f'{folder_name}')
        m.upload(filename, Folder[0])
        print((count/size) *100 + "%", "\n")
        count += 1

    print("\n", "Upload Complete!")


elif download_type == "video":
    video_link = input("Enter video url: ")
    yt = YouTube(video_link)
    yt.streams.get_highest_resolution().download(path)
    print("\n","Download Complete!")

    filename = f"{path}/{yt.title}.mp4"
    Folder = mega.find(f'{folder_name}')
    m.upload(filename, Folder[0])
    print("\n", "Upload Complete!")

else:
    print("Invalid action")
