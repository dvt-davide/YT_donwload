##MIT License

##Copyright (c) 2019 dvt-davide
##
##Permission is hereby granted, free of charge, to any person obtaining a copy
##of this software and associated documentation files (the "Software"), to deal
##in the Software without restriction, including without limitation the rights
##to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##copies of the Software, and to permit persons to whom the Software is
##furnished to do so, subject to the following conditions:
##
##The above copyright notice and this permission notice shall be included in all
##copies or substantial portions of the Software.
##
##THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
##SOFTWARE.
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
        
