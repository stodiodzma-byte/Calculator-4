from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.window import Window
import webbrowser

# إعدادات ألوان الخلفية وحجم الشاشة الافتراضي
Window.clearcolor = (0, 0, 0, 1)

class ZardCalculatorApp(App):
    def build(self):
        self.title = "آلة حاسبة ZARD"
        self.expression = ""
        
        # الواجهة الرئيسية (شاشة الترحيب أولاً)
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.show_splash_screen()
        return self.main_layout

    def show_splash_screen(self):
        # شاشة الترحيب والتعريف
        self.splash_box = BoxLayout(orientation='vertical', spacing=10, padding=[0, 150, 0, 0])
        
        title_label = Label(text="ZARD CALCULATOR", font_size='32sp', bold=True, color=(1, 0.28, 0.34, 1))
        dev_label = Label(text="تم التطوير من قبل ZARD", font_size='20sp', bold=True, color=(1, 1, 1, 1))
        made_label = Label(text="Made for Mobile", font_size='14sp', italic=True, color=(0.32, 0.36, 0.41, 1))
        
        self.splash_box.add_widget(title_label)
        self.splash_box.add_widget(dev_label)
        self.splash_box.add_widget(made_label)
        
        self.main_layout.add_widget(self.splash_box)
        
        # الانتظار ثانيتين ثم الانتقال للآلة الحاسبة
        Clock.schedule_once(self.start_calculator, 2)

    def start_calculator(self, dt):
        self.main_layout.remove_widget(self.splash_box)
        
        # شاشة العرض (الـ Entry)
        self.display = TextInput(
            font_size='36sp', readonly=True, halign='right', multiline=False,
            background_color=(0.12, 0.12, 0.12, 1), foreground_color=(1, 0.28, 0.34, 1),
            size_hint_y=0.2, border=(0,0,0,0)
        )
        self.main_layout.add_widget(self.display)
        
        # شبكة الأزرار
        grid = GridLayout(cols=4, spacing=10, size_hint_y=0.8)
        
        buttons = [
            ('7', (0.32, 0.36, 0.41, 1)), ('8', (0.32, 0.36, 0.41, 1)), ('9', (0.32, 0.36, 0.41, 1)), ('/', (0.17, 0.2, 0.21, 1)),
            ('4', (0.32, 0.36, 0.41, 1)), ('5', (0.32, 0.36, 0.41, 1)), ('6', (0.32, 0.36, 0.41, 1)), ('*', (0.17, 0.2, 0.21, 1)),
            ('1', (0.32, 0.36, 0.41, 1)), ('2', (0.32, 0.36, 0.41, 1)), ('3', (0.32, 0.36, 0.41, 1)), ('-', (0.17, 0.2, 0.21, 1)),
            ('C', (1, 0.62, 0.26, 1)),     ('0', (0.32, 0.36, 0.41, 1)), ('=', (1, 0.12, 0.24, 1)),     ('+', (0.17, 0.2, 0.21, 1)),
        ]
        
        for text, color in buttons:
            btn = Button(
                text=text, font_size='24sp', bold=True,
                background_normal='', background_color=color, color=(1,1,1,1)
            )
            btn.bind(on_press=self.on_button_press)
            grid.add_widget(btn)
            
        self.main_layout.add_widget(grid)

    def on_button_press(self, instance):
        text = instance.text
        
        if text == 'C':
            self.expression = ""
            self.display.text = ""
        elif text == '=':
            self.equal_press()
        else:
            self.expression += text
            self.display.text = self.expression

    def equal_press(self):
        try:
            # المفاجآت الأسطورية بتاعتك!
            if self.expression == "67":
                self.display.text = "67..."
                webbrowser.open("https://youtube.com/shorts/9pnpI-7YmV4?si=r7TnnVZlw10MNosa")
                self.expression = ""
                return
            elif self.expression == "1":
                self.display.text = "جاري فتح الصورة..."
                webbrowser.open("https://drive.google.com/file/d/1f9epdADrjGfqvbWRNvnu0bMEzoVQtLBE/view?usp=drivesdk")
                self.expression = ""
                return
            elif self.expression == "2":
                self.display.text = "Subscribe to Zard"
                self.expression = ""
                return
            elif self.expression == "3":
                webbrowser.open("https://flappybird.io/")
                self.expression = ""
                return
            elif self.expression == "4":
                webbrowser.open("https://supermarioplay.com/")
                self.expression = ""
                return
            elif self.expression == "5":
                webbrowser.open("https://www.retrogames.cc/sega-games/sonic-the-hedgehog-usa-europe.html")
                self.expression = ""
                return
            elif self.expression == "6":
                webbrowser.open("https://www.google.com/fbx?fbx=pacman")
                self.expression = ""
                return
            elif self.expression == "7":
                webbrowser.open("https://tetris.com/play-tetris")
                self.expression = ""
                return
            elif self.expression == "8":
                webbrowser.open("https://poki.com/en/g/dress-up-the-lovely-princess")
                self.expression = ""
                return
            elif self.expression == "9":
                webbrowser.open("https://www.crazygames.com/game/penalty-shooters-2")
                self.expression = ""
                return
            elif self.expression == "0":
                webbrowser.open("https://poki.com/en/g/venge-io")
                self.expression = ""
                return

            # الحساب العادي
            total = str(eval(self.expression))
            self.display.text = total
            self.expression = total
        except:
            self.display.text = " خطأ "
            self.expression = ""

if __name__ == '__main__':
    ZardCalculatorApp().run()
        
