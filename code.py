import wave
import numpy as np
import matplotlib.pyplot as plt



wav_o = wave.open('sample-file-4.wav', 'r')
signal = wav_o.readframes(-1)
data = np.frombuffer(signal, dtype='int16')
metadata = wav_o.getparams()
sample_freq = metadata.framerate
n_samples = metadata.nframes
time = np.linspace(0, n_samples / sample_freq, num=n_samples)

print(metadata)
print('______________________________')

noise = np.random.normal(scale=120, size=len(data)) 
print(noise) 



noisy_data = data + noise

#(SNR)
snr = 20 * np.log10(np.sqrt(np.mean(data ** 2)) / np.sqrt(np.mean(noise ** 2)))

print("SNR: {:.2f} dB".format(snr))

# Save the noisy audio to a new WAV file
with wave.open('noisy_sample.wav', 'w') as wav_n:
    wav_n.setparams(metadata)
    wav_n.writeframes(noisy_data.tobytes())
    
with wave.open('just_noise.wav', 'w') as wav_n:
    wav_n.setparams(metadata)
    wav_n.writeframes(noise.tobytes())

channel1 = data[::2]


plt.plot(time, channel1, label='Original Audio')
plt.plot(time, noise[::2], c='green', label='Noise')  
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Original Audio vs  just noise')
plt.legend()
plt.show()
