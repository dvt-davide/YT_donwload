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

