from tkinter import *                                       #GUI
import csv
from math import *

                
lst0 = {'ไม่มีบัตรสมาชิก':'0','M Generation':'1','M Generation Student':'2'}   #list
F_TH = 'TH-Sarabun-PSK 12 bold'
   

# หน้าจอหลัก -------------------------     
movie = Tk()
movie.title(' Discount Movie ')
movie.minsize(400,300)

photo = PhotoImage(file = 'mu.png')               
p = Label(movie, image = photo)
p.grid(row = 0, column = 1, columnspan = 3)


myinput = StringVar()
display = StringVar()
nmc = StringVar()
nmc1 = []

lstm = StringVar()
lstMG = StringVar()
lstMG.set('0')

data1 = []

lb0 = Label(movie, text = 'Select Member Card', font = F_TH) 
lb0.grid(row = 2, column = 1)


def read():                                                                 #main function
    price = 250
    if lstMG.get() == '0':
        disc = Tk()
        disc.title('Discount Movie')
        disc.minsize(200,250)
        lb = Label(disc, text= 'ไม่มีบัตรสมาชิก', font = F_TH)
        lb.grid(row = 1, column = 1)
        lb = Label(disc, text= 'ส่วนลด = 0', font = F_TH)
        lb.grid(row = 2, column = 2)
        lb1 = Label(disc, text= 'ราคา = 250 บาท', font = F_TH)
        lb1.grid(row = 3, column = 2)
    elif lstMG.get() == '1':
        with open('myfileregis.csv', 'r', encoding = 'utf-8') as outfile:           #read file
            data = csv.reader(outfile)
            for readfile in (data):
                if nmc.get() in readfile :
                    if readfile[4] == '1':
                        disc = Tk()
                        disc.title(' Discount Movie ')
                        disc.minsize(180,250)
                        lb0 = Label(disc, text = readfile[0], font = F_TH)
                        lb0.grid(row = 1, column = 1, columnspan = 3)
                        lb1 = Label(disc, text = readfile[3], font = F_TH)
                        lb1.grid(row = 2, column = 1, columnspan = 3)
                        lb2 = Label(disc, text = readfile[1], font = F_TH)
                        lb2.grid(row = 3, column = 1)
                        lb3 = Label(disc, text = readfile[2], font = F_TH)
                        lb3.grid(row = 3, column = 2, columnspan = 3)

                        discount = 10
                        dis = price * (discount/100)
                        total = price - dis
                        stotal = ceil(total)
                        lb4 = Label(disc, text = 'ราคา = {}'.format(stotal), font = F_TH)
                        lb4.grid(row = 5, column = 1, columnspan = 3, pady =10)
                        lb6 = Label(disc, text = 'ส่วนลด 10% ', font = F_TH)
                        lb6.grid(row = 4, column = 1, columnspan = 3, pady =10)
                    else:
                        lb1 = Label(movie, text = 'รหัสผิด')
                        lb1.grid(row = 6, column = 2)


                    
    elif lstMG.get() == '2':
        with open('myfileregis.csv', 'r', encoding = 'utf-8') as outfile:
            data = csv.reader(outfile)
            for readfile in (data):
                if nmc.get() in readfile :
                    if readfile[4] == '2':
                        disc = Tk()
                        disc.title(' Discount Movie ')
                        disc.minsize(200,250)
                        lb0 = Label(disc, text = readfile[0], font = F_TH)
                        lb0.grid(row = 1, column = 1, columnspan = 3)
                        lb1 = Label(disc, text = readfile[3], font = F_TH)
                        lb1.grid(row = 2, column = 1, columnspan = 3)
                        lb2 = Label(disc, text = readfile[1], font = F_TH)
                        lb2.grid(row = 3, column = 1)
                        lb3 = Label(disc, text = readfile[2], font = F_TH)
                        lb3.grid(row = 3, column = 2, columnspan = 3)

                        discount = 15
                        dis = price * (discount/100)
                        total = price - dis
                        stotal = ceil(total)
                        lb4 = Label(disc, text = 'ราคา = {}'.format(stotal), font = F_TH)
                        lb4.grid(row = 5, column = 1, columnspan = 3, pady =10)
                        lb6 = Label(disc, text = 'ส่วนลด 15% ', font = F_TH)
                        lb6.grid(row = 4, column = 1, columnspan = 3, pady =10)
                    else:
                        lb1 = Label(movie, text = 'รหัสผิด')
                        lb1.grid(row = 6, column = 2)


