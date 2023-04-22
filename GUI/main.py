import tkinter
import tkinter.messagebox
import customtkinter
import os
from PIL import Image

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
is_login = False

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        

        # configure window
        self.title("Next-Gen Key Sharing.py")
        self.geometry(f"{1100}x{580}")
        self.attributes('-fullscreen',True)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        # ---------- PHONE ----------
        # Phone frame
        self.phone_space = customtkinter.CTkFrame(self, fg_color="transparent")#, width=140)
        self.phone_space.grid(row=0, column=1, sticky="nsew")
        self.phone_space.grid_columnconfigure(0, weight=1)

        # ---------- CAR ----------
        # Car frame
        self.car_space = customtkinter.CTkFrame(self, fg_color="transparent")#, width=140)
        self.car_space.grid(row=0, column=0, sticky="nsew")
        self.car_space.grid_columnconfigure(0, weight=1)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.car_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "garbusv69.png")), size=(1013, 470))
        self.car_image_bigger = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Untitled69.png")), size=(1013, 470))
        self.graphs = customtkinter.CTkImage(Image.open(os.path.join(image_path, "graphs.png")), size=(1100, 650))

        self.logout()



    def logout(self):
        self.clearGUI(self.car_space)
       
        # ---------- PHONE ----------
        # Phone label
        self.phone_text = customtkinter.CTkLabel(master=self.phone_space, text="Phone", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.phone_text.grid(row=0, column=0, sticky="n")

        # Phone frame
        self.phone = customtkinter.CTkFrame(self.phone_space, corner_radius=50)#, width=140)
        self.phone.grid(row=1, column=0, sticky="nsew")
        #self.phone.grid_rowconfigure(4, weight=1)

        # Phone label
        self.phone_label = customtkinter.CTkLabel(master=self.phone, text="Next-Gen Car Sharnig", font=customtkinter.CTkFont(size=30, weight="bold"))#, image=bg)#, text_font=("Comic Sans", 24))
        self.phone_label.grid(row=0, column=0, padx=10, pady=130)

        entry1 = customtkinter.CTkEntry(master=self.phone, placeholder_text="Username", width=350, font=customtkinter.CTkFont(size=30))
        entry1.grid(row=1, column=0, padx=20, pady=10)

        entry2 = customtkinter.CTkEntry(master=self.phone, placeholder_text="Password", width=350, show="*", font=customtkinter.CTkFont(size=30))
        entry2.grid(row=2, column=0, padx=20, pady=10)

        button = customtkinter.CTkButton(master=self.phone, text="Login", width=350, command=self.login, font=customtkinter.CTkFont(size=30))
        button.grid(row=3, column=0, padx=20, pady=10)

        checkbox = customtkinter.CTkCheckBox(master=self.phone, text="Remember Me :)", font=customtkinter.CTkFont(size=30))
        checkbox.grid(row=4, column=0, padx=20, pady=110)



        # ---------- CAR ----------
        # Car image
        self.home_frame_large_image_label = customtkinter.CTkLabel(master=self.car_space, text="", image=self.car_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=180, sticky="nsew")

        # Car label
        self.car_text = customtkinter.CTkLabel(master=self.car_space, text="Car", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.car_text.grid(row=0, column=0, sticky="n")

        

    def login(self):
        self.clearGUI(self.car_space)

        # ---------- PHONE ----------
        # Phone label
        self.phone_text = customtkinter.CTkLabel(master=self.phone_space, text="Phone", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.phone_text.grid(row=0, column=0, sticky="n")

        # Phone frame
        self.phone = customtkinter.CTkFrame(self.phone_space, corner_radius=50)
        self.phone.grid(row=1, column=0, sticky="nsew")
        #self.phone.grid_rowconfigure(4, weight=1)

        # Phone label
        self.phone_label = customtkinter.CTkLabel(master=self.phone, text="Login Next-Gen Car Sharnig", font=customtkinter.CTkFont(size=30, weight="bold"))#, image=bg)#, text_font=("Comic Sans", 24))
        self.phone_label.grid(row=0, column=0, padx=10, pady=20)

        # create scrollable checkbox frame
        opcje = ["Lock", "AC", "OC", "Wipes", "Airplane mode", "Summarine", "Cabrio", "Reverse cabrio","Power", "Sebix mode"]
        self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self.phone, width=350, command=self.checkbox_frame_event,
                                                                 item_list=[opcje[i] for i in range(len(opcje))])    
        #self.scrollable_checkbox_frame.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_checkbox_frame.grid(row=2, column=0, padx=15, pady=15, sticky="ns")
        
        button = customtkinter.CTkButton(master=self.phone, text="Uprawnione osoby", width=50, command=self.logout, font=customtkinter.CTkFont(size=20))
        button.grid(row=7, column=0, padx=0, pady=5, sticky="s")
        button = customtkinter.CTkButton(master=self.phone, text="Ostatnia lokalizacja", width=50, command=self.logout, font=customtkinter.CTkFont(size=20))
        button.grid(row=8, column=0, padx=0, pady=5, sticky="s")

        button = customtkinter.CTkButton(master=self.phone, text="Logout", width=50, command=self.logout, font=customtkinter.CTkFont(size=30))
        button.grid(row=9, column=0, padx=0, pady=10, sticky="s")



        # ---------- CAR ----------
        # Car image
        self.home_frame_large_image_label = customtkinter.CTkLabel(master=self.car_space, text="", image=self.graphs)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=100, sticky="nsew")

        # Car label
        self.car_text = customtkinter.CTkLabel(master=self.car_space, text="Car", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.car_text.grid(row=0, column=0, sticky="n")



        self.progressbar_1 = customtkinter.CTkProgressBar(self.phone)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_2 = customtkinter.CTkProgressBar(self.phone)
        self.progressbar_2.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_3 = customtkinter.CTkProgressBar(self.phone, orientation="vertical")
        self.progressbar_3.grid(row=0, column=1, rowspan=13, padx=(10, 20), pady=(10, 10), sticky="ns")
        self.slider_1 = customtkinter.CTkSlider(self.phone, from_=0, to=1, number_of_steps=4)
        self.slider_1.grid(row=4, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_2 = customtkinter.CTkSlider(self.phone, orientation="vertical")
        self.slider_2.grid(row=5, column=0, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="w")

        self.slider_1.configure(command=self.progressbar_2.set)
        self.slider_2.configure(command=self.progressbar_3.set)
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()


    def clearGUI(self, window) -> None:  # for everyone
        for widget in window.winfo_children():
            widget.destroy()



    def checkbox_frame_event(self):
        self.show_info()

        

    def show_info(self):
        self.clearGUI(self.car_space)

        # ---------- CAR ----------
        # Car label
        self.car_text = customtkinter.CTkLabel(master=self.car_space, text="Car", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.car_text.grid(row=0, column=0, sticky="n")

        # Car frame
        self.car = customtkinter.CTkFrame(self.car_space, corner_radius=50, fg_color="transparent")#, width=140)
        self.car.grid(row=1, column=0, sticky="nsew")
        #self.car.grid_rowconfigure(4, weight=1)

        # Car label
        self.car_label = customtkinter.CTkLabel(master=self.car, text="Car info", font=customtkinter.CTkFont(size=30, weight="bold"))#, image=bg)#, text_font=("Comic Sans", 24))
        self.car_label.grid(row=0, column=0, padx=10, pady=130,  sticky="w")

        checkbox = f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}"
        print(checkbox)

        # Car label
        self.car_label = customtkinter.CTkLabel(master=self.car, text=checkbox, font=customtkinter.CTkFont(size=30, weight="bold"))#, image=bg)#, text_font=("Comic Sans", 24))
        self.car_label.grid(row=1, column=0, padx=10, pady=10)



    
class ScrollableCheckBoxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.checkbox_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def add_item(self, item):
        checkbox = customtkinter.CTkCheckBox(self, text=item)
        if self.command is not None:
            checkbox.configure(command=self.command)
        checkbox.grid(row=len(self.checkbox_list), column=0, pady=(0, 10))
        self.checkbox_list.append(checkbox)

    def remove_item(self, item):
        for checkbox in self.checkbox_list:
            if item == checkbox.cget("text"):
                checkbox.destroy()
                self.checkbox_list.remove(checkbox)
                return

    def get_checked_items(self):
        return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]
    



if __name__ == "__main__":
    app = App()
    app.mainloop()