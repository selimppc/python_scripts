# Python example
# http://jasminsms.com
import urllib2
import urllib
import cookielib

site= "https://login.smspicker.com/API/SendSMSV2?userId=reseller1&password=test123&commaSeperatedReceiverNumbers=8801914785791&mask=&smsText=Python"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib2.Request(site, headers=hdr)

try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.fp.read()
#content = page.read()
#print content

##############

#baseParams = {'userId':'reseller1', 'password':'test123', 'commaSeperatedReceiverNumbers':'8801914785791', 'mask':'', 'smsText':'HelloPython'}

# Send an SMS-MT with minimal parameters
#urllib2.urlopen("https://login.smspicker.com/API/SendSMSV2?%s" % urllib.urlencode(baseParams)).read()
#urllib2.urlopen("http://127.0.0.1:1401/send?%s" % urllib.urlencode(baseParams)).read()

# Send an SMS-MT with defined originating address
#baseParams['from'] = 'Jasmin GW'
#urllib2.urlopen("http://127.0.0.1:1401/send?%s" % urllib.urlencode(baseParams)).read()
#https://login.smspicker.com/API/SendSMSV2?userId=reseller1&password=test123&commaSeperatedReceiverNumbers=$to&mask=&smsText=$content
