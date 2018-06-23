import re

buildingAll = [['백년', '본관'],
               ['어문'],
               ['교양'],
               ['자대', '자연'],
               ['인문', '경상', '인경'],
               ['공학', '공대'],
               ['학생', '학관'],
               ]

checking = ['건물', '강의실', '위치']

buildingInfo = ["백년관\n건물번호 : 0 \nex) 0301->백년관 3층 301호\n", "어문학관\n건물번호 : 1\nex) 1301->어문관 3층 301호\n",
                "교양관\n건물번호 : 2\nex) 2301->교양관 3층 301호\n", "자연과학관\n건물번호 : 3\nex) 3301->자연과학관 3층 301호\n",
                "인문경상관\n건물번호 : 4\nx) 4301->인문경상관 3층 301호\n", "공학관\n건물번호 : 5 \nex) 5301->공학관 3층 301호\n",
                "학생회관\n건물번호 : 6 \nex) 6301->학생회관 3층 301호\n"
                ]

pictureUrl = [
    "http://i67.tinypic.com/5jz6ac.jpg",  # 백년
    "http://i68.tinypic.com/27x4qw.jpg",  # 어문
    "http://i66.tinypic.com/2uzp98o.jpg",  # 교양
    "http://i67.tinypic.com/5e989j.jpg",    # 자연
    "http://i66.tinypic.com/35aits7.jpg",   # 인문
    "http://i64.tinypic.com/warfw6.jpg",    # 공대
    "http://i64.tinypic.com/pzzo.jpg"   # 학생
]

class CheckBuilding:
    info = buildingInfo

    def __init__(self):
        self.where = 'empty'
        self.numb = 'empty'

    def building_check(self, question):
        self.where = question
        div_num = 0

        num = re.sub('[^0-9]', '', question)
        if (len(num) >= 3) and (len(num) <= 5):
            self.numb = num
        elif len(num) is not 0:
            self.numb = 'error'

        if len(num) >= 4:
            if '-' in question:
                div_num = 1

        check_name = self.building_classify(div_num)

        if check_name is not ('empty' or 'error'):
            return check_name

        for i in range(len(checking)):  # set number according to Building number
            if checking[i] in self.where:
                check_name = 'checkBuilding'

        return check_name

    def building_classify(self, div_num):
        info = 'empty'
        check_fin = 'empty'

        for j in range(len(buildingAll)):   # check building if building information is in where
            for i in range(len(buildingAll[j])):  # set number according to Buinding number
                if buildingAll[j][i] in self.where:
                    info = j
                    check_fin = 'finish'
                    break
            if check_fin is not 'empty':   # because of error '학관' 단어가 있을시 무조건 마지막 6번 건물번호로 가는 에러
                break

        if self.numb is not ('empty' or 'error'):  # define if there's error in numb part
            if info is 'empty':
                if len(self.numb) is 3:
                    info = 'error'
                elif (len(self.numb) is 4) and div_num is 1:
                    info = 'error'
                else:
                    info = 'number'

        if info is not ('error' or 'empty'):
            return self. result(info, div_num)
        else:
            return info

    def result(self, info, div_num):
        if info is 'number':    # Just answer class number
            a = int(self.numb[0])
            result = buildingInfo[a]+self.numb[1]+"층"+self.numb[1:4]+"호"
            if div_num is 1:
                result = result+"-1 호"
            return result

        elif info is not 'error' and info is not 'empty':  # Answer building name
            a = int(info)
            result = buildingInfo[a]
            if self.numb is not ('empty' or 'error'):    # Include class nubmer
                num_len = len(self.numb)
                if num_len is 3:
                    result = result + self.numb[0] + "층" + self.numb[0:3] + "호"
                elif num_len is 4:
                    if div_num is 0:
                        if int(self.numb[0]) != a:
                            result = result + "호실번호 에러-해당 건물의 호실번호가 아닙니다."
                        else:
                            result = result + self.numb[1] + "층" + self.numb[1:4] + "호"
                    else:
                        result = result + self.numb[0] + "층" + self.numb[0:3] + "-1 호"
                elif num_len is 5:
                    if int(self.numb[0]) != a:
                        result = result + "호실번호 에러-해당 건물의 호실번호가 아닙니다."
                    else:
                        result = result + self.numb[1] + "층" + self.numb[1:4] + "-1 호"
        elif info is 'error':
            result = 'error'
        else:
            result = "empty"
        return result
