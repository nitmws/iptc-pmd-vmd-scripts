<#
    Video Metadata Hub - Script to create a JSON file for Exiftool with all IPTC properties populated
#>

# ********** Intro ********************************************************
# ***** Parameters
# $inputFp = "" # input file path
$jsonOutputFp = "IPTC-VMHub-etData-1.json" # JSON output file path

[string]$valStr = "" # string representation of the property value
[int]$valInt = -1 # integer representation of the property value

$vmd = [ordered]@{} # initialize the Video Metadata object 
$vmd.SourceFile = "*" # = can be applied to a video with any file name

# ********** Creating a video metadata object - properties in alphabetical order

# XMP markers: the array is initated, markers may be added by different properties
$vmd.'XMP-xmpDM:markers' = @()

# VMDp audioBitRate
$valStr = "2018000"
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:AudioBitRate' = $valStr }

# VMDp AudioBitsPerSample (new 1.2)
$valStr = "16"
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:AudioBitsPerSample' = $valStr }

# VMDp audioBitRateMode
$valStr = "variable"
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:AudioBitRateMode#' = $valStr }

# VMDp audioChannelType
$valStr = "5.1"
if ($valStr-ne "")
{ $vmd.'XMP-xmpDM:AudioChannelType#' = $valStr }

# VMDp audioChannelCount
$valStr = "2"
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:AudioChannelCount' = $valStr }

# VMDp audioCompressor
$valStr = "MP3"
if ($valStr-ne "")
{ $vmd.'XMP-xmpDM:AudioCompressor' = $valStr }

# VMDp audioSampleRate
$valStr = "48016"
if ($valStr-ne "")
{ $vmd.'XMP-xmpDM:AudioSampleRate' = $valStr }


# VMDp CircaDateCreated
$valStr = "Circa Date Created "
if ($valStr-ne "")
{  $vmd.'XMP-iptcExt:CircaDateCreated' = $valStr }

# VMDp Contributor
$vmd.'XMP-iptcExt:Contributor' = @()
$propObject = @{}
$valStr = "Contributor Id 1 "
if ($valStr -ne "")
{ $propObject.'Identifier' = $valStr}
$valStr = "Contributor Name 1 "
if ($valStr -ne "")
{ $propObject.'Name' = $valStr}
$valStr = "http://example.org/cv/vmh/role-contrib/code0101"
if ($valStr -ne "")
{ $propObject.'Role' = $valStr}
$vmd.'XMP-iptcExt:Contributor' += $propObject
# 2nd entry
$propObject = @{}
$valStr = "Contributor Id 2 "
if ($valStr -ne "")
{ $propObject.'Identifier' = $valStr}
$valStr = "Contributor Name 2 "
if ($valStr -ne "")
{ $propObject.'Name' = $valStr}
$valStr = "http://example.org/cv/vmh/role-contrib/code0101"
if ($valStr -ne "")
{ $propObject.'Role' = $valStr}
$vmd.'XMP-iptcExt:Contributor' += $propObject


# VMDp Copyright Notice
$valStr = "Copyright (Notice) 2016 IPTC - www.iptc.org  "
if ($valStr-ne "")
{ $vmd.'XMP-dc:Rights' = $valStr }

# VMDp CopyrightYear
$valStr = "2016"
if ($valStr-ne "")
{  $vmd.'XMP-iptcExt:CopyrightYear' = $valStr }

# VMDp Creator
$vmd.'XMP-iptcExt:Creator' = @()
$propObject = @{}
$valStr = "Creator Id 1 "
if ($valStr -ne "")
{ $propObject.'Identifier' = $valStr}
$valStr = "Creator Name 1 "
if ($valStr -ne "")
{ $propObject.'Name' = $valStr}
$valStr = "http://example.org/cv/vmh/role-creator/code0101"
if ($valStr -ne "")
{ $propObject.'Role' = $valStr}
$vmd.'XMP-iptcExt:Creator' += $propObject
# 2nd entry
$propObject = @{}
$valStr = "Creator Id 2 "
if ($valStr -ne "")
{ $propObject.'Identifier' = $valStr}
$valStr = "Creator Name 2 "
if ($valStr -ne "")
{ $propObject.'Name' = $valStr}
$valStr = "http://example.org/cv/vmh/role-creator/code0101"
if ($valStr -ne "")
{ $propObject.'Role' = $valStr}
$vmd.'XMP-iptcExt:Creator' += $propObject

# VMDp Credit Line
$valStr = "Credit Line "
if ($valStr-ne "")
{ $vmd.'XMP-photoshop:Credit' = $valStr }

# VMDp CV-Term About video
$vmd.'XMP-iptcExt:AboutCvTerm' = @()
$propObject = @{}
$valStr = "http://example.com/cv/about/test0102/code987"
if ($valStr-ne "")
{ $propObject.'CvTermId' += $valStr }
$valStr = "CV-Term Name 1 "
if ($valStr-ne "")
{ $propObject.'CvTermName' += $valStr }
$valStr = "http://example.com/cv/about/test0102"
if ($valStr-ne "")
{ $propObject.'CvId' += $valStr }
$valStr = "http://example.com/cv/refinements2/test0102/codeX145"
if ($valStr-ne "")
{ $propObject.'CvTermRefinedAbout' += $valStr }
$vmd.'XMP-iptcExt:AboutCvTerm' += $propObject

# VMDp DataOnScreen
$vmd.'XMP-iptcExt:DataOnScreen' = @()
$propObject = @{}
$valStr = "Data on Screen 1 "
if ($valStr -ne "")
{ $propObject.'RegionText' = $valStr}
$propObject2 = @{}
$valStr = "30"
if ($valStr -ne "")
{ $propObject2.'x' = $valStr}
$valStr = "500"
if ($valStr -ne "")
{ $propObject2.'y' = $valStr}
$valStr = "200"
if ($valStr -ne "")
{ $propObject2.'h' = $valStr}
$valStr = "1000"
if ($valStr -ne "")
{ $propObject2.'w' = $valStr}
$valStr = "pixel"
if ($valStr -ne "")
{ $propObject2.'unit' = $valStr}
$propObject.'Region' = $propObject2
$vmd.'XMP-iptcExt:DataOnScreen' += $propObject

