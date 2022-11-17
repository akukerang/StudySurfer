import wave
import numpy as np
import pyttsx3
import re
def getAudio():
    script = open("./resources/script.txt", "r", encoding="utf8")
    data = script.read().replace("\"","").replace(', ','. ') #commas pausing is inconsitant, so replaced with period
    engine = pyttsx3.init() #Generates TTS audio from script.txt
    engine.save_to_file(data,"./resources/audio.wav")
    engine.runAndWait()
    script.close()
    

def analyzeAudio():
    getAudio()
    timing = []
    silence = []
    script = open("./resources/script.txt", "r", encoding="utf8")
    sentences = splitParagraph(script.read())
    script.close()
    raw = wave.open('./resources/audio.wav','r')
    frameData = raw.readframes(-1)
    frameData = np.frombuffer(frameData, dtype ="int16")
    length = len(frameData)
    fps = raw.getframerate()
    raw.close()
    i = 0
    tolerance = 200
    while frameData[i] >= -tolerance and frameData[i] <= tolerance: #Beginning pause
        i+=1
    silence.append([0,i])

    while i in range(i,length): #Period pauses
        if frameData[i] >= -tolerance and frameData[i] <= tolerance:
            start = i
            j = i
            while j in range (i, length):
                if frameData[j] >= -tolerance and frameData[j] <= tolerance:
                    j+=1
                    i+=1
                else:
                    if j - start >= 5000:
                        silence.append([start,j])
                    break
        i+=1
    sLength = len(silence)
    for i in range(0,sLength-1):
        timing.append([round(silence[i][1] /fps,3), round(silence[i+1][0],3) /fps, sentences[i]])
    timing.append([round(silence[sLength-1][0] /fps,3), round(length/fps,3), sentences[len(sentences)-1]]) #end of last silence, end of audio clip
    return timing #Returns sentences along with the timing [start, end, sentence] 


def splitParagraph(pargraph :str):
    pargraph = pargraph.replace('\n','').replace("\"",'').replace(', ','. ') #Gets rid of all empty lines
    sentences = re.split(r' *[\.\?!,"()][\'"\)\]]* *', pargraph)
    sentences = [x for x in sentences if x]
    return sentences

def genSRT(timing: list):
    f = open("resources/subtitles.srt", "w")
    for i in range(0,len(timing)):
        f.write(str(i+1) + '\n')
        f.write(f'{convertToTime(timing[i][0])} --> {convertToTime(timing[i][1])} \n')
        f.write(timing[i][2]+ '\n' + '\n')
    f.close()

def convertToTime(seconds: float): #Conversion from seconds to 00:00:00,000 for SRT file
    millisecond = round(seconds % 1 * 1000)
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f'{"%02d" %hour}:{"%02d" %minutes}:{"%02d" %seconds},{"%03d" %millisecond}'

