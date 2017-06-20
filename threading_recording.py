import threading
import time
import pyaudio
import wave
import numpy as np
import plot_data
import find_note
from scipy import signal, stats

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 2

class Threading(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        self.interval = interval
        self.note = 'none'

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            p = pyaudio.PyAudio()
            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)

            frames = []
            # print("recording")

            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):  # Record Data in frames as byte list
                data = stream.read(CHUNK,exception_on_overflow = False)
                frames.append(data)
            stream.stop_stream()  # Close
            stream.close()
            p.terminate()
            decoded = np.fromstring(np.asarray(frames), np.int16);  # Convert to int array

            Data = 1 / len(decoded) * np.absolute(np.fft.fft(decoded)) ** 2  # PSD of data
            Data = Data[0:4000:2]  # Truncate to important frequencies
            Data_norm = Data / np.amax(Data)  # Truncate to important frequencies

            # plot_data.plot_data(Data)  # Make plot


            kurt = stats.kurtosis(Data_norm)
            if kurt > 500:
                played_note = find_note.find_note(Data_norm)
                print('played note: ' + played_note)
                self.note = played_note
            else:
                self.note = 'none'
                print('played note: none')
            # time.sleep(1)



