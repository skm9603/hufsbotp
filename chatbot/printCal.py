from datetime import datetime
from .crawCal import crawCal

crawling = crawCal()
month = datetime.today().month
thisMonth = month

class printCal:
    def __init__(self):
        self.calNum, self.calName = crawling.crawlingCal()

    def calMonthPrint(self, month):
        calNum = self.calNum
        calName = self.calName
        resultArray = []
        for i in range(len(calNum[month])):
            resultArray.append(calNum[month][i] + '\n' +calName[month][i])  #1차원배열로 만들어서 보냄
        return self.arrayToString(resultArray)

    def checkSemester(self, data):
        checking = 0
        startNum = 0
        endNum = 0
        for i in range(len(data)):
            if data[i].find('1학기') != -1 or data[i].find('2학기') != -1 or data[i].find('동계') != -1 or data[i].find('하계') != -1 :
               checking += 1
               return self.calSelectPrint(data, 0, 14)
#              break

        if checking == 0 and thisMonth < 9:
            startNum = 0
            endNum = 7
        elif checking == 0 and thisMonth > 8:
            startNum = 9
            endNum = 14
        return self.calSelectPrint(data, startNum, endNum)


    def calSelectPrint(self, data, startNum, endNum):
        calNum = self.calNum
        calName = self.calName
        resultArray = []

        for i in range(startNum, endNum):
            for j in range(len(calName[i])):
                checking = 0
                for k in range(len(data)):
                    if calName[i][j].find(data[k]) != -1:
                        checking += 1

                if checking >= len(data):
                    resultArray.append(calNum[i][j] + '\n' + calName[i][j]) #1차원 배열로 만듬

        return self.arrayToString(resultArray)


    def arrayToString(self, array):
        result = ''
        count = 0
        for a in array:
            if count != 0:
                result += '\n'
            result += a
            count += 1

        return result
