from .phoneData import phoneData

phone_data = phoneData()

class printPhone:

    #주요기관 전화번호를 정보를 리턴해준다.
    def departmentPrint(self, data):
        resultArray = []
        department = phone_data.phoneDepartment()
        for i in range(len(department)):
            if department[i][0].find(data.upper()) != -1:
                resultArray.append(department[i])

        return self.arrayToString_2(resultArray)

    #과사무실 전화번호 정보를 리턴해준다.
    def majorPrint(self, data):
        cheaking = 0
        major = phone_data.phoneMajor()
        for i in range(len(major)):                     #찾는 정보가 바로 일치할때 ex)학사종합지원센터, 스페인어통번역학과
            if major[i][0].find(data) != -1:
                cheaking += 1
                return self.arrayToString(major[i])

        #찾는 정보가 바로 일치하지 않아서 글자 하나씩 비교해서 찾을때
        # ex>일통, 스통 -> '일','통'이  과사무실이름에 전부 들어있으면 출력한다.
        if cheaking == 0:
            for i in range(len(major)):
                check = 0                               #check는 들어온 단어의 한 글자가 일치하는지 체크
                for j in range(len(data)):
                    if major[i][0].find(data[j]) != -1:
                        check += 1

                if check >= len(data):                  #cheak가 들어온 단어(dat)의 길이보다 크면 출력한다.
                    return self.arrayToString(major[i])

    #치킨집 전화번호를 리턴해준다.
    def chickenPrint(self, num , data):
        chicken = phone_data.phoneChicken()

        #치킨집 전화번호 전체를 찾을 때
        if num == 11:
            return self.arrayToString_2(chicken)

        #정확한 치킨집 이름을 입력했을 경우 ex>미파닭
        elif num == 5:
            checking = 0
            for i in range(len(chicken)):                   #찾는정보가 바로 일치할때
                if chicken[i][0].find(data) != -1:
                    checking += 1
                    return self.arrayToString(chicken[i])


            if checking == 0:                              #찾는정보가 바로 일치하지 않을때
                for i in range(len(chicken)):
                    check = 0
                    for j in range(len(data)):
                        if chicken[i][0].find(data[j]) != -1:
                            check += 1
                    if check >= len(data):
                        return self.arrayToString(chicken[i])

    # 피자집 전화번호를 리턴해준다.
    def pizzaPrint(self, num, data):
        pizza = phone_data.phonePizza()
        if num == 12:
            return self.arrayToString_2(pizza)

        elif num == 6:
            checking = 0
            for i in range(len(pizza)):
                if pizza[i][0].find(data) != -1:
                    checking += 1
                    return self.arrayToString(pizza[i])


            if checking == 0:
                for i in range(pizza):
                    check = 0
                    for j in range(len(data)):
                        if pizza[i][0].find(data[j]) != -1:
                            check += 1
                    if check >= len(data):
                        return self.arrayToString(pizza[i])

    # 중국집 전화번호를 리턴해준다.
    def chinaPrint(self, num, data):
        china = phone_data.phoneChina()
        if num == 13:
            return self.arrayToString_2(china)

        elif num == 7:
            for i in range(len(china)):
                if china[i][0].find(data) != -1:
                    return self.arrayToString(china[i])

    # 족발,보쌈집 전화번호를 리턴해준다.
    def jokbalPrint(self, num, data):
        jokbal = phone_data.phoneJokbal()
        if num == 14:
            return self.arrayToString_2(jokbal)

        elif num == 8:
            for i in range(len(jokbal)):
                if jokbal[i][0].find(data) != -1:
                    return self.arrayToString(jokbal[i])

    # 분식집 전화번호를 리턴해준다.
    def snackPrint(self, num, data):
        snack = phone_data.phoneSnack()
        if num == 15:
            return self.arrayToString_2(snack)

        elif num == 9:
            checking = 0
            for i in range(len(snack)):
                if snack[i][0].find(data) != -1:
                    checking += 1
                    return self.arrayToString(snack[i])


            if checking == 0:
                for i in range(len(snack)):
                    check = 0
                    for j in range(len(data)):
                        if snack[i][0].find(data[j]) != -1:
                            check += 1
                    if check >= len(data):
                        return self.arrayToString(snack[i])

    # 요리류집 전화번호를 리턴해준다.
    def foodPrint(self, num, data):
        food = phone_data.phoneFood()
        if num == 16:
            return self.arrayToString_2(food)

        elif num == 10:
            checking = 0
            for i in range(len(food)):
                if food[i][0].find(data) != -1:
                    checking += 1
                    return self.arrayToString(food[i])


            if checking == 0:
                for i in range(len(food)):
                    check = 0
                    for j in range(len(data)):
                        if food[i][0].find(data[j]) != -1:
                            check += 1
                    if check >= len(data):
                        return self.arrayToString(food[i])

    #1차원배열을 String 타입으로 변환하는 함수
    def arrayToString(self, array):
        result = ''
        val = array
        count = 0

        for a in val:
            if count != 0:
                result += '\n'
            result += a
            count += 1

        return result

    #2차원배열을 String 타입으로 변환하는 함수
    def arrayToString_2(self, array):
        result = ''
        val = array
        count = 0

        for a in val:
            if count != 0:
                result += '\n'
            for b in a:
                if count != 0:
                    result += '\n'
                result += b
                count += 1

        return result
