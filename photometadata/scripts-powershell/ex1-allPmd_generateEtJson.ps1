<#
    IPTC Photo Metadata - script to create a JSON file for Exiftool 
    with all properties of the IPTC Photo Metadata Standard 2017.1 populated
#>

# ********** Intro ********************************************************
# ***** Parameters
$jsonOutputFp = "ex1-allPmd_etData.json" # JSON output file path

[string]$valStr = "" # string representation of the property value
[int]$valInt = -1 # integer representation of the property value

$pmd = [ordered]@{} # initialize the Photo Metadata object 
$pmd.SourceFile = "*" # = can be applied to an image with any file name

# ********** Creating a photo metadata object ******************************

# ***********************************
# ***** Rights related properties

# PMDp Creator
$valStr = "Creator1 "
if ($valStr-ne "")
{
$pmd.'IFD0:Artist' = $valStr
$pmd.'IPTC:By-line' = $valStr
$pmd.'XMP-dc:Creator' = @()
$pmd.'XMP-dc:Creator' += $valStr
$valStr = "Creator2 "
if ($valStr-ne "")
{
$pmd.'XMP-dc:Creator' += $valStr
}
}

# PMDp Image Creator
$pmd.'XMP-plus:ImageCreator' = @()
$imageCreator = @{}
$valStr = "Image Creator Id 1 "
if ($valStr -ne "")
{ $imageCreator.'ImageCreatorID' = $valStr}
$valStr = "Image Creator Name 1 "
if ($valStr -ne "")
{ $imageCreator.'ImageCreatorName' = $valStr}
$pmd.'XMP-plus:ImageCreator' += $imageCreator

$imageCreator = @{}
$valStr = "Image Creator Id 2 "
if ($valStr -ne "")
{ $imageCreator.'ImageCreatorID' = $valStr}
$valStr = "Image Creator Name 2 "
if ($valStr -ne "")
{ $imageCreator.'ImageCreatorName' = $valStr}
$pmd.'XMP-plus:ImageCreator' += $imageCreator


# PMDp Creator's Job Title
$valStr = "Creator's Job Title  "
if ($valStr-ne "")
{
$pmd.'IPTC:By-lineTitle' = $valStr
$pmd.'XMP-photoshop:AuthorsPosition' = $valStr
}

# PMDp Creator's Contact Info
$pmd.'XMP-iptcCore:CreatorContactInfo' = @{}
$valStr = "Creator's CI: City "
if ($valStr-ne "")
{ $pmd.'XMP-iptcCore:CreatorContactInfo'.CiAdrCity = $valStr }
$valStr = "Creator's CI: Country "
if ($valStr-ne "")
{ $pmd.'XMP-iptcCore:CreatorContactInfo'.CiAdrCtry= $valStr }
$valStr = "Creator's CI: Address, line 1 "
if ($valStr-ne "")
{ $pmd.'XMP-iptcCore:CreatorContactInfo'.CiAdrExtadr = $valStr }
$valStr = "Creator's CI: Postcode "
if ($valStr-ne "")
{ $pmd.'XMP-iptcCore:CreatorContactInfo'.CiAdrPcode = $valStr }
$valStr = "Creator's CI: State/Province "
if ($valStr-ne "")
{ $pmd.'XMP-iptcCore:CreatorContactInfo'.CiAdrRegion = $valStr }
$valStr = "Creator's CI: Email@1, Email@2 "
if ($valStr-ne "")
{ $pmd.'XMP-iptcCore:CreatorContactInfo'.CiEmailWork = $valStr }
$valStr = "Creator's CI: Phone # 1, Phone # 2 "
if ($valStr-ne "")
{ $pmd.'XMP-iptcCore:CreatorContactInfo'.CiTelWork = $valStr }
$valStr = "http://www.Creators.CI/WebAddress/test2018a"
if ($valStr-ne "")
{ $pmd.'XMP-iptcCore:CreatorContactInfo'.CiUrlWork = $valStr }

