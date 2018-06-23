from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup


class crawCal:
    def crawlingCal(self):
        try:
            html = urlopen(
                "http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=37069&siteId=hufs&menuType=T&uId=4&sortChar=AAA&menuFrame=&linkUrl=04_0101.html&mainFrame=right")
        except HTTPError as e:
            print(e)
            print('학사일정 홈페이지를 읽어올 수 없습니다.')
        else:
            bsObj = BeautifulSoup(html, "html.parser")
            calNum = [] * 13
            calName = [] * 13

        for month_number in range(0, 14):
            number = month_number
            month = '#' + str(number)
            soup = bsObj.findAll("div", {"id": month})

            for i in soup:
                num = i.findAll("td", {"valign": "top"})
                name = i.findAll("td", {"class": "_title"})
                for j in range(len(num)):
                    calNum.append([])
                    calNum[number].append(num[j].string.strip())
                    calName.append([])
                    calName[number].append(name[j].span.string.strip())


        return calNum, calName