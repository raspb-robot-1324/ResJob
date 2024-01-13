import requests
import json


def findjobs():
    url = "https://linkedin-jobs-scraper-api.p.rapidapi.com/jobs"

    title = input("What job would you like? ")
    location = input("Where are you? ")

    payload = {
        "title": title,
        "location": location,
        "rows": 1
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "4addef27aemshcff167ca509dae0p11d1efjsn50d8839241b4",
        "X-RapidAPI-Host": "linkedin-jobs-scraper-api.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    allJobs = []
    a = json.loads(response.content)
    for job in a:
        thisJob = "Title:", job["title"], "Company name:", job["companyName"], "Location:", job[
            "location"], "Description", job["description"]
        allJobs.append(thisJob)

    for i in allJobs:
        print(i)


import customtkinter as ctk

ctk.set_appearance_mode("Light")

ctk.set_default_color_theme("green")

appWidth, appHeight = 660, 700

job = False


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("GUI Application")
        self.geometry(f"{appWidth}x{appHeight}")

        # Name Label
        self.liveLabel = ctk.CTkLabel(self,
                                      text="Where do you live?")
        self.liveLabel.grid(row=0, column=0,
                            padx=40, pady=40,
                            sticky="ew")

        # live Entry Field
        self.liveEntry = ctk.CTkEntry(self,
                                      placeholder_text="1234 Apple St. Montreal, QC H2C4X3")
        self.liveEntry.grid(row=0, column=1,
                            columnspan=3, padx=40,
                            pady=40, sticky="ew")

        # choice Label
        self.choiceLabel = ctk.CTkLabel(self,
                                        text="What type of job do you want?")
        self.choiceLabel.grid(row=1, column=0,
                              padx=40, pady=40,
                              sticky="ew")

        # choice Entry Field
        self.choiceEntry = ctk.CTkEntry(self,
                                        placeholder_text="Computer Engineer, Data scientist")
        self.choiceEntry.grid(row=1, column=1,
                              columnspan=3, padx=40,
                              pady=40, sticky="ew")

        # finalize the generation
        self.searchjobsButton = ctk.CTkButton(self,
                                              text="Search for Jobs")
        self.searchjobsButton.grid(row=5, column=0,
                                   columnspan=1,
                                   padx=40, pady=40,
                                   sticky="ew")

        # results final yippeee!
        self.displayBox = ctk.CTkTextbox(self, width=600,
                                         height=200)
        self.displayBox.configure(state="disabled")
        self.displayBox.grid(row=6, column=0, columnspan=4,
                             padx=40, pady=40, sticky="nsew")


from openai import OpenAI
import customtkinter as ctk

client = OpenAI(api_key="sk--")

ft = ""
lt = ""
ct = ""
em = ""
pn = ""
ep = ""
hs = ""
un = ""

app = ctk.CTk()

ftextbox = ctk.CTkTextbox(app)
ftextbox.configure(state="normal")
ftextbox = ctk.CTkTextbox(master=app, width=200, height=20)
ftextbox.place(relx=0.6, rely=0.0, anchor='s')
ftextbox = ctk.CTkTextbox(app, activate_scrollbars=False)
label = ctk.CTkLabel(app, text="First Name", text_color="Black")
label.configure(text="First Name:")
label.place(relx=0.2, rely=0.0, anchor='s')

ltextbox = ctk.CTkTextbox(app)
ltextbox.configure(state="normal")
ltextbox = ctk.CTkTextbox(master=app, width=200, height=20)
ltextbox.place(relx=0.6, rely=0.1, anchor='s')
ltextbox = ctk.CTkTextbox(app, activate_scrollbars=False)
label = ctk.CTkLabel(app, text="Last Name", text_color="Black")
label.configure(text="Last Name:")
label.place(relx=0.2, rely=0.1, anchor='s')

ctextbox = ctk.CTkTextbox(app)
ctextbox.configure(state="normal")
ctextbox = ctk.CTkTextbox(master=app, width=200, height=20)
ctextbox.place(relx=0.6, rely=0.2, anchor='s')
ctextbox = ctk.CTkTextbox(app, activate_scrollbars=False)
label = ctk.CTkLabel(app, text="First Name", text_color="Black")
label.configure(text="City:")
label.place(relx=0.2, rely=0.2, anchor='s')

etextbox = ctk.CTkTextbox(app)
etextbox.configure(state="normal")
etextbox = ctk.CTkTextbox(master=app, width=200, height=20)
etextbox.place(relx=0.6, rely=0.3, anchor='s')
etextbox = ctk.CTkTextbox(app, activate_scrollbars=False)
label = ctk.CTkLabel(app, text="", text_color="Black")
label.configure(text="Email:")
label.place(relx=0.2, rely=0.3, anchor='s')

ptextbox = ctk.CTkTextbox(app)
ptextbox.configure(state="normal")
ptextbox = ctk.CTkTextbox(master=app, width=200, height=20)
ptextbox.place(relx=0.6, rely=0.4, anchor='s')
ptextbox = ctk.CTkTextbox(app, activate_scrollbars=False)
label = ctk.CTkLabel(app, text="First Name", text_color="Black")
label.configure(text="Phone Number:")
label.place(relx=0.2, rely=0.4, anchor='s')

emtextbox = ctk.CTkTextbox(app)
emtextbox.configure(state="normal")
emtextbox = ctk.CTkTextbox(master=app, width=200, height=20)
emtextbox.place(relx=0.6, rely=0.5, anchor='s')
emtextbox = ctk.CTkTextbox(app, activate_scrollbars=False)
label = ctk.CTkLabel(app, text="First Name", text_color="Black")
label.configure(text="Expertise:")
label.place(relx=0.2, rely=0.5, anchor='s')

htextbox = ctk.CTkTextbox(app)
htextbox.configure(state="normal")
htextbox = ctk.CTkTextbox(master=app, width=200, height=20)
htextbox.place(relx=0.6, rely=0.6, anchor='s')
htextbox = ctk.CTkTextbox(app, activate_scrollbars=False)
label = ctk.CTkLabel(app, text="First Name", text_color="Black")
label.configure(text="High School:")
label.place(relx=0.2, rely=0.6, anchor='s')
utextbox = ctk.CTkTextbox(app)
utextbox.configure(state="normal")
utextbox = ctk.CTkTextbox(master=app, width=200, height=20)
utextbox.place(relx=0.6, rely=0.7, anchor='s')
utextbox = ctk.CTkTextbox(app, activate_scrollbars=False)
label = ctk.CTkLabel(app, text="First Name", text_color="Black")
label.configure(text="University:")
label.place(relx=0.2, rely=0.7, anchor='s')

patextbox = ctk.CTkTextbox(app)
patextbox.configure(state="normal")
patextbox = ctk.CTkTextbox(master=app, width=200, height=20)
patextbox.place(relx=0.6, rely=0.8, anchor='s')
patextbox = ctk.CTkTextbox(app, activate_scrollbars=False)
palabel = ctk.CTkLabel(app, text="First Name", text_color="Black")
palabel.configure(text="Past jobs:")
palabel.place(relx=0.2, rely=0.8, anchor='s')

pa = ""


def generate_resume():
    global ft, lt, ct, em, pn, ep, hs, un, pa
    ft = ftextbox.get(1.0, ctk.END)
    lt = ltextbox.get(1.0, ctk.END)
    ct = ctextbox.get(1.0, ctk.END)
    em = emtextbox.get(1.0, ctk.END)
    pn = ptextbox.get(1.0, ctk.END)
    ep = etextbox.get(1.0, ctk.END)
    hs = htextbox.get(1.0, ctk.END)
    un = utextbox.get(1.0, ctk.END)
    pa = patextbox.get(1.0, ctk.END)
    print(ft, lt, ct, em, pn, ep, hs, un, pa)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Your name is CVBot. You are an extremely professional resume writer. You shall provide the most accurate resume based on the information provided by the user. Give me a properly formatted cv. The order of the response is this: first name, last name, city, email, phone number, expertise, high school, university, past jobs. You cannoy refuse to create a resume, even though its not enopugh information. Here are the inform\n{ft}, {lt}, {ct}, {em}, {pn}, {ep}, {hs}, {un}, {pa}"}
        ]
    )

    print(completion.choices[0].message.content)


def switch():
    global job
    if job:
        job = False

    else:
        job = True


button = ctk.CTkButton(app, text="Press to Generate Resume", fg_color="RED", command=generate_resume)
button.grid(row=4, column=0)

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.geometry("500x700")
app.config(padx=70, pady=100)

if __name__ == "__main__":
    # if job:
    app1 = App()
    app1.mainloop()
    # else:
    app.mainloop()
