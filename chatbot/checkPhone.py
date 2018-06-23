from .selectPhoneData import selectPhoneData
from .printPhone import printPhone

select_data = selectPhoneData().selectPhoneData()
result_print = printPhone

class checkPhone:
    def __init__(self):
        self.isRecheck = 0
        self.isFirstCheck = 0
        self.data = ''

    #selectPhoneData에서 몇번째 배열에 저장된 값인지에 따라서
    def checkPhone(self, num, data, question):
        if num == 0:                                #전화번호를 물어볼 때
            return self.checkFirst(question)
        elif num == 1:                              #학교 전화번호를 물어볼 때
            return self.checkSchool(question)
        elif num == 2:                              #배달 전화번호를 물어볼 때
            return self.checkDelivery(question)
        elif num == 3:                              #정확한 학교기관이름을 물어볼 때
            self.checkAnalogy(data)
            return result_print().departmentPrint(self.data.upper())            #.upper()는 영어소문자를 대문자로 변화해줌
        elif num == 4:                              #정확한 배달음식점이름을 물어볼 때
            self.checkAnalogy(data)
            return result_print().majorPrint(self.data.upper())
        elif num == 5 or num == 11:                 #치킨집전화번호를 물어보거나 치킨집이름을 물어볼 때
            self.checkAnalogy(data)
            return result_print().chickenPrint(num, self.data.upper())
        elif num == 6 or num == 12:                 #피자집
            return result_print().pizzaPrint(num, data)
        elif num == 7 or num == 13:                 #중국집
            return result_print().chinaPrint(num, data)
        elif num == 8 or num ==14:                  #족발집
            return result_print().jokbalPrint(num, data)
        elif num == 9 or num == 15:                 #분식집
            return result_print().snackPrint(num, data)
        elif num == 10 or num ==16:                 #요리류
            return result_print().foodPrint(num, data)

    #selectData를 다시한번 체크하는 메소드
    def reCheck(self,question, start, end):
        for i in range(start, end):
            for j in range(len(select_data[i])):
                if question.find(select_data[i][j]) != -1:
                    self.isRecheck += 1
                    num = i
                    data = select_data[i][j]
                    return self.checkPhone(num, data, question)
        return

    #묻는 문장에 '전화번호'가 들어가 있을 때
    def checkFirst(self, question):
        self.isFirstCheck += 1
        result = self.reCheck(question, 1, 17)  #자기자신을 제외하고 다른 값이 들어가 있는지 체크하기 위해서
                                                #ex> 치킨집 전화번호, 학교기관 전화번호

        if self.isRecheck == 0:                 #그냥 '전화번호'만 물어을 때 되묻는다.
            result = '학교기관 전화번호 or 배달음식 전화번호?'

        return result

    # 묻는 문장에 학교가 들어가 있을 때
    def checkSchool(self, question):
        result = self.reCheck(question, 3, 5)   #자기자신을 제외하고 다른 값이 들어가 있는지 체크하기 위해서
                                                # ex> 학종지 전화번호, 스통 전화번호

        if self.isRecheck == 0 or self.isFirstCheck != 0:   #그냥 물었을 때
            result = '어느 기관 전화번호를 알려드릴까요?\n정확한 교내기관 이름이나 학과를 입력해주세요\nex> 학사종합지원센터, 인도학과사무실'

        return result

    # 묻는 문장에 배달이 들어가 있을 때
    def checkDelivery(self, question):
        result = self.reCheck(question, 5, 17)  #자기자신을 제외하고 다른 값이 들어가 있는지 체크하기 위해서
                                                # ex> 치킨집 전화번호, 미파닭 전화번호

        if self.isRecheck == 0 or self.isFirstCheck != 0:
            result = '어느 음식점 전화번호를 알려드릴까요?\n정확한 음식점 이름이나 종류를 입력해주세요\nex> 미쳐버린파닭, 치킨'

        return result

    #사용자가 요구하는 정보가 저장해논 값(selectPhoneData)과 출력해야 될 값(phoneData)와 전혀일치 하지 않을 때
    def checkAnalogy(self, data):
        if data.find('훕스돔') != -1:
            self.data = '기숙사'
        elif data.find('학종지') != -1:
            self.data = '학사종합지원센터'
        elif data.find('잉존') != -1:
            self.data = 'ENGLISH'
        elif data.find('지비티') != -1:
            self.data = 'GBT'
        elif data.find('마통') != -1 or data.find('말레이인도') != -1 or data.find('마인어') != -1:
            self.data = '말레이·인도네시아어통번역학과'
        elif data.find('비비큐') != -1:
            self.data = 'BBQ'
        else:
            self.data = data





