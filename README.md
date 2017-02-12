# wr941ndv5-ddwrt
Source and pre-compiled DD-WRT firmware for TP-LINK WR941ND V5 (beta build 02-07-2017-r31277)

This firmware is based on DD-WRT for WR**8**41ND**V8**, which is based on the same hardware but has different model and checksum identifiers.

**Warning:** be sure your device has the FCC ID tagged TE7WR941NX**V5**. Otherwise, don't upload this firmware or you may brick your device.

## Requires:
* Python 3.4

On Ubuntu 14.04 or 16.04, run:
```
sudo apt-get update && sudo apt-get -y install python3
git clone https://github.com/leonidasv/wr941ndv5-ddwrt.git
cd wr941ndv5-ddwrt
python3 make.py
```

*Or simply use the precompiled file* ¯&#92;&#95;(ツ)&#95;/¯
