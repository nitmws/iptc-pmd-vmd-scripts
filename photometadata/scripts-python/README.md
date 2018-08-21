# Overview

This folder includes an example for processing [Photo Metadata Standard](https://iptc.org/standards/photo-metadata/iptc-standard/) data by Python scripts. (The scripts have been tested with Python 3.5.2)

Read also the [README](../README.md) of the parenting folder.

# Examples

## Example 1 = ex1-allPmd...

This example shows how to generate a JSON file for Exiftool for all properties (also called fields) of the Photo Metadata Standard and how to embed the XMP metadata into an image file.

* ex1-allPmd_generateEtJson.py: generates a value for each metadata property defined by the IPTC Photo Metadata Standard as mapped to an exiftool property. The property identifiers and the values are expressed as JSON object in a format required by exiftool.
* ex1-allPmd_propValues.yml: the values of the Python script are retrieved from this YAML file. Each line shows - in double-quotes - first the property identifier of exiftool and to the right of a colon a value for this property. These values can be changed as required. Warning: the properties with a # as suffix in their identifier need a value from an enumeration.
* ex1-allPmd_etData.json: the JSON object created by the Python script using the YAML file for the property values.
* ex1-allPmd_embedAndDocument.cmd: a Windows command line script for a/ copying the generic image file without metadata to a local file, b/ embedding the metadata and c/ retrieving the XMP packet from the image file and saving it as XML file. This script creates:
  * ex1-allPmd_photo1.jpg: the image file with the embedded metadata
  * ex1-allPmd_photo1.xmp.xml: the XML file with the retrieved XMP packet