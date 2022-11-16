# StudySurfer (WIP)

How to use:
1. Install requirements
    - ` pip install -r requirements.txt `
    - Install ImageMagick for caption functionality
        - For window users: Go to moviepy directory and edit config_defaults.py
        - In `IMAGEMAGICK_BINARY = `. Enter the directory for magick.exe. 
2. Enter the text material into resources/script.txt
    - For best use case, use a paragraph with no quotation marks.
3. Run StudySurfer.py
4. Output video is returned as final.mp4

To do:
- Learn regex, so can split the paragraph into sentences and sentences within quotation marks
- Once that is done, edit the timing values.