# PMDp Copyright Notice
$valStr = "Copyright (Notice) 2017.1 IPTC - www.iptc.org  "
if ($valStr-ne "")
{
$pmd.'IFD0:Copyright' = $valStr
$pmd.'IPTC:CopyrightNotice' = $valStr
$pmd.'XMP-dc:Rights' = $valStr
}

# PMDp Copyright Owner
$pmd.'XMP-plus:CopyrightOwner' = @()
$copyrightOwner = @{}
$valStr = "Copyright Owner Id 1 "
if ($valStr -ne "")
{ $copyrightOwner.'CopyrightOwnerID' = $valStr}
$valStr = "Copyright Owner Name 1 "
if ($valStr -ne "")
{ $copyrightOwner.'CopyrightOwnerName' = $valStr}
$pmd.'XMP-plus:CopyrightOwner' += $copyrightOwner

$copyrightOwner = @{}
$valStr = "Copyright Owner Id 2 "
if ($valStr -ne "")
{ $copyrightOwner.'CopyrightOwnerID' = $valStr}
$valStr = "Copyright Owner Name 2 "
if ($valStr -ne "")
{ $copyrightOwner.'CopyrightOwnerName' = $valStr}
$pmd.'XMP-plus:CopyrightOwner' += $copyrightOwner

# PMDp Licensor 
$pmd.'XMP-plus:Licensor' = @()
$licensor = @{}
$valStr = "Licensor ID 1 "
if ($valStr -ne "")
{ $licensor.'LicensorID' = $valStr}
$valStr = "Licensor Name 1 "
if ($valStr -ne "")
{ $licensor.'LicensorName' = $valStr}
$valStr = "Licensor Street Addr 1 "
if ($valStr -ne "")
{ $licensor.'LicensorStreetAddress' = $valStr}
$valStr = "Licensor Ext Addr 1 "
if ($valStr -ne "")
{ $licensor.'LicensorExtendedAddress' = $valStr}
$valStr = "Licensor City 1 "
if ($valStr -ne "")
{ $licensor.'LicensorCity' = $valStr}
$valStr = "Licensor Region 1 "
if ($valStr -ne "")
{ $licensor.'LicensorRegion' = $valStr}
$valStr = "Licensor Country 1 "
if ($valStr -ne "")
{ $licensor.'LicensorCountry' = $valStr}
$valStr = "Licensor Postcode 1 "
if ($valStr -ne "")
{ $licensor.'LicensorPostalCode' = $valStr}
$valStr = "Licensor Phone1 1 "
if ($valStr -ne "")
{ $licensor.'LicensorTelephone1' = $valStr}
$valStr = "Licensor Phone2 1 "
if ($valStr -ne "")
{ $licensor.'LicensorTelephone2' = $valStr}
$valStr = "Licensor Email 1 "
if ($valStr -ne "")
{ $licensor.'LicensorEmail' = $valStr}
$valStr = "Licensor URL 1 "
if ($valStr -ne "")
{ $licensor.'LicensorURL' = $valStr}
$pmd.'XMP-plus:Licensor' += $licensor

$licensor = @{}
$valStr = "Licensor ID 2 "
if ($valStr -ne "")
{ $licensor.'LicensorID' = $valStr}
$valStr = "Licensor Name 2 "
if ($valStr -ne "")
{ $licensor.'LicensorName' = $valStr}
$valStr = "Licensor Street Addr 2 "
if ($valStr -ne "")
{ $licensor.'LicensorStreetAddress' = $valStr}
$valStr = "Licensor Ext Addr 2 "
if ($valStr -ne "")
{ $licensor.'LicensorExtendedAddress' = $valStr}
$valStr = "Licensor City 2 "
if ($valStr -ne "")
{ $licensor.'LicensorCity' = $valStr}
$valStr = "Licensor Region 2 "
if ($valStr -ne "")
{ $licensor.'LicensorRegion' = $valStr}
$valStr = "Licensor Country 2 "
if ($valStr -ne "")
{ $licensor.'LicensorCountry' = $valStr}
$valStr = "Licensor Postcode 2 "
if ($valStr -ne "")
{ $licensor.'LicensorPostalCode' = $valStr}
$valStr = "Licensor Phone1 2 "
if ($valStr -ne "")
{ $licensor.'LicensorTelephone1' = $valStr}
$valStr = "Licensor Phone2 2 "
if ($valStr -ne "")
{ $licensor.'LicensorTelephone2' = $valStr}
$valStr = "Licensor Email 2 "
if ($valStr -ne "")
{ $licensor.'LicensorEmail' = $valStr}
$valStr = "Licensor URL 2 "
if ($valStr -ne "")
{ $licensor.'LicensorURL' = $valStr}
$pmd.'XMP-plus:Licensor' += $licensor

