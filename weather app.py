from urllib2 import urlopen
import json
from datetime import datetime
from Tkinter import *



def find_weather(city):
    city_dict = {"jamshedpur" : 1269300,
        "delhi" : 1261481,
        "jaipur" : 1269515}
    weather(city_dict[city])
    
    
def weather(city_id):
    user_api = "" # Obtain your API KEY form: http://openweathermap.org/
    apiurl = 'http://api.openweathermap.org/data/2.5/weather?id=' + str(city_id) + '&mode=json&units=metric&APPID=' + user_api

    try :
        url = urlopen(apiurl)
    except IOError:
        print "No Internet"
    output = url.read().decode('utf-8')
    response = json.loads(output)
    url.close()

    city = "City : {}".format(response.get('name'))
    country = "\nCountry : {}".format(response.get('sys').get('country'))
    temp = "\nTemp : {} deg".format(response.get('main').get('temp'))
    humidity = "\nHumidity : {}".format(response.get('main').get('humidity'))
    pressure = "\nPressure : {}".format(response.get('main').get('pressure'))
    sky = "\nSky : {}".format(response['weather'][0]['main'])

    def time(t):
        conv = datetime.fromtimestamp(int(t)).strftime('%I:%M %p')
        return conv

    sunrise = "\nSunrise at {}".format(time(response.get('sys').get('sunrise')))
    sunset = "\nSunset at {}".format(time(response.get('sys').get('sunset')))
    wind = "\nWind speed : {}".format(response.get('wind').get('speed'))
    last ="\nLast Updated at : {}".format(time(response.get('dt')))
    sen = city + country + temp + humidity + pressure + sky + sunrise + sunset + wind + last
    l2.configure(text=sen)

tk = Tk()
tk.configure(background='light blue')
tk.title('Weather App')
tk.geometry('520x600')

l = Label(tk,text="Weather",bg="light blue",font="Times 25 bold")
l.place(x=200,y=10)
l2 = Label(tk,text="",bg="light blue",font="Times 15 bold")
b1=Button(tk,text="Jaipur",command=lambda : find_weather("jaipur"),bg="light blue",activebackground="red",bd=10)
b1.place(x=90,y=100)
b2=Button(tk,text="Jamshedpur",command=lambda : find_weather("jamshedpur"),bg="light blue",activebackground="red",bd=10)
b2.place(x=220,y=100)
b2=Button(tk,text="Delhi",command=lambda : find_weather("delhi"),bg="light blue",activebackground="red",bd=10)
b2.place(x=370,y=100)
l2.place(x=150,y=200)

tk.mainloop()
