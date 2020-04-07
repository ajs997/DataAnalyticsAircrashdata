#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 11:48:07 2017


"""

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

from analytics_main import *
from tkinter import *

class AnalysisGraph(Frame):
    
    def __init__(self,master): #Function to initialize the window
        #Initialize the frame
        super(AnalysisGraph,self).__init__(master)
        self.grid()
        self.display_widgets()
        self.dataset=readData()
        self.dataset=cleanData(self.dataset)
        self.configure(bg="lightblue")
        
    def display_widgets(self):  #Function to create the widgets to take data
        
        Label(self,text="FILTER COLUMNS",bg="lightblue",font="times 16 bold italic").grid(row=0,column=0,columnspan=2,sticky=W)
        Label(self,text="   ",bg="lightblue",width=25).grid(row=0,column=1,sticky=W)
        Label(self,text="   ",bg="lightblue",width=25).grid(row=0,column=2,sticky=W)
        Label(self,text="   ",bg="lightblue",width=25).grid(row=0,column=3,sticky=W)
        Label(self,text="   ",bg="lightblue",width=25).grid(row=0,column=4,sticky=W)
        Label(self,text="   ",bg="lightblue",width=25).grid(row=0,column=5,sticky=W)
#        self.close=Button(self,text="Quit",command=self.closeWindow)
#        self.close.grid(row=0,column=3,sticky=W)
        
        #Radiobutton for selecting columns
        Label(self,bg="lightblue",text="Select Columns:* ",width=25).grid(row=1,column=0,sticky=W)
        self.col=StringVar()
        Radiobutton(self,bg="lightblue",text="ABOARD",variable=self.col,value='Aboard').grid(row=1,column=1,sticky=W)
        Radiobutton(self,bg="lightblue",text="FATALITIES",variable=self.col,value='Fatalities').grid(row=1,column=2,sticky=W)
        Radiobutton(self,bg="lightblue",text="GROUND",variable=self.col,value='Ground').grid(row=1,column=3,sticky=W)
        
        #Filter by From and To date
        Label(self,text="From (YYYY-MM-DD) :",bg="lightblue",width=25).grid(row=2,column=0,sticky=W)
        self.frm=Entry(self)
        self.frm.grid(row=2,column=1,sticky=W)
        
        Label(self,bg="lightblue",text="To (YYYY-MM-DD) :").grid(row=2,column=2,sticky=W)
        self.to=Entry(self)
        self.to.grid(row=2,column=3,sticky=W)
        
        #Filter by Start and End indices of rows
        Label(self,bg="lightblue",text="Filter by Start Index:").grid(row=5,column=0,sticky=W)
        self.rowStart=Entry(self)
        self.rowStart.grid(row=5,column=1,sticky=W)
        Label(self,bg="lightblue",text="Filter by End Index:").grid(row=5,column=2,sticky=W)
        self.rowEnd=Entry(self)
        self.rowEnd.grid(row=5,column=3,sticky=W)
        
        #Radiobutton for selecting type of graph
        Label(self,bg="lightblue",text="Type of Graph: ",width=25).grid(row=48,column=0,sticky=W)
        self.type_graph=StringVar()
        Radiobutton(self,bg="lightblue",text="Line",variable=self.type_graph,value='line').grid(row=48,column=1,sticky=W)
        Radiobutton(self,bg="lightblue",text="Bar",variable=self.type_graph,value='bar').grid(row=48,column=2,sticky=W)
        Radiobutton(self,bg="lightblue",text="Histogram",variable=self.type_graph,value='hist').grid(row=48,column=3,sticky=W)
        Radiobutton(self,bg="lightblue",text="Boxplot",variable=self.type_graph,value='box').grid(row=48,column=4,sticky=W)
        
        #Radiobutton for selecting type of output
        Label(self,bg="lightblue",text="Type of Output:* ",width=25).grid(row=49,column=0,sticky=W)
        self.type_op=StringVar()
        Radiobutton(self,bg="lightblue",text="Tkinter Canvas",variable=self.type_op,value='tkcanvas').grid(row=49,column=1,sticky=W)
        Radiobutton(self,bg="lightblue",text="IPython Console",variable=self.type_op,value='ipconsole').grid(row=49,column=2,sticky=W)
        
        #Button to submit the data
        Label(self,bg="lightblue",text=" ").grid(row=50,column=0,sticky=W)
        self.btn1=Button(self,font="Georgia 10 bold ",text="SUBMIT COLUMNS",command=self.displayGraph)
        self.btn1.grid(row=51,column=1,columnspan=2,sticky=N)
        
    def displayGraph(self): #Function to display the graph
        newds=self.dataset
        
        if self.col.get():
            col=self.col.get()
            
        #Taking start and end index
        if  self.rowStart.get() and self.rowEnd.get():
            rowStart=int(self.rowStart.get())
            rowEnd=int(self.rowEnd.get())
        else:
            rowStart=0
            rowEnd=desDataset(newds,"shape")[0]
        
        #Taking type of graph
        if self.type_graph.get():
            type_graph=self.type_graph.get()
            print(type_graph)
            
        #Taking from and to data the entries
        if self.frm.get() and self.to.get():
            frm=datetime.datetime.strptime(self.frm.get(), "%Y-%m-%d").date()
            to=datetime.datetime.strptime(self.to.get(), "%Y-%m-%d").date()
        else:
            frm=datetime.datetime.strptime("1910-01-01", "%Y-%m-%d").date()
            to=datetime.datetime.strptime("1990-01-01", "%Y-%m-%d").date()
            
        
        #filtering the dataset by dates
        newds=filterByDates(newds,frm,to)
        
        if self.type_op.get()=='tkcanvas':
            draw(newds,col)   #Calls the function that creates a window that displays the graph
        else:
            newds=groupBySum(newds,'Operator',col)
            plotGraph(newds,rowStart,rowEnd,'Operator',col,type_graph)
    
    def closeWindow(self):  #Function to close the window
        self.master.quit()
        self.master.destroy()


def draw(dataset,col):  #Function to display the graph in a separate window
    #initialize the new window
    root = Tk()
    root.wm_title("Embedding in TK")
    
    #initialize the Fugure object
    f = Figure(figsize=(14, 6), dpi=100)
    a = f.add_subplot(111)
    
    #plot the graph
    a.plot(dataset[col])
    a.set_title('Line graph for analysis of number of '+col)
    a.set_xlabel(col)
    a.set_ylabel('Number')
    
    
    #create a DrawingArea
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
    
    def _quit():    #Function to quit the window
        root.quit()     # stops mainloop
        root.destroy()  # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    
    #button to quit the window
    button = Button(master=root, text='Quit', command=_quit)
    button.pack(side=BOTTOM)
    
    #creating the loop
    root.mainloop()
    
#root=Tk()
#root.title("Data analysis of Aircrash Dataset")
#root.geometry("2000x1000")
#root.configure(bg="lightblue")
#app=AnalysisGraph(root)
#root.mainloop()
