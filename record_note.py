import threading
import time
import pyaudio
import wave
import numpy as np
import detect_note
import plot_data
import find_note
from scipy import signal, stats

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 2
treshhold = 1e3

class Threading(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
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
                data = stream.read(CHUNK)
                frames.append(data)
            stream.stop_stream()  # Close
            stream.close()
            p.terminate()
            decoded = np.fromstring(np.asarray(frames), np.int16);  # Convert to int array

            # data = wave.open('output.wav')
            # data = data.readframes(data.getnframes())
            # decoded = np.fromstring(data, np.int16);

            Data = 1 / len(decoded) * np.absolute(np.fft.fft(decoded)) ** 2  # PSD of data
            Data = Data[0:4000:2]  # Truncate to important frequencies
            Data_norm = Data / np.amax(Data)  # Truncate to important frequencies

            # plot_data.plot_data(Data)  # Make plot


            kurt = stats.kurtosis(Data_norm)
            if kurt > 700:
                played_note = find_note.find_note(Data_norm)
                print('played note: ' + played_note)
                self.note = played_note
            else:
                self.note = 'none'
            # if np.amax(Data) > treshhold:  # If amplitude above a certain threshhold -> detect the note
            #     played_note = find_note.find_note(Data_norm)
            #     print('played note: ' + played_note)

            # print('Note frequency is: ' + str(fnote) + '\t Which is a ' + nnote)


            # time.sleep(self.interval)



example = Threading()

# import threading
# import time
# import pyaudio
# import wave
# import numpy as np
# import detect_note
# import plot_data
# import record_segment
# from scipy import signal
#
# CHUNK = 1024
# FORMAT = pyaudio.paInt16
# CHANNELS = 2
# RATE = 44100
# RECORD_SECONDS = 1
# WAVE_OUTPUT_FILENAME = "output.wav"
# treshhold = 1e5
#
# class record_note(object):
#     """ Threading example class
#     The run() method will be started and it will run in the background
#     until the application exits.
#     """
#
#     def __init__(self, interval=1):
#         """ Constructor
#         :type interval: int
#         :param interval: Check interval, in seconds
#         """
#         self.interval = interval
#
#         thread = threading.Thread(target=self.run, args=())
#         thread.daemon = True                            # Daemonize thread
#         thread.start()                                  # Start the execution
#
#     def run(self):
#         """ Method that runs forever """
#         while True:
#             p = pyaudio.PyAudio()
#             stream = p.open(format=FORMAT,
#                             channels=CHANNELS,
#                             rate=RATE,
#                             input=True,
#                             frames_per_buffer=CHUNK)
#             frames = []
#             # print("recording")
#
#             for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):  # Record Data in frames as byte list
#                 data = stream.read(CHUNK)
#                 frames.append(data)
#             decoded = np.fromstring(np.asarray(frames), np.int16);  # Convert to int array
#
#             # data = wave.open('output.wav')
#             # data = data.readframes(data.getnframes())
#             # decoded = np.fromstring(data, np.int16);
#
#             Data = 1 / len(decoded) * np.absolute(np.fft.fft(decoded)) ** 2  # PSD of data
#             Data = Data[0:600]  # Truncate to important frequencies
#
#             # plot_data.plot_data(Data)  # Make plot
#
#             fnote = 0
#             if np.amax(Data) > treshhold:  # If amplitude above a certain threshhold -> detect the note
#                 fnote, nnote = detect_note.detect_note(Data)
#
#             print('Note frequency is: ' + str(fnote) + '\t Which is a ' + nnote)
#
#
#             stream.stop_stream()  # Close
#             stream.close()
#             p.terminate()
#             time.sleep(self.interval)
#
#
