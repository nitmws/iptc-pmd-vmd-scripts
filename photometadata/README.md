# How to embed IPTC Photo Metadata

IPTC defines by its [Photo Metadata Standard](https://iptc.org/standards/photo-metadata/iptc-standard/) a rich set of metadata properties (also called fields). All these properties can be embedded into image files as IPTC IIM, and/or XMP metadata and/or Exif metadata.

For this action these scripts use [exiftool](http://owl.phy.queensu.ca/~phil/exiftool/). Exiftool has its own identfiers for all the IPTC properties/fields - [see the ExifTool Tag Names](http://owl.phy.queensu.ca/~phil/exiftool/TagNames/index.html).

This mapping is implemented by the scripts: for each Photo Metadata Standard property exists a comment telling its name, the script lines below start with a generic variable holding its value and transforming it to a JSON property for exiftool. In a next step this JSON file can be used as command line argument of exiftool to embed the metadata.

## Files

The aPhoto1-nomd.jpg video file shows a flower and does not have any embedded IPTC metadata. It is used by scripts in the sub-folders as starting point for embedding metadata.