# PMDp Web Statement of Rights (new 2017.1)
$valStr = "http://www.WebStatementOfRights.org/2017.1"
if ($valStr-ne "")
{ $pmd.'XMP-xmpRights:WebStatement' = $valStr }

# PMDp Rights Usage Terms
$valStr = "Rights Usage Termns "
if ($valStr-ne "")
{ $pmd.'XMP-xmpRights:UsageTerms' += $valStr }

# PMDp Source
$valStr = "Source "
if ($valStr-ne "")
{
$pmd.'IPTC:Source' = $valStr
$pmd.'XMP-photoshop:Source' = $valStr
}

# PMDp Credit Line
$valStr = "Credit Line "
if ($valStr-ne "")
{
$pmd.'IPTC:Credit' = $valStr
$pmd.'XMP-photoshop:Credit' = $valStr
}

# ***********************************
# ***** Encoded Rights Expressions (new 2014)

# PMDp Embedded Encoded Rights Expression (new 2014)
$pmd.'XMP-iptcExt:EmbdEncRightsExpr' = @()

$eere = @{}
$valStr = "The Encoded Rights Expression "
if ($valStr -ne "")
{ $eere.'EncRightsExpr' = $valStr
$valStr = "IANA Media Type of ERE "
if ($valStr -ne "")
{ $eere.'RightsExprEncType' = $valStr }
$valStr = "http://example.org/RELids/id4711/test2018a"
if ($valStr -ne "")
{ $eere.'RightsExprLangId' = $valStr }
}
$pmd.'XMP-iptcExt:EmbdEncRightsExpr' += $eere

# PMDp Linked Encoded Rights Expression (new 2014)
$pmd.'XMP-iptcExt:LinkedEncRightsExpr' = @()

$lere = @{}
$valStr = "http://example.org/linkedrightsexpression/id986/test2018a"
if ($valStr -ne "")
{ $lere.'LinkedRightsExpr' = $valStr
$valStr = "IANA Media Type of ERE "
if ($valStr -ne "")
{ $lere.'RightsExprEncType' = $valStr }
$valStr = "http://example.org/RELids/id4712/test2018a"
if ($valStr -ne "")
{ $lere.'RightsExprLangId' = $valStr }
}
$pmd.'XMP-iptcExt:LinkedEncRightsExpr' += $lere

# ***********************************
# ***** General description of the visual content 

# PMDp Headline
$valStr = "The Headline "
# $valStr = ""
if ($valStr-ne "")
{
$pmd.'IPTC:Headline' = $valStr
$pmd.'XMP-photoshop:Headline' = $valStr
}

# PMDp Description
$valStr = "The description aka caption "
# $valStr = ""
if ($valStr-ne "")
{
$pmd.'EXIF:ImageDescription' = $valStr
$pmd.'IPTC:Caption-Abstract' = $valStr
$pmd.'XMP-dc:Description' = $valStr
}

# PMDp Description Writer
$valStr = "Description Writer "
if ($valStr-ne "")
{
$pmd.'IPTC:Writer-Editor' = $valStr
$pmd.'XMP-photoshop:CaptionWriter' = $valStr
}

