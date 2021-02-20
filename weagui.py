import tkinter as tk
from datetime import datetime
from PIL import ImageTk, Image 
import requests
from tkinter import messagebox, Label , Text , Button , RAISED , END
import json

 
class weather():
    def w_r(self):
        self.url ="http://api.openweathermap.org/data/2.5/weather?"
        self.cityname = self.loc.get(1.0,END)
        self.api_key = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
        + self.cityname + "&units=metric&appid="+'66118cf69a5f6c7a9db528c5df919bfe')
        self.data = json.loads(self.api_key.content)

        if self.data['cod'] == '404':
            messagebox.showerror('Error','city not found!!')
        else:
            self.location['text'] = self.data['name'] + ","+self.data['sys']['country']
            self.c = self.data['main']['temp_max']+32
            self.f = self.c*9/5+32
            self.weather['text'] = self.data['weather'][0]['main']
            self.weather['font'] = ('verdana',20,'bold')
            self.temperature['text'] = f'{self.c}C \n {self.f}F'
            self.temperature['font'] = ('verdana',20,'bold')
            self.humidity['text'] = self.data['main']['humidity']
            self.humidity['font'] = ('verdana',20,'bold')
            self.pressure['text'] = self.data['main']['pressure']
            self.pressure['font'] = ('verdana',20,'bold')
        

    def __init__(self):     
        self.root = tk.Tk()
        self.root.geometry("900x600")
        self.root.title("gui weather app")
        self.header = Label(self.root,width=200,height=2,bg="#00274c")
        self.header.place(x=0,y=0)
        self.date = Label(self.root,text=datetime.now().date(),bg="#00274c",fg="white")
        self.date.place(x=400,y=5)
        self.heading = Label(self.root,text="Weather report",bg="#00274c",fg="white",font=('verdana',10,'bold'),)
        self.heading.place(x=180,y=5)
        self.location = Label(self.root,text="NA-/",bg="#00274c",fg="white",font=('verdana',10,'bold'),)
        self.location.place(x=10,y=5)
        self.name = Label(self.root,text="city or country name",fg="#00274c",font=('verdana',10,'bold'),)
        self.name.place(x=140,y=45)
        self.loc = Text(self.root,width=25,height=2)
        self.loc.place(x=140,y=70)
        self.button = Button(self.root,text="search",bg="#00274c",fg="white",relief=RAISED,borderwidth=3,command=self.w_r)
        self.button.place(x=350,y=73)
        self.line1 = Label(self.root,width=20,height=0,bg="#00274c")
        self.line1.place(x=0,y=150)
        self.line2 = Label(self.root,width=70,height=0,bg="#00274c")
        self.line2.place(x=350,y=150)
        self.report = Label(self.root,text="weather report",bg="#00274c",fg="white",padx=10)
        self.report.place(x=180,y=150)
        self.weather = Label(self.root,text="weather",fg="#00274c")
        self.weather.place(x=90,y=230)
        self.temperature = Label(self.root,text="temperature",fg="#00274c",font=('verdana',10,'bold'),)
        self.temperature.place(x=200,y=230)
        self.humidity = Label(self.root,text="humidity",fg="#00274c")
        self.humidity.place(x=610,y=230)
        self.pressure = Label(self.root,text="pressure",fg="#00274c")
        self.pressure.place(x=780,y=230)
        self.root.mainloop()
        
if __name__ == '__main__':
 weather()