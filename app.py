from pytube import Playlist

# Replace with the actual playlist URL
playlist_url = "https://youtube.com/playlist?list=PLeHoly7hGE4XztXJh5hA9P_zneVclUxqR&si=rkuJabAuOdlniu8k"

# Create a Playlist object
playlist = Playlist(playlist_url)

# Access the video URLs
video_urls = playlist.video_urls

# Print the URLs (or process them as needed)
for url in video_urls:
    print(url)