# VMDp Date (and Time) Created
$valStr = "2018-04-25T18:01:02+00:00"
$valStrDate = $valStr.Substring(0,10).Replace("-",":")
$ValStrTime = $valStr.Substring(11)
if ($valStr-ne "")
{ $vmd.'XMP-photoshop:DateCreated' = $valStrDate + " " + $ValStrTime }

# VMDp ModifyDate
$valStr = "2018-06-12T18:01:02+00:00"
$valStrDate = $valStr.Substring(0,10).Replace("-",":")
$ValStrTime = $valStr.Substring(11)
if ($valStr-ne "")
{ $vmd.'XMP-xmp:ModifyDate' = $valStrDate + " " + $ValStrTime }

# VMDp releaseDate
$valStr = "2016-11-22T12:00:00+00:00"
$valStrDate = $valStr.Substring(0,10).Replace("-",":")
$ValStrTime = $valStr.Substring(11)
if ($valStr-ne "")
{ $vmd.'XMP-xmpDM:ReleaseDate' = $valStrDate + " " + $ValStrTime }

# VMDp Description
$valStr = "The description"
# $valStr = ""
if ($valStr-ne "")
{ $vmd.'XMP-dc:Description' = $valStr }

# VMDp videoDisplayAspectRatio
$valStr = "16/10"
# $valStr = ""
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:VideoDisplayAspectRatio' = $valStr }

# VMDp Dopesheet
$valStr = "This is the Dopesheet "
# $valStr = ""
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:Dopesheet' = $valStr }

# VMDp DopesheetLink
$vmd.'XMP-iptcExt:DopesheetLink' = @()
$propObject = @{}
$valStr = "http://example.com/dopesheets/test0102"
if ($valStr-ne "")
{ $propObject.'Link' += $valStr }
$valStr = "http://example.com/linkqualifier/test0102"
if ($valStr-ne "")
{ $propObject.'LinkQualifier' += $valStr }
$vmd.'XMP-iptcExt:DopesheetLink' += $propObject

# VMDp Editorial Duration Start
$propObject = @{}
$propObject.'type' = "http://cv.iptc.org/newscodes/videoqualifier/editorialDurationStart"
$propObject.'startTime' = "258f25"
$propObject.'comment' = "VMHub comment: the start marker for a *duration by start and end markers* design."
$vmd.'XMP-xmpDM:Markers' += $propObject

# VMDp Editorial Duration End 
$propObject = @{}
$propObject.'type' = "http://cv.iptc.org/newscodes/videoqualifier/editorialDurationEnd"
$propObject.'startTime' = "2589f25"
$propObject.'comment' = "VMHub comment: the end marker for a *duration by start and end markers* design."
$vmd.'XMP-xmpDM:Markers' += $propObject

# VMDp Editorial Duration 
$propObject = @{}
$propObject.'type' = "http://cv.iptc.org/newscodes/videoqualifier/editorialDuration"
$propObject.'startTime' = "258f25"
$propObject.'duration' = "2331f25"
$propObject.'comment' = "VMHub comment: the start + duration marker for a *duration by a single start + duration marker* design."
$vmd.'XMP-xmpDM:Markers' += $propObject


# VMDp Episode
$vmd.'XMP-iptcExt:Episode' = @()
$propObject = @{}
$valStr = "http://example.com/series/season/episode/test0102"
if ($valStr-ne "")
{ $propObject.'Identifier' += $valStr }
$valStr = "Episode Name 1 "
if ($valStr-ne "")
{ $propObject.'Name' += $valStr }
$valStr = "EpR0101"
if ($valStr-ne "")
{ $propObject.'Number' += $valStr }
$vmd.'XMP-iptcExt:Episode' += $propObject

# VMDp ExternalMetadataLink
$valStr = "http://example.com/externalmetadata/test0102)"
# $valStr = ""
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:ExternalMetadataLink' = $valStr }

# VMDp Name of company featured in the image
$vmd.'XMP-iptcExt:OrganisationInImageName' = @()
$valStr = "Organisation Name 1 "
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:OrganisationInImageName' += $valStr }
$valStr = "Organisation Name 2 "
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:OrganisationInImageName' += $valStr }
$valStr = "Organisation Name 3 "
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:OrganisationInImageName' += $valStr }

# VMDp Code of company featured in the image
$vmd.'XMP-iptcExt:OrganisationInImageCode' = @()
$valStr = "Organisation Code 1 "
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:OrganisationInImageCode' += $valStr }
$valStr = "Organisation Code 2 "
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:OrganisationInImageCode' += $valStr }
$valStr = "Organisation Code 3 "
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:OrganisationInImageCode' += $valStr }

# VMDp FeedIdentifier
$valStr = "Feed Identifier "
# $valStr = ""
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:FeedIdentifier' = $valStr }

# VMDp fileDataRate
$valStr = "10000000"
# $valStr = ""
if ($valStr-ne "")
{ $vmd.'XMP-xmpDM:FileDataRate' = $valStr }

# VMDp duration
$vmd.'XMP-xmpDM:duration' = @()
$propObject = @{}
$valStr = "1/25"
if ($valStr-ne "")
{ $propObject.'scale' += $valStr }
$valStr = "25000"
if ($valStr-ne "")
{ $propObject.'value' += $valStr }
$vmd.'XMP-xmpDM:Duration' += $propObject

