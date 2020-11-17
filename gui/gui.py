import tkinter
import tkinter.messagebox as tmb
import voice_assistant

root = tkinter.Tk()

root.geometry("200x100")

def start():
	voice_assistant.main()

def exit():
	sys.exit()

start = tkinter.Button(root, text ="Start the Voice Assistant", command = start).pack()

exit = tkinter.Button(root, text = "Exit", command = root.destroy).pack()

root.mainloop()