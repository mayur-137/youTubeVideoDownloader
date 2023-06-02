import pytube
from flask import Flask, render_template, request, session, jsonify
from pytube.cli import on_progress
from werkzeug.exceptions import abort
import test

app = Flask(__name__)
app.config['SECRET_KEY'] = "high"

global video_reso

@app.route('/')
def Home():
    return render_template("home.html")


@app.route('/Videos', methods=['POST', 'GET'])
def Videos():
    if request.method == 'POST':
        session['link'] = request.form['link']
        yt = pytube.YouTube(session['link'], on_progress_callback=on_progress)
        img = yt.thumbnail_url
        title = yt.title
        return render_template('Videos.html', img=img, title=title)
    else:
        return abort(402)


@app.route('/Download-144p')
def Download_144():
    if 'link' in session:
        yt = pytube.YouTube(session['link'],on_progress_callback=on_progress)
        yts = yt.streams.get_lowest_resolution()
        this = test.main(session['link'], video_reso=yts)
        return this
    else:
        return '<h2> Enter Correct link </h2>'


@app.route('/Download-360p')
def Download_360():
    if 'link' in session:
        yt = pytube.YouTube(session['link'],on_progress_callback=on_progress)
        yts = yt.streams.get_by_resolution('360p')
        this = test.main(session['link'], video_reso=yts)
        return this
    else:
        return '<h2> Enter Correct link </h2>'


@app.route('/Download-1080p')
def Download_1080():
    if 'link' in session:
        yt = pytube.YouTube(session['link'],on_progress_callback=on_progress)
        yts = yt.streams.get_highest_resolution()
        this = test.main(session['link'], video_reso=yts)
        return this
    else:
        return '<h2> Enter Correct link </h2>'


@app.route('/Download-audio')
def Download_audio():
    if 'link' in session:
        yt = pytube.YouTube(session['link'],on_progress_callback=on_progress)
        yts = yt.streams.get_audio_only()
        this = test.main(session['link'], video_reso=yts)
        return this
    else:
        return '<h2> Enter Correct link </h2>'

# @app.route('/progress')
# def progress():
#     # Your code to retrieve the progress percentage
#     # percentage = test.on_progress(stream=video_reso, chunk=1024, bytes_remaining=video_reso.filesize) 
#     #  # Replace with your logic to get the actual progress percentage
#     test.p
#     return jsonify({'progress': percentage})


if __name__ == '__main__':
    app.run(debug=True)
