from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=3d475f70e270ec51dd8272559f4c3d06").json()
    W1_lable.config(text=data["weather"][0]["main"])
    Wb_lable1.config(text=data["weather"][0]["description"])
    temp_lable1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_lable1.config(text=str(data["main"]["pressure"]))


win = Tk()
win.title("Weather")
win.config(bg="blue")
win.geometry("500x570")

name_lable = Label(win,text="City Weather App",
                   font=("Times New Roman",30,"bold"))

name_lable.place(x=25,y=50,height=50,width=450)


city_name = StringVar()
list_name =["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win,values=list_name,
                   font=("Times New Roman",20,"bold"),textvariable=city_name)

com.place(x=25,y=120,height=50,width=450)






W_lable = Label(win,text="Weather Climate",
                   font=("Times New Roman",20,))

W_lable.place(x=25,y=260,height=50,width=210)

W1_lable = Label(win,text="",
                   font=("Times New Roman",20,))
W1_lable.place(x=250,y=260,height=50,width=210)





Wb_lable = Label(win,text="Weather Description",
                   font=("Times New Roman",16,))

Wb_lable.place(x=25,y=330,height=50,width=210)

Wb_lable1 = Label(win,text="",
                   font=("Times New Roman",17,))

Wb_lable1.place(x=250,y=330,height=50,width=210)





temp_lable = Label(win,text="Temperature",
                   font=("Times New Roman",17,))

temp_lable.place(x=25,y=400,height=50,width=210)


temp_lable1 = Label(win,text="",
                   font=("Times New Roman",17,))

temp_lable1.place(x=250,y=400,height=50,width=210)





per_lable = Label(win,text="Pressure",
                   font=("Times New Roman",17,))

per_lable.place(x=25,y=470,height=50,width=210)


per_lable1 = Label(win,text="",
                   font=("Times New Roman",17,))

per_lable1.place(x=250,y=470,height=50,width=210)


done_button = Button(win,text="Done",
                   font=("Times New Roman",20,"bold"),command=data_get)

done_button.place(x=200,y=190,height=50,width=100)






win.mainloop()