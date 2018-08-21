#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    This script generates all photo metadata properties defined by the IPTC Photo Metadata Standard 2017.1
    For this purpose a JSON document is generated - as file - which can be processed by the exiftool.

    The values of the properties are set by the content of the ex1-allPmd_propValues.yml YAML file.
    The key of each YAML entry is the identifier of the property defined by exiftool.
    The used YAML file has default values which reflect the name of each property.


"""
import json
import yaml

# Exiftool-JSON output file, adjust the name to your needs
jsonOutputFp = "ex1-allPmd_etData.json"

def generate_IPTCPMD_etJSON():
    print("START")
    ipmdpropvalYamlfile = open('ex1-allPmd_propValues.yml', 'r', encoding="utf-8")
    ipmdpval = yaml.load(ipmdpropvalYamlfile)
    # print(ipmdpval)

    pmd = {}
    pmd['Sourcefile'] = '*'

    # PMD property City (legacy)
    valstr = ipmdpval['XMP-photoshop:City']
    if valstr != '':
        pmd['XMP-photoshop:City'] = valstr
    valstr = ipmdpval['IPTC:City']
    if valstr != '':
        pmd['IPTC:City'] = valstr

    # PMD property Copyright Notice
    valstr = ipmdpval['XMP-dc:Rights']
    if valstr != '':
        pmd['XMP-dc:Rights'] = valstr
    valstr = ipmdpval['IPTC:CopyrightNotice']
    if valstr != '':
        pmd['IPTC:CopyrightNotice'] = valstr
    valstr = ipmdpval['IFD0:Copyright']
    if valstr != '':
        pmd['IFD0:Copyright'] = valstr

    # PMD property Country (legacy)
    valstr = ipmdpval['XMP-photoshop:Country']
    if valstr != '':
        pmd['XMP-photoshop:Country'] = valstr
    valstr = ipmdpval['IPTC:Country-PrimaryLocationName']
    if valstr != '':
        pmd['IPTC:Country-PrimaryLocationName'] = valstr

    # PMD property Country Code (legacy)
    valstr = ipmdpval['XMP-iptcCore:CountryCode']
    if valstr != '':
        pmd['XMP-iptcCore:CountryCode'] = valstr
    valstr = ipmdpval['IPTC:Country-PrimaryLocationCode']
    if valstr != '':
        pmd['IPTC:Country-PrimaryLocationCode'] = valstr

    # PMD property Creator
    vallist = []
    valstr = ipmdpval['XMP-dc:Creator'] + ' - value 1'
    if valstr != '':
        vallist.append(valstr)
    valstr = ipmdpval['XMP-dc:Creator'] + ' value 2'
    if valstr != '':
        vallist.append(valstr)
    pmd['XMP-dc:Creator'] = vallist
    vallist = []
    valstr = ipmdpval['IPTC:By-line'] + ' - value 1'
    if valstr != '':
        vallist.append(valstr)
    valstr = ipmdpval['IPTC:By-line'] + ' value 2'
    if valstr != '':
        vallist.append(valstr)
    pmd['IPTC:By-line'] = vallist
    valstr = ipmdpval['IFD0:Artist']
    if valstr != '':
        pmd['IFD0:Artist'] = valstr

    # PMD property Creator´s Contact Info
    # * STRUCTURE ContactInfo: arrayround = 0 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-iptcCore:CreatorContactInfo.CiAdrExtadr'] + ' -  value'
    if valstr != '':
        valobj1['CiAdrExtadr'] = valstr
    valstr = ipmdpval['XMP-iptcCore:CreatorContactInfo.CiAdrCity'] + ' -  value'
    if valstr != '':
        valobj1['CiAdrCity'] = valstr
    valstr = ipmdpval['XMP-iptcCore:CreatorContactInfo.CiAdrCtry'] + ' -  value'
    if valstr != '':
        valobj1['CiAdrCtry'] = valstr
    valstr = ipmdpval['XMP-iptcCore:CreatorContactInfo.CiEmailWork'] + ' -  value'
    if valstr != '':
        valobj1['CiEmailWork'] = valstr
    valstr = ipmdpval['XMP-iptcCore:CreatorContactInfo.CiTelWork'] + ' -  value'
    if valstr != '':
        valobj1['CiTelWork'] = valstr
    valstr = ipmdpval['XMP-iptcCore:CreatorContactInfo.CiAdrPcode'] + ' -  value'
    if valstr != '':
        valobj1['CiAdrPcode'] = valstr
    valstr = ipmdpval['XMP-iptcCore:CreatorContactInfo.CiAdrRegion'] + ' -  value'
    if valstr != '':
        valobj1['CiAdrRegion'] = valstr
    valstr = ipmdpval['XMP-iptcCore:CreatorContactInfo.CiUrlWork'] + ' -  value'
    if valstr != '':
        valobj1['CiUrlWork'] = valstr
    # STRUCTURE END ContactInfo: arrayround = 0 - recursion = 1
    pmd['XMP-iptcCore:CreatorContactInfo'] = valobj1
    valstr = ipmdpval['IPTC:Contact']
    if valstr != '':
        pmd['IPTC:Contact'] = valstr

    # PMD property Creator´s jobtitle
    valstr = ipmdpval['XMP-photoshop:AuthorsPosition']
    if valstr != '':
        pmd['XMP-photoshop:AuthorsPosition'] = valstr
    valstr = ipmdpval['IPTC:By-lineTitle']
    if valstr != '':
        pmd['IPTC:By-lineTitle'] = valstr

    # PMD property Credit Line
    valstr = ipmdpval['XMP-photoshop:Credit']
    if valstr != '':
        pmd['XMP-photoshop:Credit'] = valstr
    valstr = ipmdpval['IPTC:Credit']
    if valstr != '':
        pmd['IPTC:Credit'] = valstr

    # PMD property Date Created
    valstr = ipmdpval['XMP-photoshop:DateCreated']
    if valstr != '':
        pmd['XMP-photoshop:DateCreated'] = valstr
    tempval = ipmdpval['IPTC:DateCreated+IPTC:TimeCreated']
    valparts = tempval.split(' ')
    valstr = valparts[0]
    if valstr != '':
        pmd['IPTC:DateCreated'] = valstr
    valstr = valparts[1]
    if valstr != '':
        pmd['IPTC:TimeCreated'] = valstr

    # PMD property Description
    valstr = ipmdpval['XMP-dc:Description']
    if valstr != '':
        pmd['XMP-dc:Description'] = valstr
    valstr = ipmdpval['IPTC:Caption-Abstract']
    if valstr != '':
        pmd['IPTC:Caption-Abstract'] = valstr
    valstr = ipmdpval['EXIF:ImageDescription']
    if valstr != '':
        pmd['EXIF:ImageDescription'] = valstr

    # PMD property Description Writer
    valstr = ipmdpval['XMP-photoshop:CaptionWriter']
    if valstr != '':
        pmd['XMP-photoshop:CaptionWriter'] = valstr
    valstr = ipmdpval['IPTC:Writer-Editor']
    if valstr != '':
        pmd['IPTC:Writer-Editor'] = valstr

    # PMD property Headline
    valstr = ipmdpval['XMP-photoshop:Headline']
    if valstr != '':
        pmd['XMP-photoshop:Headline'] = valstr
    valstr = ipmdpval['IPTC:Headline']
    if valstr != '':
        pmd['IPTC:Headline'] = valstr

    # PMD property Instructions
    valstr = ipmdpval['XMP-photoshop:Instructions']
    if valstr != '':
        pmd['XMP-photoshop:Instructions'] = valstr
    valstr = ipmdpval['IPTC:SpecialInstructions']
    if valstr != '':
        pmd['IPTC:SpecialInstructions'] = valstr

    # PMD property Intellectual Genre
    valstr = ipmdpval['XMP-iptcCore:IntellectualGenre']
    if valstr != '':
        pmd['XMP-iptcCore:IntellectualGenre'] = valstr
    valstr = ipmdpval['IPTC:ObjectAttributeReference']
    if valstr != '':
        pmd['IPTC:ObjectAttributeReference'] = valstr

    # PMD property Job Id
    valstr = ipmdpval['XMP-photoshop:TransmissionReference']
    if valstr != '':
        pmd['XMP-photoshop:TransmissionReference'] = valstr
    valstr = ipmdpval['IPTC:OriginalTransmissionReference']
    if valstr != '':
        pmd['IPTC:OriginalTransmissionReference'] = valstr

    # PMD property Keywords
    vallist = []
    valstr = ipmdpval['XMP-dc:Subject'] + ' - value 1'
    if valstr != '':
        vallist.append(valstr)
    valstr = ipmdpval['XMP-dc:Subject'] + ' value 2'
    if valstr != '':
        vallist.append(valstr)
    pmd['XMP-dc:Subject'] = vallist
    vallist = []
    valstr = ipmdpval['IPTC:Keywords'] + ' - value 1'
    if valstr != '':
        vallist.append(valstr)
    valstr = ipmdpval['IPTC:Keywords'] + ' value 2'
    if valstr != '':
        vallist.append(valstr)
    pmd['IPTC:Keywords'] = vallist

    # PMD property Province or State (legacy)
    valstr = ipmdpval['XMP-photoshop:State']
    if valstr != '':
        pmd['XMP-photoshop:State'] = valstr
    valstr = ipmdpval['IPTC:Province-State']
    if valstr != '':
        pmd['IPTC:Province-State'] = valstr

    # PMD property Rights Usage Terms
    valstr = ipmdpval['XMP-xmpRights:UsageTerms']
    if valstr != '':
        pmd['XMP-xmpRights:UsageTerms'] = valstr

    # PMD property Scene Code
    vallist = []
    valstr = ipmdpval['XMP-iptcCore:Scene'] + ' - value 1'
    if valstr != '':
        vallist.append(valstr)
    valstr = ipmdpval['XMP-iptcCore:Scene'] + ' value 2'
    if valstr != '':
        vallist.append(valstr)
    pmd['XMP-iptcCore:Scene'] = vallist

    # PMD property Source
    valstr = ipmdpval['XMP-photoshop:Source']
    if valstr != '':
        pmd['XMP-photoshop:Source'] = valstr
    valstr = ipmdpval['IPTC:Source']
    if valstr != '':
        pmd['IPTC:Source'] = valstr

    # PMD property Subject Code
    vallist = []
    valstr = ipmdpval['XMP-iptcCore:SubjectCode'] + ' - value 1'
    if valstr != '':
        vallist.append(valstr)
    valstr = ipmdpval['XMP-iptcCore:SubjectCode'] + ' value 2'
    if valstr != '':
        vallist.append(valstr)
    pmd['XMP-iptcCore:SubjectCode'] = vallist
    vallist = []
    valstr = ipmdpval['IPTC:SubjectReference'] + ' - value 1'
    if valstr != '':
        vallist.append(valstr)
    valstr = ipmdpval['IPTC:SubjectReference'] + ' value 2'
    if valstr != '':
        vallist.append(valstr)
    pmd['IPTC:SubjectReference'] = vallist

    # PMD property Sublocation (legacy)
    valstr = ipmdpval['XMP-iptcCore:Location']
    if valstr != '':
        pmd['XMP-iptcCore:Location'] = valstr
    valstr = ipmdpval['IPTC:Sub-location']
    if valstr != '':
        pmd['IPTC:Sub-location'] = valstr

    # PMD property Title
    valstr = ipmdpval['XMP-dc:Title']
    if valstr != '':
        pmd['XMP-dc:Title'] = valstr
    valstr = ipmdpval['IPTC:ObjectName']
    if valstr != '':
        pmd['IPTC:ObjectName'] = valstr

    # PMD property Additional Model Information
    valstr = ipmdpval['XMP-iptcExt:AdditionalModelInformation']
    if valstr != '':
        pmd['XMP-iptcExt:AdditionalModelInformation'] = valstr

    # PMD property Artwork or Object in the Image
    vallist = []
    # * STRUCTURE ArtworkOrObjectDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCircaDateCreated'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOCircaDateCreated'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOContentDescription'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOContentDescription'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOContributionDescription'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOContributionDescription'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCopyrightNotice'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOCopyrightNotice'] = valstr
    vallist1 = []
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCreator'] + ' -  value 1  [1]'
    if valstr != '':
        vallist1.append(valstr)
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCreator'] + ' -  value 2 [1]'
    if valstr != '':
        vallist1.append(valstr)
    valobj1['AOCreator'] = vallist1
    vallist1 = []
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCreatorId'] + ' -  value 1  [1]'
    if valstr != '':
        vallist1.append(valstr)
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCreatorId'] + ' -  value 2 [1]'
    if valstr != '':
        vallist1.append(valstr)
    valobj1['AOCreatorId'] = vallist1
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCurrentCopyrightOwnerId'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOCurrentCopyrightOwnerId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCurrentCopyrightOwnerName'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOCurrentCopyrightOwnerName'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCurrentLicensorId'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOCurrentLicensorId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCurrentLicensorName'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOCurrentLicensorName'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AODateCreated']
    if valstr != '':
        valobj1['AODateCreated'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOPhysicalDescription'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOPhysicalDescription'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOSource'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOSource'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOSourceInvNo'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOSourceInvNo'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOSourceInvURL'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOSourceInvURL'] = valstr
    vallist1 = []
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOStylePeriod'] + ' -  value 1  [1]'
    if valstr != '':
        vallist1.append(valstr)
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOStylePeriod'] + ' -  value 2 [1]'
    if valstr != '':
        vallist1.append(valstr)
    valobj1['AOStylePeriod'] = vallist1
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOTitle'] + ' -  value [1]'
    if valstr != '':
        valobj1['AOTitle'] = valstr
    # STRUCTURE END ArtworkOrObjectDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE ArtworkOrObjectDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCircaDateCreated'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOCircaDateCreated'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOContentDescription'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOContentDescription'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOContributionDescription'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOContributionDescription'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCopyrightNotice'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOCopyrightNotice'] = valstr
    vallist1 = []
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCreator'] + ' -  value 1  [2]'
    if valstr != '':
        vallist1.append(valstr)
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCreator'] + ' -  value 2 [2]'
    if valstr != '':
        vallist1.append(valstr)
    valobj1['AOCreator'] = vallist1
    vallist1 = []
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCreatorId'] + ' -  value 1  [2]'
    if valstr != '':
        vallist1.append(valstr)
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCreatorId'] + ' -  value 2 [2]'
    if valstr != '':
        vallist1.append(valstr)
    valobj1['AOCreatorId'] = vallist1
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCurrentCopyrightOwnerId'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOCurrentCopyrightOwnerId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCurrentCopyrightOwnerName'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOCurrentCopyrightOwnerName'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCurrentLicensorId'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOCurrentLicensorId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOCurrentLicensorName'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOCurrentLicensorName'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AODateCreated']
    if valstr != '':
        valobj1['AODateCreated'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOPhysicalDescription'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOPhysicalDescription'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOSource'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOSource'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOSourceInvNo'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOSourceInvNo'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOSourceInvURL'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOSourceInvURL'] = valstr
    vallist1 = []
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOStylePeriod'] + ' -  value 1  [2]'
    if valstr != '':
        vallist1.append(valstr)
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOStylePeriod'] + ' -  value 2 [2]'
    if valstr != '':
        vallist1.append(valstr)
    valobj1['AOStylePeriod'] = vallist1
    valstr = ipmdpval['XMP-iptcExt:ArtworkOrObject.AOTitle'] + ' -  value [2]'
    if valstr != '':
        valobj1['AOTitle'] = valstr
    # STRUCTURE END ArtworkOrObjectDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    pmd['XMP-iptcExt:ArtworkOrObject'] = vallist

    # PMD property Code of Organisation Featured in the Image
    vallist = []
    valstr = ipmdpval['XMP-iptcExt:OrganisationInImageCode'] + ' - value 1'
    if valstr != '':
        vallist.append(valstr)
    valstr = ipmdpval['XMP-iptcExt:OrganisationInImageCode'] + ' value 2'
    if valstr != '':
        vallist.append(valstr)
    pmd['XMP-iptcExt:OrganisationInImageCode'] = vallist

    # PMD property Copyright Owner
    vallist = []
    # * STRUCTURE PlusEntityDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-plus:CopyrightOwner.ID'] + ' -  value [1]'
    if valstr != '':
        valobj1['CopyrightOwnerID'] = valstr
    valstr = ipmdpval['XMP-plus:CopyrightOwner.Name'] + ' -  value [1]'
    if valstr != '':
        valobj1['CopyrightOwnerName'] = valstr
    # STRUCTURE END PlusEntityDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE PlusEntityDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-plus:CopyrightOwner.ID'] + ' -  value [2]'
    if valstr != '':
        valobj1['CopyrightOwnerID'] = valstr
    valstr = ipmdpval['XMP-plus:CopyrightOwner.Name'] + ' -  value [2]'
    if valstr != '':
        valobj1['CopyrightOwnerName'] = valstr
    # STRUCTURE END PlusEntityDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    pmd['XMP-plus:CopyrightOwner'] = vallist

    # PMD property CV-Term About Image
    vallist = []
    # * STRUCTURE CVTermDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-iptcExt:AboutCvTerm.CvId'] + ' -  value [1]'
    if valstr != '':
        valobj1['CvId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:AboutCvTerm.CvTermId'] + ' -  value [1]'
    if valstr != '':
        valobj1['CvTermId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:AboutCvTerm.CvTermName'] + ' -  value [1]'
    if valstr != '':
        valobj1['CvTermName'] = valstr
    valstr = ipmdpval['XMP-iptcExt:AboutCvTerm.CvTermRefinedAbout'] + ' -  value [1]'
    if valstr != '':
        valobj1['CvTermRefinedAbout'] = valstr
    # STRUCTURE END CVTermDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE CVTermDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-iptcExt:AboutCvTerm.CvId'] + ' -  value [2]'
    if valstr != '':
        valobj1['CvId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:AboutCvTerm.CvTermId'] + ' -  value [2]'
    if valstr != '':
        valobj1['CvTermId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:AboutCvTerm.CvTermName'] + ' -  value [2]'
    if valstr != '':
        valobj1['CvTermName'] = valstr
    valstr = ipmdpval['XMP-iptcExt:AboutCvTerm.CvTermRefinedAbout'] + ' -  value [2]'
    if valstr != '':
        valobj1['CvTermRefinedAbout'] = valstr
    # STRUCTURE END CVTermDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    pmd['XMP-iptcExt:AboutCvTerm'] = vallist

    # PMD property Digital Image GUID
    valstr = ipmdpval['XMP-iptcExt:DigitalImageGUID']
    if valstr != '':
        pmd['XMP-iptcExt:DigitalImageGUID'] = valstr

    # PMD property Digital Source Type
    valstr = ipmdpval['XMP-iptcExt:DigitalSourceType']
    if valstr != '':
        pmd['XMP-iptcExt:DigitalSourceType'] = valstr

    # PMD property Embedded Encoded Rights Expression
    vallist = []
    # * STRUCTURE EEREDEtails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-iptcExt:EmbdEncRightsExpr.EncRightsExpr'] + ' -  value [1]'
    if valstr != '':
        valobj1['EncRightsExpr'] = valstr
    valstr = ipmdpval['XMP-iptcExt:EmbdEncRightsExpr.RightsExprEncType'] + ' -  value [1]'
    if valstr != '':
        valobj1['RightsExprEncType'] = valstr
    valstr = ipmdpval['XMP-iptcExt:EmbdEncRightsExpr.RightsExprLangId'] + ' -  value [1]'
    if valstr != '':
        valobj1['RightsExprLangId'] = valstr
    # STRUCTURE END EEREDEtails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE EEREDEtails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-iptcExt:EmbdEncRightsExpr.EncRightsExpr'] + ' -  value [2]'
    if valstr != '':
        valobj1['EncRightsExpr'] = valstr
    valstr = ipmdpval['XMP-iptcExt:EmbdEncRightsExpr.RightsExprEncType'] + ' -  value [2]'
    if valstr != '':
        valobj1['RightsExprEncType'] = valstr
    valstr = ipmdpval['XMP-iptcExt:EmbdEncRightsExpr.RightsExprLangId'] + ' -  value [2]'
    if valstr != '':
        valobj1['RightsExprLangId'] = valstr
    # STRUCTURE END EEREDEtails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    pmd['XMP-iptcExt:EmbdEncRightsExpr'] = vallist

    # PMD property Event
    valstr = ipmdpval['XMP-iptcExt:Event']
    if valstr != '':
        pmd['XMP-iptcExt:Event'] = valstr

    # PMD property Genre
    vallist = []
    # * STRUCTURE CVTermDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-iptcExt:Genre.CvId'] + ' -  value [1]'
    if valstr != '':
        valobj1['CvId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:Genre.CvTermId'] + ' -  value [1]'
    if valstr != '':
        valobj1['CvTermId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:Genre.CvTermName'] + ' -  value [1]'
    if valstr != '':
        valobj1['CvTermName'] = valstr
    valstr = ipmdpval['XMP-iptcExt:Genre.CvTermRefinedAbout'] + ' -  value [1]'
    if valstr != '':
        valobj1['CvTermRefinedAbout'] = valstr
    # STRUCTURE END CVTermDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE CVTermDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-iptcExt:Genre.CvId'] + ' -  value [2]'
    if valstr != '':
        valobj1['CvId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:Genre.CvTermId'] + ' -  value [2]'
    if valstr != '':
        valobj1['CvTermId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:Genre.CvTermName'] + ' -  value [2]'
    if valstr != '':
        valobj1['CvTermName'] = valstr
    valstr = ipmdpval['XMP-iptcExt:Genre.CvTermRefinedAbout'] + ' -  value [2]'
    if valstr != '':
        valobj1['CvTermRefinedAbout'] = valstr
    # STRUCTURE END CVTermDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    pmd['XMP-iptcExt:Genre'] = vallist

    # PMD property Image Creator
    vallist = []
    # * STRUCTURE PlusEntityDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-plus:ImageCreator.ID'] + ' -  value [1]'
    if valstr != '':
        valobj1['ImageCreatorID'] = valstr
    valstr = ipmdpval['XMP-plus:ImageCreator.Name'] + ' -  value [1]'
    if valstr != '':
        valobj1['ImageCreatorName'] = valstr
    # STRUCTURE END PlusEntityDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE PlusEntityDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-plus:ImageCreator.ID'] + ' -  value [2]'
    if valstr != '':
        valobj1['ImageCreatorID'] = valstr
    valstr = ipmdpval['XMP-plus:ImageCreator.Name'] + ' -  value [2]'
    if valstr != '':
        valobj1['ImageCreatorName'] = valstr
    # STRUCTURE END PlusEntityDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    pmd['XMP-plus:ImageCreator'] = vallist

    # PMD property Image Rating
    valstr = ipmdpval['XMP-xmp:Rating']
    valnumber = float(valstr)
    if valnumber:
        pmd['XMP-xmp:Rating'] = valnumber

    # PMD property Image Registry Entry
    vallist = []
    # * STRUCTURE RegistryEntryDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-iptcExt:RegistryID.RegItemId'] + ' -  value [1]'
    if valstr != '':
        valobj1['RegItemId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:RegistryID.RegOrgId'] + ' -  value [1]'
    if valstr != '':
        valobj1['RegOrgId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:RegistryID.RegEntryRole'] + ' -  value [1]'
    if valstr != '':
        valobj1['RegEntryRole'] = valstr
    # STRUCTURE END RegistryEntryDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE RegistryEntryDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-iptcExt:RegistryID.RegItemId'] + ' -  value [2]'
    if valstr != '':
        valobj1['RegItemId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:RegistryID.RegOrgId'] + ' -  value [2]'
    if valstr != '':
        valobj1['RegOrgId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:RegistryID.RegEntryRole'] + ' -  value [2]'
    if valstr != '':
        valobj1['RegEntryRole'] = valstr
    # STRUCTURE END RegistryEntryDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    pmd['XMP-iptcExt:RegistryID'] = vallist

    # PMD property Image Supplier
    vallist = []
    # * STRUCTURE PlusEntityDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-plus:ImageSupplier.ID'] + ' -  value [1]'
    if valstr != '':
        valobj1['ImageSupplierID'] = valstr
    valstr = ipmdpval['XMP-plus:ImageSupplier.Name'] + ' -  value [1]'
    if valstr != '':
        valobj1['ImageSupplierName'] = valstr
    # STRUCTURE END PlusEntityDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE PlusEntityDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-plus:ImageSupplier.ID'] + ' -  value [2]'
    if valstr != '':
        valobj1['ImageSupplierID'] = valstr
    valstr = ipmdpval['XMP-plus:ImageSupplier.Name'] + ' -  value [2]'
    if valstr != '':
        valobj1['ImageSupplierName'] = valstr
    # STRUCTURE END PlusEntityDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    pmd['XMP-plus:ImageSupplier'] = vallist

    # PMD property Image Supplier Image ID
    valstr = ipmdpval['XMP-plus:ImageSupplierImageID']
    if valstr != '':
        pmd['XMP-plus:ImageSupplierImageID'] = valstr

    # PMD property Licensor
    vallist = []
    # * STRUCTURE PlusEntityDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-plus:Licensor.ID'] + ' -  value [1]'
    if valstr != '':
        valobj1['LicensorID'] = valstr
    valstr = ipmdpval['XMP-plus:Licensor.Name'] + ' -  value [1]'
    if valstr != '':
        valobj1['LicensorName'] = valstr
    # STRUCTURE END PlusEntityDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE PlusEntityDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-plus:Licensor.ID'] + ' -  value [2]'
    if valstr != '':
        valobj1['LicensorID'] = valstr
    valstr = ipmdpval['XMP-plus:Licensor.Name'] + ' -  value [2]'
    if valstr != '':
        valobj1['LicensorName'] = valstr
    # STRUCTURE END PlusEntityDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    pmd['XMP-plus:Licensor'] = vallist

    # PMD property Linked  Encoded Rights Expression
    vallist = []
    # * STRUCTURE LEREDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-iptcExt:LinkedEncRightsExpr.RightsExprEncType'] + ' -  value [1]'
    if valstr != '':
        valobj1['RightsExprEncType'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LinkedEncRightsExpr.LinkedRightsExpr'] + ' -  value [1]'
    if valstr != '':
        valobj1['LinkedRightsExpr'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LinkedEncRightsExpr.RightsExprLangId'] + ' -  value [1]'
    if valstr != '':
        valobj1['RightsExprLangId'] = valstr
    # STRUCTURE END LEREDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE LEREDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-iptcExt:LinkedEncRightsExpr.RightsExprEncType'] + ' -  value [2]'
    if valstr != '':
        valobj1['RightsExprEncType'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LinkedEncRightsExpr.LinkedRightsExpr'] + ' -  value [2]'
    if valstr != '':
        valobj1['LinkedRightsExpr'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LinkedEncRightsExpr.RightsExprLangId'] + ' -  value [2]'
    if valstr != '':
        valobj1['RightsExprLangId'] = valstr
    # STRUCTURE END LEREDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    pmd['XMP-iptcExt:LinkedEncRightsExpr'] = vallist

    # PMD property Location created
    # * STRUCTURE LocationDetails: arrayround = 0 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-iptcExt:LocationCreated.City'] + ' -  value'
    if valstr != '':
        valobj1['City'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationCreated.CountryCode'] + ' -  value'
    if valstr != '':
        valobj1['CountryCode'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationCreated.CountryName'] + ' -  value'
    if valstr != '':
        valobj1['CountryName'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationCreated.LocationId'] + ' -  value'
    if valstr != '':
        valobj1['LocationId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationCreated.LocationName'] + ' -  value'
    if valstr != '':
        valobj1['LocationName'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationCreated.ProvinceState'] + ' -  value'
    if valstr != '':
        valobj1['ProvinceState'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationCreated.Sublocation'] + ' -  value'
    if valstr != '':
        valobj1['Sublocation'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationCreated.WorldRegion'] + ' -  value'
    if valstr != '':
        valobj1['WorldRegion'] = valstr
    # STRUCTURE END LocationDetails: arrayround = 0 - recursion = 1
    pmd['XMP-iptcExt:LocationCreated'] = valobj1

    # PMD property Location Shown in the Image
    vallist = []
    # * STRUCTURE LocationDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-iptcExt:LocationShown.City'] + ' -  value [1]'
    if valstr != '':
        valobj1['City'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationShown.CountryCode'] + ' -  value [1]'
    if valstr != '':
        valobj1['CountryCode'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationShown.CountryName'] + ' -  value [1]'
    if valstr != '':
        valobj1['CountryName'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationShown.LocationId'] + ' -  value [1]'
    if valstr != '':
        valobj1['LocationId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationShown.LocationName'] + ' -  value [1]'
    if valstr != '':
        valobj1['LocationName'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationShown.ProvinceState'] + ' -  value [1]'
    if valstr != '':
        valobj1['ProvinceState'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationShown.Sublocation'] + ' -  value [1]'
    if valstr != '':
        valobj1['Sublocation'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationShown.WorldRegion'] + ' -  value [1]'
    if valstr != '':
        valobj1['WorldRegion'] = valstr
    # STRUCTURE END LocationDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE LocationDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-iptcExt:LocationShown.City'] + ' -  value [2]'
    if valstr != '':
        valobj1['City'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationShown.CountryCode'] + ' -  value [2]'
    if valstr != '':
        valobj1['CountryCode'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationShown.CountryName'] + ' -  value [2]'
    if valstr != '':
        valobj1['CountryName'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationShown.LocationId'] + ' -  value [2]'
    if valstr != '':
        valobj1['LocationId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationShown.LocationName'] + ' -  value [2]'
    if valstr != '':
        valobj1['LocationName'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationShown.ProvinceState'] + ' -  value [2]'
    if valstr != '':
        valobj1['ProvinceState'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationShown.Sublocation'] + ' -  value [2]'
    if valstr != '':
        valobj1['Sublocation'] = valstr
    valstr = ipmdpval['XMP-iptcExt:LocationShown.WorldRegion'] + ' -  value [2]'
    if valstr != '':
        valobj1['WorldRegion'] = valstr
    # STRUCTURE END LocationDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    pmd['XMP-iptcExt:LocationShown'] = vallist

    # PMD property Max Avail Height
    valstr = ipmdpval['XMP-iptcExt:MaxAvailHeight']
    valnumber = int(valstr)
    if valnumber:
        pmd['XMP-iptcExt:MaxAvailHeight'] = valnumber

    # PMD property Max Avail Width
    valstr = ipmdpval['XMP-iptcExt:MaxAvailWidth']
    valnumber = int(valstr)
    if valnumber:
        pmd['XMP-iptcExt:MaxAvailWidth'] = valnumber

    # PMD property Minor Model Age Disclosure
    valstr = ipmdpval['XMP-plus:MinorModelAgeDisclosure']
    if valstr != '':
        pmd['XMP-plus:MinorModelAgeDisclosure'] = valstr

    # PMD property Model Age
    vallist = []
    valstr = ipmdpval['XMP-iptcExt:ModelAge']
    valnumber = int(valstr)
    if valnumber:
        vallist.append(valnumber)
    valstr = ipmdpval['XMP-iptcExt:ModelAge']
    valnumber = int(valstr)
    if valnumber:
        vallist.append(valnumber)
    pmd['XMP-iptcExt:ModelAge'] = vallist

    # PMD property Model Release Id
    vallist = []
    valstr = ipmdpval['XMP-plus:ModelReleaseID'] + ' - value 1'
    if valstr != '':
        vallist.append(valstr)
    valstr = ipmdpval['XMP-plus:ModelReleaseID'] + ' value 2'
    if valstr != '':
        vallist.append(valstr)
    pmd['XMP-plus:ModelReleaseID'] = vallist

    # PMD property Model Release Status
    valstr = ipmdpval['XMP-plus:ModelReleaseStatus']
    if valstr != '':
        pmd['XMP-plus:ModelReleaseStatus'] = valstr

    # PMD property Name of Organisation Featured in the Image
    vallist = []
    valstr = ipmdpval['XMP-iptcExt:OrganisationInImageName'] + ' - value 1'
    if valstr != '':
        vallist.append(valstr)
    valstr = ipmdpval['XMP-iptcExt:OrganisationInImageName'] + ' value 2'
    if valstr != '':
        vallist.append(valstr)
    pmd['XMP-iptcExt:OrganisationInImageName'] = vallist

    # PMD property Person Shown in the Image
    vallist = []
    valstr = ipmdpval['XMP-iptcExt:PersonInImage'] + ' - value 1'
    if valstr != '':
        vallist.append(valstr)
    valstr = ipmdpval['XMP-iptcExt:PersonInImage'] + ' value 2'
    if valstr != '':
        vallist.append(valstr)
    pmd['XMP-iptcExt:PersonInImage'] = vallist

    # PMD property Person Shown in the Image with Details
    vallist = []
    # * STRUCTURE PersonDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    vallist1 = []
    # * STRUCTURE CVTermDetails: arrayround = 1 - recursion = 2
    valobj2 = {}
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvId'] + ' -  value [1]'
    if valstr != '':
        valobj2['CvId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermId'] + ' -  value [1]'
    if valstr != '':
        valobj2['CvTermId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermName'] + ' -  value [1]'
    if valstr != '':
        valobj2['CvTermName'] = valstr
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermRefinedAbout'] + ' -  value [1]'
    if valstr != '':
        valobj2['CvTermRefinedAbout'] = valstr
    # STRUCTURE END CVTermDetails: arrayround = 1 - recursion = 2
    vallist1.append(valobj2)
    # * STRUCTURE CVTermDetails: arrayround = 2 - recursion = 2
    valobj2 = {}
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvId'] + ' -  value [2]'
    if valstr != '':
        valobj2['CvId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermId'] + ' -  value [2]'
    if valstr != '':
        valobj2['CvTermId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermName'] + ' -  value [2]'
    if valstr != '':
        valobj2['CvTermName'] = valstr
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermRefinedAbout'] + ' -  value [2]'
    if valstr != '':
        valobj2['CvTermRefinedAbout'] = valstr
    # STRUCTURE END CVTermDetails: arrayround = 2 - recursion = 2
    vallist1.append(valobj2)
    valobj1['PersonCharacteristic'] = vallist1
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonDescription'] + ' -  value [1]'
    if valstr != '':
        valobj1['PersonDescription'] = valstr
    vallist1 = []
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonId'] + ' -  value 1  [1]'
    if valstr != '':
        vallist1.append(valstr)
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonId'] + ' -  value 2 [1]'
    if valstr != '':
        vallist1.append(valstr)
    valobj1['PersonId'] = vallist1
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonName'] + ' -  value [1]'
    if valstr != '':
        valobj1['PersonName'] = valstr
    # STRUCTURE END PersonDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE PersonDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    vallist1 = []
    # * STRUCTURE CVTermDetails: arrayround = 1 - recursion = 2
    valobj2 = {}
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvId'] + ' -  value [1]'
    if valstr != '':
        valobj2['CvId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermId'] + ' -  value [1]'
    if valstr != '':
        valobj2['CvTermId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermName'] + ' -  value [1]'
    if valstr != '':
        valobj2['CvTermName'] = valstr
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermRefinedAbout'] + ' -  value [1]'
    if valstr != '':
        valobj2['CvTermRefinedAbout'] = valstr
    # STRUCTURE END CVTermDetails: arrayround = 1 - recursion = 2
    vallist1.append(valobj2)
    # * STRUCTURE CVTermDetails: arrayround = 2 - recursion = 2
    valobj2 = {}
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvId'] + ' -  value [2]'
    if valstr != '':
        valobj2['CvId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermId'] + ' -  value [2]'
    if valstr != '':
        valobj2['CvTermId'] = valstr
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermName'] + ' -  value [2]'
    if valstr != '':
        valobj2['CvTermName'] = valstr
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonCharacteristic.CvTermRefinedAbout'] + ' -  value [2]'
    if valstr != '':
        valobj2['CvTermRefinedAbout'] = valstr
    # STRUCTURE END CVTermDetails: arrayround = 2 - recursion = 2
    vallist1.append(valobj2)
    valobj1['PersonCharacteristic'] = vallist1
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonDescription'] + ' -  value [2]'
    if valstr != '':
        valobj1['PersonDescription'] = valstr
    vallist1 = []
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonId'] + ' -  value 1  [2]'
    if valstr != '':
        vallist1.append(valstr)
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonId'] + ' -  value 2 [2]'
    if valstr != '':
        vallist1.append(valstr)
    valobj1['PersonId'] = vallist1
    valstr = ipmdpval['XMP-iptcExt:PersonInImageWDetails.PersonName'] + ' -  value [2]'
    if valstr != '':
        valobj1['PersonName'] = valstr
    # STRUCTURE END PersonDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    pmd['XMP-iptcExt:PersonInImageWDetails'] = vallist

    # PMD property Product Shown in the Image
    vallist = []
    # * STRUCTURE ProductDetails: arrayround = 1 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-iptcExt:ProductInImage.ProductDescription'] + ' -  value [1]'
    if valstr != '':
        valobj1['ProductDescription'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ProductInImage.ProductGTIN'] + ' -  value [1]'
    if valstr != '':
        valobj1['ProductGTIN'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ProductInImage.ProductName'] + ' -  value [1]'
    if valstr != '':
        valobj1['ProductName'] = valstr
    # STRUCTURE END ProductDetails: arrayround = 1 - recursion = 1
    vallist.append(valobj1)
    # * STRUCTURE ProductDetails: arrayround = 2 - recursion = 1
    valobj1 = {}
    valstr = ipmdpval['XMP-iptcExt:ProductInImage.ProductDescription'] + ' -  value [2]'
    if valstr != '':
        valobj1['ProductDescription'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ProductInImage.ProductGTIN'] + ' -  value [2]'
    if valstr != '':
        valobj1['ProductGTIN'] = valstr
    valstr = ipmdpval['XMP-iptcExt:ProductInImage.ProductName'] + ' -  value [2]'
    if valstr != '':
        valobj1['ProductName'] = valstr
    # STRUCTURE END ProductDetails: arrayround = 2 - recursion = 1
    vallist.append(valobj1)
    pmd['XMP-iptcExt:ProductInImage'] = vallist

    # PMD property Property Release Id
    vallist = []
    valstr = ipmdpval['XMP-plus:PropertyReleaseID'] + ' - value 1'
    if valstr != '':
        vallist.append(valstr)
    valstr = ipmdpval['XMP-plus:PropertyReleaseID'] + ' value 2'
    if valstr != '':
        vallist.append(valstr)
    pmd['XMP-plus:PropertyReleaseID'] = vallist

    # PMD property Property Release Status
    valstr = ipmdpval['XMP-plus:PropertyReleaseStatus']
    if valstr != '':
        pmd['XMP-plus:PropertyReleaseStatus'] = valstr

    # PMD property Web Statement of Rights
    valstr = ipmdpval['XMP-xmpRights:WebStatement']
    if valstr != '':
        pmd['XMP-xmpRights:WebStatement'] = valstr

    print(pmd)

    exifToolWrapper = []
    exifToolWrapper.append(pmd)

    # **************************************************************************
    # finally: making a pretty JSON file for exiftool
    print(json.dumps(exifToolWrapper, indent=4))
    with open(jsonOutputFp, 'w') as fp:
        json.dump(exifToolWrapper, fp, indent=4)



generate_IPTCPMD_etJSON()




