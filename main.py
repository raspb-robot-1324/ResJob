from openai import OpenAI
import customtkinter as ctk

client = OpenAI(api_key="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")

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


def generate_resume():
    global ft, lt, ct, em, pn, ep, hs, un
    ft = ftextbox.get(1.0, "end-1c")
    lt = ltextbox.get(1.0, "end-1c")
    ct = ctextbox.get(1.0, "end-1c")
    em = emtextbox.get(1.0, "end-1c")
    pn = ptextbox.get(1.0, "end-1c")
    ep = entextbox.get(1.0, "end-1c")
    hs = htextbox.get(1.0, "end-1c")
    un = utextbox.get(1.0, "end-1c")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "Your name is CVBot. You are an extremely professional resume writer. You shall provide the most accurate resume based on the experiences provided by the user. Don't create/imagine/lie about experiences if experience has not been given. Give me a properly formatted cv."},
            {"role": "user", "content": f"Here are my experiences:\n{ft}, {lt}, {ct}, {em}, {pn}, {ep}, {hs}, {un}"}
        ]
    )

    print(completion.choices[0].message.content)

button = ctk.CTkButton(app, text="Press to Generate Resume", fg_color="RED", command=generate_resume)
button.grid(row=4, column=0)

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.geometry("500x700")
app.config(padx=70, pady=100)

app.mainloop()
