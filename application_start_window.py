#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 11:49:12 2017


"""

from tkinter import *
from analysis_by_number_window import *
from analysis_by_graph_window import *
from PIL import ImageTk, Image

class StartPage:
    
    def __init__(self, master): #Function to initialize the frame
        self.master = master
        self.frame = Frame(self.master)
        self.frame["bg"]="lightblue"

        self.img = ImageTk.PhotoImage(Image.open("./data/DSA_Logopng.gif"))
        #self.panel = Label(self.frame, image = self.img)
        #self.panel.pack(side = "bottom", fill = "both", expand = "yes")
        self.label1=Label(image = self.img)
        self.label1.pack(pady="30")
        
        #Creating the buttons
        self.button1 = Button(self.frame, text = 'ANALYSIS BY NUMBERS',font="Georgia 10 bold", command = self.new_window1)
        self.button1.pack(pady="10")
        self.button2 = Button(self.frame, text = 'ANALYSIS BY GRAPH',font="Georgia 10 bold", command = self.new_window2)
        self.button2.pack(pady="10")
#        self.button3 = Button(self.frame, text = 'CLOSE', width = 50, command = self.closeWindow)
#        self.button3.pack()
        self.frame.pack()

    def new_window1(self):  #Function to create an Analysis by numbers window
        print("\nOpening Analysis by numbers frame...")
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("Analysis by Numbers")
        self.newWindow.geometry("2000x1000")
        self.newWindow.configure(bg="lightblue")
        self.app = AnalysisNumber(self.newWindow)
        
    def new_window2(self):  #Function to create an Analysis by graph window
        print("\nOpening Analysis by graph frame...")
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("Analysis by Graph")
        self.newWindow.geometry("1000x1000")
        self.newWindow.configure(bg="lightblue")
        self.app=AnalysisGraph(self.newWindow)
    
    def closeWindow(self):  #Function to close the window
        self.master.quit()
        self.master.destroy()


def main(): #Main Function
    print("\nOpening master window frame...")
    root = Tk()
    root.geometry("300x300")
    root.title("Data Analysis of Aircrash Dataset")
    root.configure(bg="lightblue")
    app = StartPage(root)
    root.mainloop()

if __name__ == '__main__':
    main()
