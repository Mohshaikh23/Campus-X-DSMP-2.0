from tkinter import *
from my_db import Database
from tkinter import messagebox
from my_api import API

class NLPApp:
    def __init__(self):

        self.dbo = Database()
        self.apio = API()
        self.root = Tk()
        self.root.title("NLP App")
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg="#34495E")

        #logging into GUI
        self.login_gui()

        self.root.mainloop()

    def clear(self):
        # clear the GUI
        for i in self.root.pack_slaves():
            i.destroy()

    def login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        respose = self.dbo.search(email,password)

        if respose:
            messagebox.showinfo('Success','Logged In Successfully')
            self.home_gui()
        else:
            messagebox.showerror("Error",'Password does not match')

    def perform_registration(self):
        # Fetch data from GUI
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo("Success","Registered Successfully")
        else:
            messagebox.showerror("Error",'Email Already exists')

    def login_gui(self):
        self.clear()
        heading = Label(self.root, text="NLP APP", bg="#34495E", fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 24, 'bold'))

        label1 = Label(self.root, text="Enter Email")
        label1.pack(pady=(10, 10))
        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text="Enter password")
        label2.pack(pady=(10, 10))
        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root, text="Login", width=10, height=1,command=self.login)
        login_btn.pack(pady=(5, 10), ipady=4)

        label3 = Label(self.root, text="Not a Member?")
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text="Register Now", width=10, height=1, command=self.register_gui)
        redirect_btn.pack(pady=(5, 10), ipady=4)

    def register_gui(self):
        self.clear()

        heading = Label(self.root, text="NLP APP", bg="#34495E", fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 24, 'bold'))

        label0 = Label(self.root, text="Enter Name")
        label0.pack(pady=(10, 10))
        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text="Enter email")
        label1.pack(pady=(10, 10))
        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text="Enter password")
        label2.pack(pady=(10, 10))
        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text="Register", width=10, height=1,command=self.perform_registration)
        register_btn.pack(pady=(5, 10), ipady=4)

        label3 = Label(self.root, text="Already a Member?")
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text="Login Now", width=10, height=1, command=self.login_gui)
        redirect_btn.pack(pady=(5, 10), ipady=4)

    def home_gui(self):
        self.clear()
        heading = Label(self.root, text="NLP APP", bg="#34495E", fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 24, 'bold'))

        sentiment_btn = Button(self.root, text="Sentiment Analysis", width=50, height=1, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(5, 10), ipady=4)

        NER_btn = Button(self.root, text="NER", width=50, height=1, command=self.NER_gui)
        NER_btn.pack(pady=(5, 10), ipady=4)

        Emotion_detection_btn = Button(self.root, text="Emotion_detection", width=50, height=1, command=self.Emotion_detection_gui)
        Emotion_detection_btn.pack(pady=(5, 10), ipady=4)

        Logout_btn = Button(self.root, text="Logout", width=10, height=1, command=self.login_gui)
        Logout_btn.pack(pady=(5, 10), ipady=4)

    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root, text="NLP APP", bg="#34495E", fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 24, 'bold'))

        heading2 = Label(self.root, text="Sentiment Analysis", bg="#34495E", fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=("verdana", 24, 'bold'))

        self.sentiment_input = Entry(self.root,width=50)
        self.sentiment_input.pack(pady=(10,10))

        sentiment_btn =Button(self.root, text='Anlayze Sentiment',command=self.sentiment_analyze)
        sentiment_btn.pack(pady=(10,10))

        self.sentiment_result = Label(self.root,text='',bg="#34495E", fg='white')
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=("verdana", 16, 'bold'))

        back_btn = Button(self.root,text='Home',width=10,height=1,command=self.home_gui)
        back_btn.pack(pady=(5, 10), ipady=4)

    def NER_gui(self):
        self.clear()
        heading = Label(self.root, text="NLP APP", bg="#34495E", fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 24, 'bold'))

        heading2 = Label(self.root, text="NER", bg="#34495E", fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=("verdana", 24, 'bold'))

        self.NER_input = Entry(self.root, text = "Enter Text",width=50)
        self.NER_input.pack(pady=(10, 10))

        self.NER_labels = Entry(self.root, text = "Enter Labels",width=50)
        self.NER_labels.pack(pady=(10, 10))

        self.NER_result = Label(self.root, text='', bg="#34495E", fg='white')
        self.NER_result.pack(pady=(10, 10))
        self.NER_result.configure(font=("verdana", 16, 'bold'))

        NER_btn = Button(self.root, text='Anlayze NER', command=self.NER_analyze)
        NER_btn.pack(pady=(10, 10))

        back_btn = Button(self.root, text='Home', width=10, height=1, command=self.home_gui)
        back_btn.pack(pady=(5, 10), ipady=4)

    def Emotion_detection_gui(self):
        self.clear()
        heading = Label(self.root, text="NLP APP", bg="#34495E", fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 24, 'bold'))

        heading2 = Label(self.root, text="Emotion Detection", bg="#34495E", fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=("verdana", 24, 'bold'))

        self.Emotion_detection_input = Entry(self.root, width=50)
        self.Emotion_detection_input.pack(pady=(10, 10))

        Emotion_detection_btn = Button(self.root, text='Anlayze Emotion_detection', command = self.Emotion_detection_analyze)
        Emotion_detection_btn.pack(pady=(10, 10))

        self.Emotion_detection_result = Label(self.root, text='', bg="#34495E", fg='white')
        self.Emotion_detection_result.pack(pady=(10, 10))
        self.Emotion_detection_result.configure(font=("verdana", 16, 'bold'))

        back_btn = Button(self.root, text='Home', width=10, height=1, command=self.home_gui)
        back_btn.pack(pady=(5, 10), ipady=4)

    def sentiment_analyze(self):
        text = self.sentiment_input.get()
        response = self.apio.Sentiment_analysis(text)

        if response[0]['sentiments'] != []:
            if response[0]['sentiments'][0]["positive"] == False:
                self.sentiment_result['text'] = 'Negative'
            else:
                self.sentiment_result['text'] = 'Positive'
        else:
            self.sentiment_result['text'] = 'Neutral'

    def NER_analyze(self):
        text = self.NER_input.get()
        labels = [self.NER_labels.get()]
        response = self.apio.NER_analyze(text,labels)
        dic = {'span':[],'score':[],'entity':[]}
        for i in response['entities']:
            dic["span"].append(i["span"])
            dic["score"].append(i['score'])
            dic["entity"].append(i['entity'])
        txt = (f"Span - {dic['span']} '\n' "
               f"score - {dic['score']} '\n'"
               f"entity - {dic['entity']}")
        self.NER_result['text'] = txt

    def Emotion_detection_analyze(self):
        text = self.Emotion_detection_input.get()
        response = self.apio.emotion_detection(text)
        self.Emotion_detection_result['text'] = response[0]['sentimentName']


nlp = NLPApp()