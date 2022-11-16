import wave
import numpy as np
import pyttsx3

def getAudio():
    script = open("./resources/script.txt", "r", encoding="utf8")
    data = script.read() 
    engine = pyttsx3.init() #Generates TTS audio from script.txt
    engine.save_to_file(data,"./resources/audio.wav")
    engine.runAndWait()
    script.close()
    

def analyzeAudio():
    timing = []
    silence = []
    script = open("./resources/script.txt", "r", encoding="utf8")
    data = script.read().replace('? ', '. ').replace('! ', '. ').replace('\n','')
    script.close()
    raw = wave.open('./resources/audio.wav','r')
    frameData = raw.readframes(-1)
    frameData = np.frombuffer(frameData, dtype ="int16")
    length = len(frameData)
    fps = raw.getframerate()
    raw.close()
    sentences = data.split('.')
    i = 0
    while frameData[i] >= -50 and frameData[i] <= 50: #Beginning pause
        i+=1
    silence.append([0,i])

    while i in range(i,length): #Period pauses
        if frameData[i] >= -50 and frameData[i] <= 50:
            start = i
            j = i
            while j in range (i, length):
                if frameData[j] >= -50 and frameData[j] <= 50:
                    j+=1
                    i+=1
                else:
                    if j - start >= 15000: 
                        silence.append([start,j])
                    break
        i+=1
    sLength = len(silence)
    for i in range(0,sLength-1):
        timing.append([silence[i][1] / fps, silence[i+1][0] / fps, sentences[i]])
    timing.append([silence[sLength-1][1]/ fps, length / fps, sentences[sLength-1]]) #end of last silence, end of audio clip
    return timing #Returns sentences along with the timing [start, end, sentence] 

