import pytube

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

youtube_object = pytube.YouTube(video_url)

youtube_object.streams.get_highest_resolution().download()
