from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newFile():
    global file
    root.title("Notepad")
    file=None
    TextArea.delete(1.0,END)
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All  Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) +" - Notepad")
        TextArea.delete(1.0,END)
        f=open( file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
        

def saveFile():
    global file
    if file==None:
        file =asksaveasfilename(initialfile="Untitles.txt",defaultextension=".txt",filetypes=[("All  Files","*.*"),("Text Documents","*.txt")])
        
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) +" - Notepad")
    else:
         f=open(file,"w")
         f.write(TextArea.get(1.0,END))
         f.close() 

def quitApp():
    pass
def cut():
    TextArea.event_generator(("<<Cut>>"))

def copy():
    TextArea.event_generator(("<<Copy>>"))

def paste():
    TextArea.event_generator(("<<Paste>>"))

def about():
    showinfo("Notepad", "Hello Sir/Ma'am\n How Uru'S Notepad can help you")


if __name__ == '__main__':
    
    #basic tkinter setup
    root=Tk()
    root.title("Urvashi'S NotePad")
    root.geometry("800x500")
    
    #add text area
    TextArea=Text(root, font="lucida 13")
    file=None
    TextArea.pack(expand=True,fill=BOTH)
    
    #lets create menubar
    Menubar=Menu(root)
    
    #fimemenu start
    Filemenu=Menu(Menubar,tearoff=0)
    
    #to open new file
    Filemenu.add_command(label="new", command=newFile)
    #to open existing file
    Filemenu.add_command(label="Open", command=openFile)
    #to save the current file
    Filemenu.add_command(label="Save", command=saveFile)
    Filemenu.add_separator()
    Filemenu.add_command(label="Exit", command=quitApp)
    Menubar.add_cascade(label="File",menu=Filemenu)
    
    #edit menu start
    Editmenu=Menu(Menubar,tearoff=0)
    #to give feature of cut
    Editmenu.add_command(label="Cut",command=cut)
    Editmenu.add_command(label="copy",command=copy)
    Editmenu.add_command(label="Paste",command=paste)
    Menubar.add_cascade(label="Edit",menu=Editmenu)
    #edit menu end
    
    #help menu start
    Helpmenu=Menu(Menubar,tearoff=0)
    Helpmenu.add_command(label="About Notepad",command=about)
    Menubar.add_cascade(label="Help",menu=Helpmenu)
    root.config(menu=Menubar)
    
    #adding scrollbar                    
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
   
root.mainloop()
