from bs4 import BeautifulSoup
import requests

# HTTP Get Request
class Crawl():
    def __init__(self):
        self.answer  = 'empty'

    def HooseangHaksik(self, when, day):        # day에 오늘이면 오늘날짜 ex)20180608, 내일이면 오늘날짜 + 1을 넣는다
        haksikURL = requests.get(
            'https://wis.hufs.ac.kr/jsp/HUFS/cafeteria/viewWeek.jsp?startDt=' + day + '&endDt=' + day + '&caf_name=후생관 학생식당&caf_id=h203')

        html = haksikURL.text                   #html파일을 beautifulsoap를 통해 변환
        soup = BeautifulSoup(html, 'lxml')
        my_title = soup.select('tr')

        data = []  # 임시 저장하는 데이터 - 정리 x
        menu = []  # 들어온 메뉴들을 정리해 저장하는 데이터

        checksuk = 0 # 석식의 유무 체크

        for title in my_title:
            data.append(title.text)

        for i in data:
            if len(data) == 1:
                menu = ''
                return menu
            elif '조식' in i:
                if ('아침' in when) or ('오늘' in when):  # when 이'오늘' 일시 오늘 전체의 식단 출력
                    i = i.replace("조식1030~1130", "조식-10:30~11:30")
                    i = i.replace("\n", " ").split()
                    menu.append(i)
            elif '뚝배기1100' in i:
                if ('점심' in when) or ('오늘' in when):
                    i = i.replace("뚝배기1100~1830", "뚝배기-11:00~18:30")
                    i = i.replace("\n", " ").split()
                    menu.append(i)
            elif '일품' in i:
                if ('점심' in when) or ('오늘' in when):
                    if '일품1' in i:
                        i = i.replace("일품1", "일품1-")
                    else:
                        i = i.replace("일품2", "일품2-")
                    i = i.replace("1100~1830", "11:00~18:30")
                    i = i.replace("\n", " ").split()
                    menu.append(i)
            elif '석식' in i:
                if ('저녁' in when) or ('오늘' in when):
                    i = i.replace("석식1730~1830", "석식-17:30~18:30")
                    i = i.replace("\n", " ").split()
                    menu.append(i)

        result = ''

        for size in range(len(menu)):
            result = result + '-----------------\n'

            for detail in range(len(menu[size])):
                if detail == 0:
                    result = result + menu[size][detail] + '\n\n'
                else:
                    result = result + menu[size][detail] + '\n'

        return result

    def UmonHaksik(self, when, day):  # day에 오늘이면 오늘날짜 ex)20180608, 내일이면 오늘날짜 + 1을 넣는다
        haksikURL = requests.get(
            'https://wis.hufs.ac.kr/jsp/HUFS/cafeteria/viewWeek.jsp?startDt=' + day + '&endDt=' + day + '&caf_name=어문관&caf_id=h204')

        html = haksikURL.text  # html파일을 beautifulsoap를 통해 변환
        soup = BeautifulSoup(html, 'lxml')
        my_title = soup.select('tr')

        data = []  # 임시 저장하는 데이터 - 정리 x
        menu = []  # 들어온 메뉴들을 정리해 저장하는 데이터

        for title in my_title:
            data.append(title.text)

        for i in data:
            if len(data) == 1:
                menu = ''
                return menu
            elif '일품' in i:
                i = i.replace("일품0930~1500", "일품-09:30~15:00")
                i = i.replace("\n", " ").split()
                menu.append(i)
            elif '밥1030' in i:
                i = i.replace("\n", " ").split()
                menu.append(i)
            elif '국1030' in i:
                i = i.replace("\n", " ").split()
                menu.append(i)
            elif '반찬1030' in i:
                i = i.replace("\n", " ").split()
                menu.append(i)
            elif '김치1030' in i:
                i = i.replace("\n", " ").split()
                menu.append(i)
            elif '진라면' in i:
                break

        if when is "아침":
            return ''
        elif when is "저녁":
            return ''

        result = ''

        for size in range(len(menu)):
            if size is (0 or 1):
                result = result + '-----------------\n'
            if size is 1:
                result = result + "선택식\n\n"

            for detail in range(len(menu[size])):
                if size is not 0:
                    if detail is not 0:
                        result = result + menu[size][detail] + '\n'
                else:
                    if detail == 0:
                        result = result + menu[size][detail] + '\n\n'
                    else:
                        result = result + menu[size][detail] + '\n'

        return result

    def HufsdormHaksik(self, when, day):
        haksikURL = requests.get(
            'https://wis.hufs.ac.kr/jsp/HUFS/cafeteria/viewWeek.jsp?startDt=' + day + '&endDt=' + day + '&caf_name=HufsDorm 식당&caf_id=h205')

        html = haksikURL.text  # html파일을 beautifulsoap를 통해 변환
        soup = BeautifulSoup(html, 'lxml')
        my_title = soup.select('tr')

        data = []  # 임시 저장하는 데이터 - 정리 x
        menu = []  # 들어온 메뉴들을 정리해 저장하는 데이터

        for title in my_title:
            data.append(title.text)

        for i in data:
            if len(data) == 1:  # 길이가 0일시 - 메뉴 없을시
                menu = 'empty'
                return menu
            elif '우리 식당은' in i:  # 뒤의 넣지 않을 list들의 시작 단어
                break
            elif '조식(한식)' in i:
                if ('아침' in when) or ('오늘' in when):  # when 이'오늘' 일시 오늘 전체의 식단 출력
                    i = i.replace("(한식)0800~0930", "(한식)-08:00~09:30")
                    i = i.replace("\n", " ").split()
                    menu.append(i)
            elif '조식(T/O)' in i:
                if '운영이' and '없습니다' in i:
                    checka = 1
                elif ('아침' in when) or ('오늘' in when):  # when 이'오늘' 일시 오늘 전체의 식단 출력
                    i = i.replace("(T/O)0800~0930", "(T/O)-08:00~09:30")
                    i = i.replace("\n", " ").split()
                    menu.append(i)
            elif '중식(일반)' in i:
                if ('점심' in when) or ('오늘' in when):
                    i = i.replace("(일반)1200~1400", "(일반)-12:00~14:00")
                    i = i.replace("\n", " ").split()
                    menu.append(i)
            elif '중식(특식)' in i:
                if 'Chef' in i:  # 휴일일시 제외
                    checka = 1
                elif ('점심' in when) or ('오늘' in when):
                    i = i.replace("(특식)1200~1400", "(특식)-12:00~14:00")
                    i = i.replace("\n", " ").split()
                    menu.append(i)
            elif '스넥' in i:
                if 'Chef' in i:  # 휴일일시 제외
                    checka = 1
                elif ('점심' in when) or ('오늘' in when):
                    i = i.replace("스넥1400~1600", "스넥-14:00~16:00")
                    i = i.replace("\n", " ").split()
                    menu.append(i)
            elif '석식' in i:
                if ('저녁' in when) or ('오늘' in when):
                    i = i.replace("석식1730~1900", "석식-17:30~19:00")
                    i = i.replace("\n", " ").split()
                    menu.append(i)


        result = ''

        for size in range(len(menu)):
            result = result + '-----------------\n'

            for detail in range(len(menu[size])):
                if detail == 0:
                    result = result + menu[size][detail] + '\n\n'
                else:
                    result = result + menu[size][detail] + '\n'

        return result

