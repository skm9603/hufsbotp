from .selectCalData import selectCalData
from .checkCal import checkCal
from .selectPhoneData import selectPhoneData
from .checkPhone import checkPhone

phone_data = selectPhoneData().selectPhoneData()
phone_check = checkPhone()
cal_data = selectCalData().selectCalData()
cal_check = checkCal()

class checkAll():
    #phoneNumber에 대한 질문인지 체크
    def checkPhoneNumber(self,question):
        checking = 0
        result = None

        for i in range(len(phone_data)):
            for j in range(len(phone_data[i])):
                if question.find(phone_data[i][j]) != -1:
                    checking += 1
                    num = i
                    data = phone_data[i][j]
                    phone_check.__init__() #생성자를 초기화하기 위해서
                    result = phone_check.checkPhone(num, data, question)
            if checking >= 1:
                break
            else:
                continue

        return result
    #Calendar에 대한 질문인지 체크
    def checkCalendar(self,question):
        checking = 0
        for i in range(len(cal_data)):
            for j in range(len(cal_data[i])):
                if question.find(cal_data[i][j]) != -1:
                    checking += 1
                    num = i
                    data = cal_data[i][j]
                    cal_check.__init__() #생성자를 초기화하기 위해서
                    result = cal_check.checkCal(num, data, question)
                    return result
            if checking >= 1:
                break