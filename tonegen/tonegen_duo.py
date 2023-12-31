import math
import binascii
import itertools
import random

# Generated wav files will be saved there
tones_path = "../tones/"

# File generated by ANU Quantum randomiser. File contains 2000 characters, "1" or "0"
# Source: https://qrng.anu.edu.au/contact/faq/#downloads
qrnd_data_path = "data/anu_qrng_set.txt"

# Blocks for building wav files, hex
# Wav files characteristics: 8kHz, 16bit, Square wave, 1000Hz base tone
wav_meta = binascii.unhexlify("52494646a4bb000057415645666d74201000000001000100401f0000803e0000020010006461746180bb0000")
tone_sqr = binascii.unhexlify("000078840000897b")
tone_nul = binascii.unhexlify("0000000000000000")

# Set to True if you want noise over 500Hz tone
tone500 = False

random.seed(0)


# Generating 9 wav files with different level of noise
for y in range(1, 10):
    file_path = tones_path + str(y) + "d.wav"
    noise_count = 0
    with open(qrnd_data_path) as qrnd_set, open(file_path, "wb") as wav_file:
        wav_file.write(wav_meta)
        for c in itertools.chain.from_iterable(qrnd_set):
            if tone500:
                wav_file.write(tone_sqr)
            if c == "1":
                wav_file.write(tone_sqr)
                noise_count += 1
            else:
                wav_file.write(tone_nul)
        for x in range(2000):
            if tone500:
                wav_file.write(tone_sqr)
            calc_random = random.random() * 10 # Deterministically randomised noise
            if y > calc_random:
                wav_file.write(tone_sqr)
                noise_count += 1
            else:
                wav_file.write(tone_nul)
    print(y, noise_count)
    wav_file.close
    qrnd_set.close