# VMDp ContainerFormat (file format)
$vmd.'XMP-iptcExt:ContainerFormat' = @()
$propObject = @{}
$valStr = "ContainerFormat Id 1 "
if ($valStr -ne "")
{ $propObject.'Identifier' = $valStr}
$valStr = "ContainerFormat Name 1 "
if ($valStr -ne "")
{ $propObject.'Name' = $valStr}
$vmd.'XMP-iptcExt:ContainerFormat' += $propObject

# VMDp videoFrameSize (frame size)
$vmd.'XMP-xmpDM:videoFrameSize' = @()
$propObject = @{}
$valStr = "1080"
if ($valStr -ne "")
{ $propObject.'h' = $valStr}
$valStr = "1920"
if ($valStr -ne "")
{ $propObject.'w' = $valStr}
$valStr = "pixel"
if ($valStr -ne "")
{ $propObject.'unit' = $valStr}
$vmd.'XMP-xmpDM:VideoFrameSize' += $propObject


# VMDp (generic) Genre 
$vmd.'XMP-iptcExt:Genre' = @()
$propObject = @{}
$valStr = "http://example.com/cv/genre/test0102/code1369"
if ($valStr-ne "")
{ $propObject.'CvTermId' += $valStr }
$valStr = "Genre CV-Term Name 1 "
if ($valStr-ne "")
{ $propObject.'CvTermName' += $valStr }
$valStr = "http://example.com/cv/genre/test0102"
if ($valStr-ne "")
{ $propObject.'CvId' += $valStr }
$valStr = "http://example.com/cv/genrerefinements2/test0102/codeY864"
if ($valStr-ne "")
{ $propObject.'CvTermRefinedAbout' += $valStr }
$vmd.'XMP-iptcExt:Genre' += $propObject

# vMDp Headline
$valStr = "The Headline "
# $valStr = ""
if ($valStr-ne "")
{ $vmd.'XMP-photoshop:Headline' = $valStr }

# vMDp Keyword(s)
$vmd.'XMP-dc:Subject' = @()
$valStr = "Keyword1test0102"
if ($valStr-ne "")
{ $vmd.'XMP-dc:Subject' += $valStr }
$valStr = "Keyword2test0102"
if ($valStr-ne "")
{ $vmd.'XMP-dc:Subject' += $valStr }
$valStr = "Keyword3test0102"
if ($valStr-ne "")
{ $vmd.'XMP-dc:Subject' += $valStr }

# VMDp language
$valStr = "en-GB "
# $valStr = ""
if ($valStr-ne "")
{ $vmd.'XMP-dc:Language' = $valStr }

# VMDp Licensor 
$vmd.'XMP-plus:Licensor' = @()
$propObject = @{}
$valStr = "Licensor ID 1 "
if ($valStr -ne "")
{ $propObject.'LicensorID' = $valStr}
$valStr = "Licensor Name 1 "
if ($valStr -ne "")
{ $propObject.'LicensorName' = $valStr}
$valStr = "Licensor Street Addr 1 "
if ($valStr -ne "")
{ $propObject.'LicensorStreetAddress' = $valStr}
$valStr = "Licensor Ext Addr 1 "
if ($valStr -ne "")
{ $propObject.'LicensorExtendedAddress' = $valStr}
$valStr = "Licensor City 1 "
if ($valStr -ne "")
{ $propObject.'LicensorCity' = $valStr}
$valStr = "Licensor Region 1 "
if ($valStr -ne "")
{ $propObject.'LicensorRegion' = $valStr}
$valStr = "Licensor Country 1 "
if ($valStr -ne "")
{ $propObject.'LicensorCountry' = $valStr}
$valStr = "Licensor Postcode 1 "
if ($valStr -ne "")
{ $propObject.'LicensorPostalCode' = $valStr}
$valStr = "Licensor Phone1 1 "
if ($valStr -ne "")
{ $propObject.'LicensorTelephone1' = $valStr}
$valStr = "Licensor Phone2 1 "
if ($valStr -ne "")
{ $propObject.'LicensorTelephone2' = $valStr}
$valStr = "Licensor Email 1 "
if ($valStr -ne "")
{ $propObject.'LicensorEmail' = $valStr}
$valStr = "Licensor URL 1 "
if ($valStr -ne "")
{ $propObject.'LicensorURL' = $valStr}
$vmd.'XMP-plus:Licensor' += $propObject

# VMDp Location Created
$vmd.'XMP-iptcExt:LocationCreated' = @()
$propObject = @{}
$valStr = "Name of Location Created 1 "
if ($valStr-ne "")
{ $propObject.'LocationName' = $valStr }
$valStr = "Sublocation (Location created1) "
if ($valStr-ne "")
{ $propObject.'Sublocation' = $valStr }
$valStr = "City (Location created1) "
if ($valStr-ne "")
{ $propObject.'City' = $valStr }
$valStr = "Province/State (Location created1) "
if ($valStr-ne "")
{ $propObject.'ProvinceState' = $valStr }
$valStr = "CountryName (Location created1) "
if ($valStr-ne "")
{ $propObject.'CountryName' = $valStr }
$valStr = "R16"
if ($valStr-ne "")
{ $propObject.'CountryCode' = $valStr }
$valStr = "Worldregion (Location created1) "
if ($valStr-ne "")
{ $propObject.'WorldRegion' = $valStr }
$valStr = "Location Id (Location created1) "
if ($valStr-ne "")
{ $propObject.'LocationId' = $valStr }
$valStr = "48,14.03E"
if ($valStr-ne "")
{ $propObject.'GPSLongitude' = $valStr }
$valStr = "16,20.02N"
if ($valStr-ne "")
{ $propObject.'GPSLatitude' = $valStr }
$valStr = "180"
if ($valStr-ne "")
{ $propObject.'GPSAltitude' = $valStr }
$vmd.'XMP-iptcExt:LocationCreated'+= $propObject

