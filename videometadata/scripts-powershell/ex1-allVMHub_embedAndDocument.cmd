echo off

REM create a copy of a generic video without any IPTC metadata
copy ..\aVideo1-nomd.mp4 ex1-allVMHub_video1.mp4

REM embed the metadata by exiftool using the data of the JSON file
exiftool -v -all= -j=ex1-allVMHub_etData.json ex1-allVMHub_video1.mp4

REM retrieve the XMP metadata and write it to an XML file
exiftool -xmp -b ex1-allVMHub_video1.mp4 > ex1-allVMHub_video1.xmp.xml

echo DONE

pause
