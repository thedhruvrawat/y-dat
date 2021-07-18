# Y-DAT: Youtube Video Download and Transcription

Allows the user to download Youtube video using it's URL (using `youtube_dl` library) and then generate it's transcript using `SpeechRecognizer` library

### Installation
Make sure you have `Python 3.5 or higher` installed along with `pip`.

#### Cloning the repository
```bash
git clone https://github.com/thedhruvrawat/y-dat.git
```

#### Installing the requirements
To install the requirements, run 
```bash
pip install -r requirements.txt
```

### Downloading the video
To download the video from a link, run
```bash
python downloader.py -url <YOUTUBE_VIDEO_URL>
```

### Generating the transcript
To recognize the speech in video, run
```bash
python3 recognizer.py -video <VIDEO_NAME>
```
By default, the video will be saved by the name `video.mkv`

The generated text will be saved in the file `transcript.txt`, along with this an `audio.wav` file containing solely the audio of the downloaded video will also be generated in the same folder. Works only for English language.

> Best results obtained when the audio is free from any kind of background sounds

### Further Reading
* [Youtube-dl](https://github.com/ytdl-org/youtube-dl)
* [SpeechRecognizer](https://github.com/Uberi/speech_recognition)
* [Librosa](https://github.com/librosa/librosa)
* [Russian-Subtitles-Generator](https://github.com/nestyme/Subtitles-generator)

### License
MIT