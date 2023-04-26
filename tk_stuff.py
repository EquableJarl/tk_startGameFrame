import tkinter as tk
import tkinter.ttk as ttk


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, SecondPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Abled Glands",width="10", height="3", font=("Comic Sans MS", "70"))
        label.pack()

        button1 = tk.Button(self, text="New Game", width="20", height="3")
        button2 = tk.Button(self, text="Load Game", width="20", height="3")
        button1.pack(pady=10)
        button2.pack()

class SecondPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self, 
            text="Abled Glands",
            width= "900",
            height="300",
            background="red"
            )
        label.pack()

        button1 = tk.Button(self, text="New Game", background="yellow")
        button2 = tk.Button(self, text="Load Game")
        button1.pack()
        button2.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("1000x750")
    app.config(bg="red")
    app.mainloop()


