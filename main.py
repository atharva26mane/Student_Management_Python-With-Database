from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3
from PIL import Image, ImageTk, ImageFilter

def Database():
    global conn, cursor
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS STUD_REGISTRATION (STU_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, STU_NAME TEXT, STU_CONTACT TEXT, STU_EMAIL TEXT, STU_ROLLNO TEXT, STU_BRANCH TEXT)")

def DisplayForm():
    display_screen = Tk()
    display_screen.geometry("900x400")
    display_screen.title("Student Management System")

    global tree, SEARCH, name, contact, email, rollno, branch
    SEARCH = StringVar()
    name = StringVar()
    contact = StringVar()
    email = StringVar()
    rollno = StringVar()
    branch = StringVar()

    bg_color = "#F0F0F0"
    btn_color = "#4CAF50"
    btn_hover_color = "#45a049"
    lbl_text_color = "white"

    try:
        # Load and display the background image with blur effect
        image = Image.open("C:/Users/athar/Downloads/student management/student-management-system/images/BACKGROUND.png")
        image = image.resize((900, 400), Image.ANTIALIAS)
        blurred_image = image.filter(ImageFilter.BLUR)
        photo = ImageTk.PhotoImage(blurred_image)

        # Create a label to display the image
        image_label = Label(display_screen, image=photo)
        image_label.image = photo
        image_label.place(x=0, y=0, relwidth=1, relheight=1)  # Position the image label to cover the entire window

    except FileNotFoundError:
        print("Error: background image not found")

    TopViewForm = Frame(display_screen, width=600, bg="#1C2833")
    TopViewForm.pack(side=TOP, fill=X)

    lbl_text = Label(TopViewForm, text="Student Management System", font=('verdana', 18), width=600, bg="#1C2833", fg=lbl_text_color)
    lbl_text.pack(fill=X)

    LFrom = Frame(display_screen, width="350", bg=bg_color)
    LFrom.pack(side=LEFT, fill=Y)

    LeftViewForm = Frame(display_screen, width=500, bg=bg_color)
    LeftViewForm.pack(side=LEFT, fill=Y)

    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)

    Label(LFrom, text="Name", font=("Arial", 12), bg=bg_color).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=name).pack(side=TOP, padx=10, fill=X)

    Label(LFrom, text="Contact", font=("Arial", 12), bg=bg_color).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=contact).pack(side=TOP, padx=10, fill=X)

    Label(LFrom, text="Email", font=("Arial", 12), bg=bg_color).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=email).pack(side=TOP, padx=10, fill=X)

    Label(LFrom, text="Rollno", font=("Arial", 12), bg=bg_color).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=rollno).pack(side=TOP, padx=10, fill=X)

    Label(LFrom, text="Branch", font=("Arial", 12), bg=bg_color).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=branch).pack(side=TOP, padx=10, fill=X)

    Button(LFrom, text="Submit", font=("Arial", 10, "bold"), command=register, bg=btn_color, fg="white", activebackground=btn_hover_color).pack(side=TOP, padx=10, pady=5, fill=X)

    lbl_txtsearch = Label(LeftViewForm, text="Enter name to Search", font=('verdana', 10), bg=bg_color)
    lbl_txtsearch.pack()

    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)

    btn_search = Button(LeftViewForm, text="Search", command=SearchRecord, bg=btn_color, fg="white", activebackground=btn_hover_color)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_view = Button(LeftViewForm, text="View All", command=DisplayData, bg=btn_color, fg="white", activebackground=btn_hover_color)
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_reset = Button(LeftViewForm, text="Reset", command=Reset, bg=btn_color, fg="white", activebackground=btn_hover_color)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_delete = Button(LeftViewForm, text="Delete", command=Delete, bg=btn_color, fg="white", activebackground=btn_hover_color)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_update = Button(LeftViewForm, text="Update", command=Update, bg=btn_color, fg="white", activebackground=btn_hover_color)
    btn_update.pack(side=TOP, padx=10, pady=10, fill=X)

    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("Student Id", "Name", "Contact", "Email", "Rollno", "Branch"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Student Id', text="Student Id", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Contact', text="Contact", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('Rollno', text="Rollno", anchor=W)
    tree.heading('Branch', text="Branch", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()

    DisplayData()

def register():
    Database()
    
    # Retrieve values from entry fields
    name1 = name.get()
    con1 = contact.get()
    email1 = email.get()
    rol1 = rollno.get()
    branch1 = branch.get()

    # Check if any field is empty
    if name1 == '' or con1 == '' or email1 == '' or rol1 == '' or branch1 == '':
        tkMessageBox.showinfo("Warning", "Fill all the fields!!!")
    else:
        # Insert data into the database
        conn.execute('INSERT INTO STUD_REGISTRATION (STU_NAME,STU_CONTACT,STU_EMAIL,STU_ROLLNO,STU_BRANCH) VALUES (?,?,?,?,?)',(name1, con1, email1, rol1, branch1))
        conn.commit()
        tkMessageBox.showinfo("Message", "Stored successfully")
        DisplayData()
        conn.close()

def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")
    name.set("")
    contact.set("")
    email.set("")
    rollno.set("")
    branch.set("")

def Delete():
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning", "Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor = conn.execute("DELETE FROM STUD_REGISTRATION WHERE STU_ID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def SearchRecord():
    Database()
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        cursor = conn.execute("SELECT * FROM STUD_REGISTRATION WHERE STU_NAME LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def Update():
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning", "Select data to update")
    else:
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        name1 = name.get()
        con1 = contact.get()
        email1 = email.get()
        rol1 = rollno.get()
        branch1 = branch.get()

        if name1 == '' or con1 == '' or email1 == '' or rol1 == '' or branch1 == '':
            tkMessageBox.showinfo("Warning", "Fill all the fields!!!")
        else:
            conn.execute("UPDATE STUD_REGISTRATION SET STU_NAME=?, STU_CONTACT=?, STU_EMAIL=?, STU_ROLLNO=?, STU_BRANCH=? WHERE STU_ID=?", (name1, con1, email1, rol1, branch1, selecteditem[0]))
            conn.commit()
            tkMessageBox.showinfo("Message", "Updated successfully")
            DisplayData()
            conn.close()

def DisplayData():
    Database()
    tree.delete(*tree.get_children())
    cursor = conn.execute("SELECT * FROM STUD_REGISTRATION")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

DisplayForm()
if __name__ == '__main__':
    mainloop()
