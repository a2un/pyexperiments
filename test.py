from pocketsphinx import AudioFile

audio = AudioFile(lm=False, keyphrase='forward', kws_threshold=1e+20)
for phrase in audio:
    print(phrase.segments(detailed=True)) # => "[('forward', -617, 63, 121)]"