# Admin Finder CMS Lokomedia

import requests

logo = """
  __       _           _         _____ _           _           
 / _ \    | |         (_)       |  ___(_)         | |          
/ /_\ \ __| |_ __ ___  _ _ __   | |_   _ _ __   __| | ___ _ __ 
|  _  |/ _` | '_ ` _ \| | '_ \  |  _| | | '_ \ / _` |/ _ \ '__|
| | | | (_| | | | | | | | | | | | |   | | | | | (_| |  __/ |   
\_| |_/\__,_|_| |_| |_|_|_| |_| \_|   |_|_| |_|\__,_|\___|_|   
"""
print logo

# input target nya
target = raw_input("Target : ")
# wordlist
wordlist = open("wordlist.txt", "r")
site = wordlist.read()
ay = site.split('\n')

#
for i in ay:
    url = target + "/"+ i
    code = requests.get(str(url)).status_code   
    if code == 200:
        print ("FOUND : ") + url 
        result = open("result.txt", "a")
        result.write(url + "\n")
        result.close()
    else:
        print ("NOT FOUND : ") + url
