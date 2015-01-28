from glob import iglob
import shutil
import os

PATH = r'mp3'
destination = open('luoji.mp3', 'wb')
for filename in iglob(os.path.join(PATH, '*.mp3')):
    shutil.copyfileobj(open(filename, 'rb'), destination)
destination.close()