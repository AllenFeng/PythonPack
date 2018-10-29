#!/usr/bin/python

import random

cnt = 0        # control code length
rand = 0       # generate code
pincode =''    # last code
codelist = ('0','1','2','3','4','5','6','7','8','9')

for cnt in range(0,6):
	pincode=pincode+codelist[int(random.uniform(0,9))]
	cnt+=1
	
print 'pin is : %s' % pincode