# VMDp Location Shown
$vmd.'XMP-iptcExt:LocationShown' = @()
$propObject = @{}
$valStr = "Name of Location Shown 1 "
if ($valStr-ne "")
{ $propObject.'LocationName' = $valStr }
$valStr = "Sublocation (Location shown1) "
if ($valStr-ne "")
{ $propObject.'Sublocation' = $valStr }
$valStr = "City (Location shown1) "
if ($valStr-ne "")
{ $propObject.'City' = $valStr }
$valStr = "Province/State (Location shown1) "
if ($valStr-ne "")
{ $propObject.'ProvinceState' = $valStr }
$valStr = "CountryName (Location shown1) "
if ($valStr-ne "")
{ $propObject.'CountryName' = $valStr }
$valStr = "R16"
if ($valStr-ne "")
{ $propObject.'CountryCode' = $valStr }
$valStr = "Worldregion (Location shown1) "
if ($valStr-ne "")
{ $propObject.'WorldRegion' = $valStr }
$propObject.'LocationId' = @()
$valStr = "Location Id 1a(Location shown1) "
if ($valStr-ne "")
{ $propObject.'LocationId' += $valStr }
$valStr = "Location Id 1b(Location shown1) "
if ($valStr -ne "")
{ $propObject.'LocationId' += $valStr }
$valStr = "48,15.03E"
if ($valStr-ne "")
{ $propObject.'GPSLongitude' = $valStr }
$valStr = "16,21.02N"
if ($valStr-ne "")
{ $propObject.'GPSLatitude' = $valStr }
$valStr = "180"
if ($valStr-ne "")
{ $propObject.'GPSAltitude' = $valStr }
$vmd.'XMP-iptcExt:LocationShown'+= $propObject

$propObject = @{}
$valStr = "Name of Location Shown 2 "
if ($valStr-ne "")
{ $propObject.'LocationName' = $valStr }
$valStr = "Sublocation (Location shown2) "
if ($valStr-ne "")
{ $propObject.'Sublocation' = $valStr }
$valStr = "City (Location shown2) "
if ($valStr-ne "")
{ $propObject.'City' = $valStr }
$valStr = "Province/State (Location shown2) "
if ($valStr-ne "")
{ $propObject.'ProvinceState' = $valStr }
$valStr = "CountryName (Location shown2) "
if ($valStr-ne "")
{ $propObject.'CountryName' = $valStr }
$valStr = "R16"
if ($valStr-ne "")
{ $propObject.'CountryCode' = $valStr }
$valStr = "Worldregion (Location shown2) "
if ($valStr-ne "")
{ $propObject.'WorldRegion' = $valStr }
$valStr = "Location Id (Location shown2) "
if ($valStr-ne "")
{ $propObject.'LocationId' = $valStr }
$propObject.'LocationId' = @()
$valStr = "Location Id 2a(Location shown2) "
if ($valStr-ne "")
{ $propObject.'LocationId' += $valStr }
$valStr = "Location Id 2b(Location shown2) "
if ($valStr-ne "")
{ $propObject.'LocationId' += $valStr } 
$valStr = "48,16.03E"
if ($valStr-ne "")
{ $propObject.'GPSLongitude' = $valStr }
$valStr = "16,22.02N"
if ($valStr-ne "")
{ $propObject.'GPSLatitude' = $valStr }
$valStr = "180"
if ($valStr-ne "")
{ $propObject.'GPSAltitude' = $valStr }
$vmd.'XMP-iptcExt:LocationShown'+= $propObject

# VMDp format
$valStr = "video/H264 "
if ($valStr-ne "")
{ $vmd.'XMP-dc:Format' = $valStr }

# VMDp Model Release Id
$vmd.'XMP-plus:ModelReleaseID' = @()
$valStr = "Model Release ID 1 "
if ($valStr-ne "")
{ $vmd.'XMP-plus:ModelReleaseID' += $valStr}
$valStr = "Model Release ID 2 "
if ($valStr-ne "")
{ $vmd.'XMP-plus:ModelReleaseID' += $valStr}

# VMDp Model Release Status
$valStr = "Not Applicable"
if ($valStr-ne "")
{ $vmd.'XMP-plus:ModelReleaseStatus' = $valStr }

# VMDp Object Shown
$vmd.'XMP-iptcExt:ArtworkOrObject' = @()
$ao = @{}
$ao.'AOCreator' = @()
$valStr = "AO Creator Name 1a "
$ao.'AOCreator' += $valStr
$valStr = "AO Creator Name 1b "
$ao.'AOCreator' += $valStr
$valStr = "1916-10-26T12:13:14+00:00"
$valStrDate = $valStr.Substring(0,10).Replace("-",":")
$ValStrTime = $valStr.Substring(11)
if ($valStr-ne "")
{ $ao.'AODateCreated' = $valStrDate + " " + $ValStrTime }
$valStr = "AO Copyright Notice 1 "
if ($valStr-ne "")
{ $ao.'AOCopyrightNotice' = $valStr }
$valStr = "AO Title 1 "
if ($valStr-ne "")
{ $ao.'AOTitle' = $valStr }
$valStr = "AO Source 1 "
if ($valStr-ne "")
{ $ao.'AOSource' = $valStr }
$valStr = "AO Source Inventory No 1 "
if ($valStr-ne "")
{ $ao.'AOSourceInvNo' = $valStr }
$ao.'AOCreatorId' = @()
$valStr = "AO Creator Id 1a "
if ($valStr-ne "")
{ $ao.'AOCreatorId' += $valStr }
$valStr = "AO Creator Id 1b "
if ($valStr-ne "")
{ $ao.'AOCreatorId' += $valStr }
$valStr = "AO Circa Date: between 1550 and 1600 "
if ($valStr-ne "")
{ $ao.'AOCircaDateCreated' = $valStr }
$valStr = "AO Content Description 1 "
if ($valStr-ne "")
{ $ao.'AOContentDescription' = $valStr }
$valStr = "AO Contribution Description 1 "
if ($valStr-ne "")
{ $ao.'AOContributionDescription' = $valStr }
$valStr = "AO Current Copyright Owner ID 1 "
if ($valStr-ne "")
{ $ao.'AOCurrentCopyrightOwnerId' = $valStr }
$valStr = "AO Current Copyright Owner Name 1 "
if ($valStr-ne "")
{ $ao.'AOCurrentCopyrightOwnerName' = $valStr }
$valStr = "AO Current Licensor ID 1 "
if ($valStr-ne "")
{ $ao.'AOCurrentLicensorId' = $valStr }
$valStr = "AO Current Licensor Name 1 "
if ($valStr-ne "")
{ $ao.'AOCurrentLicensorName' = $valStr }
$valStr = "AO Physical Description 1 "
if ($valStr-ne "")
{ $ao.'AOPhysicalDescription' = $valStr }
$valStr = "AO Source Inventory URL "
if ($valStr-ne "")
{ $ao.'AOSourceInvURL' = $valStr }
$ao.'AOStylePeriod' = @()
$valStr = "AO Style Baroque "
if ($valStr-ne "")
{ $ao.'AOStylePeriod' += $valStr }
$valStr = "AO Style Italian Baroque "
if ($valStr-ne "")
{ $ao.'AOStylePeriod' += $valStr }
# finally: add the Artwork/Object object to the VMD
$vmd.'XMP-iptcExt:ArtworkOrObject' += $ao

