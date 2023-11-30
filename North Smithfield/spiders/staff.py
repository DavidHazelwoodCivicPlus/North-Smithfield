import scrapy
import re


class StaffSpider(scrapy.Spider):
    name = "staff"
    allowed_domains = ["https://www.nsmithfieldri.org"]
    start_urls = ["https://www.nsmithfieldri.org/departments"]


    def parse(self, response):
        rows = response.xpath('//tbody/tr')
        for row in rows :
            def extractNumber(text) :
                for c in text :
                    if c.isdigit() == False :
                        text.replace(c, '')
                    return text
            name = row.xpath('normalize-space(td[@class="views-field views-field-title"]/a/text())').extract_first()
            address1 = row.xpath('normalize-space(td[@class="views-field views-field-address"]/div[@class="location vcard"]/div[@class="adr"]/span[@class="fn"]/text())').extract_first() 
            address2 = row.xpath('normalize-space(td[@class="views-field views-field-address"]/div[@class="location vcard"]/div[@class="adr"]/div[@class="street-address"]/text())').extract_first()
            city = row.xpath('normalize-space(td[@class="views-field views-field-address"]/div[@class="location vcard"]/div[@class="adr"]/span[@class="locality"]/text())').extract_first()
            state = row.xpath('normalize-space(td[@class="views-field views-field-address"]/div[@class="location vcard"]/div[@class="adr"]/span[@class="region"]/text())').extract_first()
            zipcode = row.xpath('normalize-space(td[@class="views-field views-field-address"]/div[@class="location vcard"]/div[@class="adr"]/span[@class="postal-code"]/text())').extract_first()
            mailAddress1 = row.xpath('normalize-space(td[@class="views-field views-field-address"]/div[@class="location vcard"]/div[@class="adr"]/div[@class="street-address"]/div[@class="additional"]/text())').extract_first()
            mailAddress2 = ''
            mailCity = ''
            mailState = ''
            mailZipcode = ''
            phoneNumber = ''
            phoneText = row.xpath('normalize-space(td[@class="views-field views-field-field-dept-phone"]/text())').extract_first()
            if(phoneText) :
                for c in phoneText :
                    if c.isdigit():
                            phoneNumber+= c
                phone = phoneNumber[:3] + "-" + phoneNumber[3:6] + "-" + phoneNumber[6:]
            else :
                phone = ''
            emergencyPhone = ''
            fax = ''
            email = ''
            showEmailAs = ''
            link = ''
            linkText = name + ' Page'
            briefDescription = ''
            subDepartment1 = row.xpath('td/a/text()').extract_first()
            subDepartment2 = ''

            if address1 == '' :
                address1 = address2
                address2 = ''

            print(mailAddress1)
            if mailAddress1 != '' :
                mailCity = row.xpath('normalize-space(td[@class="views-field views-field-address"]/div[@class="location vcard"]/div[@class="adr"]/span[@class="locality"]/text())').extract_first()
                mailState = row.xpath('normalize-space(td[@class="views-field views-field-address"]/div[@class="location vcard"]/div[@class="adr"]/span[@class="region"]/text())').extract_first()
                mailZipcode = row.xpath('normalize-space(td[@class="views-field views-field-address"]/div[@class="location vcard"]/div[@class="adr"]/span[@class="postal-code"]/text())').extract_first()



            # Everything in the yield section does not need to be touched.
            yield {
                'Name' : name,
                'Address 1' : address1,
                'Address 2' : address2,
                'City' : city,
                'State' : state,
                'Zipcode' : zipcode,
                'Mail Address 1' : mailAddress1,
                'Mail Address 2' : mailAddress2,
                'Mail City' : mailCity,
                'Mail State' : mailState,
                'Mail Zipcode' : mailZipcode,
                'Phone' : phone,
                'Emergency Phone' : emergencyPhone,
                'Fax' : fax,
                'Email' : email,
                'Show Email As' : showEmailAs,
                'Link' : link,
                'Link Text' : linkText,
                'Brief Description' : briefDescription,
                'Hidden' : 'false',
                'Show Archive' : 'false',
                'Sub Department1' : subDepartment1,
                'Sub Department2' : subDepartment2,
            }
