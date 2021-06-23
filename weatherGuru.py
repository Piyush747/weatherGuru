from tkinter import *
import requests
import json
from PIL import ImageTk,Image

#This function is the main engine of the app
def search():
    # get the searched city in string format
    loc = location.get()
    global app
    global img
    #clear previous results
    app.destroy()
    try:
        #to make api request
        api_request = requests.get("http://api.weatherapi.com/v1/forecast.json?key=abb23d683258474d86794817212106&q={}&days=1&aqi=yes&alerts=yes".format(loc))
        #read api content (the content is recieved in JSON format) 
        api = json.loads(api_request.content)
        #name of the city
        city = api["location"]["name"]
        #name of the country 
        country = api["location"]["country"]
        #temp in degree celcius
        temp = api["current"]["temp_c"]
        #data update status 
        modified_date = api["current"]["last_updated"]
        #date and time in the city
        time = api["location"]["localtime"]
        #weather condition in the city
        condition = api["current"]["condition"]["text"]

        #relative humidity in percentage
        humidity = api["current"]["humidity"]

        #creating frame to display result
        app = Frame(root,background="linen")
        app.pack()
        #display city and country
        mylabel = Label(app,text="Location: "+city+", "+country,background="linen",font="Helvetica 15 bold",fg="firebrick1")
        mylabel.pack()
        #display time
        mylabel2 = Label(app,text="World Clock : "+time,background="linen",font="Helvetica 10 bold italic",fg="cornflowerblue")
        mylabel2.pack()
        #display temp and weather condtions
        info = Label(app,text="Temp: "+str(temp)+"\N{DEGREE SIGN}C || Condition: "+condition+" || RH: "+str(humidity)+"%",background="linen",fg="cornflowerblue",font="Helvetica 10 bold italic")
        info.pack()

        #link to image 
        w_image = api["current"]["condition"]["icon"]
        #display the image Setting it up
        img = ImageTk.PhotoImage(Image.open(str(w_image.split("//")[1])))
        #Displaying it
        imglabel = Label(app, image=img,height=130,width=130,bg="linen").pack() 
        #display date modified
        last_modified = Label(app,text="Last Updated On: "+str(modified_date),background="linen",font="Helvetica 8")
        last_modified.pack(side="bottom",)
    except Exception as e:
        app = Frame(root)
        app.pack()
        #display error in case of exception
        error = Label(app,text="City not avaliable...",pady=50,font="Helvetica 10 bold",fg="firebrick1",background="linen")
        error.pack()
        api = "Error..."
        print(e)

root = Tk()
#setting default size of window
root.geometry("500x340")
root.wm_maxsize(500, 340)
#setting title of app
root.title("WeatherGuru")
#set the icon
root.iconbitmap("favicon.ico")
#set background color
root.configure(background="linen")

#search box label
locationlabel = Label(root,text="Enter City Name: ",background="linen",font="Helvetica 10",fg="firebrick1")
locationlabel.pack()

#search box
location = Entry(root,borderwidth = 3,relief="ridge")
location.pack(side="top",pady=5,)

#submit btn
submit = Button(root,text="Search",bg = "skyblue",fg="white",font="Helvetica 10 bold",command=search)
submit.pack(side="top",)

#creating frame
app = Frame(root)
app.pack()

#credits label
credit = Label(root,text="Powered by WeatherAPI.com",background="linen",font="Helvetica 8")
credit.pack(side=BOTTOM,)

root.mainloop()