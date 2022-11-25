from tkinter import *
#created dictionary 
digits={'black':'0','brown':'1','red':'2','orange':'3','yellow':'4','green':'5','blue':'6','purple':'7','gray':'8','white':'9','gold':'-','silver':'-','no color':'-'}

mult ={'black':1,'brown':10,'red':10**2,'orange':10**3,'yellow':10**4,'green':10**5,'blue':10**6,'purple':10**7,'gray':10**8,'white':10**9,'gold':0.1,'silver':0.01,'no color':'-'}

tolerance ={'black':'-','brown':1,'red':2,'orange':'-','yellow':'-','green':0.5,'blue':0.25,'purple':0.1,'gray':'-','white':'-','gold':5,'silver':10,'no color':20}

#Function of 4 bands
def band4():

    def results():

        c1 = color1.get()
        c2 = color2.get()
        c3 = color3.get()
        c4 = color4.get()

        digit1 = digits[c1]
        digit2 = digits[c2]
        mult1 = mult[c3]
        tol1 = tolerance[c4]

        result = int((digit1 + digit2)) * mult1

        Label(screen,text='resistance '+ str(result) + 'ohms + ' + str(tol1) +'%',font= 30).grid(row=6,column=2)


    global digits
    global mult
    global tolerance

    global color1
    global color2
    global color3
    global color4


    color1 = StringVar()
    color2 = StringVar()
    color3 = StringVar()
    color4 = StringVar()


    color1_entry = Entry(screen, textvariable= color1)
    color1_entry.grid(row=1,column=2)

    color2_entry = Entry(screen, textvariable= color2)
    color2_entry.grid(row=2,column=2)

    color3_entry = Entry(screen, textvariable= color3)
    color3_entry.grid(row=3,column=2)

    color4_entry = Entry(screen, textvariable= color4)
    color4_entry.grid(row=4,column=2)
    
    res = Button(screen,text='result',command=results)
    res.grid(row=5,column=2)

def band5():
    global color5

    def answer():
        c1 = color1.get()
        c2 = color2.get()
        c3 = color3.get()
        c4 = color4.get()
        c5 = color5.get()

        digit1 = digits[c1]
        digit2 = digits[c2]
        digit3 = digits[c3]
        mult1 = mult[c4]
        tol1 = tolerance[c5]

        result = int((digit1 + digit2 + digit3)) * mult1
        Label(screen,text='resistance ' + str(result) + 'ohms + ' + str(tol1) + '%', font=30).grid(row=7,column=4)
    
    color1 = StringVar()
    color2 = StringVar()
    color3 = StringVar()
    color4 = StringVar()
    color5 = StringVar()

    color1_entry = Entry(screen, textvariable= color1)
    color2_entry = Entry(screen, textvariable= color2)
    color3_entry = Entry(screen, textvariable= color3)
    color4_entry = Entry(screen, textvariable= color4)
    color5_entry = Entry(screen, textvariable= color5)

    color1_entry.grid(row=1,column=4)
    color2_entry.grid(row=2,column=4)
    color3_entry.grid(row=3,column=4)
    color4_entry.grid(row=4,column=4)
    color5_entry.grid(row=5,column=4)

    res = Button(screen,text='result',command=answer)
    res.grid(row=6,column=4)



screen = Tk()
screen.geometry('500x300')
screen.title('resistor code')



# color band choice
Label(screen,text='choose  color Band', font= 30).grid(row=0,column=0)

band_4 = Button(screen, text=4, bg='blue',command=band4) 
band_4.grid(row=0,column=1)

band_5 = Button(screen,text= 5, bg='blue',command=band5)
band_5.grid(row=0,column=3)

screen.mainloop()