class HaksikResult:
    def __init__(self):
        self.output = 'empty'
        self.hooseang = 'empty'
        self.umon = 'empty'
        self.hufsdorm = 'empty'

    def result(self, input, day):
        crwal = Crawl()
        sum_result = ''

        if input is 0:
            if day is 'tomorrow':
                self.output = '다음 URL을 통해 이번주 학식을 알 수 있어요!\nhttps://wis.hufs.ac.kr/jsp/HUFS/cafeteria/frame_view.jsp'
            else:
                self.output = '언제 혹은 어디 학식을 알려드릴까요?'
            return self.output
        else:
            if input is 4:
                input = '후생관'
                self.hooseang = crwal.HooseangHaksik('오늘', day)

                sum_result = self.hooseang
            elif input is 5:
                input = '어문관'
                self.umon = crwal.UmonHaksik('오늘', day)

                sum_result = self.umon
            elif input is 6:
                input = 'Hufsdorm'
                self.hufsdorm = crwal.HufsdormHaksik('오늘', day)

                sum_result = self.hufsdorm
            else:   # input 이 아침 or 점심 or 저녁일시
                if input is 1:
                    input = '아침'
                elif input is 2:
                    input = '점심'
                elif input is 3:
                    input = '저녁'

                self.hooseang = crwal.HooseangHaksik(input, day)
                self.umon = crwal.UmonHaksik(input, day)
                self.hufsdorm = crwal.HufsdormHaksik(input, day)

                if len(self.hooseang) is not 0:
                    sum_result = '※후생관 학식\n' + self.hooseang
                if len(self.umon) is not 0:
                    sum_result = sum_result + '\n※어문관 메뉴\n' + self.umon
                if len(self.hufsdorm) is not 0:
                    sum_result = sum_result + '\n※HufsDorm 메뉴\n' + self.hufsdorm

            self.output = day + '일 ' + input + '학식\n'

            if len(sum_result) is 0:
                self.output = self.output + '학식을 불러올 수 없어요 ㅠㅠ'
            else:
                self.output = self.output + sum_result

        return self.output
