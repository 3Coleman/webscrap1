# import requests
# from bs4 import BeautifulSoup
# url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
# r=requests.get(url)
# # print(r)
# soup=BeautifulSoup(r.text)
# print(soup)
# boxes=soup.findAll("div", class_="col-md-4 col-xl-4 col-lg-4")
# # print(boxes)
# # print(len(boxes))
# name=soup.find_all("a",class_="title")
# # print(name)
# # for i in name:
# #      # print(i.text)
# price=soup.find_all("h4",class_="float-end price card-pull-right price")
# for i in price:
#     print(i.text)
# import requests
# from bs4 import BeautifulSoup
# url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
# r=requests.get(url)
# print(r)
# soup=BeautifulSoup(r.text,"lxml")
# # print(soup)
# box=soup.findAll("div",class_="col-md-4 col-xl-4 col-lg-4")
# # print(box)
# title=soup.findAll("a",class_="title")
# # for i in title:
# #     # print(i.text)
# price=soup.findAll("h4",class_="float-end price card-title pull-right")
# for i in price:
#     print(i.text)


# import requests
# from bs4 import BeautifulSoup
# link="https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=06c3b9ad-fea0-4a9a-97ad-4405579a722e"
# r=requests.get(link)
# print(r)
# soup=BeautifulSoup(r.text,"lxml")
# # print(soup)
# price=soup.findAll("div",class_="_4rR01T")
# for i in price:
#     print(i.text)
# # name=soup.findAll("a",class_="title")
# # for i in name:
# #     print(i.text)





# import requests
# from bs4 import BeautifulSoup
# url="https://www.iplt20.com/auction/2022"
# r=requests.get(url)
# soup=BeautifulSoup(r.content,"html.parser")
# r1=soup.title
# print(r1.get_text())
# this one is the proper one




# import requests
# from bs4 import BeautifulSoup
# url=""
# R=requests.get("https://www.canadapost-postescanada.ca/cpc/en/personal/sending/letters-mail/postage-rates.page")
# soup=BeautifulSoup(R.content,"html.parser")
# print(soup.prettify())





# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# url="https://www.iplt20.com/auction/2022"
# r=requests.get(url)
# # print(r)
# soup=BeautifulSoup(r.text,"lxml")
# # print(soup)
# table=soup.find("table",class_="ih-td-tab auction-tbl")
# # print(table)
#
# title=table.findAll("th")
# header=[]
# for i in title:
#     name=i.text
#     header.append(name)
# # print(header)

# df=pd.DataFrame(columns=header)
# # print(df)
# row=table.findAll("tr")
# # print(row)
# for i in row[1:]:
#     first_td=i.find_all("td")[0].find("div",class_="ih-pt-ic").text.strip()
#     data=i.find_all("td")[1:]
#     # print(data)
#     row=[tr.text for tr in data]
#     # print(row)
#     row.insert(0,first_td)
#     l=len(df)
#     df.loc[l]=row
# print(df)
# df.to_csv("IPL auction stats.csv")








# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# response=requests.get("https://www.iplt20.com/auction/2022")
# soup=BeautifulSoup(response.text,"lxml")
# table=soup.find("table", class_="ih-td-tab auction-tbl")
# title=table.findAll("th")
# header=[]
# for i in title:
#     name=i.text
#     header.append(name)
#
# df=pd.DataFrame(columns=header)
# rows=table.find_all("tr")
#
# for i in rows[1:]:
#     first_td=i.find_all("td")[0].find("div",class_="ih-pt-ic").text.strip()
#     data=i.find_all("td")[1:]
#     row=[tr.text for tr in data]
#     row.insert(0,first_td)
#     l=len(df)
#     df.loc[l]=row
# print(df)
# df.to_csv("IPL auction status 2024.csv")


import requests
from bs4 import BeautifulSoup
import pandas as pd
http_response=requests.get("https://www.iplt20.com/auction/2022")
soup=BeautifulSoup(http_response.content,"html.parser")
table=soup.find("table",class_="ih-td-tab auction-tbl")
title=table.find_all("th")
header=[]
for i in title:
    name=i.text
    header.append(name)
df=pd.DataFrame(columns=header)
row=table.find_all("tr")
for i in row[1:]:
    first_td=i.find_all("td")[0].find("div",class_="ih-pt-ic").text.strip()
    data=i.find_all("td")[1:]

    row=[tr.text for tr in data]
    row.insert(0,first_td)
    l=len(df)
    df.loc[l]=row
df.to_csv("ipl auction details 2024.csv")










