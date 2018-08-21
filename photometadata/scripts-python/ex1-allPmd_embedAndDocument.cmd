echo off

REM create a copy of a generic photo without any IPTC metadata
copy ..\aPhoto1-nomd.jpg ex1-allPmd_photo1.jpg

REM embed the metadata by exiftool using the data of the JSON file
exiftool -v -all= -j=ex1-allPmd_etData.json ex1-allPmd_photo1.jpg

REM retrieve the XMP metadata and write it to an XML file
exiftool -xmp -b ex1-allPmd_photo1.jpg > ex1-allPmd_photo1.xmp.xml

echo DONE

pause