# PMDp Keyword(s)
$pmd.'IPTC:Keywords' = @()
$pmd.'XMP-dc:Subject' = @()
$valStr = "Keyword1test2018a"
if ($valStr-ne "")
{ 
$pmd.'IPTC:Keywords' += $valStr
$pmd.'XMP-dc:Subject' += $valStr
}
$valStr = "Keyword2test2018a"
if ($valStr-ne "")
{ 
$pmd.'IPTC:Keywords' += $valStr
$pmd.'XMP-dc:Subject' += $valStr
}
$valStr = "Keyword3test2018a"
if ($valStr-ne "")
{ 
$pmd.'IPTC:Keywords' += $valStr
$pmd.'XMP-dc:Subject' += $valStr
}

# PMDp Genre
$valStr = "A Genre "
if ($valStr-ne "")
{
$pmd.'IPTC:ObjectAttributeReference' = $valStr
$pmd.'XMP-iptcCore:IntellectualGenre' = $valStr
}

# PMDp Subject Code
# ... for IIM
$pmd.'IPTC:SubjectReference' = @()
$valStr = "IPTC:1test2018a"
if ($valStr-ne "")
{ $pmd.'IPTC:SubjectReference' += $valStr}
$valStr = "IPTC:2test2018a"
if ($valStr-ne "")
{ $pmd.'IPTC:SubjectReference' += $valStr}
$valStr = "IPTC:3test2018a"
if ($valStr-ne "")
{ $pmd.'IPTC:SubjectReference' += $valStr}
# ... for XMP
$pmd.'XMP-iptcCore:SubjectCode' = @()
$valStr = "1test2018a"
if ($valStr-ne "")
{ $pmd.'XMP-iptcCore:SubjectCode' += $valStr}
$valStr = "2test2018a"
if ($valStr-ne "")
{ $pmd.'XMP-iptcCore:SubjectCode' += $valStr}
$valStr = "3test2018a"
if ($valStr-ne "")
{ $pmd.'XMP-iptcCore:SubjectCode' += $valStr}


# PMDp Scene Code
$pmd.'XMP-iptcCore:Scene' = @()
$valStr = "IPTC-Scene-Code1 "
$pmd.'XMP-iptcCore:Scene' += $valStr
$valStr = "IPTC-Scene-Code2 "
$pmd.'XMP-iptcCore:Scene' += $valStr

# PMDp Event
$valStr = "An Event "
if ($valStr-ne "")
{ $pmd.'XMP-iptcExt:Event' = $valStr }

# PMDp Name of company featured in the image
$pmd.'XMP-iptcExt:OrganisationInImageName' = @()
$valStr = "Organisation Name 1 "
if ($valStr-ne "")
{ $pmd.'XMP-iptcExt:OrganisationInImageName' += $valStr }
$valStr = "Organisation Name 2 "
if ($valStr-ne "")
{ $pmd.'XMP-iptcExt:OrganisationInImageName' += $valStr }
$valStr = "Organisation Name 3 "
if ($valStr-ne "")
{ $pmd.'XMP-iptcExt:OrganisationInImageName' += $valStr }

# PMDp Code of company featured in the image
$pmd.'XMP-iptcExt:OrganisationInImageCode' = @()
$valStr = "Organisation Code 1 "
if ($valStr-ne "")
{ $pmd.'XMP-iptcExt:OrganisationInImageCode' += $valStr }
$valStr = "Organisation Code 2 "
if ($valStr-ne "")
{ $pmd.'XMP-iptcExt:OrganisationInImageCode' += $valStr }
$valStr = "Organisation Code 3 "
if ($valStr-ne "")
{ $pmd.'XMP-iptcExt:OrganisationInImageCode' += $valStr }

# PMDp CV-Term About Image (new 2014)
$pmd.'XMP-iptcExt:AboutCvTerm' = @()

$cvt = @{}
$valStr = "http://example.com/cv/about/test2018a/code987"
if ($valStr-ne "")
{ $cvt.'CvTermId' += $valStr }
$valStr = "CV-Term Name 1 "
if ($valStr-ne "")
{ $cvt.'CvTermName' += $valStr }
$valStr = "http://example.com/cv/about/test2018a"
if ($valStr-ne "")
{ $cvt.'CvId' += $valStr }
$valStr = "http://example.com/cv/refinements2/test2018a/codeX145"
if ($valStr-ne "")
{ $cvt.'CvTermRefinedAbout' += $valStr }
$pmd.'XMP-iptcExt:AboutCvTerm' += $cvt