# VMDp Orientation
$valStr = "1"
if ($valStr-ne "")
{ $vmd.'XMP-tiff:Orientation#' = $valStr }

# VMDp PersonHeard
$vmd.'XMP-iptcExt:PersonHeard' = @()
$propObject = @{}
$valStr = "PersonHeard Id 1 "
if ($valStr -ne "")
{ $propObject.'Identifier' = $valStr}
$valStr = "PersonHeard Name 1 "
if ($valStr -ne "")
{ $propObject.'Name' = $valStr}
$vmd.'XMP-iptcExt:PersonHeard' += $propObject

# VMDp Person Shown in the Image with Details 
$vmd.'XMP-iptcExt:PersonInImageWDetails' = @()

$pers = @{}
$valStr = "Person Name 1 "
if ($valStr-ne "")
{ $pers.'PersonName' = $valStr}
$pers.'PersonId' = @()
$valStr = "http://wikidata.org/item/Q123456789/test0102"
if ($valStr-ne "")
{ $pers.'PersonId' += $valStr}
$valStr = "http://freebase.com/m/987654321/test0102"
if ($valStr-ne "")
{ $pers.'PersonId' += $valStr}
$valStr = "Person Description 1 "
if ($valStr-ne "")
{ $pers.'PersonDescription' += $valStr}

$pers.'PersonCharacteristic' = @()
$perschar = @{}
$valStr = "http://example.com/cv/test99/code987/test0102"
if ($valStr-ne "")
{ $perschar.'CvTermId' += $valStr }
$valStr = "Person Characteristic Name 1 "
if ($valStr-ne "")
{ $perschar.'CvTermName' += $valStr }
$valStr = "http://example.com/cv/test99/test0102"
if ($valStr-ne "")
{ $perschar.'CvId' += $valStr }
$valStr = "http://example.com/cv/refinements987/codeY765/test0102"
if ($valStr-ne "")
{ $perschar.'CvTermRefinedAbout' += $valStr }
$pers.'PersonCharacteristic' += $perschar

$vmd.'XMP-iptcExt:PersonInImageWDetails' += $pers

# VMDp Planning Reference (new 1.2)
$vmd.'XMP-iptcExt:PlanningRef' = @()
$propObject = @{}
$valStr = "Planning Ref Id 1 "
if ($valStr -ne "")
{ $propObject.'Identifier' = $valStr}
$valStr = "Planning Ref Name 1 "
if ($valStr -ne "")
{ $propObject.'Name' = $valStr}
$valStr = "http://example.org/cv/vmh/role-contrib/codeA-test0102"
if ($valStr -ne "")
{ $propObject.'Role' = $valStr}
$vmd.'XMP-iptcExt:PlanningRef' += $propObject
# 2nd entry
$propObject = @{}
$valStr = "Planning Ref Id 2 "
if ($valStr -ne "")
{ $propObject.'Identifier' = $valStr}
$valStr = "Planning Ref Name 2 "
if ($valStr -ne "")
{ $propObject.'Name' = $valStr}
$valStr = "http://example.org/cv/vmh/role-contrib/codeB-test0102"
if ($valStr -ne "")
{ $propObject.'Role' = $valStr}
$vmd.'XMP-iptcExt:PlanningRef' += $propObject

# VMDp Property Release Id
$vmd.'XMP-plus:PropertyReleaseID' = @()
$valStr = "Property Release ID 1 "
if ($valStr-ne "")
{ $vmd.'XMP-plus:PropertyReleaseID' += $valStr }
$valStr = "Property Release ID 2 "
if ($valStr-ne "")
{ $vmd.'XMP-plus:PropertyReleaseID' += $valStr }

# VMDp Property Release Status
$valStr = "Not Applicable"
if ($valStr-ne "")
{ $vmd.'XMP-plus:PropertyReleaseStatus' = $valStr }

# VMDp PublicationEvent
$vmd.'XMP-iptcExt:PublicationEvent' = @()
$propObject = @{}
$valStr = "PublicationEvent Id 1 "
if ($valStr -ne "")
{ $propObject.'Identifier' = $valStr}
$valStr = "PublicationEvent Name 1 "
if ($valStr -ne "")
{ $propObject.'Name' = $valStr}
$valStr = "2018-06-12T20:00:00+00:00"
if ($valStr -ne "")
{ $propObject.'Date' = $valStr}
$vmd.'XMP-iptcExt:PublicationEvent' += $propObject

