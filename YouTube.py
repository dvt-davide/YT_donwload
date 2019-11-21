import os, subprocess
def Update():
    print('youtube-dl: check for updates...')
    subprocess.run(['youtube-dl', '-U'])
    
def YTdownload(urls, path):
    YT = []
    print(fr'Download from URL:{urls}')
    if isinstance(urls, str):
        YT.append(urls)
    for url in YT:
        os.system(fr"youtube-dl -f bestaudio {url}  -o {path}\%(title)s.%(ext)s  --ffmpeg-location \ffmpeg\bin")

def converter(path, out):
    print('Converting file...')
    lista_scaricati = os.listdir(path)
    for file in lista_scaricati:
        print(file)
        subprocess.run(fr'{os.getcwd()}\ffmpeg\bin\ffmpeg.exe -i "{path}\{file}" -vn -ar 44100 -ac 2 -ab 192k -f mp3 "{out}\{file.replace(".webm", ".mp3")}"')
    return [file.replace(".webm", ".mp3") for file in lista_scaricati]
        
