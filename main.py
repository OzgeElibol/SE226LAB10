import tkinter as tk
r=tk.Tk()
r.title("se226 lab10")

def buttonRead():
    textBox.delete("1.0",tk.END)
    with open("Marvel.txt") as f:
     text = f.read()
    textBox.insert("end", text)
    print(textBox)

def calculateFreq():
    textBox.delete('1.0', tk.END)
    with open("Marvel.txt") as f:
        string = f.read()
    stringList = []
    for word in string.split():
        stringList.append(word)

    for word in stringList:
        x=str("Frequency of "+ str(word)+ " = "+ str(stringList.count(word))+ "\n")
        textBox.insert(tk.INSERT, (x))

    textBox.pack(side=tk.LEFT, expand=True)


    frame.pack(expand=True)

l1=tk.Label(r,text="READ button will read everything in Marvel.txt file.\n CALCULATE button  will calculate frequency of the words in text file.")
l1.pack()

frame = tk.LabelFrame(r,text="Words in the file")
frame.pack()

textBox = tk.Text(frame)
textBox.pack()

b1=tk.Button(frame,text="READ",bg="black",fg="red",font="Arial 20 bold",command=buttonRead)
b1.pack()

b2=tk.Button(frame,text="CALCULATE",bg="black",fg="red",font="Arial 20 bold",command=calculateFreq)
b2.pack()

r.mainloop()
