#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import yaml


jsonOutputFp = "IPTC-VMHub-etData-1.json"

def generate_IPTCVMD_etJSON():
    print("START")
    ivmdpropvalYamlfile = open('IptcVMHpropValues.yml', 'r', encoding="utf-8")
    ivmdpval = yaml.load(ivmdpropvalYamlfile)
    print(ivmdpval)

    # INSERT raw code

    # !!! Insert this code into a function generating IPTC VMHub using Exiftool JSON - THIS IS RAW CODE

    vmd = {}
    vmd['Sourcefile'] = '*'

    # VMHub property (administrative) Circa Date Created
    valstr = ivmdpval['XMP-iptcExt:CircaDateCreated']
    if valstr != '':
        vmd['XMP-iptcExt:CircaDateCreated'] = valstr

    # VMHub property (administrative) Date Created
    valstr = ivmdpval['XMP-photoshop:DateCreated']
    if valstr != '':
        vmd['XMP-photoshop:DateCreated'] = valstr

    # VMHub property (administrative) Date Modified
    valstr = ivmdpval['XMP-xmp:ModifyDate']
    if valstr != '':
        vmd['XMP-xmp:ModifyDate'] = valstr

    # VMHub property (administrative) Date Released
    valstr = ivmdpval['XMP-xmpDM:ReleaseDate']
    if valstr != '':
        vmd['XMP-xmpDM:ReleaseDate'] = valstr

    # VMHub property (administrative) Episode
    # * STRUCTURE EpisodeSeason: arrayround = 0 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:Episode.Name'] + ' -  value'
    if valstr != '':
        valobj1['Name'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Episode.Number'] + ' -  value'
    if valstr != '':
        valobj1['Number'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Episode.Identifier'] + ' -  value'
    if valstr != '':
        valobj1['Identifier'] = valstr
    # STRUCTURE END EpisodeSeason: arrayround = 0 - recursion = 1
    vmd['XMP-iptcExt:Episode'] = valobj1

    # VMHub property (administrative) External Metadata URL
    vallist = []
    valstr = ivmdpval['XMP-iptcExt:ExternalMetadataLink'] + ' - value 1'
    if valstr != '':
        vallist.append(valstr)
    valstr = ivmdpval['XMP-iptcExt:ExternalMetadataLink'] + ' value 2'
    if valstr != '':
        vallist.append(valstr)
    vmd['XMP-iptcExt:ExternalMetadataLink'] = vallist

    # VMHub property (administrative) Feed Identifier
    valstr = ivmdpval['XMP-iptcExt:FeedIdentifier']
    if valstr != '':
        vmd['XMP-iptcExt:FeedIdentifier'] = valstr

    # VMHub property (administrative) Publication Event
    # * STRUCTURE PublicationEvent: arrayround = 0 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:PublicationEvent.Date']
    if valstr != '':
        valobj1['Date'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PublicationEvent.Name'] + ' -  value'
    if valstr != '':
        valobj1['Name'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PublicationEvent.Identifier'] + ' -  value'
    if valstr != '':
        valobj1['Identifier'] = valstr
    # STRUCTURE END PublicationEvent: arrayround = 0 - recursion = 1
    vmd['XMP-iptcExt:PublicationEvent'] = valobj1

    # VMHub property (administrative) Rating
    vallist = []
    # * STRUCTURE Rating: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingValue'] + ' -  value [1]'
    if valstr != '':
        valobj1['RatingValue'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingSourceLink'] + ' -  value [1]'
    if valstr != '':
        valobj1['RatingSourceLink'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingScaleMinValue'] + ' -  value [1]'
    if valstr != '':
        valobj1['RatingScaleMinValue'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingScaleMaxValue'] + ' -  value [1]'
    if valstr != '':
        valobj1['RatingScaleMaxValue'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingValueLogoLink'] + ' -  value [1]'
    if valstr != '':
        valobj1['RatingValueLogoLink'] = valstr
    vallist1 = []
    # * STRUCTURE LocationDetails: arrayround = 1 - recursion = 2
    valobj2 = {}
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.LocationId'] + ' -  value [1]'
    if valstr != '':
        valobj2['LocationId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.Name'] + ' -  value [1]'
    if valstr != '':
        valobj2['Name'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.Sublocation'] + ' -  value [1]'
    if valstr != '':
        valobj2['Sublocation'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.City'] + ' -  value [1]'
    if valstr != '':
        valobj2['City'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.ProvinceState'] + ' -  value [1]'
    if valstr != '':
        valobj2['ProvinceState'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.CountryName'] + ' -  value [1]'
    if valstr != '':
        valobj2['CountryName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.CountryCode'] + ' -  value [1]'
    if valstr != '':
        valobj2['CountryCode'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.WorldRegion'] + ' -  value [1]'
    if valstr != '':
        valobj2['WorldRegion'] = valstr
    # STRUCTURE END LocationDetails: arrayround = 1 - recursion = 2
    vallist1.append(valobj2)
    # * STRUCTURE LocationDetails: arrayround = 2 - recursion = 2
    valobj2 = {}
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.LocationId'] + ' -  value [2]'
    if valstr != '':
        valobj2['LocationId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.Name'] + ' -  value [2]'
    if valstr != '':
        valobj2['Name'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.Sublocation'] + ' -  value [2]'
    if valstr != '':
        valobj2['Sublocation'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.City'] + ' -  value [2]'
    if valstr != '':
        valobj2['City'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.ProvinceState'] + ' -  value [2]'
    if valstr != '':
        valobj2['ProvinceState'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.CountryName'] + ' -  value [2]'
    if valstr != '':
        valobj2['CountryName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.CountryCode'] + ' -  value [2]'
    if valstr != '':
        valobj2['CountryCode'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.WorldRegion'] + ' -  value [2]'
    if valstr != '':
        valobj2['WorldRegion'] = valstr
    # STRUCTURE END LocationDetails: arrayround = 2 - recursion = 2
    vallist1.append(valobj2)
    valobj1['RatingRegion'] = vallist1
    # STRUCTURE END Rating: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE Rating: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingValue'] + ' -  value [2]'
    if valstr != '':
        valobj1['RatingValue'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingSourceLink'] + ' -  value [2]'
    if valstr != '':
        valobj1['RatingSourceLink'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingScaleMinValue'] + ' -  value [2]'
    if valstr != '':
        valobj1['RatingScaleMinValue'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingScaleMaxValue'] + ' -  value [2]'
    if valstr != '':
        valobj1['RatingScaleMaxValue'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingValueLogoLink'] + ' -  value [2]'
    if valstr != '':
        valobj1['RatingValueLogoLink'] = valstr
    vallist1 = []
    # * STRUCTURE LocationDetails: arrayround = 1 - recursion = 2
    valobj2 = {}
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.LocationId'] + ' -  value [1]'
    if valstr != '':
        valobj2['LocationId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.Name'] + ' -  value [1]'
    if valstr != '':
        valobj2['Name'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.Sublocation'] + ' -  value [1]'
    if valstr != '':
        valobj2['Sublocation'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.City'] + ' -  value [1]'
    if valstr != '':
        valobj2['City'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.ProvinceState'] + ' -  value [1]'
    if valstr != '':
        valobj2['ProvinceState'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.CountryName'] + ' -  value [1]'
    if valstr != '':
        valobj2['CountryName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.CountryCode'] + ' -  value [1]'
    if valstr != '':
        valobj2['CountryCode'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.WorldRegion'] + ' -  value [1]'
    if valstr != '':
        valobj2['WorldRegion'] = valstr
    # STRUCTURE END LocationDetails: arrayround = 1 - recursion = 2
    vallist1.append(valobj2)
    # * STRUCTURE LocationDetails: arrayround = 2 - recursion = 2
    valobj2 = {}
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.LocationId'] + ' -  value [2]'
    if valstr != '':
        valobj2['LocationId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.Name'] + ' -  value [2]'
    if valstr != '':
        valobj2['Name'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.Sublocation'] + ' -  value [2]'
    if valstr != '':
        valobj2['Sublocation'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.City'] + ' -  value [2]'
    if valstr != '':
        valobj2['City'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.ProvinceState'] + ' -  value [2]'
    if valstr != '':
        valobj2['ProvinceState'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.CountryName'] + ' -  value [2]'
    if valstr != '':
        valobj2['CountryName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.CountryCode'] + ' -  value [2]'
    if valstr != '':
        valobj2['CountryCode'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Rating.RatingRegion.WorldRegion'] + ' -  value [2]'
    if valstr != '':
        valobj2['WorldRegion'] = valstr
    # STRUCTURE END LocationDetails: arrayround = 2 - recursion = 2
    vallist1.append(valobj2)
    valobj1['RatingRegion'] = vallist1
    # STRUCTURE END Rating: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:Rating'] = vallist

    # VMHub property (administrative) Ready for Release
    valstr = ivmdpval['XMP-iptcExt:ReleaseReady']
    if valstr != '':
        vmd['XMP-iptcExt:ReleaseReady'] = valstr

    # VMHub property (administrative) Season
    # * STRUCTURE EpisodeSeason: arrayround = 0 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:Season.Name'] + ' -  value'
    if valstr != '':
        valobj1['Name'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Season.Number'] + ' -  value'
    if valstr != '':
        valobj1['Number'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Season.Identifier'] + ' -  value'
    if valstr != '':
        valobj1['Identifier'] = valstr
    # STRUCTURE END EpisodeSeason: arrayround = 0 - recursion = 1
    vmd['XMP-iptcExt:Season'] = valobj1

    # VMHub property (administrative) Series
    # * STRUCTURE Series: arrayround = 0 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:Series.Name'] + ' -  value'
    if valstr != '':
        valobj1['Name'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Series.Identifier'] + ' -  value'
    if valstr != '':
        valobj1['Identifier'] = valstr
    # STRUCTURE END Series: arrayround = 0 - recursion = 1
    vmd['XMP-iptcExt:Series'] = valobj1

    # VMHub property (administrative) Storyline Identifier
    vallist = []
    valstr = ivmdpval['XMP-iptcExt:StorylineIdentifier'] + ' - value 1'
    if valstr != '':
        vallist.append(valstr)
    valstr = ivmdpval['XMP-iptcExt:StorylineIdentifier'] + ' value 2'
    if valstr != '':
        vallist.append(valstr)
    vmd['XMP-iptcExt:StorylineIdentifier'] = vallist

    # VMHub property (administrative) Style Period
    valstr = ivmdpval['XMP-iptcExt:ArtworkStylePeriod']
    if valstr != '':
        vmd['XMP-iptcExt:ArtworkStylePeriod'] = valstr

    # VMHub property (administrative) Temporal Coverage
    # * STRUCTURE TemporalCoverage: arrayround = 0 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:TemporalCoverage.TempCoverageFrom']
    if valstr != '':
        valobj1['TempCoverageFrom'] = valstr
    valstr = ivmdpval['XMP-iptcExt:TemporalCoverage.TempCoverageTo']
    if valstr != '':
        valobj1['TempCoverageTo'] = valstr
    # STRUCTURE END TemporalCoverage: arrayround = 0 - recursion = 1
    vmd['XMP-iptcExt:TemporalCoverage'] = valobj1

    # VMHub property (administrative) Video Identifier
    valstr = ivmdpval['XMP-dc:Identifier']
    if valstr != '':
        vmd['XMP-dc:Identifier'] = valstr

    # VMHub property (administrative) Video Rendition
    valstr = ivmdpval['XMP-xmpMM:RenditionClass']
    if valstr != '':
        vmd['XMP-xmpMM:RenditionClass'] = valstr

    # VMHub property (administrative) Video Version
    valstr = ivmdpval['XMP-xmpMM:VersionID']
    if valstr != '':
        vmd['XMP-xmpMM:VersionID'] = valstr

    # VMHub property (administrative) Workflow Tag
    # * STRUCTURE CvTermDetails: arrayround = 0 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:WorkflowTag.CvId'] + ' -  value'
    if valstr != '':
        valobj1['CvId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:WorkflowTag.CvTermId'] + ' -  value'
    if valstr != '':
        valobj1['CvTermId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:WorkflowTag.CvTermName'] + ' -  value'
    if valstr != '':
        valobj1['CvTermName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:WorkflowTag.CvTermRefinedAbout'] + ' -  value'
    if valstr != '':
        valobj1['CvTermRefinedAbout'] = valstr
    # STRUCTURE END CvTermDetails: arrayround = 0 - recursion = 1
    vmd['XMP-iptcExt:WorkflowTag'] = valobj1

    # VMHub property (administrative) Registry Entry
    vallist = []
    # * STRUCTURE RegistryEntryDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:RegistryId.RegItemId'] + ' -  value [1]'
    if valstr != '':
        valobj1['RegItemId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:RegistryId.RegOrgId'] + ' -  value [1]'
    if valstr != '':
        valobj1['RegOrgId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:RegistryId.RegEntryRole'] + ' -  value [1]'
    if valstr != '':
        valobj1['RegEntryRole'] = valstr
    # STRUCTURE END RegistryEntryDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE RegistryEntryDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:RegistryId.RegItemId'] + ' -  value [2]'
    if valstr != '':
        valobj1['RegItemId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:RegistryId.RegOrgId'] + ' -  value [2]'
    if valstr != '':
        valobj1['RegOrgId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:RegistryId.RegEntryRole'] + ' -  value [2]'
    if valstr != '':
        valobj1['RegEntryRole'] = valstr
    # STRUCTURE END RegistryEntryDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:RegistryId'] = vallist

    # VMHub property (administrative) Recording Device
    # * STRUCTURE Device: arrayround = 0 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:RecDevice.Manufacturer'] + ' -  value'
    if valstr != '':
        valobj1['Manufacturer'] = valstr
    valstr = ivmdpval['XMP-iptcExt:RecDevice.ModelName'] + ' -  value'
    if valstr != '':
        valobj1['ModelName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:RecDevice.SerialNumber'] + ' -  value'
    if valstr != '':
        valobj1['SerialNumber'] = valstr
    valstr = ivmdpval['XMP-iptcExt:RecDevice.AttLensDescription'] + ' -  value'
    if valstr != '':
        valobj1['AttLensDescription'] = valstr
    valstr = ivmdpval['XMP-iptcExt:RecDevice.OwnersDeviceId'] + ' -  value'
    if valstr != '':
        valobj1['OwnersDeviceId'] = valstr
    # STRUCTURE END Device: arrayround = 0 - recursion = 1
    vmd['XMP-iptcExt:RecDevice'] = valobj1

    # VMHub property (administrative) Planning Reference
    vallist = []
    # * STRUCTURE EntityWRole: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:PlanningRef.Identifier'] + ' -  value [1]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PlanningRef.Name'] + ' -  value [1]'
    if valstr != '':
        valobj1['Name'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PlanningRef.Role'] + ' -  value [1]'
    if valstr != '':
        valobj1['Role'] = valstr
    # STRUCTURE END EntityWRole: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE EntityWRole: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:PlanningRef.Identifier'] + ' -  value [2]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PlanningRef.Name'] + ' -  value [2]'
    if valstr != '':
        valobj1['Name'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PlanningRef.Role'] + ' -  value [2]'
    if valstr != '':
        valobj1['Role'] = valstr
    # STRUCTURE END EntityWRole: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:PlanningRef'] = vallist

    # VMHub property (describing a/v content) CV Term About the Content
    # * STRUCTURE CvTermDetails: arrayround = 0 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:AboutCvTerm.CvId'] + ' -  value'
    if valstr != '':
        valobj1['CvId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:AboutCvTerm.CvTermId'] + ' -  value'
    if valstr != '':
        valobj1['CvTermId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:AboutCvTerm.CvTermName'] + ' -  value'
    if valstr != '':
        valobj1['CvTermName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:AboutCvTerm.CvTermRefinedAbout'] + ' -  value'
    if valstr != '':
        valobj1['CvTermRefinedAbout'] = valstr
    # STRUCTURE END CvTermDetails: arrayround = 0 - recursion = 1
    vmd['XMP-iptcExt:AboutCvTerm'] = valobj1

    # VMHub property (describing a/v content) Data Displayed on Screen
    vallist = []
    # * STRUCTURE TextRegion: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:DataOnScreen.RegionText'] + ' -  value [1]'
    if valstr != '':
        valobj1['RegionText'] = valstr
    valstr = ivmdpval['XMP-iptcExt:DataOnScreen.Unit'] + ' -  value [1]'
    if valstr != '':
        valobj1['Unit'] = valstr
    valstr = ivmdpval['XMP-iptcExt:DataOnScreen.X'] + ' -  value [1]'
    if valstr != '':
        valobj1['X'] = valstr
    valstr = ivmdpval['XMP-iptcExt:DataOnScreen.Y'] + ' -  value [1]'
    if valstr != '':
        valobj1['Y'] = valstr
    valstr = ivmdpval['XMP-iptcExt:DataOnScreen.W'] + ' -  value [1]'
    if valstr != '':
        valobj1['W'] = valstr
    valstr = ivmdpval['XMP-iptcExt:DataOnScreen.H'] + ' -  value [1]'
    if valstr != '':
        valobj1['H'] = valstr
    # STRUCTURE END TextRegion: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE TextRegion: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:DataOnScreen.RegionText'] + ' -  value [2]'
    if valstr != '':
        valobj1['RegionText'] = valstr
    valstr = ivmdpval['XMP-iptcExt:DataOnScreen.Unit'] + ' -  value [2]'
    if valstr != '':
        valobj1['Unit'] = valstr
    valstr = ivmdpval['XMP-iptcExt:DataOnScreen.X'] + ' -  value [2]'
    if valstr != '':
        valobj1['X'] = valstr
    valstr = ivmdpval['XMP-iptcExt:DataOnScreen.Y'] + ' -  value [2]'
    if valstr != '':
        valobj1['Y'] = valstr
    valstr = ivmdpval['XMP-iptcExt:DataOnScreen.W'] + ' -  value [2]'
    if valstr != '':
        valobj1['W'] = valstr
    valstr = ivmdpval['XMP-iptcExt:DataOnScreen.H'] + ' -  value [2]'
    if valstr != '':
        valobj1['H'] = valstr
    # STRUCTURE END TextRegion: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:DataOnScreen'] = vallist

    # VMHub property (describing a/v content) Description
    valstr = ivmdpval['XMP-dc:Description']
    if valstr != '':
        vmd['XMP-dc:Description'] = valstr

    # VMHub property (describing a/v content) Dopesheet
    valstr = ivmdpval['XMP-iptcExt:Dopesheet']
    if valstr != '':
        vmd['XMP-iptcExt:Dopesheet'] = valstr

    # VMHub property (describing a/v content) Dopesheet Link
    # * STRUCTURE QualifiedLink: arrayround = 0 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:DopesheetLink.Link'] + ' -  value'
    if valstr != '':
        valobj1['Link'] = valstr
    valstr = ivmdpval['XMP-iptcExt:DopesheetLink.LinkQualifier'] + ' -  value'
    if valstr != '':
        valobj1['LinkQualifier'] = valstr
    # STRUCTURE END QualifiedLink: arrayround = 0 - recursion = 1
    vmd['XMP-iptcExt:DopesheetLink'] = valobj1

    # VMHub property (describing a/v content) Featured Organisation
    vallist = []
    # * STRUCTURE Entity: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:OrganisationInImageName.Identifier'] + ' -  value [1]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:OrganisationInImageName.Name'] + ' -  value [1]'
    if valstr != '':
        valobj1['Name'] = valstr
    # STRUCTURE END Entity: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE Entity: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:OrganisationInImageName.Identifier'] + ' -  value [2]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:OrganisationInImageName.Name'] + ' -  value [2]'
    if valstr != '':
        valobj1['Name'] = valstr
    # STRUCTURE END Entity: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:OrganisationInImageName'] = vallist
    vallist = []
    # * STRUCTURE Entity: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:OrganisationInImageCode.Identifier'] + ' -  value [1]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:OrganisationInImageCode.Name'] + ' -  value [1]'
    if valstr != '':
        valobj1['Name'] = valstr
    # STRUCTURE END Entity: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE Entity: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:OrganisationInImageCode.Identifier'] + ' -  value [2]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:OrganisationInImageCode.Name'] + ' -  value [2]'
    if valstr != '':
        valobj1['Name'] = valstr
    # STRUCTURE END Entity: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:OrganisationInImageCode'] = vallist

    # VMHub property (describing a/v content) Genre
    # * STRUCTURE CvTermDetails: arrayround = 0 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:Genre.CvId'] + ' -  value'
    if valstr != '':
        valobj1['CvId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Genre.CvTermId'] + ' -  value'
    if valstr != '':
        valobj1['CvTermId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Genre.CvTermName'] + ' -  value'
    if valstr != '':
        valobj1['CvTermName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Genre.CvTermRefinedAbout'] + ' -  value'
    if valstr != '':
        valobj1['CvTermRefinedAbout'] = valstr
    # STRUCTURE END CvTermDetails: arrayround = 0 - recursion = 1
    vmd['XMP-iptcExt:Genre'] = valobj1

    # VMHub property (describing a/v content) Headline
    valstr = ivmdpval['XMP-iptcExt:Headline']
    if valstr != '':
        vmd['XMP-iptcExt:Headline'] = valstr

    # VMHub property (describing a/v content) Keyword
    vallist = []
    valstr = ivmdpval['XMP-dc:Subject'] + ' - value 1'
    if valstr != '':
        vallist.append(valstr)
    valstr = ivmdpval['XMP-dc:Subject'] + ' value 2'
    if valstr != '':
        vallist.append(valstr)
    vmd['XMP-dc:Subject'] = vallist

    # VMHub property (describing a/v content) Language Version
    valstr = ivmdpval['XMP-dc:Language']
    if valstr != '':
        vmd['XMP-dc:Language'] = valstr

    # VMHub property (describing a/v content) Location Shot
    vallist = []
    # * STRUCTURE LocationDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:LocationCreated.LocationId'] + ' -  value [1]'
    if valstr != '':
        valobj1['LocationId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationCreated.Name'] + ' -  value [1]'
    if valstr != '':
        valobj1['Name'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationCreated.Sublocation'] + ' -  value [1]'
    if valstr != '':
        valobj1['Sublocation'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationCreated.City'] + ' -  value [1]'
    if valstr != '':
        valobj1['City'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationCreated.ProvinceState'] + ' -  value [1]'
    if valstr != '':
        valobj1['ProvinceState'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationCreated.CountryName'] + ' -  value [1]'
    if valstr != '':
        valobj1['CountryName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationCreated.CountryCode'] + ' -  value [1]'
    if valstr != '':
        valobj1['CountryCode'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationCreated.WorldRegion'] + ' -  value [1]'
    if valstr != '':
        valobj1['WorldRegion'] = valstr
    # STRUCTURE END LocationDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE LocationDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:LocationCreated.LocationId'] + ' -  value [2]'
    if valstr != '':
        valobj1['LocationId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationCreated.Name'] + ' -  value [2]'
    if valstr != '':
        valobj1['Name'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationCreated.Sublocation'] + ' -  value [2]'
    if valstr != '':
        valobj1['Sublocation'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationCreated.City'] + ' -  value [2]'
    if valstr != '':
        valobj1['City'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationCreated.ProvinceState'] + ' -  value [2]'
    if valstr != '':
        valobj1['ProvinceState'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationCreated.CountryName'] + ' -  value [2]'
    if valstr != '':
        valobj1['CountryName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationCreated.CountryCode'] + ' -  value [2]'
    if valstr != '':
        valobj1['CountryCode'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationCreated.WorldRegion'] + ' -  value [2]'
    if valstr != '':
        valobj1['WorldRegion'] = valstr
    # STRUCTURE END LocationDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:LocationCreated'] = vallist

    # VMHub property (describing a/v content) Location Shown
    vallist = []
    # * STRUCTURE LocationDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:LocationShown.LocationId'] + ' -  value [1]'
    if valstr != '':
        valobj1['LocationId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationShown.Name'] + ' -  value [1]'
    if valstr != '':
        valobj1['Name'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationShown.Sublocation'] + ' -  value [1]'
    if valstr != '':
        valobj1['Sublocation'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationShown.City'] + ' -  value [1]'
    if valstr != '':
        valobj1['City'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationShown.ProvinceState'] + ' -  value [1]'
    if valstr != '':
        valobj1['ProvinceState'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationShown.CountryName'] + ' -  value [1]'
    if valstr != '':
        valobj1['CountryName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationShown.CountryCode'] + ' -  value [1]'
    if valstr != '':
        valobj1['CountryCode'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationShown.WorldRegion'] + ' -  value [1]'
    if valstr != '':
        valobj1['WorldRegion'] = valstr
    # STRUCTURE END LocationDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE LocationDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:LocationShown.LocationId'] + ' -  value [2]'
    if valstr != '':
        valobj1['LocationId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationShown.Name'] + ' -  value [2]'
    if valstr != '':
        valobj1['Name'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationShown.Sublocation'] + ' -  value [2]'
    if valstr != '':
        valobj1['Sublocation'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationShown.City'] + ' -  value [2]'
    if valstr != '':
        valobj1['City'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationShown.ProvinceState'] + ' -  value [2]'
    if valstr != '':
        valobj1['ProvinceState'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationShown.CountryName'] + ' -  value [2]'
    if valstr != '':
        valobj1['CountryName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationShown.CountryCode'] + ' -  value [2]'
    if valstr != '':
        valobj1['CountryCode'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LocationShown.WorldRegion'] + ' -  value [2]'
    if valstr != '':
        valobj1['WorldRegion'] = valstr
    # STRUCTURE END LocationDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:LocationShown'] = vallist

    # VMHub property (describing a/v content) Object Shown
    vallist = []
    # * STRUCTURE ArtworkOrObjectDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCircaDateCreated'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOCircaDateCreated'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOContentDescription'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOContentDescription'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOContributionDescription'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOContributionDescription'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCopyrightNotice'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOCopyrightNotice'] = valstr
    vallist1 = []
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCreator'] + ' -  value 1  [1]'
    if valstr != '':
        vallist1.append(valstr)
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCreator'] + ' -  value 2 [1]'
    if valstr != '':
        vallist1.append(valstr)
    valobj1['AOCreator'] = vallist1
    vallist1 = []
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCreatorId'] + ' -  value 1  [1]'
    if valstr != '':
        vallist1.append(valstr)
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCreatorId'] + ' -  value 2 [1]'
    if valstr != '':
        vallist1.append(valstr)
    valobj1['AOCreatorId'] = vallist1
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCurrentCopyrightOwnerId'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOCurrentCopyrightOwnerId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCurrentCopyrightOwnerName'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOCurrentCopyrightOwnerName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCurrentLicensorId'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOCurrentLicensorId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCurrentLicensorName'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOCurrentLicensorName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AODateCreated']
    if valstr != '':
        valobj1['AODateCreated'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOPhysicalDescription'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOPhysicalDescription'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOSource'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOSource'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOSourceInvNo'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOSourceInvNo'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOSourceInvURL'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOSourceInvURL'] = valstr
    vallist1 = []
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOStylePeriod'] + ' -  value 1  [1]'
    if valstr != '':
        vallist1.append(valstr)
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOStylePeriod'] + ' -  value 2 [1]'
    if valstr != '':
        vallist1.append(valstr)
    valobj1['AOStylePeriod'] = vallist1
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOTitle'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOTitle'] = valstr
    # STRUCTURE END ArtworkOrObjectDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE ArtworkOrObjectDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCircaDateCreated'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOCircaDateCreated'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOContentDescription'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOContentDescription'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOContributionDescription'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOContributionDescription'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCopyrightNotice'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOCopyrightNotice'] = valstr
    vallist1 = []
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCreator'] + ' -  value 1  [2]'
    if valstr != '':
        vallist1.append(valstr)
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCreator'] + ' -  value 2 [2]'
    if valstr != '':
        vallist1.append(valstr)
    valobj1['AOCreator'] = vallist1
    vallist1 = []
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCreatorId'] + ' -  value 1  [2]'
    if valstr != '':
        vallist1.append(valstr)
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCreatorId'] + ' -  value 2 [2]'
    if valstr != '':
        vallist1.append(valstr)
    valobj1['AOCreatorId'] = vallist1
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCurrentCopyrightOwnerId'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOCurrentCopyrightOwnerId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCurrentCopyrightOwnerName'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOCurrentCopyrightOwnerName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCurrentLicensorId'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOCurrentLicensorId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOCurrentLicensorName'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOCurrentLicensorName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AODateCreated']
    if valstr != '':
        valobj1['AODateCreated'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOPhysicalDescription'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOPhysicalDescription'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOSource'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOSource'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOSourceInvNo'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOSourceInvNo'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOSourceInvURL'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOSourceInvURL'] = valstr
    vallist1 = []
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOStylePeriod'] + ' -  value 1  [2]'
    if valstr != '':
        vallist1.append(valstr)
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOStylePeriod'] + ' -  value 2 [2]'
    if valstr != '':
        vallist1.append(valstr)
    valobj1['AOStylePeriod'] = vallist1
    valstr = ivmdpval['XMP-iptcExt:ArtworkOrObject.AOTitle'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOTitle'] = valstr
    # STRUCTURE END ArtworkOrObjectDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:ArtworkOrObject'] = vallist

    # VMHub property (describing a/v content) Person Heard
    vallist = []
    # * STRUCTURE Entity: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:PersonHeard.Identifier'] + ' -  value [1]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PersonHeard.Name'] + ' -  value [1]'
    if valstr != '':
        valobj1['Name'] = valstr
    # STRUCTURE END Entity: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE Entity: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:PersonHeard.Identifier'] + ' -  value [2]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PersonHeard.Name'] + ' -  value [2]'
    if valstr != '':
        valobj1['Name'] = valstr
    # STRUCTURE END Entity: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:PersonHeard'] = vallist

    # VMHub property (describing a/v content) Person Shown
    vallist = []
    # * STRUCTURE PersonDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonId'] + ' -  value [1]'
    if valstr != '':
        valobj1['PersonId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonName'] + ' -  value [1]'
    if valstr != '':
        valobj1['PersonName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonDescription'] + ' -  value [1]'
    if valstr != '':
        valobj1['PersonDescription'] = valstr
    vallist1 = []
    # * STRUCTURE CVTermDetails: arrayround = 1 - recursion = 2
    valobj2 = {}
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvId'] + ' -  value [1]'
    if valstr != '':
        valobj2['CvId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermId'] + ' -  value [1]'
    if valstr != '':
        valobj2['CvTermId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermName'] + ' -  value [1]'
    if valstr != '':
        valobj2['CvTermName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermRefinedAbout'] + ' -  value [1]'
    if valstr != '':
        valobj2['CvTermRefinedAbout'] = valstr
    # STRUCTURE END CVTermDetails: arrayround = 1 - recursion = 2
    vallist1.append(valobj2)
    # * STRUCTURE CVTermDetails: arrayround = 2 - recursion = 2
    valobj2 = {}
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvId'] + ' -  value [2]'
    if valstr != '':
        valobj2['CvId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermId'] + ' -  value [2]'
    if valstr != '':
        valobj2['CvTermId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermName'] + ' -  value [2]'
    if valstr != '':
        valobj2['CvTermName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermRefinedAbout'] + ' -  value [2]'
    if valstr != '':
        valobj2['CvTermRefinedAbout'] = valstr
    # STRUCTURE END CVTermDetails: arrayround = 2 - recursion = 2
    vallist1.append(valobj2)
    valobj1['PersonCharacteristic'] = vallist1
    # STRUCTURE END PersonDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE PersonDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonId'] + ' -  value [2]'
    if valstr != '':
        valobj1['PersonId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonName'] + ' -  value [2]'
    if valstr != '':
        valobj1['PersonName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonDescription'] + ' -  value [2]'
    if valstr != '':
        valobj1['PersonDescription'] = valstr
    vallist1 = []
    # * STRUCTURE CVTermDetails: arrayround = 1 - recursion = 2
    valobj2 = {}
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvId'] + ' -  value [1]'
    if valstr != '':
        valobj2['CvId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermId'] + ' -  value [1]'
    if valstr != '':
        valobj2['CvTermId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermName'] + ' -  value [1]'
    if valstr != '':
        valobj2['CvTermName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermRefinedAbout'] + ' -  value [1]'
    if valstr != '':
        valobj2['CvTermRefinedAbout'] = valstr
    # STRUCTURE END CVTermDetails: arrayround = 1 - recursion = 2
    vallist1.append(valobj2)
    # * STRUCTURE CVTermDetails: arrayround = 2 - recursion = 2
    valobj2 = {}
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvId'] + ' -  value [2]'
    if valstr != '':
        valobj2['CvId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermId'] + ' -  value [2]'
    if valstr != '':
        valobj2['CvTermId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermName'] + ' -  value [2]'
    if valstr != '':
        valobj2['CvTermName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermRefinedAbout'] + ' -  value [2]'
    if valstr != '':
        valobj2['CvTermRefinedAbout'] = valstr
    # STRUCTURE END CVTermDetails: arrayround = 2 - recursion = 2
    vallist1.append(valobj2)
    valobj1['PersonCharacteristic'] = vallist1
    # STRUCTURE END PersonDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:PersonInImageWDetails'] = vallist

    # VMHub property (describing a/v content) Product Shown
    vallist = []
    # * STRUCTURE ProductDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:ProductInImage.ProductGTIN'] + ' -  value [1]'
    if valstr != '':
        valobj1['ProductGTIN'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ProductInImage.ProductName'] + ' -  value [1]'
    if valstr != '':
        valobj1['ProductName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ProductInImage.ProductDescription'] + ' -  value [1]'
    if valstr != '':
        valobj1['ProductDescription'] = valstr
    # STRUCTURE END ProductDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE ProductDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:ProductInImage.ProductGTIN'] + ' -  value [2]'
    if valstr != '':
        valobj1['ProductGTIN'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ProductInImage.ProductName'] + ' -  value [2]'
    if valstr != '':
        valobj1['ProductName'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ProductInImage.ProductDescription'] + ' -  value [2]'
    if valstr != '':
        valobj1['ProductDescription'] = valstr
    # STRUCTURE END ProductDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:ProductInImage'] = vallist

    # VMHub property (describing a/v content) Shot Type
    vallist = []
    # * STRUCTURE Entity: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:VideoShotType.Identifier'] + ' -  value [1]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:VideoShotType.Name'] + ' -  value [1]'
    if valstr != '':
        valobj1['Name'] = valstr
    # STRUCTURE END Entity: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE Entity: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:VideoShotType.Identifier'] + ' -  value [2]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:VideoShotType.Name'] + ' -  value [2]'
    if valstr != '':
        valobj1['Name'] = valstr
    # STRUCTURE END Entity: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:VideoShotType'] = vallist

    # VMHub property (describing a/v content) Shown Event
    vallist = []
    # * STRUCTURE Entity: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:ShownEvent.Identifier'] + ' -  value [1]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ShownEvent.Name'] + ' -  value [1]'
    if valstr != '':
        valobj1['Name'] = valstr
    # STRUCTURE END Entity: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE Entity: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:ShownEvent.Identifier'] + ' -  value [2]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ShownEvent.Name'] + ' -  value [2]'
    if valstr != '':
        valobj1['Name'] = valstr
    # STRUCTURE END Entity: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:ShownEvent'] = vallist

    # VMHub property (describing a/v content) Snapshot Link
    vallist = []
    # * STRUCTURE LinkedImage: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:SnapshotLink.Link'] + ' -  value [1]'
    if valstr != '':
        valobj1['Link'] = valstr
    valstr = ivmdpval['XMP-iptcExt:SnapshotLink.LinkQualifier'] + ' -  value [1]'
    if valstr != '':
        valobj1['LinkQualifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:SnapshotLink.ImageRole'] + ' -  value [1]'
    if valstr != '':
        valobj1['ImageRole'] = valstr
    valstr = ivmdpval['XMP-iptcExt:SnapshotLink.Format'] + ' -  value [1]'
    if valstr != '':
        valobj1['Format'] = valstr
    valstr = ivmdpval['XMP-iptcExt:SnapshotLink.WidthPixels'] + ' -  value [1]'
    if valstr != '':
        valobj1['WidthPixels'] = valstr
    valstr = ivmdpval['XMP-iptcExt:SnapshotLink.HeightPixels'] + ' -  value [1]'
    if valstr != '':
        valobj1['HeightPixels'] = valstr
    valstr = ivmdpval['XMP-iptcExt:SnapshotLink.VideoTime'] + ' -  value [1]'
    if valstr != '':
        valobj1['VideoTime'] = valstr
    # STRUCTURE END LinkedImage: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE LinkedImage: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:SnapshotLink.Link'] + ' -  value [2]'
    if valstr != '':
        valobj1['Link'] = valstr
    valstr = ivmdpval['XMP-iptcExt:SnapshotLink.LinkQualifier'] + ' -  value [2]'
    if valstr != '':
        valobj1['LinkQualifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:SnapshotLink.ImageRole'] + ' -  value [2]'
    if valstr != '':
        valobj1['ImageRole'] = valstr
    valstr = ivmdpval['XMP-iptcExt:SnapshotLink.Format'] + ' -  value [2]'
    if valstr != '':
        valobj1['Format'] = valstr
    valstr = ivmdpval['XMP-iptcExt:SnapshotLink.WidthPixels'] + ' -  value [2]'
    if valstr != '':
        valobj1['WidthPixels'] = valstr
    valstr = ivmdpval['XMP-iptcExt:SnapshotLink.HeightPixels'] + ' -  value [2]'
    if valstr != '':
        valobj1['HeightPixels'] = valstr
    valstr = ivmdpval['XMP-iptcExt:SnapshotLink.VideoTime'] + ' -  value [2]'
    if valstr != '':
        valobj1['VideoTime'] = valstr
    # STRUCTURE END LinkedImage: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:SnapshotLink'] = vallist

    # VMHub property (describing a/v content) Title
    valstr = ivmdpval['XMP-dc:Title']
    if valstr != '':
        vmd['XMP-dc:Title'] = valstr

    # VMHub property (describing a/v content) Transcript
    valstr = ivmdpval['XMP-iptcExt:Transcript']
    if valstr != '':
        vmd['XMP-iptcExt:Transcript'] = valstr

    # VMHub property (describing a/v content) Transcript Link
    vallist = []
    # * STRUCTURE QualifiedLink: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:TranscriptLink.Link'] + ' -  value [1]'
    if valstr != '':
        valobj1['Link'] = valstr
    valstr = ivmdpval['XMP-iptcExt:TranscriptLink.LinkQualifier'] + ' -  value [1]'
    if valstr != '':
        valobj1['LinkQualifier'] = valstr
    # STRUCTURE END QualifiedLink: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE QualifiedLink: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:TranscriptLink.Link'] + ' -  value [2]'
    if valstr != '':
        valobj1['Link'] = valstr
    valstr = ivmdpval['XMP-iptcExt:TranscriptLink.LinkQualifier'] + ' -  value [2]'
    if valstr != '':
        valobj1['LinkQualifier'] = valstr
    # STRUCTURE END QualifiedLink: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:TranscriptLink'] = vallist

    # VMHub property (describing a/v content) Visual Colour
    valstr = ivmdpval['XMP-iptcExt:VisualColor#']
    if valstr != '':
        vmd['XMP-iptcExt:VisualColor#'] = valstr

    # VMHub property (rights) Contributor
    vallist = []
    # * STRUCTURE EntityWRole: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:Contributor.Identifier'] + ' -  value [1]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Contributor.Name'] + ' -  value [1]'
    if valstr != '':
        valobj1['Name'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Contributor.Role'] + ' -  value [1]'
    if valstr != '':
        valobj1['Role'] = valstr
    # STRUCTURE END EntityWRole: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE EntityWRole: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:Contributor.Identifier'] + ' -  value [2]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Contributor.Name'] + ' -  value [2]'
    if valstr != '':
        valobj1['Name'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Contributor.Role'] + ' -  value [2]'
    if valstr != '':
        valobj1['Role'] = valstr
    # STRUCTURE END EntityWRole: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:Contributor'] = vallist

    # VMHub property (rights) Copyright Notice
    valstr = ivmdpval['XMP-dc:Rights']
    if valstr != '':
        vmd['XMP-dc:Rights'] = valstr

    # VMHub property (rights) Copyright Year
    valstr = ivmdpval['XMP-iptcExt:CopyrightYear']
    valnumber = int(valstr)
    if valnumber:
        vmd['XMP-iptcExt:CopyrightYear'] = valnumber

    # VMHub property (rights) Creator
    vallist = []
    # * STRUCTURE EntityWRole: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:Creator.Identifier'] + ' -  value [1]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Creator.Name'] + ' -  value [1]'
    if valstr != '':
        valobj1['Name'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Creator.Role'] + ' -  value [1]'
    if valstr != '':
        valobj1['Role'] = valstr
    # STRUCTURE END EntityWRole: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE EntityWRole: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:Creator.Identifier'] + ' -  value [2]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Creator.Name'] + ' -  value [2]'
    if valstr != '':
        valobj1['Name'] = valstr
    valstr = ivmdpval['XMP-iptcExt:Creator.Role'] + ' -  value [2]'
    if valstr != '':
        valobj1['Role'] = valstr
    # STRUCTURE END EntityWRole: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:Creator'] = vallist

    # VMHub property (rights) Credit Line
    valstr = ivmdpval['XMP-photoshop:Credit']
    if valstr != '':
        vmd['XMP-photoshop:Credit'] = valstr

    # VMHub property (rights) Licensor
    vallist = []
    # * STRUCTURE PlusEntityDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-plus:Licensor.ID'] + ' -  value [1]'
    if valstr != '':
        valobj1['LicensorID'] = valstr
    valstr = ivmdpval['XMP-plus:Licensor.Name'] + ' -  value [1]'
    if valstr != '':
        valobj1['LicensorName'] = valstr
    # STRUCTURE END PlusEntityDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE PlusEntityDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-plus:Licensor.ID'] + ' -  value [2]'
    if valstr != '':
        valobj1['LicensorID'] = valstr
    valstr = ivmdpval['XMP-plus:Licensor.Name'] + ' -  value [2]'
    if valstr != '':
        valobj1['LicensorName'] = valstr
    # STRUCTURE END PlusEntityDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-plus:Licensor'] = vallist

    # VMHub property (rights) Model Release Document
    vallist = []
    valstr = ivmdpval['XMP-plus:ModelReleaseID'] + ' - value 1'
    if valstr != '':
        vallist.append(valstr)
    valstr = ivmdpval['XMP-plus:ModelReleaseID'] + ' value 2'
    if valstr != '':
        vallist.append(valstr)
    vmd['XMP-plus:ModelReleaseID'] = vallist

    # VMHub property (rights) Model Release Status
    valstr = ivmdpval['XMP-plus:ModelReleaseStatus']
    if valstr != '':
        vmd['XMP-plus:ModelReleaseStatus'] = valstr

    # VMHub property (rights) Property Release Document
    vallist = []
    valstr = ivmdpval['XMP-plus:PropertyReleaseID'] + ' - value 1'
    if valstr != '':
        vallist.append(valstr)
    valstr = ivmdpval['XMP-plus:PropertyReleaseID'] + ' value 2'
    if valstr != '':
        vallist.append(valstr)
    vmd['XMP-plus:PropertyReleaseID'] = vallist

    # VMHub property (rights) Property Release Status
    valstr = ivmdpval['XMP-plus:PropertyReleaseStatus']
    if valstr != '':
        vmd['XMP-plus:PropertyReleaseStatus'] = valstr

    # VMHub property (rights) Rights and Licensing Terms
    vallist = []
    # * STRUCTURE EEREDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:EmbdEncRightsExpr.RightsExprLangId'] + ' -  value [1]'
    if valstr != '':
        valobj1['RightsExprLangId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:EmbdEncRightsExpr.RightsExprEncType'] + ' -  value [1]'
    if valstr != '':
        valobj1['RightsExprEncType'] = valstr
    valstr = ivmdpval['XMP-iptcExt:EmbdEncRightsExpr.EncRightsExpr'] + ' -  value [1]'
    if valstr != '':
        valobj1['EncRightsExpr'] = valstr
    # STRUCTURE END EEREDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE EEREDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:EmbdEncRightsExpr.RightsExprLangId'] + ' -  value [2]'
    if valstr != '':
        valobj1['RightsExprLangId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:EmbdEncRightsExpr.RightsExprEncType'] + ' -  value [2]'
    if valstr != '':
        valobj1['RightsExprEncType'] = valstr
    valstr = ivmdpval['XMP-iptcExt:EmbdEncRightsExpr.EncRightsExpr'] + ' -  value [2]'
    if valstr != '':
        valobj1['EncRightsExpr'] = valstr
    # STRUCTURE END EEREDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:EmbdEncRightsExpr'] = vallist
    vallist = []
    # * STRUCTURE LEREDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:LinkedEncRightsExpr.RightsExprLangId'] + ' -  value [1]'
    if valstr != '':
        valobj1['RightsExprLangId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LinkedEncRightsExpr.RightsExprEncType'] + ' -  value [1]'
    if valstr != '':
        valobj1['RightsExprEncType'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LinkedEncRightsExpr.LinkedRightsExpr'] + ' -  value [1]'
    if valstr != '':
        valobj1['LinkedRightsExpr'] = valstr
    # STRUCTURE END LEREDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE LEREDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:LinkedEncRightsExpr.RightsExprLangId'] + ' -  value [2]'
    if valstr != '':
        valobj1['RightsExprLangId'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LinkedEncRightsExpr.RightsExprEncType'] + ' -  value [2]'
    if valstr != '':
        valobj1['RightsExprEncType'] = valstr
    valstr = ivmdpval['XMP-iptcExt:LinkedEncRightsExpr.LinkedRightsExpr'] + ' -  value [2]'
    if valstr != '':
        valobj1['LinkedRightsExpr'] = valstr
    # STRUCTURE END LEREDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:LinkedEncRightsExpr'] = vallist

    # VMHub property (rights) Rights Owner
    vallist = []
    # * STRUCTURE EntityWRole: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-plus:CopyrightOwner.Identifier'] + ' -  value [1]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-plus:CopyrightOwner.Name'] + ' -  value [1]'
    if valstr != '':
        valobj1['Name'] = valstr
    valstr = ivmdpval['XMP-plus:CopyrightOwner.Role'] + ' -  value [1]'
    if valstr != '':
        valobj1['Role'] = valstr
    # STRUCTURE END EntityWRole: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE EntityWRole: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-plus:CopyrightOwner.Identifier'] + ' -  value [2]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-plus:CopyrightOwner.Name'] + ' -  value [2]'
    if valstr != '':
        valobj1['Name'] = valstr
    valstr = ivmdpval['XMP-plus:CopyrightOwner.Role'] + ' -  value [2]'
    if valstr != '':
        valobj1['Role'] = valstr
    # STRUCTURE END EntityWRole: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-plus:CopyrightOwner'] = vallist

    # VMHub property (rights) Supplier
    # * STRUCTURE PlusEntityDetails: arrayround = 0 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-plus:ImageSupplier.ID'] + ' -  value'
    if valstr != '':
        valobj1['ImageSupplierID'] = valstr
    valstr = ivmdpval['XMP-plus:ImageSupplier.Name'] + ' -  value'
    if valstr != '':
        valobj1['ImageSupplierName'] = valstr
    # STRUCTURE END PlusEntityDetails: arrayround = 0 - recursion = 1
    vmd['XMP-plus:ImageSupplier'] = valobj1

    # VMHub property (rights) Supply Chain Source
    vallist = []
    # * STRUCTURE Entity: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:SupplyChainSource.Identifier'] + ' -  value [1]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:SupplyChainSource.Name'] + ' -  value [1]'
    if valstr != '':
        valobj1['Name'] = valstr
    # STRUCTURE END Entity: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE Entity: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:SupplyChainSource.Identifier'] + ' -  value [2]'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:SupplyChainSource.Name'] + ' -  value [2]'
    if valstr != '':
        valobj1['Name'] = valstr
    # STRUCTURE END Entity: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    vmd['XMP-iptcExt:SupplyChainSource'] = vallist

    # VMHub property (technical) Audio Bits per Sample
    valstr = ivmdpval['XMP-iptcExt:AudioBitsPerSample']
    valnumber = int(valstr)
    if valnumber:
        vmd['XMP-iptcExt:AudioBitsPerSample'] = valnumber

    # VMHub property (technical) Audio Bitrate
    valstr = ivmdpval['XMP-iptcExt:AudioBitRate']
    valnumber = int(valstr)
    if valnumber:
        vmd['XMP-iptcExt:AudioBitRate'] = valnumber

    # VMHub property (technical) Audio Bitrate Type
    valstr = ivmdpval['XMP-iptcExt:AudioBitRateMode#']
    if valstr != '':
        vmd['XMP-iptcExt:AudioBitRateMode#'] = valstr

    # VMHub property (technical) Audio Channel Layout
    valstr = ivmdpval['XMP-xmpDM:AudioChannelType#']
    if valstr != '':
        vmd['XMP-xmpDM:AudioChannelType#'] = valstr

    # VMHub property (technical) Audio Channels
    valstr = ivmdpval['XMP-iptcExt:AudioChannelCount']
    valnumber = int(valstr)
    if valnumber:
        vmd['XMP-iptcExt:AudioChannelCount'] = valnumber

    # VMHub property (technical) Audio Coding
    valstr = ivmdpval['XMP-xmpDM:AudioCompressor']
    if valstr != '':
        vmd['XMP-xmpDM:AudioCompressor'] = valstr

    # VMHub property (technical) Audio Sample Rate
    valstr = ivmdpval['XMP-xmpDM:AudioSampleRate']
    valnumber = int(valstr)
    if valnumber:
        vmd['XMP-xmpDM:AudioSampleRate'] = valnumber

    # VMHub property (technical) Display Aspect Ratio
    valstr = ivmdpval['XMP-iptcExt:VideoDisplayAspectRatio']
    valnumber = float(valstr)
    if valnumber:
        vmd['XMP-iptcExt:VideoDisplayAspectRatio'] = valnumber

    # VMHub property (technical) File Bitrate
    valstr = ivmdpval['XMP-xmpDM:FileDataRate']
    valnumber = float(valstr)
    if valnumber:
        vmd['XMP-xmpDM:FileDataRate'] = valnumber

    # VMHub property (technical) File Duration
    # * STRUCTURE Time: arrayround = 0 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-xmpDM:Duration.Scale']
    valnumber = float(valstr)
    if valnumber:
        valobj1['Scale'] = valnumber
    valstr = ivmdpval['XMP-xmpDM:Duration.Value']
    valnumber = int(valstr)
    if valnumber:
        valobj1['Value'] = valnumber
    # STRUCTURE END Time: arrayround = 0 - recursion = 1
    vmd['XMP-xmpDM:Duration'] = valobj1

    # VMHub property (technical) File Format
    # * STRUCTURE Entity: arrayround = 0 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-iptcExt:ContainerFormat.Identifier'] + ' -  value'
    if valstr != '':
        valobj1['Identifier'] = valstr
    valstr = ivmdpval['XMP-iptcExt:ContainerFormat.Name'] + ' -  value'
    if valstr != '':
        valobj1['Name'] = valstr
    # STRUCTURE END Entity: arrayround = 0 - recursion = 1
    vmd['XMP-iptcExt:ContainerFormat'] = valobj1

    # VMHub property (technical) Frame Size
    # * STRUCTURE FrameSize: arrayround = 0 - recursion = 1
    valobj1 = {}
    valstr = ivmdpval['XMP-xmpDM:VideoFrameSize.W']
    valnumber = float(valstr)
    if valnumber:
        valobj1['W'] = valnumber
    valstr = ivmdpval['XMP-xmpDM:VideoFrameSize.H']
    valnumber = float(valstr)
    if valnumber:
        valobj1['H'] = valnumber
    valstr = ivmdpval['XMP-xmpDM:VideoFrameSize.Unit'] + ' -  value'
    if valstr != '':
        valobj1['Unit'] = valstr
    # STRUCTURE END FrameSize: arrayround = 0 - recursion = 1
    vmd['XMP-xmpDM:VideoFrameSize'] = valobj1

    # VMHub property (technical) Media Type
    valstr = ivmdpval['XMP-dc:Format']
    if valstr != '':
        vmd['XMP-dc:Format'] = valstr

    # VMHub property (technical) Orientation
    valstr = ivmdpval['XMP-tiff:Orientation#']
    if valstr != '':
        vmd['XMP-tiff:Orientation#'] = valstr

    # VMHub property (technical) Signal Aspect Ratio
    valstr = ivmdpval['XMP-xmpDM:VideoPixelAspectRatio']
    valnumber = float(valstr)
    if valnumber:
        vmd['XMP-xmpDM:VideoPixelAspectRatio'] = valnumber

    # VMHub property (technical) Signal Format
    valstr = ivmdpval['XMP-xmpDM:VideoFieldOrder#']
    if valstr != '':
        vmd['XMP-xmpDM:VideoFieldOrder#'] = valstr

    # VMHub property (technical) Stream-ready
    valstr = ivmdpval['XMP-iptcExt:StreamReady#']
    if valstr != '':
        vmd['XMP-iptcExt:StreamReady#'] = valstr

    # VMHub property (technical) Video Bitrate
    valstr = ivmdpval['XMP-iptcExt:VideoBitRate']
    valnumber = int(valstr)
    if valnumber:
        vmd['XMP-iptcExt:VideoBitRate'] = valnumber

    # VMHub property (technical) Video Bitrate Type
    valstr = ivmdpval['XMP-iptcExt:VideoBitRateMode#']
    if valstr != '':
        vmd['XMP-iptcExt:VideoBitRateMode#'] = valstr

    # VMHub property (technical) Video Coding
    valstr = ivmdpval['XMP-xmpDM:VideoCompressor']
    if valstr != '':
        vmd['XMP-xmpDM:VideoCompressor'] = valstr

    # VMHub property (technical) Video Frame Rate
    valstr = ivmdpval['XMP-xmpDM:VideoFrameRate']
    valnumber = float(valstr)
    if valnumber:
        vmd['XMP-xmpDM:VideoFrameRate'] = valnumber

    # VMHub property (technical) Video Profile
    valstr = ivmdpval['XMP-iptcExt:VideoEncodingProfile']
    if valstr != '':
        vmd['XMP-iptcExt:VideoEncodingProfile'] = valstr

    # VMHub property (technical) Video Streams Count
    valstr = ivmdpval['XMP-iptcExt:VideoStreamsCount']
    valnumber = int(valstr)
    if valnumber:
        vmd['XMP-iptcExt:VideoStreamsCount'] = valnumber

    # *************************************************************************
    # END OF INSERTED Code
    print(vmd)

    exifToolWrapper = []
    exifToolWrapper.append(vmd)

    # **************************************************************************
    # finally: doing something with the JSON
    print(json.dumps(exifToolWrapper, indent=4))
    with open(jsonOutputFp, 'w') as fp:
        json.dump(exifToolWrapper, fp, indent=4)



generate_IPTCVMD_etJSON()






