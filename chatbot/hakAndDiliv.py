from . import checkBuildingNum
from . import haksikResult
from . import checkAll
import re, datetime

hnb = ['배고파', '배고프', '밥', '리스트', '먹지', '먹', '음식', '리스트', '메뉴']

haksikAll = [['학식', '식당', '식단'],
             ['조식', '아침'],
             ['중식', '점심'],
             ['석식', '저녁'],
             ['후식', '후복관', '후생'],
             ['어식'],
             ['기숙사', '긱식', '기식', '긱밥'],
             ['어문']
             ]

class Checking:
    def __init__(self):
        self.result = 'empty'

    def hnd(self, question):
        aaa = self.haksik(question)
        if self.haksik(question) is 'empty':
            for i in range(len(hnb)):
                if hnb[i] in question:
                    aaa = self.dilivery(question)
        if aaa is None:
            aaa = "학식 또는 배달음식 어떤 정보에 대해 알고싶으신가요?"

        return aaa

    def haksik(self, question):
        findother = 'empty'
        ha = haksikResult.HaksikResult()
        checkingDone = 0
        today = datetime.date.today()   # datetime을 통해 오늘의 날짜를 받아옴
        today_P = today.strftime("%Y%m%d")      # ex) 20180101과 같은 형식으로 나타냄
        tomorrow = today + datetime.timedelta(days=1)
        tomorrow_P = tomorrow.strftime("%Y%m%d")    # 내일을 출력

        for i in range(len(haksikAll)):
            for j in range(len(haksikAll[i])):
                if haksikAll[i][j] in question:
                    if self.result is not 'empty':
                        findother = self.result
                    self.result = i

        if self.result is 7:
            for i in range(len(hnb)):
                if hnb[i] in question:
                    findother = '1'
            if findother is not 'empty':
                if '내일' in question:
                    self.result = ha.result(5, tomorrow_P)
                else:
                    self.result = ha.result(5, today_P)
            else:
                for i in range(len(checkBuildingNum.checking)):
                    if checkBuildingNum.checking[i] in question:
                        self.result = 'building'
                        checkingDone = 1
                if '번호' in question:
                    self.result = 'building'
                    checkingDone = 1
                if 3 < len(re.sub('[^0-9]', '', question)) <= 5:
                    self.result = 'building'
                    checkingDone = 1
                if checkingDone is 0:
                    return "umon"
        elif self.result is not 'empty':
            if self.result is 0:
                if '내일' in question:
                    self.result = ha.result(self.result, 'tomorrow')
                else:
                    self.result = ha.result(self.result, today_P)
            else:
                if '내일' in question:
                    self.result = ha.result(self.result, tomorrow_P)
                else:
                    self.result = ha.result(self.result, today_P)

        return self.result

    def dilivery(self, question):
        Dchecking = checkAll.checkAll()
        checkDelivery = Dchecking.checkPhoneNumber(question)

        return checkDelivery
