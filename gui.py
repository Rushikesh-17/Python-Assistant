import pickle
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import engine as e
import main


class mainscreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mainpage")
        self.geometry('1600x1300')

        def resize_image(event):
            new_width = event.width
            new_height = event.height
            image = copy_of_image.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(image)
            label.config(image=photo)
            label.image = photo


        image = Image.open("bg.png")
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(self, image=photo)
        label.bind('<Configure>', resize_image)
        label.pack(fill=BOTH, expand=YES)


        microphone_button = ttk.Button(label,text="Recognize", command=Process_audio,width=20)
        microphone_button.place(x=1200,y=300)

        settings_button = ttk.Button(label,text="Settings", command=self.open_settings, width=20)
        settings_button.place(x=1200,y=400)

        info_button = ttk.Button(label,text="Info", command=self.open_info,width=20)
        info_button.place(x=1200,y=500)

        main.wishMe()
        main.user_name()
        self.mainloop()



    def open_settings(self):
        window = settings_page(self)
        window.grab_set()

    def open_info(self):
        window = info_page(self)
        window.grab_set()



class settings_page(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.title("Settings")
        self.geometry('300x300')
        self.configure(background="light sky blue")
        label1 = ttk.Label(self,text="Assistant Name :")
        label2 = ttk.Label(self,text="User Name :")
        E1 = ttk.Entry(self)
        E2 = ttk.Entry(self)


        def Update():
            new_AName = E1.get()
            if new_AName != "":
                A = open("Assistant_name.pickle", "wb")
                pickle.dump(new_AName, A)
                A.close()
            new_UName = E2.get()
            if new_UName != "":
                B = open("User_name.pickle","wb")
                pickle.dump(new_UName,B)
                B.close()
            main.update_names()
            self.destroy()

        b1 = ttk.Button(self,text="Update",command=Update)

        label1.grid(row=0,column=0,padx=5,pady=5)
        E1.grid(row=0,column=1,padx=5,pady=5)
        label2.grid(row=1,column=0,padx=5,pady=5)
        E2.grid(row=1,column=1,padx=5,pady=5)
        b1.grid(row=3,column=1,columnspan=2,padx=5,pady=5)
        self.mainloop()


class info_page(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.title("Info")
        self.geometry('500x150')
        self.configure(background="light sky blue")
        treev = ttk.Treeview(self, selectmode='browse')
        treev.pack(side='right')
        verscrlbar = ttk.Scrollbar(self, orient="vertical", command=treev.yview)
        verscrlbar.pack(side='right', fill='x')
        treev.configure(xscrollcommand=verscrlbar.set)
        treev['columns'] = ('no.', 'Command', 'Query')
        treev.column("#0", width=0)
        treev.column("no.", anchor=CENTER, width=25)
        treev.column("Command", anchor=CENTER)
        treev.column("Query", anchor=CENTER,width=300)
        treev.heading("#0", text="", anchor=CENTER)
        treev.heading("no.", text="No.", anchor=CENTER)
        treev.heading("Command", text="Command", anchor=CENTER)
        treev.heading("Query", text="Description", anchor=CENTER)
        treev.insert(parent='', index='end', iid=0, text='', values=('1', 'Open Google', 'Opens Google.com'))
        treev.insert(parent='', index='end', iid=1, text='', values=('2', 'Open Youtube', 'Opens Youtube.com'))
        treev.insert(parent='', index='end', iid=2, text='', values=('3', 'Search in Wikipedia ...', 'Gives Wikipedia result for given query'))
        treev.insert(parent='', index='end', iid=3, text='', values=('4', 'Play music', 'Plays random music from device'))
        treev.insert(parent='', index='end', iid=4, text='', values=('5', "What's the time", 'Tells us current time'))
        treev.insert(parent='', index='end', iid=5, text='', values=('6', 'How are you', ''))
        treev.insert(parent='', index='end', iid=6, text='', values=('7', 'Change my name', 'Changes username'))
        treev.insert(parent='', index='end', iid=7, text='', values=('8', 'Change your name', 'Changes Assistant name'))
        treev.insert(parent='', index='end', iid=8, text='', values=('9', 'Who made you', "Gives creator's name"))
        treev.insert(parent='', index='end', iid=9, text='', values=('10', 'Tell me a joke', 'Tells a programming related joke'))
        treev.insert(parent='', index='end', iid=10, text='', values=('11', 'Calculate ...', 'Calculates operations'))
        treev.insert(parent='', index='end', iid=11, text='', values=('12', "Search ...", 'Searches given query'))
        treev.insert(parent='', index='end', iid=12, text='', values=('13', "Who are you", ''))
        treev.insert(parent='', index='end', iid=13, text='', values=('14', "Reason for your creation", ''))
        treev.insert(parent='', index='end', iid=14, text='', values=('15', "Lock window", 'puts PC to sleep'))
        treev.insert(parent='', index='end', iid=15, text='', values=('16', "Write a note", " writes a note"))
        treev.insert(parent='', index='end', iid=16, text='', values=('17', "where is .....", "searches the location"))
        treev.insert(parent='', index='end', iid=17, text='', values=('18', "How is the Weather", "Tells the current weather in your location"))
        treev.insert(parent='', index='end', iid=18, text='', values=('19', "Write A note ", "Writes a note"))
        treev.insert(parent='', index='end', iid=19, text='', values=('20', "Exit", "Closes the Assistant"))

        treev.pack()

        self.mainloop()

def Process_audio():

    query = e.Assistant().takeCommand().lower()
    main.process_Query(query)


if __name__ == "__main__":
    app = mainscreen()

