import tkinter as tk
import PyPDF2
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfile

#windows
root=tk.Tk()

canvas=tk.Canvas(root,width=600,height=400)
canvas.grid(columnspan=3,rowspan=3)
# canvas.pack() #dont use grid and pack at same time in windows and pack

#logo
logo=Image.open('D:\Downloads\logo.png')

#to convert into tkinter image
logo=ImageTk.PhotoImage(logo)

#placing this image in label widget
logo_label=tk.Label(image=logo)

logo_label.image=logo#neccessary

#placing logo inside the window object
logo_label.grid(column=1,row=0)


#instructions
instructions=tk.Label(root,text='select a PDF file you want to extract all of its text',font='Raleway')
instructions.grid(columnspan =3,column=0,row=1) #row=1 below logo

#function for opening the file
def open_file():
    browse_text.set("loading")
    file=askopenfile(parent=root,mode='rb',title='choose a file',filetype=[('pdf file','*pdf')])
    if file:
       read_pdf= PyPDF2.PdfFileReader(file)
       page=read_pdf.getPage(0)
       pagecontent=page.extractText()

       #for displaying the extracted text
       textbox=tk.Text(root,height=5,width=50,padx=10,pady=10)
       textbox.insert(1.0,pagecontent)

       #to display the text in center
       textbox.tag_configure('center', justify='center')
       textbox.tag_add('center',1.0,'end')

       textbox.grid(column=1,row=3) #row=3 below button

       browse_text.set('Browse Again')


#browse button -in command we can give as lambda:open_file
browse_text=tk.StringVar()
browse_btn=tk.Button(root, textvariable=browse_text,command=open_file, font='Raleway',bg='#20bebe',fg='white',height=2,width=12)
browse_text.set("Browse")
browse_btn.grid(column=1,row=2) #row=2 below instructions

# to create a space below the button

canvas=tk.Canvas(root,width=600,height=150)
canvas.grid(columnspan=3)


#end
root.mainloop()