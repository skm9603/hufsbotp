
from .weatherResult import Weather
# zfrom .weatherOther import weather

weatherAll = ['모현', '날씨', '비', '눈', '덥', '더워', '춥', '추워', '온도', '미세먼지']
otherDay = ['내일', '어제', '이번']



class CheckW:
    def __init__(self):
        self.hufsWeather = "empty"

    def checkQuesiton(self,question):
        # question = hannanum.morphs(question)
        weather = Weather()
        for i in range(len(weatherAll)):
            if weatherAll[i] in question:
                for j in range(len(otherDay)):
                    if otherDay[j] in question:
                        self.weather = "tomorrow"
                        return self.weather
                self.hufsWeather = weather.weather(i)
        return self.hufsWeather
