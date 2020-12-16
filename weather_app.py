import tkinter as tk
from tkinter import *
import requests
# This app is fully functional, anyone can use for their personal use
# You can follow me for future update and together we can contribute to a new project
class weatherApi:
    # =========================== GUI Design part START ==================================>>>
    def __init__(self, root):
        self.searchVar = tk.StringVar()
        self.outPutVar = tk.StringVar()
        # >>>>>>>>>>> Window Start <<<<<<<<<<<<<<<<<<<<<<<
        
        self.root = root 
        self.root.title('Weather App')
        self.canvas = tk.Canvas(root, height=500, width=600)
        self.canvas.pack()
        
        self.backgroundImage = tk.PhotoImage(file='back.png')
        self.bgLabel = tk.Label(root, image=self.backgroundImage)
        self.bgLabel.place(relwidth=1, relheight=1)
        self.frame = tk.Frame(root)
        self.frame.pack()
        # >>>>>>>>>>> Window End <<<<<<<<<<<<<<
        
        self.cityLabel = tk.Label(self.root, text='Type your City:', font=('arial', 10, 'bold'))
        self.cityLabel.place(relx=0.15, rely=0.05)
        self.searchFrame = tk.Frame(self.root,height=100, width=400, )
        self.searchFrame.place(relheight=0.075,relwidth=0.70, relx=0.15,rely=0.1)
        self.searchBox = tk.Entry(self.searchFrame,textvariable=self.searchVar,relief= FLAT, bg='white', selectforeground='yellow', font=20, borderwidth=10)
        self.searchBox.place(relheight=1,relwidth=.84)
        self.searchBtn = tk.Button(self.searchFrame,text='SEARCH', bg='#232323', fg='white', command=lambda: self.get_weather(self.searchBox.get()))
        self.searchBtn.place(relheight=1,relwidth=.15, relx=.85)
        self.displayTextFrame = tk.Frame(self.root, bg='#ffffff')
        self.displayTextFrame.place(relx=0.15, rely=0.2, relwidth=0.7, relheight=0.6)
        self.outPutLabel = tk.Label(self.displayTextFrame, textvariable = self.outPutVar, fg='#232323',bg='#ffffff', font=50, justify=LEFT)
        self.outPutLabel.place(relx=.2, rely=.3)

    def get_weather(self,city):
        self.weather_key = 'feb73f96e4891ba687bdc3a8d62ebe3b'
        self.url = 'https://api.openweathermap.org/data/2.5/weather'
        self.params = {'APPID': self.weather_key, 'q': city, 'units': 'imperial'}
        self.response = requests.get(self.url, params = self.params)
        self.weather = self.response.json()
        self.name = self.weather['name']
        self.description = self.weather['weather'][0]['description']
        self.temparature = self.weather['main']['temp']
        self.wind = self.weather['wind']['speed']
        self.humidity = self.weather['main']['humidity']
        self.outPutVar.set('City: {} \nDescription: {} \nTemparature: {} \nWind Speed: {} \nHumidity: {}'.format(self.name,self.description,((self.temparature - 32) * 5//9), self.wind, self.humidity))
if __name__ == "__main__":
    root = tk.Tk()
    application = weatherApi(root)
    root.mainloop()

# END of the Program  
