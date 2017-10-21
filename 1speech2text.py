import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path
import os
_file_test='out.wav'

AUDIO_FILE = path.join(path.dirname(path.realpath(os.curdir)), _file_test)
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said \n" + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))


#!/usr/bin/env python
from os import environ, path

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
import os
MODELDIR = path.realpath("C:/Python27/Lib/site-packages/pocketsphinx/model")
DATADIR = path.dirname(path.realpath(os.curdir))#path.realpath("C:/Python27/Lib/site-packages/pocketsphinx/datacls")#"pocketsphinx/test/data"
#path.join(path.dirname(path.realpath(os.curdir)))#


# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', path.realpath(path.join(MODELDIR, 'en-us')))
config.set_string('-lm', path.realpath(path.join(MODELDIR, 'en-us.lm.bin')))
config.set_string('-dict', path.realpath(path.join(MODELDIR, 'cmudict-en-us.dict')))
decoder = Decoder(config)

# Decode streaming data.
decoder = Decoder(config)
decoder.start_utt()
stream = open(path.join(DATADIR, _file_test), 'rb')
#'M1F1-Alaw-AFsp.wav'

while True:
  buf = stream.read(1024)
  if buf:
    decoder.process_raw(buf, False, False)
  else:
    break
decoder.end_utt()
print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])