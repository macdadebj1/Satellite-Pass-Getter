import requests
import json
import time
from tkinter import *
class program:
    def __init__(self,parent):
        self.apiKeyLabel=Label(parent,text="Please input your API key!")
        self.apiKeyLabel.grid(row=0,column=0)
        self.apiKeyEntry=Entry(parent)
        self.apiKeyEntry.grid(row=0,column=1)
        self.sateliteLabel=Label(parent,text="Please enter the satellite ID")
        self.sateliteLabel.grid(row=1,column=0)
        self.sateliteEntry=Entry(parent)
        self.sateliteEntry.grid(row=1,column=1)
        self.longitudeLabel=Label(parent,text="Longitude")
        self.longitudeLabel.grid(row=2,column=0)
        self.longitudeEntry=Entry(parent)
        self.longitudeEntry.grid(row=2,column=1)
        self.lattitudeLabel=Label(parent,text="Lattitude")
        self.lattitudeLabel.grid(row=3,column=0)
        self.lattitudeEntry=Entry(parent)
        self.lattitudeEntry.grid(row=3,column=1)
        self.altidudeLabel=Label(parent,text="Altitude")
        self.altidudeLabel.grid(row=4,column=0)
        self.altidudeEntry=Entry(parent)
        self.altidudeEntry.grid(row=4,column=1)
        
        self.satNameLabel=Label(parent,text="Satellite Name:")
        self.satNameLabel.grid(row=5,column=0)
        self.satNameOutput=Label(parent,text="")
        self.satNameOutput.grid(row=5,column=1)
        self.nextPassTimeLabel=Label(parent,text="Next Pass:",width=25)
        self.nextPassTimeLabel.grid(row=6,column=0)
        self.nextPassTimeOutput=Label(parent,text="",width=20)
        self.nextPassTimeOutput.grid(row=6,column=1)
        self.durationLabel=Label(parent,text="Duration (Seconds):",width=25)
        self.durationLabel.grid(row=7,column=0)
        self.durationOutput=Label(parent,text="",width=20)
        self.durationOutput.grid(row=7,column=1)
        self.magnitudeLabel=Label(parent,text="Magnitude:",width=25)
        self.magnitudeLabel.grid(row=8,column=0)
        self.magnitudeOutput=Label(parent,text="",width=20)
        self.magnitudeOutput.grid(row=8,column=1)
        
        self.getButton=Button(parent,text="Get Pass!",command=self.getPass,width=25)
        self.getButton.grid(row=9,column=0)
        self.quitButton=Button(parent,text="Quit",command=parent.destroy,width=20)
        self.quitButton.grid(row=9,column=1)
    def getPass(self):
        licenseKey=self.apiKeyEntry.get()
        satId=self.sateliteEntry.get()
        longitude=self.longitudeEntry.get()
        lattitude=self.lattitudeEntry.get()
        altitude=self.altidudeEntry.get()
        days=1
        visibility=300
        r=requests.get("http://www.n2yo.com/rest/v1/satellite/visualpasses/{}/{}/{}/{}/{}/{}/&apiKey={}"
               .format(satId,lattitude,longitude,altitude,days,visibility,licenseKey))
        #/visualpasses/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{days}/{min_visibility}
        decoded=json.loads(r.text)
        d=""
        for x in decoded['passes']:
            a=x['startUTC']
            b=x['duration']
            c=x['mag']
        for y in decoded['info']['satname']:
            d+=y
        outputTime=time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(a))
        self.nextPassTimeOutput.configure(text=outputTime)
        self.durationOutput.configure(text=b)
        self.magnitudeOutput.configure(text=c)
        self.satNameOutput.configure(text=d)
        print(outputTime)
        print(r.text)
        
root=Tk()
app=program(root)
root.mainloop()








#https://pythonspot.com/json-encoding-and-decoding-with-python/
#https://docs.python.org/3/library/json.html
#https://www.n2yo.com/login/edit/
#https://n2yo.com/api/
#https://www.n2yo.com/rest/v1/satellite/positions/25544/41.702/-76.014/0/2/&apiKey={} 
#First Request format: https://www.n2yo.com/rest/v1/satellite/tle/<satelite_number>&apiKey=<license_key>
#http://www.n2yo.com/rest/v1/satellite/visualpasses/25544/41.702/-76.014/0/2/300/&apiKey=<license_key> 