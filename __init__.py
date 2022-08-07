from pytube import YouTube 
from requests import get 
from tempfile import NamedTemporaryFile as File 
import moviepy.editor as mpy


youtube = YouTube("https://www.youtube.com/watch?v=B6C15KXFdls")
url = youtube.streams.get_lowest_resolution().url
file = File(delete=False)
file.write(get(url).content)
clip = mpy.VideoFileClip(file.name)
clip.preview()
