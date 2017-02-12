from __future__ import absolute_import
import mmap
import urllib.request
from pathlib import Path
print('Checking for firmware...')
firmware = Path("factory-to-ddwrt.bin")
if firmware.is_file():
	print("File exists.")
else:
	print("Firmware not found, downloading it from DD-WRT servers...")
	urllib.request.urlretrieve("http://download1.dd-wrt.com/dd-wrtv2/downloads/betas/2017/02-07-2017-r31277/tplink_tl-wr841ndv8/factory-to-ddwrt.bin", "factory-to-ddwrt.bin")
	print("Success: download.")
f = open('factory-to-ddwrt.bin', 'a+')
m = mmap.mmap(f.fileno(), 0)
m[0x40:0x44] = b'\x09\x41\x00\x05'
print("Success: model fix")
m[0x4C:0x5C] = b'\xA9\x8C\x08\xBD\xD1\x70\x60\x8E\x9B\xF4\x07\xB5\x8F\xA9\x83\x7A'
print("Success: checksum fix")
print("Try uploading now.")
m.close()
f.close()
