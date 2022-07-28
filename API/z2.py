from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime,re,random,json
import xml.etree.cElementTree as ET

# generate main route for ip and countries
root = ET.Element("data")


random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen('http://ru.wikipedia.org' + articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

def getHistoryIPs(pageUrl):
    pageUrl = pageUrl.replace('/wiki/', '')
    historyUrl = f'http://ru.wikipedia.org/w/index.php?title={pageUrl}&action=history'
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html)
    ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

def getCountry(ipAddress):
    try:
        response = urlopen(f"http://ip-api.com/json/{ipAddress}").read().decode('utf-8')
    except Exception:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country")

links = getLinks("/wiki/Python_(programming_language)")
while(len(links) > 0):
    for link in links:

        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                # create subelements for xml files
                url = link.attrs["href"]
                doc = ET.SubElement(root, f'http://ru.wikipedia.org/w/index.php?title={url}&action=history')
                ET.SubElement(doc, "IP_address").text = historyIP
                ET.SubElement(doc, "Country").text = country
                tree = ET.ElementTree(root)
                ET.indent(tree, ' ')
                tree.write("data.xml")


    newLinks = links[random.randint(0, len(links) - 1)].attrs['href']
    links = getLinks(newLinks)
