echo off

copy myPhoto1-nomd.jpg myTestphoto1.jpg

exiftool -v -all:= -j=IPTC-PMD-etData-1.json myTestphoto1.jpg

exiftool -xmp -b myTestphoto1.jpg > myTestphoto1.xmp.xml

echo DONE

pause
