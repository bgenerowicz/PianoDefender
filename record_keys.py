import pyaudio
import numpy as np
import plot_data
import matplotlib.pyplot as plt
import find_note
from scipy import signal, stats

key = 'whatever'



CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 2
treshhold = 1e3



p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

frames = []
print("Recording, play " + key)

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):  # Record Data in frames as byte list
    data = stream.read(CHUNK)
    frames.append(data)

stream.stop_stream()  # Close
stream.close()
p.terminate()

print("Done!")
decoded = np.fromstring(np.asarray(frames), np.int16);

Data = 1 / len(decoded) * np.absolute(np.fft.fft(decoded)) ** 2  # PSD of data
Data = Data[0:4000:2]  # Truncate to important frequencies
Data_norm = Data / np.amax(Data)





kurt = stats.kurtosis(Data_norm)
if kurt > 500:
    played_note = find_note.find_note(Data_norm)
    print('played note: ' + played_note)
else:
    print('no note')


fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(Data_norm) # Make Plot


# np.save('keys/'+key,Data_norm)
# t1 = np.load('keys/C4.npy')
# t2 = np.load('keys/C4v2.npy')
# t3 = np.load('keys/C4v3.npy')
# t4 = np.load('keys/C4v4.npy')

# plt.plot(t1)
# plt.plot(t2)
# plt.plot(t3)
# plt.plot(t4)

# t4 = np.absolute(t1-t2)
end = 1