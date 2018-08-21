# Overview

This folder includes an example for processing [Video Metadata Hub](https://iptc.org/std/videometadatahub/recommendation/1.2) data by Python scripts.

Read also the [README](../README.md) of the parenting folder.

# Examples

## Example 1 = ex1-allVMHub...

This example shows how to generate a JSON file for Exiftool for all properties (also called fields) of the Video Metadata Hub and how to embed the XMP metadata into a video file.

* ex1-allVMHub_generateEtJson.py: generates a value for each metadata property defined by the IPTC Video Metadata Hub as mapped to an exiftool property. The property identifiers and the values are expressed as JSON object in a format required by exiftool.
* ex1-allVMHub_propValues.yml: the values of the Python script are retrieved from this YAML file. Each line show - in double-quotes - first the property identifier of exiftool and to the right of a colon a value for this property. These values can be changed as required. Warning: the properties with a # as suffix in their identifier need a value from an enumeration. See the VMHub specification for these values.
* ex1-allVMHub_etData.json: the JSON object created by the Python script using the YAML file for the property values.
* ex1-allVMHub_embedAndDocument.cmd: a Windows command line script for a/ copying the generic video without metadata to a local file, b/ embedding the metadata and c/ retrieving the XMP packet of the video file and saving it as XML file. This script creates:
  * ex1-allVMHub_video1.mp4: the video file with the embedded metadata
  * ex1-allVMHub_video1.xmp.xml: the XML file with the retrieved XMP packet