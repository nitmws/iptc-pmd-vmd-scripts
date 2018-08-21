# How to embed IPTC Video Metadata

IPTC defines by its [Video Metadata Hub](https://iptc.org/std/videometadatahub/recommendation/1.2) a rich set of metadata properties (also called fields). All these properties can be embedded into video fieles as XMP metadata. 

For this action these scripts use [exiftool](http://owl.phy.queensu.ca/~phil/exiftool/). As exiftool has its own identfiers for all the IPTC properties/fields IPTC provides as part of its Recommendation also [an official mapping](https://iptc.org/std/videometadatahub/recommendation/IPTC-VideoMetadataHub-mapping-exiftool-Rec_1.2.html) of the Video Metadata Hub properties to exiftool properties. 

This mapping is implemented by the scripts: for each Video Metadata Hub property exists a comment telling its name, the script lines below start with a generic variable holding its value and transforming it to a JSON property for exiftool. In a next step this JSON file can be used as command line argument of exiftool to embed the metadata.

# Files

The aVideo1-nomd.mp4 video file shows a short video and does not have any embedded IPTC metadata. It is used by scripts in the sub-folders as starting point for embedding metadata.