#text to speech

#importing modules

from tkinter import *
from gtts import gTTS
from playsound import playsound

#geometry of main window

rootmain = Tk()
rootmain.geometry('700x700')
rootmain.resizable(True,True)
rootmain.config(bg = 'lavender')
rootmain.title('TEXT TO SPEECH')

Label(rootmain, text ='Text To Speech Converter', font ='arial 21 bold', bg ='white smoke').place(x=180,y=60)

## inputing choice from user

Label(rootmain, text ='Enter 1 to enter your text on window', font ='arial 15 bold', bg ='white smoke').place(x=20,y=200)
Label(rootmain, text ='Enter 2 to enter file name to be read', font ='arial 15 bold', bg ='white smoke').place(x=20,y=300)
Choice = StringVar()
entry_choice = Entry(rootmain,textvariable =Choice, width ='50')
entry_choice.place(x=20 , y=400)


def Enter():
    choice = entry_choice.get()
    
    if choice=='1':

        #defing geometry of choice 1 window
        
        root = Tk()
        root.geometry('450x400')
        root.resizable(0,0)
        root.config(bg = 'LightSkyBlue1')
        root.title('Text To Speech')
        
        Label(root, text = 'TEXT TO SPEECH' , font='arial 20 bold' , bg ='white smoke').pack()
        Label(root, text ='Enter Text', font ='arial 15 bold', bg ='white smoke').place(x=20,y=60)

        #inputing string
        
        Msg = StringVar()
        entry_field = Entry(root,textvariable =Msg, width ='50')
        entry_field.place(x=20 , y=100)

        #defing button functions

        def Text_to_speech():
            Message = entry_field.get()
            speech = gTTS(text = Message)
            speech.save('audio.mp3')
            playsound('audio.mp3')
            
        def Exit():
            root.destroy()
            
        def Reset():
            Msg.set("")

        #buttons
            
        Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, bg='green2',width =4).place(x=25, y=140)
        Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'OrangeRed1').place(x=140,y=140)
        Button(root, text = 'RESET', font='arial 15 bold', command = Reset,bg='gold2').place(x=250 , y =140)

        #button app
        Label(root, text ='Click on play button to hear the entered text', font ='arial 15 bold', bg ='misty rose').place(x=20,y=200)
        Label(root, text ='Click on exit button to close the window ', font ='arial 15 bold', bg ='misty rose').place(x=20,y=240)
        Label(root, text ='Click on reset button to enter new text', font ='arial 15 bold', bg ='misty rose').place(x=20,y=280)
        
        root.mainloop()

    elif choice=='2':
        #importing module
        
        from tkinter import filedialog
        import os
        import time
        #defing geometry of choice 2 window

        rootdialog=Tk()
        rootdialog.filename=filedialog.askopenfilename(initialdir='This PC',title='select a file',filetypes=(('text file','*.txt'),('all files','*.*')))
        pt=rootdialog.filename        
        root = Tk()
        root.geometry('600x400')
        root.resizable(True,True)
        root.config(bg = 'peach puff')
        root.title('TEXT TO SPEECH')
        
        Label(root, text = 'TEXT TO SPEECH' , font='arial 20 bold').pack()

        #reading text of selected file
        
        f= open(pt,"r")
        Msg=f.read()
        Label(root, text =Msg, font ='arial 15 bold', bg ='misty rose').pack()

        #defing button fns
        
        def Text_to_speech():
            Message=Msg
            speech = gTTS(text = Message)
            speech.save('audio.mp3')
            #playsound('audio.mp3')
            os.system('start audio.mp3')
            time.sleep(10)
            os.system('close audio.mp3')

        def exitw():
            root.destroy()

        #buttons
            
        Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech,bg = 'olive drab',width =14).pack()
        Button(root, text = "EXIT" , font = 'arial 15 bold', command = exitw,width =14).pack()

        
            
        root.mainloop()
    else:
        from tkinter import messagebox
        messagebox.showerror('WARNING','INCORRECT OPTION ENTERED')

def resetMain():
    Choice.set("")
def exitMain():
    rootmain.destroy()
    
#buttons
    
Button(rootmain, text = "ENTER" , font = 'arial 15 bold', command = Enter, bg='green2',width =8).place(x=25, y=440)
Button(rootmain, text = "RESET" , font = 'arial 15 bold', command = resetMain, bg='bisque',width =8).place(x=150, y=440)
Button(rootmain, text = "EXIT" , font = 'arial 15 bold', command = exitMain, bg='coral1',width =8).place(x=275, y=440)

rootmain.mainloop()

        

