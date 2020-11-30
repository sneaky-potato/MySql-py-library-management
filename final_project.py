# MYSQL Project
# coded by Ashwani Kumar Kamal (XII/A)
# Completed on 12 November 2019

import mysql.connector as mysql
from tkinter import *
import tkinter.messagebox
import sys

top = Tk() # Authentication window
top.title('Authentication')
top.geometry("500x250")
top.config(bg='dodger blue')
displaycount=0
addreccount=0
popcount=0
searchcount=0
updatecount=0

def connect():
    global password
    password = str(password_entry.get())
    try:
        con=mysql.connect(host='localhost',user='root',passwd=password,database='book_management')
        cursor=con.cursor()
    except:
        tkinter.messagebox.showinfo('ERROR', 'Can\'t connect, try again')
        top.destroy()
        sys.exit()
    
    if con.is_connected():
        tkinter.messagebox.showinfo('CONNECTED', 'Connection successful')
        top.destroy()
        main()
    else:
        print('Connecteion not established')
        top.destroy()
        sys.exit()
        
    return con,cursor

def connectivity():
    global con
    global cursor
    con=mysql.connect(host='localhost',user='root',password=password,database='book_management')
    cursor=con.cursor()
    return con,cursor

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

def populate(frame):
    '''Put in some data'''
    for row in range(100):
        Label(frame, width=150,bg='dodger blue').grid(row=row, column=0)
        Label(frame,bg='dodger blue').grid(row=row, column=1)

        n=1
        x_coor=60
        y_coor=60
        Button(displaytop,text="Back to Main Menu",width=15,command=main,bg='lemon chiffon').place(x=20,y=20)
        Label (frame, text=('Here are all record in the database'),bg='dodger blue',fg='white',font="none 12 bold").place(x=160, y=20)
    
    for(B_ID,B_NAME,B_AUTHOR,MRP)in data:
        
        Label (frame, text=(n,"."),bg='dodger blue',fg='white',font="none 12 bold").place(x=x_coor, y=y_coor)
        y_coor+=20
        Label (frame, text=("B_ID=",str(B_ID).zfill(5)),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
        y_coor+=20
        Label (frame, text=("B_NAME=",B_NAME),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
        y_coor+=20
        Label (frame, text=("B_AUTHOR=",B_AUTHOR),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
        y_coor+=20
        Label (frame, text=("MRP=",str(MRP)),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
        y_coor+=20
        Label (frame, text=("------"),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
        n=n+1
        y_coor+=40

def display(): # display all records window
    global displaycount,addreccount,popcount,searchcount,updatecount
    global displaytop
    addreccount=popcount=searchcount=updatecount=0
    displaycount = 1
    displaytop = Tk()
    displaytop.configure(bg='dodger blue')
    displaytop.title('Table Content')
    displaytop.geometry("600x900")
    connectivity()
    cursor.execute('select * from book;')
    global data
    data=cursor.fetchall()
    
    canvas = Canvas(displaytop, borderwidth=0, background="#ffffff")
    frame = Frame(canvas, background="dodger blue")
    vsb = Scrollbar(displaytop, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set,bg='dodger blue')

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
    populate(frame)

    maintop.destroy()

def addrec(): # add a new record window
    connectivity()
    
    global displaycount, addreccount,popcount,searchcount,updatecount
    global addrectop
    global B_ID_entry, B_NAME_entry, B_AUTHOR_entry, MRP_entry
    displaycount=popcount=searchcount=updatecount=0
    addreccount=1
    addrectop = Tk()
    addrectop.title('Add Record')
    addrectop.geometry("450x320")
    addrectop.config(bg='dodger blue')
    Button(addrectop,text="Back to Main Menu",width=15,command=main,bg='lemon chiffon').place(x=20,y=20)
    Button(addrectop,text="Info about table",width=15,command=info,bg='lemon chiffon').place(x=320,y=20)
    Label (addrectop, text=('Add a new record'),font="none 12 bold", bg='dodger blue',fg='white').place(x=160, y=20)
    B_ID_label = Label(addrectop, text = 'Book ID:', bg='dodger blue',fg='white').place(x = 65, y = 80)
    B_NAME_label = Label(addrectop, text = 'Book Name:', bg='dodger blue',fg='white').place(x = 65, y = 100)
    B_AUTHOR_label = Label(addrectop, text = 'Book Author:', bg='dodger blue',fg='white').place(x = 65, y = 120)
    MRP_label = Label(addrectop, text = 'MRP:', bg='dodger blue',fg='white').place(x = 65, y = 140)
    
    B_ID_entry = Entry(addrectop)
    B_ID_entry.place(x =165, y = 80)
    B_NAME_entry = Entry(addrectop)
    B_NAME_entry.place(x =165, y = 100)
    B_AUTHOR_entry = Entry(addrectop)
    B_AUTHOR_entry.place(x =165, y = 120)
    MRP_entry = Entry(addrectop)
    MRP_entry.place(x =165, y = 140)
    
    submit = Button(addrectop, text = 'Submit', command=submit_addrec,bg='lemon chiffon').place(x = 180, y=250)
    maintop.destroy()

def info():
    tkinter.messagebox.showinfo("Information","Book ID: Integer\nBook Name: Varchar(50)\nBook Author: Varchar(30)\nMRP: Integer")

def submit_addrec(): # add a record
    connectivity()
    
    bid = int(B_ID_entry.get())
    bname = B_NAME_entry.get()
    bauthor = B_AUTHOR_entry.get()
    bmrp = int(MRP_entry.get())
    B_ID_entry.delete(0, 'end')
    B_NAME_entry.delete(0, 'end')
    B_AUTHOR_entry.delete(0, 'end')
    MRP_entry.delete(0, 'end')
    tup = (bid,bname,bauthor,bmrp)
    s = 'insert into book values (%s,%s,%s,%s)'
    try:
        cursor.execute(s,tup)
        con.commit()
        con.close()
        Label (addrectop, text=('Successfully added'),font="none 12 bold",bg='dodger blue',fg='white').place(x=150, y=280)
    except:
        Label (addrectop, text=('Error in entry, try again'),font="none 12 bold",bg='dodger blue',fg='white').place(x=130, y=280)

def del_all(): # clear the table
    try:
        connectivity()
        cursor.execute('delete from book')
        con.commit()
        con.close()
        Label(poptop,text='Successfully cleared the table',font='none 12 bold',bg='dodger blue',fg='white').place(x=220,y=280)
    except:
        Label(poptop,text='Table already empty',font='none 12 bold',bg='dodger blue',fg='white').place(x=220,y=280)
    
def del_part(): # delete particular record
    connectivity()
    del_value=del_entry.get()
    del_entry.delete(0,'end')
    try:
        connectivity()
        tup=(del_value,)
        s='delete from book where B_ID=%s'
        cursor.execute(s,tup)
        con.commit()
        r="%d"%cursor.rowcount
        con.close()
        if int(r)!=0:
            Label(poptop,text='Successfully deleted the record',font='none 12 bold',bg='dodger blue',fg='white').place(x=100,y=280)
        else:
            Label(poptop,text='No such record exists',font='none 12 bold',bg='dodger blue',fg='white').place(x=150,y=280)
    except:
        Label(poptop,text='Error in entry',font='none 12 bold',bg='dodger blue',fg='white').place(x=220,y=280)
        
def pop(): # delete record window
    global displaycount, addreccount, popcount,searchcount,updatecount
    global poptop
    global del_entry
    displaycount = addreccount=searchcount=updatecount=0
    popcount=1
    poptop = Tk()
    poptop.title('Delete Menu')
    poptop.geometry("450x320")
    poptop.config(bg='dodger blue')
    Button(poptop,text="Back to Main Menu",width=15,command=main,bg='lemon chiffon').place(x=20,y=20)
    Label (poptop, text=('Delete Record'),font="none 12 bold",fg='white',bg='dodger blue').place(x=160, y=20)
    Button(poptop, text=('Delete all records'),bg='lemon chiffon',command=del_all).place(x=170, y=90)
    Label(poptop,text='Enter Book ID', bg='dodger blue',fg='white',font='none 10 bold').place(x=100,y=160)
    Button(poptop, text=('Delete particular record'),bg='lemon chiffon',command=del_part).place(x=160, y=200)
    del_entry=Entry(poptop)
    del_entry.place(x=220,y=160)
    maintop.destroy()
    
def quitapp(): # quit application
    answer = tkinter.messagebox.askyesno("Quit Application","Do you really want to quit?")
    if answer == 1:
        maintop.destroy()
        sys.exit
    else:
        pass

def searchid(): # search by id
    connectivity()
    root=Tk()
    B_ID_value=B_ID_entry.get()
    B_ID_entry.delete(0,'end')
    B_NAME_entry.delete(0,'end')
    B_AUTHOR_entry.delete(0,'end')
    root.title('Results (ID)')
    root.geometry("500x500")
    root.config(bg='dodger blue')
    Label(root, text='Results by ID', font='none 12 bold', bg='dodger blue', fg='white').place(x=200,y=20)
    tup=(B_ID_value,)
    s='select * from book where B_ID = %s'
    cursor.execute(s,tup)
    data=cursor.fetchall()
    r="%d"%cursor.rowcount
    con.close()
    n=1
    x_coor=y_coor=60
    if int(r)!=0:
        for(B_ID,B_NAME,B_AUTHOR,MRP)in data:
            Label (root, text=(n,"."),bg='dodger blue',fg='white',font="none 12 bold").place(x=x_coor, y=y_coor)
            y_coor+=20
            Label (root, text=("B_ID=",str(B_ID).zfill(5)),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            y_coor+=20
            Label (root, text=("B_NAME=",B_NAME),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            y_coor+=20
            Label (root, text=("B_AUTHOR=",B_AUTHOR),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            y_coor+=20
            Label (root, text=("MRP=",str(MRP)),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            y_coor+=20
            Label (root, text=("------"),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            n=n+1
            y_coor+=40
    else:
        Label (root, text='No such record exists',bg='dodger blue',fg='white',font="none 12 bold").place(x=x_coor, y=y_coor)

def searchname(): # search by name
    connectivity()
    root=Tk()
    B_NAME_value=B_NAME_entry.get()
    B_ID_entry.delete(0,'end')
    B_NAME_entry.delete(0,'end')
    B_AUTHOR_entry.delete(0,'end')
    root.title('Results (ID)')
    root.geometry("500x500")
    root.config(bg='dodger blue')
    Label(root, text='Results by Name', font='none 12 bold', bg='dodger blue', fg='white').place(x=200,y=20)
    tup=(B_NAME_value,)
    s='select * from book where B_NAME = %s'
    cursor.execute(s,tup)
    data=cursor.fetchall()
    r="%d"%cursor.rowcount
    con.close()
    n=1
    x_coor=y_coor=60
    if int(r)!=0:
        for(B_ID,B_NAME,B_AUTHOR,MRP)in data:
            Label (root, text=(n,"."),bg='dodger blue',fg='white',font="none 12 bold").place(x=x_coor, y=y_coor)
            y_coor+=20
            Label (root, text=("B_ID=",str(B_ID).zfill(5)),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            y_coor+=20
            Label (root, text=("B_NAME=",B_NAME),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            y_coor+=20
            Label (root, text=("B_AUTHOR=",B_AUTHOR),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            y_coor+=20
            Label (root, text=("MRP=",str(MRP)),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            y_coor+=20
            Label (root, text=("------"),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            n=n+1
            y_coor+=40
    else:
        Label (root, text='No such record exists',bg='dodger blue',fg='white',font="none 12 bold").place(x=x_coor, y=y_coor)
 
def searchauthor(): # search by author
    connectivity()
    root=Tk()
    B_AUTHOR_value=B_AUTHOR_entry.get()
    B_ID_entry.delete(0,'end')
    B_NAME_entry.delete(0,'end')
    B_AUTHOR_entry.delete(0,'end')
    root.title('Results (ID)')
    root.geometry("500x500")
    root.config(bg='dodger blue')
    Label(root, text='Results by AUTHOR', font='none 12 bold', bg='dodger blue', fg='white').place(x=200,y=20)
    tup=(B_AUTHOR_value,)
    s='select * from book where B_AUTHOR = %s'
    cursor.execute(s,tup)
    data=cursor.fetchall()
    r="%d"%cursor.rowcount
    con.close()
    n=1
    x_coor=y_coor=60
    if int(r)!=0:
        for(B_ID,B_NAME,B_AUTHOR,MRP)in data:
            Label (root, text=(n,"."),bg='dodger blue',fg='white',font="none 12 bold").place(x=x_coor, y=y_coor)
            y_coor+=20
            Label (root, text=("B_ID=",str(B_ID).zfill(5)),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            y_coor+=20
            Label (root, text=("B_NAME=",B_NAME),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            y_coor+=20
            Label (root, text=("B_AUTHOR=",B_AUTHOR),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            y_coor+=20
            Label (root, text=("MRP=",str(MRP)),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            y_coor+=20
            Label (root, text=("------"),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            n=n+1
            y_coor+=40
    else:
        Label (root, text='No such record exists',bg='dodger blue',fg='white',font="none 12 bold").place(x=x_coor, y=y_coor)

def search(): # search window
    global displaycount, addreccount, popcount, searchcount, updatecount
    global searchtop
    global B_ID_entry, B_NAME_entry, B_AUTHOR_entry
    desplaycount=addreccount=popcount=updatecount=0
    searchcount=1
    searchtop = Tk()
    searchtop.configure(bg='dodger blue')
    searchtop.title('Search Table')
    searchtop.geometry("470x320")
    searchtop.config(bg='dodger blue')
    Button(searchtop,text="Back to Main Menu",width=15,command=main,bg='lemon chiffon').place(x=20,y=20)
    Label(searchtop, text=('Search a Record'),font="none 12 bold",fg='white',bg='dodger blue').place(x=160, y=20)
    B_ID_label = Label(searchtop, text = 'Book ID:', bg='dodger blue',fg='white').place(x = 65, y = 80)
    B_NAME_label = Label(searchtop, text = 'Book Name:', bg='dodger blue',fg='white').place(x = 65, y = 120)
    B_AUTHOR_label = Label(searchtop, text = 'Book Author:', bg='dodger blue',fg='white').place(x = 65, y = 160)
    B_ID_entry = Entry(searchtop)
    B_ID_entry.place(x =165, y = 80)
    B_NAME_entry = Entry(searchtop)
    B_NAME_entry.place(x =165, y = 120)
    B_AUTHOR_entry = Entry(searchtop)
    B_AUTHOR_entry.place(x =165, y = 160)

    Button(searchtop,command=searchid,text='Search by Book ID', width=20,bg='lemon chiffon').place(x=300,y=80)
    Button(searchtop,command=searchname,text='Search by Book Name', width=20,bg='lemon chiffon').place(x=300,y=120)
    Button(searchtop,command=searchauthor,text='Search by Book Author', width=20,bg='lemon chiffon').place(x=300,y=160)
    
    maintop.destroy()

def updatebid():
    connectivity()
    bid=int(B_ID_entryupdate.get())
    B_ID_entryupdate.delete(0,'end')
    B_NAME_entryupdate.delete(0,'end')
    B_AUTHOR_entryupdate.delete(0,'end')
    MRP_entryupdate.delete(0,'end')
    tup=(bid,B_ID_value)
    s='update book set B_ID=%s where B_ID=%s'
    try:
        cursor.execute(s,tup)
        con.commit()
        r="%d"%cursor.rowcount
        con.close()
        Label(updatetop,text='Updated '+r+' rows',bg='dodger blue', fg='white',font='none 10 bold').place(x=280,y=360)
    except:
        Label(updatetop,text='Error in entry',bg='dodger blue', fg='white',font='none 10 bold').place(x=280,y=360)

def updatename():
    connectivity()
    bid=B_NAME_entryupdate.get()
    B_ID_entryupdate.delete(0,'end')
    B_NAME_entryupdate.delete(0,'end')
    B_AUTHOR_entryupdate.delete(0,'end')
    MRP_entryupdate.delete(0,'end')
    tup=(bid,B_ID_value)
    s='update book set B_NAME=%s where B_ID=%s'
    try:
        cursor.execute(s,tup)
        con.commit()
        r="%d"%cursor.rowcount
        con.close()
        Label(updatetop,text='Updated '+r+' rows',bg='dodger blue', fg='white',font='none 10 bold').place(x=280,y=360)
    except:
        Label(updatetop,text='Error in entry',bg='dodger blue', fg='white',font='none 10 bold').place(x=280,y=360)

def updateauthor():
    connectivity()
    bid=B_AUTHOR_entryupdate.get()
    B_ID_entryupdate.delete(0,'end')
    B_NAME_entryupdate.delete(0,'end')
    B_AUTHOR_entryupdate.delete(0,'end')
    MRP_entryupdate.delete(0,'end')
    tup=(bid,B_ID_value)
    s='update book set B_AUTHOR=%s where B_ID=%s'
    try:
        cursor.execute(s,tup)
        con.commit()
        r="%d"%cursor.rowcount
        con.close()
        Label(updatetop,text='Updated '+r+' rows',bg='dodger blue', fg='white',font='none 10 bold').place(x=280,y=360)
    except:
        Label(updatetop,text='Error in entry',bg='dodger blue', fg='white',font='none 10 bold').place(x=280,y=360)

def updatemrp():
    connectivity()
    bid=MRP_entryupdate.get()
    B_ID_entryupdate.delete(0,'end')
    B_NAME_entryupdate.delete(0,'end')
    B_AUTHOR_entryupdate.delete(0,'end')
    MRP_entryupdate.delete(0,'end')
    tup=(bid,B_ID_value)
    s='update book set MRP=%s where B_ID=%s'
    try:
        cursor.execute(s,tup)
        con.commit()
        r="%d"%cursor.rowcount
        con.close()
        Label(updatetop,text='Updated '+r+' rows',bg='dodger blue', fg='white',font='none 10 bold').place(x=280,y=360)
    except:
        Label(updatetop,text='Error in entry',bg='dodger blue', fg='white',font='none 10 bold').place(x=280,y=360)

def updateid():
    global B_ID_entryupdate,B_NAME_entryupdate,B_AUTHOR_entryupdate,MRP_entryupdate
    global B_ID_value
    connectivity()
    B_ID_value=B_ID_entry.get()
    tup=(B_ID_value,)
    s='select * from book where B_ID = %s'
    cursor.execute(s,tup)
    data=cursor.fetchall()
    r="%d"%cursor.rowcount
    con.close()
    x_coor,y_coor=20,120
    if int(r)!=0:
        for(B_ID,B_NAME,B_AUTHOR,MRP)in data:
            Label (updatetop, text=("B_ID=",str(B_ID).zfill(5)),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            y_coor+=20
            Label (updatetop, text=("B_NAME=",B_NAME),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            y_coor+=20
            Label (updatetop, text=("B_AUTHOR=",B_AUTHOR),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            y_coor+=20
            Label (updatetop, text=("MRP=",str(MRP)),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            y_coor+=20
            Label (updatetop, text=("------"),bg='dodger blue',fg='white',font="none 10 bold").place(x=x_coor,y=y_coor)
            y_coor+=40
        Label(updatetop,text='Book ID selected: '+B_ID_value,fg='white',bg='dodger blue',font='none 10 bold').place(x=380,y=20)
        B_ID_label = Label(updatetop, text = 'Book ID:', bg='dodger blue',fg='white').place(x = 160, y = 120)
        B_NAME_label = Label(updatetop, text = 'Book Name:', bg='dodger blue',fg='white').place(x =160, y = 160)
        B_AUTHOR_label = Label(updatetop, text = 'Book Author:', bg='dodger blue',fg='white').place(x =160, y = 200)
        MRP_label = Label(updatetop, text = 'Book Author:', bg='dodger blue',fg='white').place(x =160, y = 240)

        B_ID_entryupdate = Entry(updatetop)
        B_ID_entryupdate.place(x =240, y = 120)
        B_NAME_entryupdate = Entry(updatetop)
        B_NAME_entryupdate.place(x =240, y = 160)
        B_AUTHOR_entryupdate = Entry(updatetop)
        B_AUTHOR_entryupdate.place(x =240, y = 200)
        MRP_entryupdate = Entry(updatetop)
        MRP_entryupdate.place(x =240, y = 240)

        Button(updatetop,command=updatebid,text='Update Book ID', width=20,bg='lemon chiffon').place(x=380,y=120)
        Button(updatetop,command=updatename,text='Update Book Name', width=20,bg='lemon chiffon').place(x=380,y=160)
        Button(updatetop,command=updateauthor,text='Update Book Author', width=20,bg='lemon chiffon').place(x=380,y=200)
        Button(updatetop,command=updatemrp,text='Update Book MRP', width=20,bg='lemon chiffon').place(x=380,y=240)
    
    else:
        Label(updatetop,text='Book ID selected: '+B_ID_value,fg='white',bg='dodger blue',font='none 10 bold').place(x=380,y=20)
        root=Tk()
        root.geometry("470x320")
        root.config(bg='dodger blue')
        Label (root, text='No such record exists',bg='dodger blue',fg='white',font="none 12 bold").place(x=x_coor, y=y_coor)

def update(): # update window
    global displaycount, addreccount, popcount, searchcount, updatecount
    global updatetop
    global B_ID_entry
    desplaycount=addreccount=popcount=searchcount=0
    updatecount=1
    updatetop = Tk()
    updatetop.configure(bg='dodger blue')
    updatetop.title('Update Table')
    updatetop.geometry("600x380")
    updatetop.config(bg='dodger blue')
    Button(updatetop,text="Back to Main Menu",width=15,command=main,bg='lemon chiffon').place(x=20,y=20)
    Label(updatetop, text=('Update a Record'),font="none 12 bold",fg='white',bg='dodger blue').place(x=200, y=20)
    B_ID_label = Label(updatetop, text = 'Book ID of record to be updated:', bg='dodger blue',fg='white').place(x = 30, y = 80)
    B_ID_entry = Entry(updatetop)
    B_ID_entry.place(x =220, y = 80)
    Button(updatetop,command=updateid,text='Sumit', width=20,bg='lemon chiffon').place(x=370,y=80)
    maintop.destroy()

def main(): # main menu window
    global displaycount,addreccount,popcount,searchcount,updatecount
    if displaycount == 1:
        displaytop.destroy()
        displaycount=0
    elif addreccount == 1:
        addrectop.destroy()
        addreccount=0
    elif popcount == 1:
        poptop.destroy()
        popcount=0
    elif searchcount == 1:
        searchtop.destroy()
        searchcount=0
    elif updatecount == 1:
        updatetop.destroy()
        updatecount=0
    connectivity()
    global maintop
    maintop = Tk()
    maintop.title('Main Menu')
    maintop.geometry("450x300")
    maintop.config(bg='dodger blue')
    Label(maintop, text = 'WELCOME TO MAIN MENU',font="none 12 bold",bg='dodger blue',fg='white').place(x=130, y=20)
    Button(maintop,text="Add Book Record",width=26, command = addrec,bg='lemon chiffon').place(x=20, y= 60)
    Button(maintop,text="Display All Records",width=26, command = display,bg='lemon chiffon').place(x=220, y= 60)
    Button(maintop,text="Search a Record",width=26,bg='lemon chiffon',command=search).place(x=20,y=100)
    Button(maintop,text="Update Book Record",width=26,bg='lemon chiffon',command=update).place(x=220, y=100)
    Button(maintop,text="Delete Book Record",width=26, command=pop,bg='lemon chiffon').place(x=20, y=140)
    Button(maintop,text="Exit",width=26, command=quitapp,bg='lemon chiffon').place(x=220, y=140)
    maintop.iconbitmap('book_ico.ico')
title_label = Label(top, text='Enter the MYSQL server password to access database', font = 'none 12 bold', fg='white', bg='dodger blue').place(x=40,y=30)
password_label = Label(top, text = 'MYSQL password:', font='none 10 bold', fg='white', bg='dodger blue').place(x = 120, y = 80)
password_entry = Entry(top)
password_entry.place(x =240, y = 80)
connect_b = Button(top, text = 'Connect to MYSQL server',font='none 10 bold' ,command=connect, bg='lemon chiffon').place(x = 160, y=140)
top.mainloop() # first window
