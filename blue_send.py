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
from bluetooth import *
from PyOBEX.client import Client
import os

def get_blue_host(device_name = ""): # get device mac address from name 
    devices = discover_devices(lookup_names = True)
    my_device = None
    for device in devices:
        if device[1] == device_name:
            my_device = device[0]
            break
    return my_device

def blue_send(device, files = []):
    service_matches = find_service(name=b'OBEX Object Push\x00', address = device )
    first_match = service_matches[0]
    port = first_match["port"]
    name = first_match["name"]
    host = first_match["host"]
    client = Client(host, port)
    client.connect()
    for file in files:
        file_content = open(file, 'rb').readlines()
        if type(file_content) == list:
            file_content = b''.join(file_content).strip()
        client.put('Output\\'+file, file_content)
    client.disconnect()

if __name__ == "__main__":
    files = os.listdir("test")
    files = ['test\\' + x for x in files]
    blue_send('insert your device mac address here', files = files)
    pass
