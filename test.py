from flask import make_response, render_template
from pytube import YouTube


def on_progress(stream, chunk, file_handle, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    return percentage_of_completion

def progress_callback(stream, chunk, bytes_remaining):
    total_bytes = stream.filesize
    downloaded_bytes = total_bytes - bytes_remaining
    percentage = int((downloaded_bytes / total_bytes) * 100)
    return percentage

global p


def main(url, video_reso):
    try:
        chunk_size = 1024
        yt = YouTube(url)
        video = video_reso
        var0 = f"Fetching \"{video.title}\".."
        var = f"Fetching successful\n"
        var2 = (f"Information: \n"
                f"File size: {round(video.filesize * 0.000001, 2)} MegaBytes\n"
                f"Resolution: {video.resolution}\n"
                f"Author: {yt.author}")
        var3 = ("Views: {:,}\n".format(yt.views))
        var4 = f"Downloading \"{video.title} \".."
        video.download('YouTubeVidDownload')
        notify = 'Download success'
        p = progress_callback(stream=video, chunk=1024, bytes_remaining=video.filesize)
        print("p--------------", p)
        this = make_response(render_template('download.html', var0=var0, var=var, var2=var2, var3=var3, var4=var4, notify=notify))
        return this
    except Exception as e:
        return 'Connect Your InterNet First'
