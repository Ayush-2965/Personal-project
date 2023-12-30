import requests
import tkinter as tk
from tkinter import messagebox
# ifsc="PYTM0123456"

#window properties
window=tk.Tk()
window.title("Bank details")
window.configure(bg="light grey")

window_width=900    # window.geometry("900x720")
window_height=720   # window.geometry("900x720")


def centre_screen():

    screen_width=window.winfo_screenwidth()
    screen_height=window.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

centre_screen()

tk.Label(window, text="Enter IFSC Code :",pady=15, bg="light grey",font=("Arial",24,"bold")).grid(row=0,sticky="W")
e=tk.Entry(window,font=("Arial",22,"bold"))
e.grid(row=0,column=1,pady=5,sticky="W")
e.focus()
var=tk.StringVar()

def getifsc():
    try:

        

        ifsc=e.get()
        request=requests.get("https://ifsc.razorpay.com/" + ifsc).json()
        # print(request.items())
        # print(type(request))

        
        a=request.items()
        for i in range(len(a)):

            b=list(request)[i]
            c=list(request.values())[i]
            d=str(c)
            
            # print(b+" = "+d)
                
            tk.Label(window, text=b +" :", bg="light grey",font=("Arial",22,"bold")).grid(row=i+1,sticky="W")
            tk.Label(window, text=d,bg="light grey",font=("Arial",22)).grid(row=i+1, column=1, sticky="w")
            
            


    except:
        tk.messagebox.showerror("showerror", "Something wrong")
    

vacant_space=" "
left_sidepadding = ('{: >30}'.format(vacant_space))

def ref():
    try:
        var.set(left_sidepadding)
        ifsc=e.get()
        request=requests.get("https://ifsc.razorpay.com/" + ifsc).json()
        a=request.items()
        for i in range(len(a)):

            tk.Label(window, textvariable=var,bg="light grey",font=("Arial",22)).grid(row=i+1, column=1, sticky="w")
        getifsc()
    except:
        tk.messagebox.showerror("showerror", "Something went wrong \n""\n1.Check your Internet connection\n2. Check your IFSC code")
    
but = tk.Button(window, text="Show",font=("Arial",18), command=ref)
but.grid(row=0, column=2,padx=100)

window.mainloop()