from flask import make_response, render_template
from pytube import YouTube


def on_progress(stream, chunk, file_handle, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    return percentage_of_completion


def main(url, video_reso):
    try:
        chunk_size = 1024
        yt = YouTube(url)
        video = video_reso
        yt.register_on_progress_callback(on_progress(video, chunk_size, 'YouTubeVidDownload', video.filesize))
        var0 = f"Fetching \"{video.title}\".."
        var = f"Fetching successful\n"
        var2 = (f"Information: \n"
                f"File size: {round(video.filesize * 0.000001, 2)} MegaBytes\n"
                f"Resolution: {video.resolution}\n"
                f"Author: {yt.author}")
        var3 = ("Views: {:,}\n".format(yt.views))
        var4 = f"Downloading \"{video.title}\".."
        video.download('YouTubeVidDownload')
        notify = 'Download success'
        this = make_response(render_template('download.html', var0=var0, var=var, var2=var2, var3=var3, var4=var4, notify=notify))
        return this
    except Exception as e:
        return 'Connect Your InterNet First'
