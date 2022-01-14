from tkinter import *
root = Tk()
root.title("Fibonacci Series:")
root.geometry("400x400")
root.configure(bg="white")
label=Label(root,text="Fibonacci Series:")
label2=Label(root)
label3=Label(root)
inputbox=Entry(root)
def Fibonacci():
    no=int(inputbox.get())
    firstnumber=0
    secondnumber=1
    counter=1
    sum=0
    while (counter<=no):
        label["text"]+=str(sum)+" "
        counter=counter+1
        firstnumber=secondnumber
        secondnumber=sum
        sum=firstnumber+secondnumber
        label2["text"]="The Flower Is Fully Blossomed"
        label3["text"]="spirals in right directions are "+str(firstnumber)+" spiral in the left direction are "+str(secondnumber)
    
button1=Button(root,text="Show",command=Fibonacci)
inputbox.pack()
button1.pack()
label.pack()
label2.pack()
label3.pack()
root.mainloop()