# PMDp (generic) Genre (new 2016-10)
$pmd.'XMP-iptcExt:Genre' = @()

$cvt = @{}
$valStr = "http://example.com/cv/genre/test2018a/code1369"
if ($valStr-ne "")
{ $cvt.'CvTermId' += $valStr }
$valStr = "Genre CV-Term Name 1 "
if ($valStr-ne "")
{ $cvt.'CvTermName' += $valStr }
$valStr = "http://example.com/cv/genre/test2018a"
if ($valStr-ne "")
{ $cvt.'CvId' += $valStr }
$valStr = "http://example.com/cv/genrerefinements2/test2018a/codeY864"
if ($valStr-ne "")
{ $cvt.'CvTermRefinedAbout' += $valStr }
$pmd.'XMP-iptcExt:Genre' += $cvt

# PMDp Image Rating (new 2017.1)
$valStr = "1.0"
if ($valStr-ne "")
{ $pmd.'XMP-xmp:Rating' = $valStr }


# ***********************************
# ***** Locations

# *** Flat list from/in IIM

# PMDp (Sub)Location (legacy)
$valStr = "Sublocation (Core) "
if ($valStr-ne "")
{
$pmd.'IPTC:Sub-location' = $valStr
$pmd.'XMP-iptcCore:Location' = $valStr
}

# PMDp City (legacy)
$valStr = "City (Core) "
if ($valStr-ne "")
{
$pmd.'IPTC:City' = $valStr
$pmd.'XMP-photoshop:City' = $valStr
}

# PMDp Province/State (legacy)
$valStr = "Province/State (Core) "
if ($valStr-ne "")
{
$pmd.'IPTC:Province-State' = $valStr
$pmd.'XMP-photoshop:State' = $valStr
}

# PMDp Country (legacy)
$valStr = "Country (Core) "
if ($valStr-ne "")
{
$pmd.'IPTC:Country-PrimaryLocationName' = $valStr
$pmd.'XMP-photoshop:Country' = $valStr
}

# PMDp County Code (legacy)
$valStr = "R17"
if ($valStr-ne "")
{
$pmd.'IPTC:Country-PrimaryLocationCode' = $valStr
$pmd.'XMP-iptcCore:CountryCode' = $valStr
}

# *** Structured properties from IPTC Extension

# PMDp Location Created
$pmd.'XMP-iptcExt:LocationCreated' = @()
$locationCreated = @{}
$valStr = "Sublocation (Location created1) "
if ($valStr-ne "")
{ $locationCreated.'Sublocation' = $valStr }
$valStr = "City (Location created1) "
if ($valStr-ne "")
{ $locationCreated.'City' = $valStr }
$valStr = "Province/State (Location created1) "
if ($valStr-ne "")
{ $locationCreated.'ProvinceState' = $valStr }
$valStr = "CountryName (Location created1) "
if ($valStr-ne "")
{ $locationCreated.'CountryName' = $valStr }
$valStr = "R17"
if ($valStr-ne "")
{ $locationCreated.'CountryCode' = $valStr }
$valStr = "Worldregion (Location created1) "
if ($valStr-ne "")
{ $locationCreated.'WorldRegion' = $valStr }
$valStr = "Location Id (Location created1) "
if ($valStr-ne "")
{ $locationCreated.'LocationId' = $valStr } # new 2014
$pmd.'XMP-iptcExt:LocationCreated'+= $locationCreated


