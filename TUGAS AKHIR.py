from tkinter import*
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Pendaftaran Mahasiswa Baru")
root.geometry("360x390")
bg = PhotoImage(file="D:\\sementara\\logo-undip-transparan.png")
lblogo = Label(root, image=bg)
lblogo.place(x=30,y=20)

def pendaftaran():
    inputan = stringnama.get()
    input = stringtelepon.get()
    errorcode = 0
    errorcode = 0
    perdaftaran=""
    if len(stringnama.get()) == 0:
       messagebox.showerror("Error","BELUM MENGISI NAMA")
       return
    for i in range(len(inputan)):
        if inputan[i:i+1] =='1':
            errorcode = 1
        elif inputan[i:i+1] =='2':
            errorcode = 1
        elif inputan[i:i+1] =='3' : 
            errorcode = 1
        elif inputan[i:i+1] =='4' :
            errorcode = 1
        elif inputan[i:i+1] =='5' :
            errorcode = 1
        elif inputan[i:i+1] =='6' :
            errorcode = 1
        elif inputan[i:i+1] =='7' :
            errorcode = 1
        elif inputan[i:i+1] =='8' : 
            errorcode = 1
        elif inputan[i:i+1] =='9' :
            errorcode = 1
        elif inputan[i:i+1] =='0' :
            errorcode = 1
        elif inputan=='': 
            errorcode = 1
    if errorcode != 0:
        messagebox.showerror("Error","TIDAK BOLEH MEMASUKKAN NOMER")
        return
    if strjurusan.get() == "" :
       messagebox.showerror("Error","BELUM MEMILIH JURUSAN")
       return
    if len(stringalamat.get()) == 0:
       messagebox.showerror("Error","BELUM MENGISI ALAMAT")
       return
    if radio.get()== 0:
       messagebox.showerror("Error","BELUM MEMILIH GENDER")
       return
    if stragama.get() == "":
       messagebox.showerror("Error","BELUM MEMILIH AGAMA")
       return
    if len(stringemail.get()) == 0:
       messagebox.showerror("Error","BELUM MENGISI ALAMAT EMAIL")
       return
    if len(stringtelepon.get()) == 0:
       messagebox.showerror("Error","BELUM MENGISI NOMOR TELEPON")
       return
    for i in range (len(input)):
        if input [i:i+1] =="A" :
            errorcode = 1
        elif input [i:i+1] =="B" :
            errorcode = 1
        elif input [i:i+1] =="C" :
            errorcode = 1
        elif input [i:i+1] =="D" :
            errorcode = 1
        elif input [i:i+1] =="E" :
            errorcode = 1
        elif input [i:i+1] =="F" :
            errorcode = 1
        elif input [i:i+1] =="G" :
            errorcode = 1
        elif input [i:i+1] =="H" :
            errorcode = 1
        elif input [i:i+1] =="I" :
            errorcode = 1
        elif input [i:i+1] =="J" :
            errorcode = 1
        elif input [i:i+1] =="K" :
            errorcode = 1
        elif input [i:i+1] =="L" :
            errorcode = 1
        elif input [i:i+1] =="M" :
            errorcode = 1
        elif input [i:i+1] =="N" :
            errorcode = 1
        elif input [i:i+1] =="O" :
            errorcode = 1
        elif input [i:i+1] =="P" :
            errorcode = 1
        elif input [i:i+1] =="Q" :
            errorcode = 1
        elif input [i:i+1] =="R" :
            errorcode = 1
        elif input [i:i+1] =="S" :
            errorcode = 1
        elif input [i:i+1] =="T" :
            errorcode = 1
        elif input [i:i+1] =="U" :
            errorcode = 1
        elif input [i:i+1] =="V" :
            errorcode = 1
        elif input [i:i+1] =="W" :
            errorcode = 1
        elif input [i:i+1] =="x" :
            errorcode = 1
        elif input [i:i+1] =="Y" :
            errorcode = 1
        elif input [i:i+1] =="Z" :
            errorcode = 1
        elif input [i:i+1] =="a" :
            errorcode = 1
        elif input [i:i+1] =="b" :
            errorcode = 1
        elif input [i:i+1] =="c" :
            errorcode = 1
        elif input [i:i+1] =="d" :
            errorcode = 1
        elif input [i:i+1] =="e" :
            errorcode = 1
        elif input [i:i+1] =="f" :
            errorcode = 1
        elif input [i:i+1] =="g" :
            errorcode = 1
        elif input [i:i+1] =="h" :
            errorcode = 1
        elif input [i:i+1] =="i" :
            errorcode = 1
        elif input [i:i+1] =="j" :
            errorcode = 1
        elif input [i:i+1] =="k" :
            errorcode = 1
        elif input [i:i+1] =="l" :
            errorcode = 1
        elif input [i:i+1] =="m" :
            errorcode = 1
        elif input [i:i+1] =="n" :
            errorcode = 1
        elif input [i:i+1] =="o" :
            errorcode = 1
        elif input [i:i+1] =="p" :
            errorcode = 1
        elif input [i:i+1] =="q" :
            errorcode = 1
        elif input [i:i+1] =="r" :
            errorcode = 1
        elif input [i:i+1] =="s" :
            errorcode = 1
        elif input [i:i+1] =="t" :
            errorcode = 1
        elif input [i:i+1] =="u" :
            errorcode = 1
        elif input [i:i+1] =="v" :
            errorcode = 1
        elif input [i:i+1] =="w" :
            errorcode = 1
        elif input [i:i+1] =="x" :
            errorcode = 1
        elif input [i:i+1] =="y" :
            errorcode = 1
        elif input [i:i+1] =="z" :
            errorcode = 1
    if errorcode != 0:
        messagebox.showerror("Error","TIDAK BOLEH MENGISI HURUF")
        return
    
    pesan = ("Pendaftaran atas nama " + stringnama.get() + " telah berhasill!!!")
    messagebox.showinfo(" Informasi ", pesan)

