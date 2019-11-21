## Scaricatore musica da you tube e caricatore su google drive
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
