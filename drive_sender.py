import json, requests, os, sys
from apiclient import discovery
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
def load(directory =fr'{os.getcwd()}\Output', lista_canzoni = []):
    print("sending files to cloud...(autorization needed!)")
    #autenticazione google
    g_login = GoogleAuth()
    g_login.LocalWebserverAuth()
    drive = GoogleDrive(g_login)
    print("waiting for auth, press any key to continue...")
    wait = input()
    for canzone in lista_canzoni:
        print(f'Uploading song: {canzone}') 
        file_drive = drive.CreateFile({  'parents': [{'id' : r'<google drive folder ID>'}],'title': fr"{canzone}"})  
        file_drive.SetContentFile(directory + "\\" + canzone) 
        file_drive.Upload()

