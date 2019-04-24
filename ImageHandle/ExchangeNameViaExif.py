# -*- coding: UTF-8 -*-

import os
import exifread

def getExif(filename):
    FIELD = 'EXIF DateTimeOriginal'
    fd = open(filename, 'rb')
    tags = exifread.process_file(fd)
    fd.close()
    print('=== ', filename)
    if FIELD in tags:
        new_name = str(tags[FIELD]).replace(':', '').replace(' ', '_') + os.path.splitext(filename)[1]
        tot = 1
        while os.path.exists(new_name):
            new_name = str(tags[FIELD]).replace(':', '').replace(' ', '_') + '_' + str(tot) + os.path.splitext(filename)[1]
            tot += 1
        print(new_name)
        os.rename(filename, new_name)
    else:
        print('No {} found'.format(FIELD))

'''
for filename in os.listdir('.'):
    if os.path.isfile(filename):
        getExif(filename)
'''

file_location = '/Users/Allen/downloads/IMG_0932.JPG'
getExif(file_location)