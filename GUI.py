import tkinter as tk
import tkinter.messagebox
import tkinter.ttk
import pickle

window=tk.Tk()
window.title('NUAA Class Schedule')
window.geometry("800x600")

tk.Label(window,text='学号:',font=('Arial',12),width=10,height=2,anchor='w').place(x=30,y=0)
tk.Label(window,text='教务密码:',font=('Arial',12),width=10,height=2,anchor='w').place(x=250,y=0)
tk.Label(window,text='验证码:',font=('Arial',12),width=10,height=2,anchor='w').place(x=500,y=0)

et_stunum=tk.Entry(window,show=None,font=('Arial',14),width=14).place(x=80,y=8)
et_passwd=tk.Entry(window,show='*',font=('Arial',14),width=14).place(x=330,y=8)
et_ideco=tk.Entry(window,show=None,font=('Arial',14),width=10).place(x=660,y=8)
canvas=tk.Canvas(window,bg='green',height=35,width=90)
#ideco_file=tk.PhotoImage(file='')
#ideco=canvas.create_image(image=ideco_file)
canvas.place(x=560,y=2)

start_term_date=''

tk.Label(window,text='学期:',font=('Arial',12),width=10,height=2,anchor='w').place(x=30,y=40)
tk.Label(window,text='开学日期: '+start_term_date,font=('Arial',12),width=30,height=2,anchor='w').place(x=430,y=40)


def Select_term():
    print('selected '+sele_term.get())

sele_term=tkinter.ttk.Combobox(window)
sele_term.place(x=80,y=50)

sele_term['value']=('1','2','3','4')
#sele_term.current(0)
sele_term.bind("<<ComboboxSelected>>",Select_term)

tk.Label(window,text='课表类型:',font=('Arial',12),width=10,height=2,anchor='w').place(x=30,y=100)


var_table_type=tk.IntVar()
def Select_TableType():
    print(var_table_type.get())

rb_presonal=tk.Radiobutton(window,text='个人',variable=var_table_type,value=0,command=Select_TableType).place(x=130,y=100)
rb_class=tk.Radiobutton(window,text='班级',variable=var_table_type,value=1,command=Select_TableType).place(x=130,y=120)


def getSch():
    print('getSchdule here')

getSchedule=tk.Button(window,text='获取课表',font=('Arial',20),width=10,height=1,command=getSch).place(x=330,y=100)


output_exam=tk.IntVar()
def Select_outputExam():
    print('solve select exam here '+str(output_exam.get()))

tk.Checkbutton(window,text='导出考试安排',variable=output_exam,onvalue=1,offvalue=0,command=Select_outputExam).place(x=30,y=150)


def outputAs_iCal():
    print('outputAs_iCal here')

bu_outputAs_iCal=tk.Button(window,text='导出iCal日历',font=('Arial',20),width=10,height=1,command=outputAs_iCal).place(x=30,y=200)

def outputAs_txt():
    print('outputAs_txt here')

bu_outputAs_txt=tk.Button(window,text='导出.txt文件',font=('Arial',20),width=10,height=1,command=outputAs_txt).place(x=280,y=200)

def outputAs_xlsx():
    print('outputAs_xlsx here')

bu_outputAs_xlsx=tk.Button(window,text='导出.xlsx表格',font=('Arial',20),width=10,height=1,command=outputAs_xlsx).place(x=530,y=200)

def outputAs_all():
    print('outputAs_all here')

bu_outputAs_all=tk.Button(window,text='一键导出',bg='#ffff9f',font=('Arial',20),width=10,height=1,command=outputAs_all).place(x=30,y=300)


def insert_log_end():
    logbox.insert('end','log data')

logbox=tk.Text(window,height=10).place(x=230,y=300)

window.mainloop()