def quit():
    root.destroy()

lbnama= Label(root, text = "Nama\t : ", font=("helvetica",10), bg="white").place(x=30,y=10)
lbjurusan= Label(root, text = "Jurusan\t : ", font=("helvetica",10), bg="white").place(x=30,y=40)
lbalamat = Label(root, text = "Alamat\t : ", font=("helvetica",10), bg="white").place(x = 30,y = 67)
lbjk = Label(root, text = "Gender\t : ", font=("helvetica",10), bg="white").place(x = 30, y=95)
lbagama = Label(text = "Agama\t : " , font=("helvetica",10), bg="white").place(x = 30, y=144)
lbemail = Label(text = "Email\t : ", font=("helvetica",10), bg="white").place(x = 30, y=174)
lbtelepon = Label(text = "Telepon\t : ", font=("helvetica",10), bg="white").place(x = 30, y=204)
lbluniv = Label(text = "                     UNIVERSITAS DIPONEGORO\t                            ", font=("helvetica 10 bold")).place(x = 0, y=250)

stringnama = StringVar()
inama = Entry(root,width = 30, textvariable=stringnama).place(x = 110, y = 11)  
stringalamat = StringVar()
ialamat= Entry(root,width = 30, textvariable=stringalamat).place(x = 110, y = 71) 
stringemail = StringVar()
iemail= Entry(root,width = 30, textvariable=stringemail).place(x = 110, y = 176) 
stringtelepon = StringVar()
itelepon= Entry(root,width = 30, textvariable=stringtelepon).place(x = 110, y = 206)


strjurusan = StringVar() 
Cb1 = ttk.Combobox(root, width = 27, textvariable = strjurusan, state="readonly")
Cb1.place(x=110, y=40)
stragama = StringVar() 
Cb2 = ttk.Combobox(root, width = 27, textvariable = stragama, state="readonly")
Cb2.place(x=110, y=144)

Cb1['values'] = ('Matematika',
                 'Fisika',
                 'Teknik Komputer',
                 'Teknik Sipil',
                 'Arsitektur')
Cb2['values'] = ('ISLAM',
                 'KRISTEN',
                 'KATOLIK',
                 'BUDHA',
                 'HINDHU')

radio = IntVar()
R1 = Radiobutton(root, text="Pria      ", variable=radio, value=1 ).place(x=110, y=95)  
R2 = Radiobutton(root, text="Wanita", variable=radio, value=2).place(x=110, y=115)

btn1 = Button(root, command = pendaftaran, text="DAFTAR").place(x=260, y= 300)
btn2 = Button(root, command = quit, text="EXIT", fg="red").place(x=40,y=300)


root.mainloop()
