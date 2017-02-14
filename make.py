from __future__ import absolute_import #compatibility layer for Python 2.7
import mmap #binary editor
import urllib.request #download library
from pathlib import Path
import time

#checks for file
print('Checking for firmware...')
firmware = Path("factory-to-ddwrt.bin")
time.sleep(0.2)

#download new file if not found
if firmware.is_file():
	print("File exists.")
else:
	print("Firmware not found, downloading it from DD-WRT servers...")
	urllib.request.urlretrieve("http://download1.dd-wrt.com/dd-wrtv2/downloads/betas/2017/02-07-2017-r31277/tplink_tl-wr841ndv8/factory-to-ddwrt.bin", "factory-to-ddwrt.bin")
	print("Success: download.")
#open firmware bin file to edit
f = open('factory-to-ddwrt.bin', 'a+')
m = mmap.mmap(f.fileno(), 0)

time.sleep(0.3)
#replace the addresses from 0x40 to 0x43; the original file contains the hex "08410008" (wr841 v8) placed here, this piece of code replaces it to 09410005 (wr941 v5)
m[0x40:0x44] = b'\x09\x41\x00\x05'
print("Success: model fix")

time.sleep(0.5)
#replaces the special checksum; if you want to recalculate the special checksum again, compile mktplinkfw.c from https://github.com/jtreml/firmware-mod-kit/tree/master/src/firmware-tools
#then, rum $mktplinkfw -i [FILENAME]
#NOTE: mktplinkfw.c requires md5.h and md5.c, also found in the same repo linked above
m[0x4C:0x5C] = b'\x13\xBC\x40\x88\x28\x2F\x0F\x21\x68\x78\x61\x98\x54\xF3\x17\x7F'
print("Success: checksum fix")
time.sleep(0.2)
print("Try uploading now.")
time.sleep(0.5)
m.close()
f.close()
