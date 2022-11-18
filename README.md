# StudySurfer
A study tool that takes advantage of low attention span, by playing eye catching videos in the background alongside with TTS and captions. (aka Minecraft Parkour Reddit Stories Family Guy Mobile Game Tiktok type videos) <br/>
[Demo Video](https://www.youtube.com/watch?v=J91lMOY1X_I)

## Requirements
- `Python >= 3.10.7`
- `ImageMagick >= 7.1.0-Q16-HDRI`
- `pip install -r requirements.txt` 

## Installation
- Run `pip install -r requirements.txt` to get the required packages to run. <br/>
- Install [ImageMagick](https://imagemagick.org/script/download.php) for caption functionality. 
    - If you are a Windows user, go into `moviepy/config_default.py` and enter the path for the ImageMagick's `magick.exe`. 
        - Like this `IMAGEMAGICK_BINARY = 'C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe'`
- Download the [gameplay videos](https://drive.google.com/file/d/1EyOVpJkyMXLRGekArK1sFkJfiBKIcrTd/view)
    - Extract the videos into `StudySurfer/resources/gameplay/`.

## Instructions
1. Enter the desired text to be spoken into `resources/script.txt`.
    - For best use cases, use paragraphs with simple english where the only puntutations are periods.
    - The captions can get out of time, due to certain punctuations like (). I need to fix this, but for now if there are issues just edit the paragraph and remove any of these possible punctuations. 
2. Open a command prompt and go to the StudySurfer folder, and run this command <br/>
`python studySurfer.py -m {TYPE}`
    - These are the possible types of videos:
        - `csgo` - CS:GO Surf
        - `mc` - Minecraft Parkour
        - `subway` - Subway Surfer
4. Let the program run, and the video should be outputted as `final.mp4`

## Gameplay Credits:
- [CSGO](https://youtu.be/_2O8X4CveYc)
- [Minecraft](https://youtu.be/Pt5_GSKIWQM)
- [Subway Surfer](https://youtu.be/j_euAlsHIMQ)
<br/>

![Pomu](https://media.tenor.com/OZK4zgP-TdcAAAAd/pomu-pomu-rainpuff.gif)
