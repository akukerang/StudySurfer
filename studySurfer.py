from classes.audio_analysis import getAudio, analyzeAudio, genSRT
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, concatenate
from moviepy.video.tools.subtitles import SubtitlesClip
def main():
    genSRT(analyzeAudio())
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
    
    #Add subtitles
    generator = lambda txt: TextClip(txt, font='Arial-Bold', color = 'white', stroke_color = 'black', stroke_width=1.5, method='caption',fontsize=40,size=[1280,900])
    subtitles = SubtitlesClip("resources/subtitles.srt", generator)
    final_clip = CompositeVideoClip([final_clip, subtitles])
    final_clip.write_videofile("final.mp4")

if __name__ == "__main__":
    main()
