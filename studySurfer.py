from classes.audio_analysis import getAudio, analyzeAudio
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, concatenate

def main():
    getAudio()
    subtitles = analyzeAudio()

    gameplay = VideoFileClip('resources/ssgameplay.mp4')
    TTSAudio = AudioFileClip('resources/audio.wav')

    audioDuration = TTSAudio.duration
    gpDuration = gameplay.duration # gameplayDuration = 267.8 for subway surfer
    clipDuration = gpDuration

    ClipList = []
    if audioDuration > gpDuration:
        while audioDuration>gpDuration: #Adds another clip if audio duration is longer than gameplay duration
            if (audioDuration > gpDuration + clipDuration):
                clip = gameplay
                ClipList.append(clip)
                gpDuration += clipDuration
            else: #If adding another full clips is too long, add a subclip of the remaining time left
                clip = gameplay.subclip(0,audioDuration-gpDuration)
                ClipList.append(clip)
                gpDuration += (audioDuration-gpDuration)
        final_clip = concatenate(ClipList)
    else: 
        final_clip = gameplay.subclip(0,TTSAudio.duration)
    final_clip.audio = TTSAudio #Adds audio to video


    subs = [final_clip]
    for i in range(0,len(subtitles)):
        txt_clip = TextClip(str(subtitles[i][2]), font='Arial-Bold', color = 'white', stroke_color = 'black', stroke_width=1.5, method='caption',fontsize=40,size=[1280,900]).set_start(float(subtitles[i][0])).set_duration(float(subtitles[i][1])-float(subtitles[i][0]))
        subs.append(txt_clip)

    final_clip = CompositeVideoClip(subs)
    final_clip.write_videofile("final.mp4")

if __name__ == "__main__":
    main()
