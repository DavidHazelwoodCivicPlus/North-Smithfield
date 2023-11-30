import scrapy
import re


class ResourceSpider(scrapy.Spider):
    name = "resource"
    start_urls = ["https://www.nsmithfieldri.org/business-directory/by-alpha/all?page=1"]


    def parse(self, response):
        rows = response.css('.views-row')
        for row in rows :
            businessName = row.css('.inner-three-column-6-3-3 h4 a ::text').get()
            contactPersonName = ''
            address1 = row.css('.street-address ::text').get()
            address2 = row.css('.additional ::text').get()
            city = row.css('.locality ::text').get()
            state = row.css('.region ::text').get()
            zipCode = row.css('.postal-code ::text').get()
            linkToMap = ''
            phoneNumber = row.css('.field-type-telephone ::text').get()
            faxNumber = ''
            emailAddress = row.css('.inner-three-column-6-3-3__second a ::attr(href)').get()
            showEmailAs = 'Email ' + row.css('.inner-three-column-6-3-3 h4 a ::text').get()
            webLink = row.css('.field-name-field-listing-website a ::attr(href)').get()
            linkText = row.css('.inner-three-column-6-3-3 h4 a ::text').get() + ' Website'
            openLinkInNewWindow = ''
            description = ''
            relatedCategories = response.css('.page-title ::text').get()

        
            # Everything in the yield section does not need to be touched.
            yield {
                'Business Name'         : businessName,
                'Contact Person Name'   : contactPersonName,
                'Address 1'             : address1,
                'Address 2'             : address2,
                'City'                  : city,
                'State'                 : state,
                'Zip Code'              : zipCode,
                'Link to Map'           : linkToMap,
                'Phone - Number'        : phoneNumber,
                'Fax - Number'          : faxNumber,
                'Email Address'         : emailAddress,
                'Show Email As'         : showEmailAs,
                'Link (web address)'    : webLink,
                'Link Text'             : linkText,
                'Open link in new window': openLinkInNewWindow,
               'Description'           : description,
               'Related Categories'    : relatedCategories,
            }



