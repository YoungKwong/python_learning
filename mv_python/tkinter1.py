import tkinter as tk
import pickle
from tkinter import messagebox  #不添加这段代码使用tk.messagebox会报错

window = tk.Tk()
window.title('Welcome to Mofan Python')
window.geometry('450x300')

#welcome image
canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='img/3-01-02.gif')
image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.pack(side='top')

#uesr information
tk.Label(window, text='User name:').place(x=50, y=150)
tk.Label(window, text='Password:').place(x=50, y=190)

var_usr_name = tk.StringVar()
var_usr_name.set('exampel@python.com')  #给username的Entry一个初始值
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)

var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)

def usr_login():  #登录功能
    usr_name = var_usr_name.get()  #.get()获得在Entry输入的username和password
    usr_pwd = var_usr_pwd.get()  #将username和password分别赋值给usr_n和usr_p
    
    try:  #错误处理
        with open('usrs_info.pickle', 'rb') as usr_file:  #将usrs_info.pickle(存放用户信息的资料夹)装载到usr_file里
            usrs_info = pickle.load(usr_file)  #.load():加载usr_file文件存到变量usrs_info里
    except FileNotFoundError:  #FileNotFoundError:如果还没有创建文件
        with open('usrs_info.pickle', 'wb') as usr_file:  #创建usrs_info.pickle并装载到usr_file里
            usrs_info = {'admin': 'admin'}  
            pickle.dump(usrs_info, usr_file)  #把字典usrs_info的内容剪切到usr_file

    if usr_name in usrs_info:  #如果在输入框输入的username在资料夹usrs_info字典里
        if usr_pwd == usrs_info[usr_name]:  #如果在输入框输入的password对应usrs_info字典里usr_name的索引
            tk.messagebox.showinfo(title='Welcome', message='How are you?' + usr_name)
        else:  #如果不对应
            tk.messagebox.showerror(message='Error, your password in wrong, try again')
    else:  #如果在资料夹usrs_info字典里没有对应的usr_name
        is_sign_up = tk.messagebox.askyesno(title='Welcome',  #用弹出窗口问你是否注册
                                            message='You have not sign up yet. Sign up now?')
        if  is_sign_up == True:
            usr_sign_up()
        else:
            pass

def usr_sign_up():  
    def sign_to_Mofan_Python():  #注册功能
        np = new_pwd.get()  #get()到在Toplevel窗口中Entry里输入的值
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('usrs_info.pickle', 'rb') as usr_file:  #以只读的形式打开usrs_info.pickle
            exist_usr_info = pickle.load(usr_file)
            if np != npf:  #如果判断np和npf不相同
                tk.messagebox.showerror(title='Error',
                                        message='Password and confirm password must be the same!')
            elif nn in exist_usr_info:  #如果用户已被注册
                tk.messagebox.showerror(title='Error', message='The user has already signed up!')
            else:
                exist_usr_info[nn] = np  #把nn和np存到字典exist_usr_info中
                with open('usrs_info.pickle', 'wb') as usr_file:  #把字典exist_usr_info里的键值对写入usrs_info.pickle
                    pickle.dump(exist_usr_info, usr_file)
                tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')  #提示注册成功
                window_sign_up.destroy()  #.destroy()：摧毁(关闭)注册窗口
        
    window_sign_up = tk.Toplevel(window)  #.Toplevel()：窗口上的窗口，不需要再window.mainloop()
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('exampel@python.com')  
    tk.Label(window_sign_up, text='User name:').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password:').place(x=10, y=50)
    entry_new_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_new_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password:').place(x=10, y=90)
    entry_new_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_new_pwd_confirm.place(x=150, y=90)

    btn_confirm_sign_up = tk.Button(window_sign_up,
                                    text='Sign up',
                                    command=sign_to_Mofan_Python)
    btn_confirm_sign_up.place(x=150, y=130)

    

#login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=150, y=230)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=250, y=230)

window.mainloop()