# PMDp Location Shown
$pmd.'XMP-iptcExt:LocationShown' = @()
$locationShown = @{}
$valStr = "Sublocation (Location shown1) "
if ($valStr-ne "")
{ $locationShown.'Sublocation' = $valStr }
$valStr = "City (Location shown1) "
if ($valStr-ne "")
{ $locationShown.'City' = $valStr }
$valStr = "Province/State (Location shown1) "
if ($valStr-ne "")
{ $locationShown.'ProvinceState' = $valStr }
$valStr = "CountryName (Location shown1) "
if ($valStr-ne "")
{ $locationShown.'CountryName' = $valStr }
$valStr = "R17"
if ($valStr-ne "")
{ $locationShown.'CountryCode' = $valStr }
$valStr = "Worldregion (Location shown1) "
if ($valStr-ne "")
{ $locationShown.'WorldRegion' = $valStr }
$locationShown.'LocationId' = @()
$valStr = "Location Id 1a(Location shown1) "
if ($valStr-ne "")
{ $locationShown.'LocationId' += $valStr }
$valStr = "Location Id 1b(Location shown1) "
if ($valStr-ne "")
{ $locationShown.'LocationId' += $valStr } # new 2014
$pmd.'XMP-iptcExt:LocationShown'+= $locationShown

$locationShown = @{}
$valStr = "Sublocation (Location shown2) "
if ($valStr-ne "")
{ $locationShown.'Sublocation' = $valStr }
$valStr = "City (Location shown2) "
if ($valStr-ne "")
{ $locationShown.'City' = $valStr }
$valStr = "Province/State (Location shown2) "
if ($valStr-ne "")
{ $locationShown.'ProvinceState' = $valStr }
$valStr = "CountryName (Location shown2) "
if ($valStr-ne "")
{ $locationShown.'CountryName' = $valStr }
$valStr = "R17"
if ($valStr-ne "")
{ $locationShown.'CountryCode' = $valStr }
$valStr = "Worldregion (Location shown2) "
if ($valStr-ne "")
{ $locationShown.'WorldRegion' = $valStr }
$valStr = "Location Id (Location shown2) "
if ($valStr-ne "")
{ $locationShown.'LocationId' = $valStr }
$locationShown.'LocationId' = @()
$valStr = "Location Id 2a(Location shown2) "
if ($valStr-ne "")
{ $locationShown.'LocationId' += $valStr }
$valStr = "Location Id 2b(Location shown2) "
if ($valStr-ne "")
{ $locationShown.'LocationId' += $valStr } # new 2014
$pmd.'XMP-iptcExt:LocationShown'+= $locationShown



# ***********************************
# ***** Persons

# PMDp (Name of) Person Shown in the Image
$pmd.'XMP-iptcExt:PersonInImage' = @()
$valStr = "Person Shown 1 "
if ($valStr-ne "")
{ $pmd.'XMP-iptcExt:PersonInImage' += $valStr}
$valStr = "Person Shown 2 "
if ($valStr-ne "")
{ $pmd.'XMP-iptcExt:PersonInImage' += $valStr}

# PMDp Person Shown in the Image with Details (new 2014)
$pmd.'XMP-iptcExt:PersonInImageWDetails' = @()

$pers = @{}
$valStr = "Person Name 1 "
if ($valStr-ne "")
{ $pers.'PersonName' = $valStr}
$pers.'PersonId' = @()
$valStr = "http://wikidata.org/item/Q123456789/test2018a"
if ($valStr-ne "")
{ $pers.'PersonId' += $valStr}
$valStr = "http://freebase.com/m/987654321/test2018a"
if ($valStr-ne "")
{ $pers.'PersonId' += $valStr}
$valStr = "Person Description 1 "
if ($valStr-ne "")
{ $pers.'PersonDescription' += $valStr}

$pers.'PersonCharacteristic' = @()
$perschar = @{}
$valStr = "http://example.com/cv/test99/code987/test2018a"
if ($valStr-ne "")
{ $perschar.'CvTermId' += $valStr }
$valStr = "Person Characteristic Name 1 "
if ($valStr-ne "")
{ $perschar.'CvTermName' += $valStr }
$valStr = "http://example.com/cv/test99/test2018a"
if ($valStr-ne "")
{ $perschar.'CvId' += $valStr }
$valStr = "http://example.com/cv/refinements987/codeY765/test2018a"
if ($valStr-ne "")
{ $perschar.'CvTermRefinedAbout' += $valStr }
$pers.'PersonCharacteristic' += $perschar

