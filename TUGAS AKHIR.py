from tkinter import*
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Pendaftaran Mahasiswa Baru")
root.geometry("420x490")
bg = PhotoImage(file="D:\\sementara\\logo-undip-transparan.png")
lblogo = Label(root, image=bg)
lblogo.place(x=50,y=20)
lbjudul = Label(root, text="Pendafataran Mahasiswa Baru",font=("helvetica 11 bold"), fg= "blue").place(x=107, y=10 )
lbakademik = Label(root, text="Tahun Akademik 2021/2022",font=("helvetica 11 bold"), fg= "blue" ).place(x=123, y=30 )

def pendaftaran():
    inputan = stringnama.get()
    input = stringtelepon.get()
    inputaan = stringtempat.get()
    errorcode = 0
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
    if len(stringtempat.get()) == 0:
       messagebox.showerror("Error","BELUM MENGISI TEMPAT LAHIR")
       return
    for i in range(len(inputaan)):
        if inputaan[i:i+1] =='1':
            errorcode = 1
        elif inputaan[i:i+1] =='2':
            errorcode = 1
        elif inputaan[i:i+1] =='3' : 
            errorcode = 1
        elif inputaan[i:i+1] =='4' :
            errorcode = 1
        elif inputaan[i:i+1] =='5' :
            errorcode = 1
        elif inputaan[i:i+1] =='6' :
            errorcode = 1
        elif inputaan[i:i+1] =='7' :
            errorcode = 1
        elif inputaan[i:i+1] =='8' : 
            errorcode = 1
        elif inputaan[i:i+1] =='9' :
            errorcode = 1
        elif inputaan[i:i+1] =='0' :
            errorcode = 1
        elif inputaan=='': 
            errorcode = 1
    if errorcode != 0:
        messagebox.showerror("Error","TIDAK BOLEH MEMASUKKAN NOMER")
        return
    if strtgl.get() == "":
       messagebox.showerror("Error","BELUM MEMILIH TGL LAHIR")
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

lbnama= Label(root, text = "Nama\t      : ", font=("helvetica",10), bg="white").place(x=30,y=90)
lbjurusan= Label(root, text = "Jurusan\t      : ", font=("helvetica",10), bg="white").place(x=30,y=115)
lbalamat = Label(root, text = "Alamat\t      : ", font=("helvetica",10), bg="white").place(x = 30,y = 140)
lbjk = Label(root, text = "Gender\t      : ", font=("helvetica",10), bg="white").place(x = 30, y=165)
lbagama = Label(root, text = "Agama\t       : " , font=("helvetica",10), bg="white").place(x = 30, y=220)
lbtempat = Label(root, text = "Tempat Lahir  : " , font=("helvetica",10), bg="white").place(x = 30, y=245)
lbtgl = Label(root, text = "Tanggal Lahir  : " , font=("helvetica",10), bg="white").place(x = 30, y=270)
lbemail = Label(text = "Email\t       :" , font=("helvetica",10), bg="white").place(x = 30, y=295)
lbtelepon = Label(text = "Telepon\t       : ", font=("helvetica",10), bg="white").place(x = 30, y=320)
lbluniv = Label(text = "UNIVERSITAS DIPONEGORO", font=("Tahoma 12 bold"), fg = "grey").place(x = 100, y=390)

stringnama = StringVar()
inama = Entry(root,width = 34, textvariable=stringnama).place(x = 150, y = 91)  
stringalamat = StringVar()
ialamat= Entry(root,width = 34, textvariable=stringalamat).place(x = 150, y = 141) 
stringtempat = StringVar()
itempat= Entry(root,width = 34, textvariable=stringtempat).place(x = 150, y = 246)
stringemail = StringVar()
iemail= Entry(root,width = 34, textvariable=stringemail).place(x = 150, y = 296) 
stringtelepon = StringVar()
itelepon= Entry(root,width = 34, textvariable=stringtelepon).place(x = 150, y = 321)


strjurusan = StringVar() 
Cb1 = ttk.Combobox(root, width = 31, textvariable = strjurusan, state="readonly")
Cb1.place(x=150, y=116)
stragama = StringVar() 
Cb2 = ttk.Combobox(root, width = 31, textvariable = stragama, state="readonly")
Cb2.place(x=150, y=221)
strtgl = StringVar()
Cb3 = ttk.Combobox(root, width = 3, textvariable = strtgl, state="readonly")
Cb3.place(x=150, y=271)
strtgl = StringVar()
Cb4 = ttk.Combobox(root, width = 12, textvariable = strtgl, state="readonly")
Cb4.place(x=196, y=271)
strtgl = StringVar()
Cb5 = ttk.Combobox(root, width = 7, textvariable = strtgl, state="readonly")
Cb5.place(x=295, y=271)

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

Cb3['values'] = ('1',
                 '2',
                 '3',
                 '4',
                 '5',
                 '6',
                 '7',
                 '8',
                 '9',
                 '10',
                 '11',
                 '12',
                 '13',
                 '14',
                 '15',
                 '16',
                 '17',
                 '18',
                 '19',
                 '20',
                 '21',
                 '22',
                 '23',
                 '24',
                 '25',
                 '26',
                 '27',
                 '28',
                 '29',
                 '30',
                 '31')
Cb4['values'] = ('JANUARI',
                 'FEBRUARI',
                 'MARET',
                 'APRIL',
                 'MEI',
                 'JUNI',
                 'JULI',
                 'AGUSTUS',
                 'SEPTEMBER',
                 'OKTOBER',
                 'NOVEMBER',
                 'DESEMBER')
Cb5['values'] = ('1991',
                 '1992',
                 '1993',
                 '1994',
                 '1995',
                 '1996',
                 '1997',
                 '1998',
                 '1999',
                 '2000',
                 '2001',
                 '2002',
                 '2003')

radio = IntVar()
R1 = Radiobutton(root, text="Pria      ", variable=radio, value=1 ).place(x=150, y=166)  
R2 = Radiobutton(root, text="Wanita", variable=radio, value=2).place(x=150, y=185)

btn1 = Button(root, command = pendaftaran, text="DAFTAR",  font=("helvetica 10 bold")).place(x=300, y= 440)
btn2 = Button(root, command = quit, text="EXIT", fg="red",  font=("helvetica 10 bold")).place(x=60,y=440)


root.mainloop()