i = 2
for k, v in lst0.items():                                       #For loop
    r = Radiobutton(movie, text=k, value=v ,width=18 ,anchor=W, variable=lstMG)
    r.grid(row=i, column=2)
    i += 1
    def on_click(e):                                            #Fucntion           
        if lstMG.get() == '0':
            btR = Button(movie, text = 'Register Now', font = F_TH, pady = 10,width = 15)     #ปุ่มสมัครสมาชิก
            btR.grid(row = 7, column = 1,pady = 10)
            btR.bind('<Button-1>',register0)
        
            
            
        else:
            lb = Label(movie, text = 'กรอกรหัสบัตร')
            lb.grid(row=5, column=1)
            vcmd = (movie.register(id_card), '%S')
            ent0 = Entry(movie,textvariable = nmc, vcmd=vcmd, validate='key')              # ค่า Entry เก็บไว้ใน nmc
            ent0.grid(row=5, column=2)
            ent0.focus()
        btOK = Button(movie ,  text = 'OK', font = F_TH , command = read,width = 15)
        btOK.grid(row = 7, column = 2,pady = 10, padx = 10)

        bt_close = Button(movie, text = 'Close', font = F_TH , command = movie.destroy, width = 15)
        bt_close.grid(row = 7, column = 3, pady = 10, padx = 10)        



btC = Button(movie, text='Click', font = F_TH, width = 15)
btC.grid(row=3, column=3)
btC.bind('<Button-1>',on_click)





#------------------------ Register การสมัคร ----------------------
lst_re = ['M Generation']

reg01 = StringVar()
reg02 = StringVar()
reg03 = IntVar()
reg03.set('')


def id_card(S):             #ใส่ได้แค่ตัวเลข
    if S.isdigit():
        return True
    movie.bell()
    return False


    
def register0(r):
    lb1 = Label(movie, text = 'ชื่อ', font = F_TH)
    lb1.grid(row = 8, column = 1)
    lb2 = Label(movie, text = 'นามสกุล', font = F_TH)
    lb2.grid(row = 9, column = 1)
    lb3 = Label(movie, text = 'เลขบัตรประชาชน', font = F_TH)
    lb3.grid(row = 10, column = 1)

    ent1 = Entry(movie,textvariable = reg01)
    ent1.grid(row=8, column=2)
    ent2 = Entry(movie,textvariable = reg02)
    ent2.grid(row=9, column=2)
    vcmd = (movie.register(id_card), '%S')
    ent3 = Entry(movie,textvariable = reg03, vcmd=vcmd, validate='key')
    ent3.grid(row=10, column=2)

    

    btr = Button(movie, text = 'Register', font = F_TH, width = 15, command = lambda:[write_lst(), succesre()])     
    btr.grid(row = 11, column = 2,pady = 10)

    

def write_lst():
    lst_re.append(reg01.get())
    lst_re.append(reg02.get())
    lst_re.append(reg03.get())
    lst_re.append(1)
    with open('myfileregis.csv', 'a', encoding = 'utf-8')as outfile:                #write file
        w = csv.writer(outfile, lineterminator = '\n')
        w.writerow(lst_re)


        
def succesre():
    lb4 = Label(movie,text = 'สมัครสมาชิกเรียบร้อย\nกรุณากด M Generation แล้วกรอกรหัสบัตรตามเลขบัตรปปช.', font = F_TH)
    lb4.grid(row = 12, column = 2)


movie.mainloop()


        