$pmd.'XMP-iptcExt:PersonInImageWDetails' += $pers


# ***********************************
# ***** Model related properties

# PMDp Additional Model Info
$valStr = "Additional Model Info "
if ($valStr-ne "")
{ $pmd.'XMP-iptcExt:AdditionalModelInformation' = $valStr }

# PMDp Model Age
$pmd.'XMP-iptcExt:ModelAge' = @()
$valInt = 25
$pmd.'XMP-iptcExt:ModelAge' += $valInt
$valInt = 27
$pmd.'XMP-iptcExt:ModelAge' += $valInt
$valInt = 30
$pmd.'XMP-iptcExt:ModelAge' += $valInt

# PMDp Minor Model Age Disclosure
$valStr = "Age 25 or Over"
if ($valStr-ne "")
{ $pmd.'XMP-plus:MinorModelAgeDisclosure' = $valStr }

# PMDp Model Release Id
$pmd.'XMP-plus:ModelReleaseID' = @()
$valStr = "Model Release ID 1 "
if ($valStr-ne "")
{ $pmd.'XMP-plus:ModelReleaseID' += $valStr}
$valStr = "Model Release ID 2 "
if ($valStr-ne "")
{ $pmd.'XMP-plus:ModelReleaseID' += $valStr}

# PMDp Model Release Status
$valStr = "Not Applicable"
if ($valStr-ne "")
{ $pmd.'XMP-plus:ModelReleaseStatus' = $valStr }

# ***********************************
# ***** Property related properties

# PMDp Property Release Id
$pmd.'XMP-plus:PropertyReleaseID' = @()
$valStr = "Property Release ID 1 "
if ($valStr-ne "")
{ $pmd.'XMP-plus:PropertyReleaseID' += $valStr }
$valStr = "Property Release ID 2 "
if ($valStr-ne "")
{ $pmd.'XMP-plus:PropertyReleaseID' += $valStr }

# PMDp Property Release Status
$valStr = "Not Applicable"
if ($valStr-ne "")
{ $pmd.'XMP-plus:PropertyReleaseStatus' = $valStr }

# ***********************************
# ***** Product shown in the Image (new 2014)
$pmd.'XMP-iptcExt:ProductInImage' = @()
$prod = @{}
$valStr = "123456782017.1"
if ($valStr-ne "")
{ $prod.'ProductGTIN' = $valStr }
$valStr = "Product Name 1 "
if ($valStr-ne "")
{ $prod.'ProductName' = $valStr }
$valStr = "Product Description 1 "
if ($valStr-ne "")
{ $prod.'ProductDescription' = $valStr }
$pmd.'XMP-iptcExt:ProductInImage' += $prod

# ***********************************
# ***** Administrative properties

# PMDp Title
$valStr = "The Title "
if ($valStr-ne "")
{
$pmd.'IPTC:ObjectName' = $valStr
$pmd.'XMP-dc:Title' = $valStr
}

# PMDp Date (and Time) Created
$valStr = "2017-07-13T17:01:00+00:00"
$valStrDate = $valStr.Substring(0,10).Replace("-",":")
$ValStrTime = $valStr.Substring(11)
if ($valStrDate-ne "")
{ $pmd.'IPTC:DateCreated' = $valStrDate }
if ($ValStrTime-ne "")
{ $pmd.'IPTC:TimeCreated' = $ValStrTime}
if ($valStr-ne "")
{ $pmd.'XMP-photoshop:DateCreated' = $valStrDate + " " + $ValStrTime }

# PMDp Instructions
$valStr = "An Instruction "
if ($valStr-ne "")
{
$pmd.'IPTC:SpecialInstructions' = $valStr
$pmd.'XMP-photoshop:Instructions' = $valStr
}

# PMDp Job Id
$valStr = "Job Id "
if ($valStr-ne "")
{
$pmd.'IPTC:OriginalTransmissionReference' = $valStr
$pmd.'XMP-photoshop:TransmissionReference' = $valStr
}

