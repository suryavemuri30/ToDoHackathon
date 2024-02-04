import pickle
import datetime
from tkinter import *
from tkinter import messagebox
import os
from plyer import notification
import pyttsx3



def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK", command=delete3).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()

def register_user():
    print("working")
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(screen1, text="Registration Success", fg="green", font=("calibri", 11)).pack()

def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="Login Success").pack()
    Button(screen3, text="OK", command=runroot).pack()

def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password, show="*")
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_entry1
    global password_entry1
    global username_entry_str
    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    username_entry_str = str(username_entry1)
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify, show="*")
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Login to To-Do List")
    Label(text="To-Do List", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    screen.mainloop()
def runroot():
    global username1
    root = Tk()
    root.title("To-Do List")
    root.resizable(0, 0)

    # GUI
    current_date = datetime.datetime.now()
    user_label = Label(root, text="Welcome, " + username1 + "!")
    while True:
        engine = pyttsx3.init()
        engine.say("Welcome" + username1)
        engine.runAndWait()
        break
    user_label.pack()
    user_date = Label(root, text="Today's date is " + current_date.strftime("%d/%m/%y"))
    user_date.pack()

    frame_tasks1 = Frame(root)
    frame_tasks1.pack(side=TOP, padx=10, pady=5)
    frame_tasks2 = Frame(root)
    frame_tasks2.pack(side=LEFT, padx=10, pady=5)
    frame_tasks3 = Frame(root)
    frame_tasks3.pack(side=RIGHT, padx=10, pady=5)
    frame_tasks4 = Frame(root)
    frame_tasks4.pack(side=BOTTOM, padx=10, pady=5)

    label_tasks1 = Label(frame_tasks1, text="Urgent and Important")
    label_tasks1.pack()
    listbox_tasks1 = Listbox(frame_tasks1, height=10, width=50)
    listbox_tasks1.pack()

    label_tasks2 = Label(frame_tasks2, text="Urgent and Not Important")
    label_tasks2.pack()
    listbox_tasks2 = Listbox(frame_tasks2, height=10, width=50)
    listbox_tasks2.pack()

    label_tasks3 = Label(frame_tasks3, text="Not Urgent and Important")
    label_tasks3.pack()
    listbox_tasks3 = Listbox(frame_tasks3, height=10, width=50)
    listbox_tasks3.pack()

    label_tasks4 = Label(frame_tasks4, text="Not Urgent and Not Important")
    label_tasks4.pack()
    listbox_tasks4 = Listbox(frame_tasks4, height=10, width=50)
    listbox_tasks4.pack()


    def add_task():
        task = entry_task.get()
        if task != "":
            answer = messagebox.askyesno(title="Urgency of Task", message='''Is this an Urgent task?''')
            if answer is True:
                imp = messagebox.askyesno(title="Importancy of Task", message="Is this task important?")
                if imp is True:
                    listbox_tasks1.insert(END, task)
                    entry_task.delete(0, END)
                else:
                    listbox_tasks2.insert(END, task)
                    entry_task.delete(0, END)
            else:
                urgent1 = messagebox.askyesno(title="Importancy of Task", message="Is this task important?")
                if urgent1 is True:
                    listbox_tasks3.insert(END, task)
                    entry_task.delete(0, END)
                else:
                    listbox_tasks4.insert(END, task)
                    entry_task.delete(0, END)
        else:
            messagebox.showwarning(title="Warning!", message="You must enter a task.")

    root.bind("<Return>", lambda event: add_task())

    def delete_task():
        try:
            task_index = listbox_tasks1.curselection()[0]
            listbox_tasks1.delete(task_index)
        except:
            try:
                task_index2 = listbox_tasks2.curselection()[0]
                listbox_tasks2.delete(task_index2)
            except:
                try:
                    task_index3 = listbox_tasks3.curselection()[0]
                    listbox_tasks3.delete(task_index3)
                except:
                    try:
                        task_index4 = listbox_tasks4.curselection()[0]
                        listbox_tasks4.delete(task_index4)
                    except:
                        messagebox.showwarning(title="Warning!", message="You must select a task.")

    root.bind("<Control-d>", lambda event: delete_task())

    def load_tasks():
        global username_entry1
        try:
            tasks = pickle.load(open("%s.dat" % username1, "rb"))
            listbox_tasks1.delete(0, END)
            for task in tasks:
                listbox_tasks1.insert(END, task)
            tasks = pickle.load(open("1%s.dat" % username1, "rb"))
            listbox_tasks2.delete(0, END)
            for task in tasks:
                listbox_tasks2.insert(END, task)
            tasks = pickle.load(open("2%s.dat" % username1, "rb"))
            listbox_tasks3.delete(0, END)
            for task in tasks:
                listbox_tasks3.insert(END, task)
            tasks = pickle.load(open("3%s.dat" % username1, "rb"))
            listbox_tasks4.delete(0, END)
            for task in tasks:
                listbox_tasks4.insert(END, task)            
        except:
            messagebox.showwarning(title="Warning!", message="The file does not exist, you must add tasks and save them first.")


    root.bind("<Control-l>", lambda event: load_tasks())


    def save_tasks():
        global username_entry1
        tasks = listbox_tasks1.get(0, listbox_tasks1.size())
        tasks1 = listbox_tasks2.get(0, listbox_tasks2.size())
        tasks2 = listbox_tasks3.get(0, listbox_tasks3.size())
        tasks3 = listbox_tasks4.get(0, listbox_tasks4.size())
        pickle.dump(tasks, open("%s.dat" % username1, "wb"))
        pickle.dump(tasks1, open("1%s.dat" % username1, "wb"))
        pickle.dump(tasks2, open("2%s.dat" % username1, "wb"))
        pickle.dump(tasks3, open("3%s.dat" % username1, "wb"))

    root.bind("<Control-s>", lambda event: save_tasks)

    def check_shortcuts():
        messagebox.showinfo(title="Shortcuts", message='''
        Add Tasks: Press Enter after typing the task
        Delete Tasks: Press Control and D at the same time after selecting the task
        you want to delete
        Load Tasks: Press Control and L at the same time
        Save Tasks: Press Control and S at the same time
        Delete All Tasks: Press Control, Alt and D at the same time''')

    def del_all():
        listbox_tasks1.delete(0, END)
        listbox_tasks2.delete(0, END)
        listbox_tasks3.delete(0, END)
        listbox_tasks4.delete(0, END)

    def reminder():
        t = Tk()
        t.title('Notifier')
        t.geometry("500x300")

        def get_details():
            get_title = title.get()
            get_msg = msg.get()
            get_time = time1.get()

            def mainreminder():
                notification.notify(title=get_title, message=get_msg, app_name="Notifier", timeout=10)

            if get_title == "" or get_msg == "" or get_time == "":
                messagebox.showerror("Alert", "All fields are required!")
            else:
                int_time = int(float(get_time))
                min_to_sec = int_time * 60 * 1000
                messagebox.showinfo("Notifier Set", "Set notification?")
                t.destroy()
                t.after(min_to_sec, mainreminder)

        t_label = Label(t, text="Title of Reminder", font=("calibri", 10))
        t_label.place(x=8, y=70)
        title = Entry(t, width="25", font=("calibri", 13))
        title.place(x=123, y=70)
        m_label = Label(t, text="Reminder", font=("calibri", 10))
        m_label.place(x=12, y=120)
        msg = Entry(t, width="40", font=("Calibri", 13))
        msg.place(x=123, height=30, y=120)
        time_label = Label(t, text="Set Time", font=("Calibri", 10))
        time_label.place(x=12, y=175)
        time1 = Entry(t, width="5", font=("Calibri", 13))
        time1.place(x=123, y=175)
        time_min_label = Label(t, text="min", font=("Calibri", 10))
        time_min_label.place(x=175, y=180)
        but = Button(t, text="SET NOTIFICATION", font=("Calibri", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
                     relief="raised", command=get_details)
        but.place(x=170, y=230)
        t.resizable(0, 0)
        t.mainloop()

    root.bind("<Control-Alt-d>", lambda event: del_all())

    def about():
        messagebox.showinfo(title="About This Project", message='''This
        Project is a To-Do List made by Surya Vemuri, and Athak Jain, Krishna Gujrati and Ratul Lakhanpal
        1) You first create an account, and then login, which shows the main app itself.
        2) You can add tasks you need to do, and depending on the type of task, it can go to either the work or the personal section.
        3) You can save tasks, and then load them once you reopen the app after closing it.
        4) You can delete all tasks as well.
        5) An extra feature is that you can remind yourself of something after a certain amount of minutes using the Reminder button. 
        You just type in the reminder, its contents, and after how many minutes do you want the reminder to remind you, 
        and it will send a notification after that amount of time.''')

    entry_task = Entry(root, width=50)
    entry_task.pack()
    button_add_task = Button(root, text="Add task", width=48, command=add_task)
    button_add_task.pack()
    button_delete_task = Button(root, text="Delete task", width=48, command=delete_task)
    button_delete_task.pack()
    button_load_work_tasks = Button(root, text="Load Tasks", width=48, command=load_tasks)
    button_load_work_tasks.pack()
    button_save_tasks = Button(root, text="Save tasks", width=48, command=save_tasks)
    button_save_tasks.pack()
    button_shortcuts = Button(root, text="Shortcuts", width=48, command=check_shortcuts)
    button_shortcuts.pack()
    button_del_all = Button(root, text="Delete all tasks", width=48, command=del_all)
    button_del_all.pack()
    button_reminder = Button(root, text="Add a Reminder", width=48, command=reminder)
    button_reminder.pack()
    button_about = Button(root, text="About This Project", width=48, command=about)
    button_about.pack()
    screen.update()
    screen3.destroy()
    screen2.destroy()
    delete2()
    screen.destroy()
    root.mainloop()

main_screen()
