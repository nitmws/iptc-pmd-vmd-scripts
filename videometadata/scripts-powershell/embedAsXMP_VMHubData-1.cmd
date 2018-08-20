echo off

copy myVideo1-nomd.mp4 myTestvideo1.mp4

exiftool -v -all:= -j=IPTC-VMHub-etData-1.json myTestvideo1.mp4

exiftool -xmp -b myTestvideo1.mp4 > myTestvideo1.xmp.xml

echo DONE

pause
