# Openweather
import tkinter as t
import requests
import json

def Update():
    path = 'https://samples.openweathermap.org/data/2.5/weather?q=Taoyuan,TW&appid=4bdfe883983f2915b06622779f51cc29'
    opwth = json.loads(requests.get(path).text)
    temp = opwth['main']['temp'] - 273.15
    feelslike = opwth['main']['feels_like'] - 273.15
    humidity = opwth['main']['humidity']
    weatherMain = opwth['weather'][0]['main']
    ans.set('氣溫: %.2f\n 體感: %.2f\n 濕度: %.2f' % (temp, feelslike, humidity))

win = t.Tk()
win.title('桃園天氣')
win.geometry('500x500')

ans = t.StringVar()
Update()

label = t.Label(win, textvariable=ans)
label.config(font=('Arial', 20), fg='blue')
label.pack()

addButton = t.Button(win, text='Update', command=Update)
addButton.config(font=('Arial', 20), fg='orange')
addButton.pack()

win.mainloop()