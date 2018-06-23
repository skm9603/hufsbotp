from datetime import datetime
from .selectCalData import selectCalData
from .printCal import printCal

year = datetime.today().year
cal_data = selectCalData().selectCalData()
cal_print = printCal()


class checkCal:
    def __init__(self):
        self.isCheckFirst = 0
        self.isCheckSecond = 0
        self.isCheckThird = 0
        self.isCheckForth = 0
        self.isCheckCalendar = 0
        self.data = []
        self.month = -1

    def checkCal(self, num, data, question):
        self.__init__()
        if num == 0:
            result = self.cheakFirst(data, question)
            if self.month != -1:
                result = cal_print.calMonthPrint(self.month)
            elif self.isCheckCalendar == 0:
                result = cal_print.checkSemester(self.data)
            return result

        elif num == 1:
            self.data.append(data)
            self.isCheckSecond += 1
            self.checkSecond(question)
            return cal_print.checkSemester(self.data)
        elif num == 2:
            self.isCheckThird += 1
            self.data.append(data)
            self.checkSecond(question)
            return cal_print.checkSemester(self.data)

        elif num == 3:
            self.isCheckForth += 1
            self.data.append(data)
            self.checkForth(question)
            return cal_print.checkSemester(self.data)

        elif num == 4:
            self.data.append(data)
            return cal_print.checkSemester(self.data)

    def cheakFirst(self, data, question):
        self.isCheckFirst += 1
        if question.find('월') != -1:
            return self.checkMonth(question)
        elif question.find('일정') != -1:
            return self.checkCalendar()
        elif question.find('고사') != -1:
            self.data.append('시험')
            self.checkSecond(question)
        elif question.find('여름') != -1:
            self.data.append('하계')
            self.checkSecond(question)
        elif question.find('겨울') != -1:
            self.data.append('동계')
            self.checkSecond(question)
        elif question.find('휴학') != -1:
            self.data.append('복학')
            self.checkSecond(question)
        elif question.find('졸시') != -1 or question.find('졸업식') != -1:
            return '홈페이지 공지사항에서 열람하시기 바랍니다.'

    def checkSecond(self, question):
        self.isCheckSecond += 1
        for i in range(len(cal_data[1])):
            if question.find(cal_data[1][i]) != -1:
                self.data.append(cal_data[1][i])
                break

        if self.isCheckThird == 0:
            self.checkThrid(question)
        if self.isCheckForth == 0:
            self.checkForth(question)

    def checkThrid(self, question):
        self.isCheckThird += 1
        for i in range(len(cal_data[2])):
            if question.find(cal_data[2][i]) != -1:
                self.data.append(cal_data[2][i])
                break

        if self.isCheckSecond == 0:
            self.checkSecond(question)
        if self.isCheckForth == 0:
            self.checkForth(question)

    def checkForth(self, question):
        self.isCheckForth += 1
        for i in range(len(cal_data[3])):
            if question.find(cal_data[3][i]) != -1:
                self.data.append(cal_data[3][i])
                break

        if self.isCheckSecond == 0:
            self.checkSecond(question)
        if self.isCheckThird == 0:
            self.checkThrid(question)

    # 학사일점만 물어봤을 때
    def checkCalendar(self):
        self.isCheckCalendar += 1
        return '어떤 학사일정을 알려드릴까요?\n정확한 월이나 행사를 입력해주세요\nex>2월, 중간시험'

    # X달을 물어봤을 경우, 2019년도 달은 ㅎ.....너무 복잡해져서 뺐습니다....2019년 2월, 2019년 3월 내년 1월까지만 달은 출력
    # 행사를 물었을때는 2019년도 2,3월 달 내용도 나옴..
    def checkMonth(self, question):
        for i in range(12, 0, -1):
            if question.find(str(i)) != -1:
                self.month = i
                break

        if self.month == 1:
            self.month = self.month + 10
        else:
            self.month = self.month - 2