# VMDp Rating
$vmd.'XMP-iptcExt:Rating' = @()
$propObject = @{}
$valStr = "RatingValue Id 1 "
if ($valStr -ne "")
{ $propObject.'RatingValue' = $valStr}
$valStr = "http://example.com/ratings/test0102"
if ($valStr -ne "")
{ $propObject.'RatingSourceLink' = $valStr}
$valStr = "1"
if ($valStr -ne "")
{ $propObject.'RatingScaleMinValue' = $valStr}
$valStr = "9"
if ($valStr -ne "")
{ $propObject.'RatingScaleMaxValue' = $valStr}
$valStr = "http://example.com/ratingsystem-logo/test0102.jpg"
if ($valStr -ne "")
{ $propObject.'RatingValueLogoLink' = $valStr}

$propObject2 = @{}
$valStr = "Name of Rating Location 1 "
if ($valStr-ne "")
{ $propObject2.'LocationName' = $valStr }
$valStr = "Sublocation (Rating Location 1) "
if ($valStr-ne "")
{ $propObject2.'Sublocation' = $valStr }
$valStr = "City (Rating Location 1) "
if ($valStr-ne "")
{ $propObject2.'City' = $valStr }
$valStr = "Province/State (Rating Location 1) "
if ($valStr-ne "")
{ $propObject2.'ProvinceState' = $valStr }
$valStr = "CountryName (Rating Location 1) "
if ($valStr-ne "")
{ $propObject2.'CountryName' = $valStr }
$valStr = "R16"
if ($valStr-ne "")
{ $propObject2.'CountryCode' = $valStr }
$valStr = "Worldregion (Rating Location 1) "
if ($valStr-ne "")
{ $propObject2.'WorldRegion' = $valStr }
$valStr = "Location Id (Rating Location 1) "
if ($valStr-ne "")
{ $propObject2.'LocationId' = $valStr }
$propObject2.'LocationId' = @()
$valStr = "Location Id 2a(Rating Location 1) "
if ($valStr-ne "")
{ $propObject2.'LocationId' += $valStr }
$valStr = "Location Id 2b(Rating Location 1) "
if ($valStr-ne "")
{ $propObject2.'LocationId' += $valStr } 
$valStr = "47,16.03E"
if ($valStr-ne "")
{ $propObject2.'GPSLongitude' = $valStr }
$valStr = "16,01.02N"
if ($valStr-ne "")
{ $propObject2.'GPSLatitude' = $valStr }
$valStr = "230"
if ($valStr-ne "")
{ $propObject2.'GPSAltitude' = $valStr }
$propObject.'RatingRegion' = $propObject2

$vmd.'XMP-iptcExt:Rating' += $propObject

# VMDp Recording Device (new 1.2, incl new structure)
$propObject = @{}
$valStr = "Rec Device Manufacturer "
if ($valStr-ne "")
{ $propObject.'Manufacturer' = $valStr }
$valStr = "Rec Device Model Name "
if ($valStr-ne "")
{ $propObject.'ModelName' = $valStr }
$valStr = "Rec Device Serial No 123 "
if ($valStr-ne "")
{ $propObject.'SerialNumber' = $valStr }
$valStr = "Rec Device Att Lens Description "
if ($valStr-ne "")
{ $propObject.'AttLensDescription' = $valStr }
$valStr = "Rec Device Owner Device ID "
if ($valStr-ne "")
{ $propObject.'OwnersDeviceId' = $valStr }
$vmd.'XMP-iptcExt:RecDevice' += $propObject

# VMDp Property Release Status
$valStr = "True"
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:ReleaseReady' = $valStr }

# VMDp Image Registry Entry
# Implementation note: only an entry with organisation *and* ItemId makes sense
$vmd.'XMP-iptcExt:RegistryID' = @()
$propObject = @{}
$valStr = "Registry Organisation ID 1 "
if ($valStr-ne "")
{
$propObject.'RegOrgId' = $valStr
$valStr = "Registry Image ID 1 "
if ($valStr-ne "")
{ $propObject.'RegItemId' = $valStr}
$valStr = "Registry Entry Role ID 1 "
if ($valStr-ne "")
{ $propObject.'RegEntryRole' = $valStr }
$vmd.'XMP-iptcExt:RegistryID' += $propObject
}

$propObject = @{}
$valStr = "Registry Organisation ID 2 "
if ($valStr-ne "")
{
$propObject.'RegOrgId' = $valStr
$valStr = "Registry Image ID 2 "
if ($valStr-ne "")
{ $propObject.'RegItemId' = $valStr }
$valStr = "Registry Entry Role ID 2 "
if ($valStr-ne "")
{ $propObject.'RegEntryRole' = $valStr }
$vmd.'XMP-iptcExt:RegistryID' += $propObject
}

# Rights and Licensing Terms
# VMDp Embedded Encoded Rights Expression 
$vmd.'XMP-iptcExt:EmbdEncRightsExpr' = @()

$propObject = @{}
$valStr = "The Encoded Rights Expression "
if ($valStr -ne "")
{ $propObject.'EncRightsExpr' = $valStr
$valStr = "IANA Media Type of ERE "
if ($valStr -ne "")
{ $propObject.'RightsExprEncType' = $valStr }
$valStr = "http://example.org/RELids/id4711/test0102"
if ($valStr -ne "")
{ $propObject.'RightsExprLangId' = $valStr }
}
$vmd.'XMP-iptcExt:EmbdEncRightsExpr' += $propObject

# VMDp Linked Encoded Rights Expression
$vmd.'XMP-iptcExt:LinkedEncRightsExpr' = @()

$propObject = @{}
$valStr = "http://example.org/linkedrightsexpression/id986/test0102"
if ($valStr -ne "")
{ $propObject.'LinkedRightsExpr' = $valStr
$valStr = "IANA Media Type of ERE "
if ($valStr -ne "")
{ $propObject.'RightsExprEncType' = $valStr }
$valStr = "http://example.org/RELids/id4712/test0102"
if ($valStr -ne "")
{ $propObject.'RightsExprLangId' = $valStr }
}
$vmd.'XMP-iptcExt:LinkedEncRightsExpr' += $propObject

