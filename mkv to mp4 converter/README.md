# Convert MKV to MP4

**Problem :** MKV files are not supported by normal Browers so you can't play mkv files in Chrome using Html files.Supporse you want to watch movie screensharing chrome tab on meet.google.com with your friends or Girlfriend :3 (somehow you cant use discord :v)

**Solution :** Convert the mkv to mp4.

This is a simple python script that will use **ffmpeg** to convert MKV file to MP4 !


It will convert all the mkv files in the current directory to mp4 files and will delete the mkv files after concerting!
Converting files into mp4 one by one so **automated** it :3

Features :i

- convert mkv files to mp4
- Fast
- **Doesn't loose quality**
- automated
- **delete** converted files automaticly

Supported Operating System:

- **Dabian** based Linux (Specially Ubuntu)

Pre-requirments :

- ffmpeg (which comes default with **Ubuntu**)

  Installation : `sudo apt install ffmpeg`

Used Command :

- `ffmpeg -i input.mkv -codec copy output.mp4`

**Note :** `-codec copy` stream copies, or "re-muxes", the streams from the input to the output without re-encoding. Think of it like a **copy and paste**.
