#compatibility layer for Python 2.7
from __future__ import absolute_import
#binary editor
import mmap
#download library
import urllib.request
from pathlib import Path

#checks for file
print('Checking for firmware...')
firmware = Path("factory-to-ddwrt.bin")

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

#replace the addresses from 0x40 to 0x43; the original file contains the hex "08410008" (wr841 v8) placed here, this piece of code replaces it to 09410005 (wr941 v5)
m[0x40:0x44] = b'\x09\x41\x00\x05'
print("Success: model fix")

#replaces the special checksum; if you want to recalculate the special checksum again, compile mktplinkfw.c from https://github.com/jtreml/firmware-mod-kit/tree/master/src/firmware-tools
#NOTE: mktplinkfw.c requires md5.h and md5.c, also found in the same repo linked above
m[0x4C:0x5C] = b'\xA9\x8C\x08\xBD\xD1\x70\x60\x8E\x9B\xF4\x07\xB5\x8F\xA9\x83\x7A'
print("Success: checksum fix")
print("Try uploading now.")
m.close()
f.close()
