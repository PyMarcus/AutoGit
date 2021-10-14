from tkinter import *
from git import Git


def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


class App:
    def __init__(self, master):
        self.fonte = ("Arial", "10")
        self.master = Frame(master)
        # container 1
        self.firstContainer = Frame(master)
        self.firstContainer['pady'] = 10
        self.firstContainer.pack()
        # container 2 (text) (diretorio)
        self.secondContainerText = Frame(master)
        self.secondContainerText['padx'] = 20
        self.secondContainerText.pack()
        # container 3
        self.thirstContainer = Frame(master)
        self.thirstContainer['pady'] = 10
        self.thirstContainer.pack()
        # container 5
        self.fifthContainer = Frame(master)
        self.fifthContainer['pady'] = 10
        self.fifthContainer.pack()
        # container 6 (text) (commit)
        self.sixtyContainerText = Frame(master)
        self.sixtyContainerText['padx'] = 20
        self.sixtyContainerText.pack()
        # container 7
        self.seventhContainer = Frame(master)
        self.seventhContainer['pady'] = 10
        self.seventhContainer.pack()
        # container 8 (text) (login)
        self.eighthContainerText = Frame(master)
        self.eighthContainerText['padx'] = 20
        self.eighthContainerText.pack()
        # container 9
        self.ninethContainer = Frame(master)
        self.ninethContainer['pady'] = 10
        self.ninethContainer.pack()
        # container 10 (button)
        self.tenthContainerText = Frame(master)
        self.tenthContainerText['padx'] = 20
        self.tenthContainerText.pack()
        # container 11
        self.eleventhContainer = Frame(master)
        self.eleventhContainer['pady'] = 10
        self.eleventhContainer.pack()

        # constructors
        # spacings
        # 1
        self.label1 = Label(self.firstContainer)
        self.label1['height'] = 1
        self.label1.pack()
        # 2
        self.label1 = Label(self.thirstContainer)
        self.label1['height'] = 1
        self.label1.pack()
        # 3
        self.label1 = Label(self.fifthContainer)
        self.label1['height'] = 1
        self.label1.pack()
        # 4
        self.label1 = Label(self.seventhContainer)
        self.label1['height'] = 1
        self.label1.pack()
        # 5
        self.label1 = Label(self.ninethContainer)
        self.label1['height'] = 1
        self.label1.pack()
        # 6
        self.label1 = Label(self.eleventhContainer)
        self.label1['height'] = 1
        self.label1.pack()

        # text1
        self.textLabel1 = Label(self.secondContainerText, text="Diretório: ")
        self.textLabel1['font'] = self.fonte
        self.textLabel1.pack(side=LEFT)
        self.text1 = Entry(self.secondContainerText)
        self.text1['width'] = 60
        self.text1['font'] = ("Arial", "10", "bold")
        self.text1.pack()

        # text3
        self.textLabel3 = Label(self.sixtyContainerText, text="Commitar:")
        self.textLabel3['font'] = self.fonte
        self.textLabel3.pack(side=LEFT)
        self.text3 = Entry(self.sixtyContainerText)
        self.text3['width'] = 60
        self.text3['font'] = ("Arial", "10", "bold")
        self.text3.pack()
        # text4
        self.textLabel4 = Label(self.eighthContainerText, text="SSH login:")
        self.textLabel4['font'] = self.fonte
        self.textLabel4.pack(side=LEFT)
        self.text4 = Entry(self.eighthContainerText)
        self.text4['width'] = 60
        self.text4['font'] = ("Arial", "10", "bold")
        self.text4.pack()

        # button
        self.button = Button(self.tenthContainerText)
        self.button['text'] = "PUSH IT"
        self.button['font'] = ('Arial', '10', 'bold')
        self.button['width'] = 10
        self.button['height'] = 1
        self.button.bind('<Button-1>', self.clickEvent)
        self.button.pack()

    def clickEvent(self, event):
        diretorio = str(self.text1.get())
        commit = str(self.text3.get())
        login = str(self.text4.get())
        git = Git(diretorio, commit, login)
        return git.gitPush()

# main settings
if __name__ == '__main__':
    root = Tk()
    App(root)
    root.title("AutoGit")
    root.geometry('600x400')
    # abre no centro
    center(root)
    root.mainloop()
