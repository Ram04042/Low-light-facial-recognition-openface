from tkinter import *
import queue
import time
import threading
import test

def bluetooth_loop(thread_queue=None, text_input=""):
	text_input = test.match_pathpack(text_input)
	thread_queue.put(text_input)
	test.load_ram()

class App:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        self.root = frame
        test.load_ram()

        self.quit_button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.quit_button.pack(side=LEFT)

        self.update_btn = Button(frame, text="Update", command=self.update_text)
        self.update_btn.pack(side=LEFT)
        self.text_label = Label(frame)
        self.text_label.config(text='No message')
        self.text_label.pack(side=RIGHT)
        self.text_input = Entry(frame, width=40)
        self.text_input.pack(side=RIGHT)

    def update_text(self):
        '''
        Spawn a new thread for running long loops in background
        '''
        self.text_label.config(text='Running loop')
        self.thread_queue = queue.Queue()
        self.new_thread = threading.Thread(
            target=bluetooth_loop,
            kwargs={'thread_queue':self.thread_queue,'text_input':self.text_input.get()})
        self.new_thread.start()
        self.root.after(100, self.listen_for_result)

    def listen_for_result(self):
        '''
        Check if there is something in the queue
        '''
        try:
            res = self.thread_queue.get(0)
            self.text_label.config(text=res)
        except queue.Empty:
            self.root.after(100, self.listen_for_result)

root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below
