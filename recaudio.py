import pyaudio
import wave
import _portaudio
 

def rec(name):
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = name
    # new pyaudio object    
    audio = pyaudio.PyAudio() 
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("recording...")
    frames = [] 
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    # stop Recording
    stream.stop_stream()
    #close stream
    stream.close()
    audio.terminate()
    #open file if exist or create new one    
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    # set chanels
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    # join existing frames
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

