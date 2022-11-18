import re
def splitParagraph(paragraph :str):
    sentences = re.split(r' *[\.\?!()][\'\)\]]* *', paragraph)
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
    millisecond = seconds % 1 * 1000
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f'{"%02d" %hour}:{"%02d" %minutes}:{"%02d" %seconds},{"%03d" %millisecond}'