# VMDp Rights/Copyright Owner
$vmd.'XMP-plus:CopyrightOwner' = @()
$propObject = @{}
$valStr = "Copyright Owner Id 1 "
if ($propObject -ne "")
{ $propObject.'CopyrightOwnerID' = $valStr}
$valStr = "Copyright Owner Name 1 "
if ($valStr -ne "")
{ $propObject.'CopyrightOwnerName' = $valStr}
$vmd.'XMP-plus:CopyrightOwner' += $propObject

$propObject = @{}
$valStr = "Copyright Owner Id 2 "
if ($valStr -ne "")
{ $propObject.'CopyrightOwnerID' = $valStr}
$valStr = "Copyright Owner Name 2 "
if ($valStr -ne "")
{ $propObject.'CopyrightOwnerName' = $valStr}
$vmd.'XMP-plus:CopyrightOwner' += $copyrightOwner

# VMDp Season
$vmd.'XMP-iptcExt:Season' = @()
$propObject = @{}
$valStr = "http://example.com/series/season/test0102"
if ($valStr-ne "")
{ $propObject.'Identifier' += $valStr }
$valStr = "Season Name 1 "
if ($valStr-ne "")
{ $propObject.'Name' += $valStr }
$valStr = "SeR0101"
if ($valStr-ne "")
{ $propObject.'Number' += $valStr }
$vmd.'XMP-iptcExt:Season' += $propObject

# VMDp Series
$vmd.'XMP-iptcExt:Series' = @()
$propObject = @{}
$valStr = "http://example.com/series/test0102"
if ($valStr-ne "")
{ $propObject.'Identifier' += $valStr }
$valStr = "Series Name 1 "
if ($valStr-ne "")
{ $propObject.'Name' += $valStr }
$vmd.'XMP-iptcExt:Series' += $propObject

# VMDp Snapshot Link (new in VMHub Recommendation 1.1)
$vmd.'XMP-iptcExt:Snapshot' = @()
$snapshotlink = @{}

$valStr = "http://example.com/snapshots/vmhubtest0102.jpg"
if ($valStr-ne "")
{ $snapshotlink.'Link' = $valStr}
$valStr = "Snapshot Link Promotion"
if ($valStr-ne "")
{ $snapshotlink.'ImageRole' = $valStr}
$valStr = "image/jpeg"
if ($valStr-ne "")
{ $snapshotlink.'Format' = $valStr}
$valStr = "4096"
if ($valStr-ne "")
{ $snapshotlink.'WidthPixels' = $valStr}
$valStr = "2160"
if ($valStr-ne "")
{ $snapshotlink.'HeightPixels' = $valStr}
$snapshotlink.'LinkQualifier' = @()
$valStr = "http://www.example.org/videosnapshotqual/frame1"
if ($valStr-ne "")
{ $snapshotlink.'LinkQualifier' += $valStr}
$valStr = "http://www.example.org/videosnapshotqual/q3131"
if ($valStr-ne "")
{ $snapshotlink.'LinkQualifier' += $valStr}
$usedVideoFrame = @{}
$valStr = "25Timecode"
if ($valStr-ne "")
{ $usedVideoFrame.'TimeFormat#' = $valStr}
$valStr = "00:03:25:03"
if ($valStr-ne "")
{ $usedVideoFrame.'TimeValue' = $valStr}
$snapshotlink.'UsedVideoFrame' = $usedVideoFrame

$vmd.'XMP-iptcExt:Snapshot' += $snapshotlink

# VMDp VideoShotType
$vmd.'XMP-iptcExt:VideoShotType' = @()
$propObject = @{}
$valStr = "VideoShotType Id 1 "
if ($valStr -ne "")
{ $propObject.'Identifier' = $valStr}
$valStr = "VideoShotType Name 1 "
if ($valStr -ne "")
{ $propObject.'Name' = $valStr}
$vmd.'XMP-iptcExt:VideoShotType' += $propObject

# VMDp EventExt
$vmd.'XMP-iptcExt:ShownEvent' = @()
$propObject = @{}
$valStr = "EventExt Id 1 "
if ($valStr -ne "")
{ $propObject.'Identifier' = $valStr}
$valStr = "EventExt Name 1 "
if ($valStr -ne "")
{ $propObject.'Name' = $valStr}
$vmd.'XMP-iptcExt:ShownEvent' += $propObject

# VMDp videoPixelAspectRatio
$valStr = "16/9"
if ($valStr-ne "")
{ $vmd.'XMP-xmpDM:videoPixelAspectRatio' = $valStr }

# VMDp videoFieldOrder
$valStr = "progressive"
if ($valStr-ne "")
{ $vmd.'XMP-xmpDM:videoFieldOrder#' = $valStr }

# VMDp StorylineIdentifier
$vmd.'XMP-iptcExt:StorylineIdentifier' = @()
$valStr = "Storyline Id 1"
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:StorylineIdentifier' += $valStr }
$valStr = "Storyline Id 2"
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:StorylineIdentifier' += $valStr }

# VMDp StreamReady
$valStr = "unknown"
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:StreamReady#' = $valStr }

# VMDp StylePeriod
$valStr = "Style Period "
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:StylePeriod' = $valStr }

# VMDp Image Supplier
$vmd.'XMP-plus:ImageSupplier' = @()
$propObject = @{}
$valStr = "Image Supplier Id "
if ($valStr -ne "")
{ $propObject.'ImageSupplierID' = $valStr}
$valStr = "Image Supplier Name "
if ($valStr -ne "")
{ $propObject.'ImageSupplierName' = $valStr}
$vmd.'XMP-plus:ImageSupplier' += $propObject

