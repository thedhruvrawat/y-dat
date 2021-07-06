# Y-DAT: Youtube Video Download and Transcription

Allows the user to download Youtube video using it's URL (using `youtube_dl` library) and then generate it's transcript using `Google Speech API`

### Installing requirements
To install the requirements, run 
```bash
pip3 install -r requirements.txt
```

### Downloading the video
To download the video from a link, run
```bash
python3 downloader.py -url <YOUTUBE_VIDEO_URL>
```

### Generating the transcript
To recognize the speech in video, run
```bash
python3 recognizer.py -video <VIDEO_NAME>
```
By default, the video will be saved by the name `video.mkv`

The generated text will be saved in the file `transcript.txt`, along with this an `audio.wav` file containing solely the audio of the downloaded video will also be generated in the same folder.

> Best results obtained when the audio is free from any kind of background sounds
