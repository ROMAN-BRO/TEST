import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')

        os.system('xdg-open https://github.com/ROMAN-BRO')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from a import Main
 
        Main()
 
 
 
elif bit == "32bit":
 
        from a import Main
 
 
        Main()
