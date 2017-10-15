import os
from pocketsphinx import DefaultConfig, Decoder, get_model_path, get_data_path

model_path = get_model_path()
data_path = get_data_path()

# Create a decoder with a certain model
config = DefaultConfig()
config.set_string('-hmm', os.path.join(model_path, 'en-us'))
config.set_string('-lm', os.path.join(model_path, 'en-us.lm.bin'))
config.set_string('-dict', os.path.join(model_path, 'cmudict-en-us.dict'))
decoder = Decoder(config)

# Decode streaming data
buf = bytearray(1024)
with open(os.path.join(data_path, 'goforward.raw'), 'rb') as f:
    decoder.start_utt()
    while f.readinto(buf):
        decoder.process_raw(buf, False, False)
    decoder.end_utt()
print('Best hypothesis segments:', [seg.word for seg in decoder.seg()])