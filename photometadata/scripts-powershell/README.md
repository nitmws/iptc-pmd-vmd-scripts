# Overview

This folder includes an example for processing [Photo Metadata Standard](https://iptc.org/standards/photo-metadata/iptc-standard/) data by Powershell scripts.

Read also the [README](../README.md) of the parenting folder.

# Examples

## Example 1 = ex1-allPMD...

This example shows how to generate a JSON file for Exiftool for all properties (also called fields) of the Photo Metadata Standard and how to embed the XMP metadata into an image file.

* ex1-allPmd_generateEtJson.ps1: generates a value for each metadata property defined by the IPTC Photo Metadata Standard as mapped to an exiftool property. The property identifiers and the values are expressed as JSON object in a format required by exiftool.
* ex1-allPmd_etData.json: the JSON object created by the Powershell script.
* ex1-allPmd_embedAndDocument.cmd: a Windows command line script for a/ copying the generic image file without metadata to a local file, b/ embedding the metadata and c/ retrieving the XMP packet of the video file and saving it as XML file. This script creates:
  * ex1-allPmd_photo1.jpg: the image file with the embedded metadata
  * ex1-allPmd_photo1.xmp.xml: the XML file with the retrieved XMP packet