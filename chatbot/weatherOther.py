from pyowm import OWM
API_key = '46d6db2120c4f8c20b1d1cfccd33bb4c'
owm = OWM(API_key)

obs = owm.weather_at_place('Seoul')
w = obs.get_weather()

class Weather():
    def __init__(self):
        self.a='empty'

    def result(self, qu):
        self.a = 'Seoul :', w.get_status(), w.get_temperature(unit='celsius')['temp']
        return self.a


a = Weather()
b = a.result('a')
print(b)