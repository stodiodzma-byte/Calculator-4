import tkinter as tk
from tkinter import messagebox
import webbrowser
import random

# --- إعدادات النافذة الرئيسية ---
app = tk.Tk()
app.title("آلة حاسبة ZARD - بايثون")
app.geometry("380x600")
app.configure(bg="black")

# ----------------------------------------------------
# --- شاشة الترحيب والتعريف (Splash Screen) ---
# ----------------------------------------------------
splash_frame = tk.Frame(app, bg="black")
splash_frame.place(relwidth=1, relheight=1)

# اسم الآلة الحاسبة
title_label = tk.Label(
    splash_frame, 
    text="ZARD CALCULATOR", 
    font=("Arial", 24, "bold"), 
    bg="black", 
    fg="#ff4757"  # أحمر نيون
)
title_label.pack(pady=(180, 10))

# تم التطوير من قبل zard
dev_label = tk.Label(
    splash_frame, 
    text="تم التطوير من قبل ZARD", 
    font=("Arial", 16, "bold"), 
    bg="black", 
    fg="white"
)
dev_label.pack(pady=10)

# Made with Pydroid 3
made_label = tk.Label(
    splash_frame, 
    text="Made with Pydroid 3", 
    font=("Arial", 12, "italic"), 
    bg="black", 
    fg="#535c68"  # رمادي هادي
)
made_label.pack(pady=10)

# دالة لإخفاء شاشة الترحيب وإظهار الآلة الحاسبة
def start_calculator():
    splash_frame.destroy()  # حذف شاشة الترحيب
    show_main_calculator()  # بناء واجهة الآلة الحاسبة

# ----------------------------------------------------

# --- متغيرات التحكم للآلة الحاسبة ---
expression = ""
equation = tk.StringVar()

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        
        # ميم الـ 67 الأسطوري
        if expression == "67":
            equation.set("67...")
            app.update()
            webbrowser.open("https://youtube.com/shorts/9pnpI-7YmV4?si=r7TnnVZlw10MNosa")
            clear()
            return

        # 1. رقم 1 -> فتح صورة جوجل درايف
        elif expression == "1":
            equation.set("جاري فتح الصورة...")
            app.update()
            webbrowser.open("https://drive.google.com/file/d/1f9epdADrjGfqvbWRNvnu0bMEzoVQtLBE/view?usp=drivesdk")
            clear()
            return
            
        # 2. رقم 2 -> رسالة الاشتراك
        elif expression == "2":
            equation.set("Subscribe to Zard")
            expression = "" 
            return
            
        # 3. رقم 3 -> لعبة فلابي بيرد
        elif expression == "3":
            equation.set("برجاء الانتظار...")
            app.update()
            webbrowser.open("https://flappybird.io/")
            clear()
            return
            
        # 4. رقم 4 -> لعبة ماريو
        elif expression == "4":
            equation.set("جاري فتح ماريو...")
            app.update()
            webbrowser.open("https://supermarioplay.com/")
            clear()
            return
            
        # 5. رقم 5 -> لعبة سونيك بجميع أجزائها
        elif expression == "5":
            equation.set("جاري فتح سونيك...")
            app.update()
            webbrowser.open("https://www.retrogames.cc/sega-games/sonic-the-hedgehog-usa-europe.html")
            clear()
            return
            
        # 6. رقم 6 -> لعبة باك مان
        elif expression == "6":
            equation.set("جاري فتح باك مان...")
            app.update()
            webbrowser.open("https://www.google.com/fbx?fbx=pacman")
            clear()
            return
            
        # 7. رقم 7 -> لعبة تيتريس (Tetris)
        elif expression == "7":
            equation.set("جاري فتح تيتريس...")
            app.update()
            webbrowser.open("https://tetris.com/play-tetris")
            clear()
            return
            
        # 8. رقم 8 -> لعبة البنات السريعة على Poki
        elif expression == "8":
            equation.set("جاري فتح لعبة البنات...")
            app.update()
            webbrowser.open("https://poki.com/en/g/dress-up-the-lovely-princess")
            clear()
            return
            
        # 9. رقم 9 -> لعبة كرة قدم (Penalty Shooters لضربات الجزاء)
        elif expression == "9":
            equation.set("جاري فتح لعبة كرة القدم...")
            app.update()
            webbrowser.open("https://www.crazygames.com/game/penalty-shooters-2")
            clear()
            return
            
        # 10. رقم 0 -> لعبة شوتر وحرب 3D أسطورية على Poki
        elif expression == "0":
            equation.set("جاري فتح لعبة الشوتر...")
            app.update()
            webbrowser.open("https://poki.com/en/g/venge-io")
            clear()
            return
        
        # الحساب العادي لباقي العمليات الرياضية
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" خطأ ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# --- دالة بناء الواجهة الرسومية بعد الترحيب ---
def show_main_calculator():
    try:
        global bg_image
        bg_image = tk.PhotoImage(file="background.png") 
        bg_label = tk.Label(app, image=bg_image)
        bg_label.place(relwidth=1, relheight=1) 
    except Exception as e:
        print(f"لم يتم العثور على صورة الخلفية: {e}")

    # شاشة العرض
    display_entry = tk.Entry(app, textvariable=equation, font=("Arial", 26, "bold"), bd=5, insertwidth=4, width=14, 
                              borderwidth=0, justify="right", bg="#1e1e1e", fg="#ff4757")
    display_entry.grid(columnspan=4, ipady=25, padx=15, pady=30, sticky="nsew")

    # تمدد الشبكة
    for i in range(4):
        app.grid_columnconfigure(i, weight=1)
    for i in range(1, 6):
        app.grid_rowconfigure(i, weight=1)

    # تصميم الأزرار
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]

    button_params = {
        'font': ("Arial", 18, "bold"),
        'height': 2,
        'width': 5,
        'bd': 0,
        'relief': 'flat'
    }

    for (text, row, col) in buttons:
        if text == '=':
            action = equalpress
            bg_color = "#ff1f3d" 
            fg_color = "white"
        elif text == 'C':
            action = clear
            bg_color = "#ff9f43" 
            fg_color = "black"
        elif text in ['+', '-', '*', '/']:
            action = lambda x=text: press(x)
            bg_color = "#2d3436" 
            fg_color = "white"
        else:
            action = lambda x=text: press(x)
            bg_color = "#535c68" 
            fg_color = "white"

        btn = tk.Button(app, text=text, fg=fg_color, bg=bg_color, **button_params, command=action)
        btn.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")

# انتظر ثانيتين ثم ابدأ التطبيق
app.after(2000, start_calculator)

app.wm_attributes("-topmost", True)
app.mainloop()