# VMDp SupplyChainSource
$vmd.'XMP-iptcExt:SupplyChainSource' = @()
$propObject = @{}
$valStr = "SupplyChainSource Id 1 "
if ($valStr -ne "")
{ $propObject.'Identifier' = $valStr}
$valStr = "SupplyChainSource Name 1 "
if ($valStr -ne "")
{ $propObject.'Name' = $valStr}
$vmd.'XMP-iptcExt:SupplyChainSource' += $propObject

# VMDp TemporalCoverage
$propObject = @{}
$valStr = "2016-10-25T00:00:00+00:00"
$valStrDate = $valStr.Substring(0,10).Replace("-",":")
$ValStrTime = $valStr.Substring(11)
if ($valStr -ne "")
{ $propObject.'tempCoverageFrom' = $valStrDate + " " + $ValStrTime }
$valStr = "2016-10-25T23:59:59+00:00"
$valStrDate = $valStr.Substring(0,10).Replace("-",":")
$ValStrTime = $valStr.Substring(11)
if ($valStr -ne "")
{ $propObject.'tempCoverageTo' = $valStrDate + " " + $ValStrTime }
$vmd.'XMP-iptcExt:TemporalCoverage' += $propObject

# VMDp Title
$valStr = "The Title "
if ($valStr-ne "")
{ $vmd.'XMP-dc:Title' = $valStr }

# VMDp Transcript
$valStr = "Transcript "
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:Transcript' = $valStr }

# VMDp TranscriptLink
$vmd.'XMP-iptcExt:TranscriptLink' = @()
$propObject = @{}
$valStr = "http://example.com/transcripts/test0102"
if ($valStr-ne "")
{ $propObject.'Link' += $valStr }
$valStr = "http://example.com/linkqualifier/test0102"
if ($valStr-ne "")
{ $propObject.'LinkQualifier' += $valStr }
$vmd.'XMP-iptcExt:TranscriptLink' += $propObject

# VMDp videoBitRate
$valStr = "20170000"
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:VideoBitRate' = $valStr }

# VMDp videoBitRateMode
$valStr = "variable"
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:VideoBitRateMode#' = $valStr }

# VMDp videoCompressor
$valStr = "H264"
if ($valStr-ne "")
{ $vmd.'XMP-xmpDM:VideoCompressor' = $valStr }

# VMDp videoFrameRate
$valStr = "60"
if ($valStr-ne "")
{ $vmd.'XMP-xmpDM:VideoFrameRate' = $valStr }

# VMDp Video identifier
$valStr = "Video identifier "
if ($valStr-ne "")
{ $vmd.'XMP-dc:Identifier' = $valStr }

# VMDp videoEncodingProfile
$valStr = "videoEncodingProfile "
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:VideoEncodingProfile' = $valStr }

# VMDp RenditionClass
$valStr = "RenditionClass "
if ($valStr-ne "")
{ $vmd.'XMP-xmpMM:RenditionClass' = $valStr }

# VMDp videoStreamsCount
$valStr = "2"
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:VideoStreamsCount' = $valStr }

# VMDp VersionID
$valStr = "VersionID "
if ($valStr-ne "")
{ $vmd.'XMP-xmpMM:VersionID' = $valStr }

# VMDp VisualColour
$valStr = "colour"
if ($valStr-ne "")
{ $vmd.'XMP-iptcExt:VisualColor#' = $valStr }

# VMDp WorkflowTag
$vmd.'XMP-iptcExt:WorkflowTag' = @()
$propObject = @{}
$valStr = "http://example.com/cv/wflowtag/test0102/code987"
if ($valStr-ne "")
{ $propObject.'CvTermId' += $valStr }
$valStr = "CV-Term Name 1 "
if ($valStr-ne "")
{ $propObject.'CvTermName' += $valStr }
$valStr = "http://example.com/cv/wflowtag/test0102"
if ($valStr-ne "")
{ $propObject.'CvId' += $valStr }
$valStr = "http://example.com/cv/refinements2/test0102/codeX145"
if ($valStr-ne "")
{ $propObject.'CvTermRefinedAbout' += $valStr }
$vmd.'XMP-iptcExt:WorkflowTag' += $propObject

# ************ Part Metadata

# VMDp Pantry
$vmd.'XMP-xmpMM:Pantry' = @()
$propObject = @{}
$propObject.'InstanceID' = "instanceId01"
$propObject.'XMP-dc:Description' = "Description of Clip 1"
$propObject.'XMP-dc:Rights' = "Copyright 2014 Video Footage Ltd."
$vmd.'XMP-xmpMM:Pantry' += $propObject
$propObject = @{}
$propObject.'InstanceID' = "instanceId02"
$propObject.'XMP-dc:Description' = "Description of Clip 2"
$propObject.'XMP-dc:Rights' = "Copyright 2015 Video Clips Inc."
$vmd.'XMP-xmpMM:Pantry' += $propObject

# VMDp Ingredients
$vmd.'XMP-xmpMM:Ingredients' = @()
$propObject = @{}
$propObject.'DocumentID' = "instanceId01"
$propObject.'FromPart' = "/time:1f25r589f25"
$propObject.'ToPart' = "/time:273f25r862f25"
$vmd.'XMP-xmpMM:Ingredients' += $propObject
$propObject = @{}
$propObject.'FromPart' = "/time:347f25r899f25"
$propObject.'ToPart' = "/time:1082f25r1634f25"
$propObject.'DocumentID' = "instanceId02"
$vmd.'XMP-xmpMM:Ingredients' += $propObject


# ***********************************
# ***** Wrap the VMD object and export it into a JSON file
$wrapper = @() # exiftool-JSON could include multiple PMD objects!
$vmds = $vmd | Sort-Object
$wrapper += $vmds # add this one

$jsonstr1 = ConvertTo-Json $wrapper -Depth 5 
$jsonstr1
$jsonstr1 | Set-Content -Encoding UTF8 -Path $jsonOutputFp
