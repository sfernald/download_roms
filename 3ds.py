import requests
import os
import urllib.parse
from urllib.parse import urlparse
import urllib.request


# read for saved file list example
filepath = '3ds_games.txt'

with open(filepath) as fp:
    # first line is save path
    downloadPath = fp.readline().strip()
    print(downloadPath)

    downloadFile = fp.readline()
    cnt = 1
    while downloadFile:
        endOfFile = downloadFile.find('.rar') + 4
        print(endOfFile)
        dlFile = downloadFile[0:endOfFile].strip()
        print("Line {}: {}".format(cnt, dlFile.strip()))
        a = urlparse(dlFile)
        b = os.path.basename(a.path)
        name = urllib.parse.unquote(b)

        outputFile = '/media/uzer/E7DD-60A5/emulation/consoles/3ds/' + name
        print(outputFile)

        url = downloadPath + urllib.parse.quote(dlFile)
        print(url)
        try:
            urllib.request.urlretrieve(url, outputFile)
        except:
            print("Could not download file.")

        downloadFile = fp.readline()
        cnt += 1