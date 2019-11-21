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
from YouTube import *
from drive_sender import *
from blue_send import *
import json, os, ctypes
res = ctypes.windll.user32.MessageBoxW(0, 'Download from default URL?', 'Mode', 4)
customizing = json.load(open('customizing.json', 'r'))
def main(url):
    #pulizia della cartella dei downloads
    print('Clearing temp folder...')
    garbage = os.listdir(fr"{os.getcwd()}\{customizing['WORK']}")
    for junk in garbage:
        os.remove(fr"{os.getcwd()}\{customizing['WORK']}\{junk}")
        
    YTdownload(url, fr"{os.getcwd()}\{customizing['WORK']}")
    songs = converter(fr"{os.getcwd()}\{customizing['WORK']}", fr"{os.getcwd()}\{customizing['OUTPUT']}")
    print(songs)
    res2 = ctypes.windll.user32.MessageBoxW(0, 'Inviare su cloud?', 'Cloud', 4)
    if res2 == 6:
        load(fr"{os.getcwd()}\{customizing['OUTPUT']}", songs)
    res3 = ctypes.windll.user32.MessageBoxW(0, 'Send music via Bluetooth?', 'Bluetooth', 4)
    if res3 == 6:
        song_path = [fr'Output\{song_name}' for song_name in songs]
        blue_send('<your devices mac address here>', song_path)


Update()        
if res == 6:
    print('Download from default URL')
    main(customizing['URL'])
    exit()
print('Download Manuale')
while True:
    os.system('cls')
    print('Insert URL:')
    in_ = input()
    main(in_)
