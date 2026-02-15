import tkinter as tk
from tkinter import messagebox
import threading
import time
from pynput import mouse, keyboard

class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoClicker Pro")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        
        # Colores
        self.bg_color = "#1a1a2e"
        self.accent_color = "#ff006e"
        self.secondary_color = "#00d9ff"
        self.text_color = "#ffffff"
        self.input_bg = "#16213e"
        
        self.root.configure(bg=self.bg_color)
        
        # Variables
        self.is_running = False
        self.click_type = tk.StringVar(value="left")
        self.start_key = tk.StringVar(value="f6")
        self.stop_key = tk.StringVar(value="f7")
        self.cps = tk.IntVar(value=10)
        self.listening_for_key = None
        self.mouse_controller = mouse.Controller()
        
        # Listeners
        self.hotkey_listener = None
        self.key_listener = None
        self.click_thread = None
        
        self.setup_ui()
        self.setup_hotkeys()
        
    def setup_ui(self):
        # Título
        title_frame = tk.Frame(self.root, bg=self.bg_color)
        title_frame.pack(pady=20)
        
        title = tk.Label(
            title_frame,
            text="AutoClicker Pro",
            font=("Arial", 32, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        )
        title.pack()
        
        subtitle = tk.Label(
            title_frame,
            text="Control your clicks with precision",
            font=("Arial", 10),
            bg=self.bg_color,
            fg=self.secondary_color
        )
        subtitle.pack()
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Sección: Tipo de click
        self.create_section(main_frame, "Click Type", self.create_click_type_selector)
        
        # Sección: Velocidad
        self.create_section(main_frame, "Speed", self.create_cps_slider)
        
        # Sección: Controles
        self.create_section(main_frame, "Keyboard Controls", self.create_key_controls)
        
        # Sección: Estado
        self.create_section(main_frame, "Control", self.create_status_section)
        
    def create_section(self, parent, title, content_creator):
        section_frame = tk.Frame(parent, bg=self.bg_color)
        section_frame.pack(fill="x", pady=15)
        
        # Línea decorativa
        line1 = tk.Frame(section_frame, height=2, bg=self.accent_color)
        line1.pack(fill="x", pady=(0, 10))
        
        # Título
        section_title = tk.Label(
            section_frame,
            text=title,
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            fg=self.secondary_color
        )
        section_title.pack(anchor="w")
        
        # Contenido
        content_frame = tk.Frame(section_frame, bg=self.bg_color)
        content_frame.pack(fill="x", pady=10)
        content_creator(content_frame)
        
        # Línea decorativa
        line2 = tk.Frame(section_frame, height=1, bg=self.accent_color)
        line2.pack(fill="x", pady=(10, 0))
    
    def create_click_type_selector(self, parent):
        for click_type, label in [("left", "🖱 Left Click"), ("right", "🖱 Right Click"), ("middle", "🖱 Middle Click")]:
            btn = tk.Radiobutton(
                parent,
                text=label,
                variable=self.click_type,
                value=click_type,
                bg=self.bg_color,
                fg=self.text_color,
                selectcolor=self.input_bg,
                activebackground=self.bg_color,
                activeforeground=self.secondary_color,
                font=("Arial", 10)
            )
            btn.pack(anchor="w", pady=5)
    
    def create_cps_slider(self, parent):
        label_frame = tk.Frame(parent, bg=self.bg_color)
        label_frame.pack(fill="x", pady=(0, 10))
        
        tk.Label(
            label_frame,
            text="Clicks per second:",
            font=("Arial", 10),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(side="left")
        
        self.cps_label = tk.Label(
            label_frame,
            text="10",
            font=("Arial", 10, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        )
        self.cps_label.pack(side="right")
        
        self.cps_slider = tk.Scale(
            parent,
            from_=1,
            to=50,
            variable=self.cps,
            orient="horizontal",
            bg=self.input_bg,
            fg=self.secondary_color,
            highlightthickness=0,
            troughcolor=self.input_bg,
            activebackground=self.accent_color,
            command=self.update_cps_label,
            length=300
        )
        self.cps_slider.pack(fill="x")
    
    def update_cps_label(self, value):
        self.cps_label.config(text=value)
    
    def create_key_controls(self, parent):
        # Fila: Tecla inicio
        start_frame = tk.Frame(parent, bg=self.bg_color)
        start_frame.pack(fill="x", pady=8)
        
        tk.Label(
            start_frame,
            text="START Key:",
            font=("Arial", 10),
            bg=self.bg_color,
            fg=self.text_color,
            width=15,
            anchor="w"
        ).pack(side="left")
        
        self.start_key_btn = tk.Button(
            start_frame,
            text=self.start_key.get().upper(),
            font=("Arial", 10, "bold"),
            bg=self.input_bg,
            fg=self.secondary_color,
            activebackground=self.accent_color,
            activeforeground=self.bg_color,
            command=lambda: self.listen_for_key(self.start_key, self.start_key_btn),
            padx=15,
            pady=5,
            relief="flat",
            cursor="hand2",
            width=15
        )
        self.start_key_btn.pack(side="right")
        
        # Fila: Tecla parada
        stop_frame = tk.Frame(parent, bg=self.bg_color)
        stop_frame.pack(fill="x", pady=8)
        
        tk.Label(
            stop_frame,
            text="STOP Key:",
            font=("Arial", 10),
            bg=self.bg_color,
            fg=self.text_color,
            width=15,
            anchor="w"
        ).pack(side="left")
        
        self.stop_key_btn = tk.Button(
            stop_frame,
            text=self.stop_key.get().upper(),
            font=("Arial", 10, "bold"),
            bg=self.input_bg,
            fg=self.secondary_color,
            activebackground=self.accent_color,
            activeforeground=self.bg_color,
            command=lambda: self.listen_for_key(self.stop_key, self.stop_key_btn),
            padx=15,
            pady=5,
            relief="flat",
            cursor="hand2",
            width=15
        )
        self.stop_key_btn.pack(side="right")
        
        # Info
        info_label = tk.Label(
            parent,
            text="💡 Click the buttons to assign new keys",
            font=("Arial", 8),
            bg=self.bg_color,
            fg="#888888"
        )
        info_label.pack(anchor="w", pady=(10, 0))
    
    def listen_for_key(self, key_var, button):
        if self.listening_for_key is not None:
            return
        
        self.listening_for_key = key_var
        button.config(text="Listening...", fg=self.accent_color, state="disabled")
        
        def on_press(key):
            try:
                key_name = ""
                if hasattr(key, 'name'):
                    key_name = key.name.lower()
                elif hasattr(key, 'char') and key.char:
                    key_name = key.char.lower()
                else:
                    key_name = str(key).replace("Key.", "").lower()
                
                if key_name and self.listening_for_key:
                    key_var.set(key_name)
                    button.config(text=key_name.upper(), fg=self.secondary_color, state="normal")
                    
                    if self.key_listener:
                        self.key_listener.stop()
                    self.listening_for_key = None
            except Exception as e:
                print(f"Error: {e}")
        
        self.key_listener = keyboard.Listener(on_press=on_press)
        self.key_listener.start()
    
    def create_status_section(self, parent):
        # Estado
        status_frame = tk.Frame(parent, bg=self.input_bg)
        status_frame.pack(fill="x", pady=(0, 15))
        
        tk.Label(
            status_frame,
            text="Status:",
            font=("Arial", 10),
            bg=self.input_bg,
            fg=self.text_color
        ).pack(side="left", padx=10, pady=10)
        
        self.status_label = tk.Label(
            status_frame,
            text="⚫ STOPPED",
            font=("Arial", 10, "bold"),
            bg=self.input_bg,
            fg="#888888"
        )
        self.status_label.pack(side="right", padx=10)
        
        # Botones
        button_frame = tk.Frame(parent, bg=self.bg_color)
        button_frame.pack(fill="x", pady=10)
        
        self.start_btn = tk.Button(
            button_frame,
            text="▶ START",
            font=("Arial", 11, "bold"),
            bg=self.accent_color,
            fg=self.bg_color,
            activebackground=self.secondary_color,
            activeforeground=self.bg_color,
            command=self.start_clicking,
            padx=20,
            pady=10,
            relief="flat",
            cursor="hand2"
        )
        self.start_btn.pack(side="left", padx=5, fill="x", expand=True)
        
        self.stop_btn = tk.Button(
            button_frame,
            text="⏹ STOP",
            font=("Arial", 11, "bold"),
            bg="#555555",
            fg=self.text_color,
            activebackground="#666666",
            activeforeground=self.text_color,
            command=self.stop_clicking,
            padx=20,
            pady=10,
            relief="flat",
            cursor="hand2",
            state="disabled"
        )
        self.stop_btn.pack(side="right", padx=5, fill="x", expand=True)
    
    def start_clicking(self):
        if self.is_running:
            return
        
        self.is_running = True
        self.status_label.config(text="🟢 RUNNING", fg=self.accent_color)
        self.start_btn.config(state="disabled", bg="#555555")
        self.stop_btn.config(state="normal", bg=self.accent_color)
        
        self.click_thread = threading.Thread(target=self.clicking_loop, daemon=True)
        self.click_thread.start()
    
    def stop_clicking(self):
        self.is_running = False
        self.status_label.config(text="⚫ STOPPED", fg="#888888")
        self.start_btn.config(state="normal", bg=self.accent_color)
        self.stop_btn.config(state="disabled", bg="#555555")
    
    def clicking_loop(self):
        click_type = self.click_type.get()
        interval = 1.0 / self.cps.get()
        
        button_map = {
            "left": mouse.Button.left,
            "right": mouse.Button.right,
            "middle": mouse.Button.middle
        }
        
        button = button_map.get(click_type, mouse.Button.left)
        
        while self.is_running:
            try:
                self.mouse_controller.click(button)
                time.sleep(interval)
            except:
                pass
    
    def setup_hotkeys(self):
        def on_press(key):
            try:
                key_name = ""
                if hasattr(key, 'name'):
                    key_name = key.name.lower()
                elif hasattr(key, 'char') and key.char:
                    key_name = key.char.lower()
                else:
                    key_name = str(key).replace("Key.", "").lower()
                
                start_key = self.start_key.get().lower()
                stop_key = self.stop_key.get().lower()
                
                if key_name == start_key and not self.is_running:
                    self.root.after(0, self.start_clicking)
                elif key_name == stop_key and self.is_running:
                    self.root.after(0, self.stop_clicking)
            except:
                pass
        
        self.hotkey_listener = keyboard.Listener(on_press=on_press)
        self.hotkey_listener.start()
    
    def on_closing(self):
        self.is_running = False
        if self.hotkey_listener:
            self.hotkey_listener.stop()
        if self.key_listener:
            self.key_listener.stop()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClickerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()