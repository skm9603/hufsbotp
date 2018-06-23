import json
import requests
import pdairp


class Weather:
    def weather(self, question):
        # 경기도 용인시 모현면 한국외국어대학교 글로벌캠퍼스
        # 위도: 37.3383890, 경도 : 127.2694870'
        params = {"version": "1", "lat":'37.3383890', "lon":'127.2694870'}
        headers = {"appKey": "99bd41f0-c296-4e49-9f4f-999280b611a2"}
        try:
            # skt weather API
            r = requests.get("https://api2.sktelecom.com/weather/current/minutely", params=params, headers=headers)
            # 미세먼지 API library
            a = pdairp.PollutionData("vKWBrSEIADQx3CgoEnV9rD6HdQJRzKV17E0APxMU%2B9B4IuL%2B0rOfbBn1U5t47lu3IzS%2FEkZkIZKU36cPMpigKw%3D%3D")
        except :
            error = '날씨 API를 얻어올 수 없습니다.'
            return error

        # json -> python 객체로 변환
        data = json.loads(r.text)
        weather = data["weather"]["minutely"]
        sky = weather[0]["sky"]["name"]
        wind = weather[0]["wind"]["wspd"]
        temp = weather[0]["temperature"]["tc"]
        tmax = weather[0]['temperature']['tmax']
        tmin = weather[0]['temperature']['tmin']

        # 소수점 없애기
        temp = int(float(temp))
        tmax = int(float(tmax))
        tmin = int(float(tmin))
        wind = int(float(wind))

        # 모현면 외국어대학교에서 가장 가까운 민세먼지 측정소 : 김량장동에 위치
        # 초 미세먼지 농도
        dust = ''
        pm25 = int(a.station("김량장동", "DAILY")['0']['pm25Value'])

        if 0 <= pm25 <= 15:
            dust = '좋음'
        elif 15 < pm25 <= 35:
            dust = '보통'
        elif 35 < pm25 <= 75:
            dust = '나쁨'
        elif 75 < pm25:
            dust = '매우나쁨'

        #종합하면
        if question < 4:
            cWeather = "모현면 날씨\n하늘은 '" + sky + "', 현재기온은 " + str(temp) + "℃, 미세먼지농도는 '" + dust \
                    + "', 최고기온은 " + str(tmax) + "℃, 최저기온은 " + str(tmin) + "℃, 풍속은 " + str(wind) + "m/s 입니다."
        elif question < 9:
            cWeather = "현재기온은 " + str(temp) + "℃, " + "', 최고기온은 " + str(tmax) + "℃, 최저기온은 " + str(tmin) + "℃ 입니다."
        else :
            cWeather = "미세먼지농도는 '" + dust + " 입니다."
        return cWeather
