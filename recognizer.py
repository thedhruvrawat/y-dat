# Recognizes the speech
import time
import scipy.io.wavfile as wavfile
import numpy as np
import speech_recognition as sr
import librosa
import argparse
import os
from glob import glob

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-video', type=str,
                        help='path to audiofile')
    arguments = parser.parse_args()
    return arguments

def recognize(wav_filename):
    """
    Recognize the audio in the wav file
    @param: wav_filename  The name of the .wav file to be recognized
    """
    data, s = librosa.load(wav_filename)
    librosa.output.write_wav('audio.wav', data, s)
    y = (np.iinfo(np.int32).max * (data/np.abs(data).max())).astype(np.int32)
    wavfile.write('tmp_32.wav', s, y)

    r = sr.Recognizer()
    with sr.AudioFile('tmp_32.wav') as source:
        audio = r.record(source)  
    print('Audio file has been loaded')

    try:
        result = r.recognize_google(audio, language = 'en').lower()
    except sr.UnknownValueError:
        print("Audio cannot be recognized")
        result = ''
        os.remove(wav_filename)  
    with open('transcript.txt', 'a', encoding='utf-8') as f:
        f.write(' {}'.format(result))

def get_audio(video):
    """
    Get the audio from the video
    @param: video   Name of the video file
    """
    os.system('ffmpeg -y  -threads 4\
 -i {} -f wav -ab 192000 -vn {}'.format(video, 'audio.wav'))

def split_into_frames(audiofile):
    """
    Split the audio file in smaller frames
    @param: audiofile    The name of the audio file to be split
    """
    data, sr = librosa.load(audiofile)
    duration = librosa.get_duration(data, sr)
    print('Video Duration, minutes: {}'.format(duration/60))
    for i in range(0,int(duration-1),50):
        tmp_batch = data[(i)*sr:sr*(i+50)]
        librosa.output.write_wav('samples/{}.wav'.format(chr(int(i/50)+65)), tmp_batch, sr)

if __name__ == '__main__':
    start = time.time()
    os.system('mkdir samples')
    args = get_arguments()
    get_audio(args.video)
    split_into_frames('audio.wav')
    files = sorted(glob('samples/*.wav'))
    print(files)
    open('transcript.txt', 'w', encoding = 'utf-8').write('')
    for file in files:
        print(file)   
    recognize('audio.wav')
    end = time.time()
    print('Finished recognition, check transcript.txt')
    print('Total time taken: {} sec'.format(end - start))
    os.system('rm -rf samples && rm tmp_32.wav')