
from tkinter import *
import tkinter
import pandas as pd
import whois
import pickle
window = tkinter.Tk()
window.geometry("512x524") # size of the window width:- 500, height:- 375
window.resizable(0, 0) # this prevents from resizing the window
window.title("AntiPhishing Tool")


# creating a function called say_hi()
def button_handler():
    print(input_text.get())
    data = [[input_text.get(), 10000]] 
    first = pd.DataFrame(data, columns = ['domain','ranking']) 
    first['domain'] = [x.lstrip("'").rstrip("'") for x in first['domain']]
    isIp=[]
    urlLen=[]
    isAtTheRate=[]
    isredirect=[]
    haveDash=[]
    domainLen=[]
    valid=[]
    nosOfSubdomain=[]
    activeDuration=[]
    c=0
    for i, j in first.iterrows():
     urlLen.append(len(j[0]))
     domain=j[0].split("/",1)[0]
     domainLen.append(len(domain))
     nosOfSubdomain.append(domain.count("."))
     c=c+1
     try :
      print(domain)
      domainInfo = whois.query(domain)
      print(domainInfo.__dict__)
      expiry_date=domainInfo.expiration_date  
      creation_date=domainInfo.creation_date
      validity=expiry_date-creation_date
      validity=validity.days
      valid.append(1)
      activeDuration.append(validity)   
     except (Exception):  #NOT FOUND
      valid.append(0)
      activeDuration.append(0) 

     if domain.find("-")!=-1:
        haveDash.append(1)
     else:
        haveDash.append(0)
        
     if j[0].find("@")!=-1:
        isAtTheRate.append(1)
     else:
        isAtTheRate.append(0)
     if j[0].find("//")!=-1:
        isredirect.append(1)
     else:
        isredirect.append(0)    
     if re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', domain) != None:
        isIp.append(1)
     else:
        isIp.append(0)
    first["isIp"]=isIp
    first["urlLen"]=urlLen
    first["is@"]=isAtTheRate
    first["isredirect"]=isredirect
    first["haveDash"]=haveDash
    first["domainLen"]=domainLen
    first["nosOfSubdomain"]=nosOfSubdomain
    print(len(valid))
    first["valid"]=valid
    first["activeDuration"]=activeDuration
    check_phish(first)
def check_phish(first):

     print(first)
     first = first[['ranking','isIp','valid','activeDuration','urlLen','is@','isredirect','haveDash','domainLen','nosOfSubdomain']]
     with open('../model_dump/RandomForest.sav', 'rb') as pickle_file:
      persistent_data = pickle.load(pickle_file)
      print("------------\n")
      result = persistent_data.predict(first) 
      print(result)    
      if result[0] == 0:
        tkinter.Label(window,font = ('arial', 18, 'bold'),fg = "green", text =input_text.get() + " is a valid URL").pack()
      else:
        tkinter.Label(window,font = ('arial', 18, 'bold'),fg = "red", text =input_text.get()+ " is a spam URL").pack()
input_frame = Frame(window, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)


input_text = StringVar()
# creating a input field inside the 'Frame'
input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = LEFT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10) # '

btn=tkinter.Button(window, text = "Validate",width = 10,bg = "green", command = button_handler).pack() # 'command' is executed when you click the button
                                                                    # in this above case we're calling the function 'say_hi'.
# btn.grid( padx=20, pady=40)
window.mainloop()