# PMDp Digital Image GUID
$valStr = "http://example.com/imageGUIDs/TestGUID12345/test2018a"
if ($valStr-ne "")
{ $pmd.'XMP-iptcExt:DigitalImageGUID' = $valStr }

# PMDp Digital Source Type
# Implementation Note: valStr is taken from an IPTC controlled vocabulary
#   find all values at: http://cv.iptc.org/newscodes/digitalsourcetype/
$valStr = "http://cv.iptc.org/newscodes/digitalsourcetype/softwareImage"
if ($valStr-ne "")
{ $pmd.'XMP-iptcExt:DigitalSourceType' = $valStr }

# PMDp Max Available Width/Height
$valInt = 20
$pmd.'XMP-iptcExt:MaxAvailWidth' = $valInt
$valInt = 14
$pmd.'XMP-iptcExt:MaxAvailHeight' = $valInt

# PMDp Image Supplier
$pmd.'XMP-plus:ImageSupplier' = @()
$imageSupplier = @{}
$valStr = "Image Supplier Id "
if ($valStr -ne "")
{ $imageSupplier.'ImageSupplierID' = $valStr}
$valStr = "Image Supplier Name "
if ($valStr -ne "")
{ $imageSupplier.'ImageSupplierName' = $valStr}
$pmd.'XMP-plus:ImageSupplier' += $imageSupplier

# PMDp Image Supplier('s) Image Id
$valStr = "Image Supplier Image ID "
if ($valStr-ne "")
{ $pmd.'XMP-plus:ImageSupplierImageID' = $valStr }

# PMDp Image Creator('s) Image Id (corrected, does not exist in IPTC PMD - 2018-08-15)
# $valStr = "Image Creator Image ID "
# if ($valStr-ne "")
# { $pmd.'XMP-plus:ImageCreatorImageID' = $valStr }

# PMDp Image Registry Entry
# Implementation note: only an entry with organisation *and* ItemId makes sense
$pmd.'XMP-iptcExt:RegistryID' = @()
$registryEntry = @{}
$valStr = "Registry Organisation ID 1 "
if ($valStr-ne "")
{
$registryEntry.'RegOrgId' = $valStr
$valStr = "Registry Image ID 1 "
if ($valStr-ne "")
{ 
$registryEntry.'RegItemId' = $valStr
}
$valStr = "Registry Entry Role ID 1 "
if ($valStr-ne "")
{ 
$registryEntry.'RegEntryRole' = $valStr
}
$pmd.'XMP-iptcExt:RegistryID' += $registryEntry
}

$registryEntry = @{}
$valStr = "Registry Organisation ID 2 "
if ($valStr-ne "")
{
$registryEntry.'RegOrgId' = $valStr
$valStr = "Registry Image ID 2 "
if ($valStr-ne "")
{ 
$registryEntry.'RegItemId' = $valStr
}
$valStr = "Registry Entry Role ID 2 "
if ($valStr-ne "")
{ 
$registryEntry.'RegEntryRole' = $valStr
}
$pmd.'XMP-iptcExt:RegistryID' += $registryEntry
}



# ***********************************
# ***** Properties about Artwork or (copyrighted) Object shown in the Image
# Be aware: that is metadata about an artwork or copyrighted object
#    shown in the image and *not* about the image itself

$pmd.'XMP-iptcExt:ArtworkOrObject' = @()

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

# below: AO properties new/added in 2014

# Implementation note: the Creator Names (above) and
#   the Creator Ids (below) *must* be in the same sequence
#   if a creator has no Id add a single space
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

# finally: add the new Artwork/Object object to the PMD
$pmd.'XMP-iptcExt:ArtworkOrObject' += $ao


# ***********************************
# ***** Wrap the PMD object and export it into a JSON file
$wrapper = @() # exiftool-JSON could include multiple PMD objects!
$pmds = $pmd | sort
$wrapper += $pmds # add this one

$jsonstr1 = ConvertTo-Json $wrapper -Depth 5 
$jsonstr1
$jsonstr1 | Set-Content -Encoding UTF8 -Path $jsonOutputFp

