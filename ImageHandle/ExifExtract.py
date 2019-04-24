# -*- coding: UTF-8 -*-

import exifread

f = open('/Users/Allen/downloads/IMG_0932.JPG' ,'rb')

tags = exifread.process_file(f)

f.close()

for tag in tags.keys():
    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
        print "Key: %s, value %s" % (tag, tags[tag])


