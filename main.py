from tkinter import *
import random

root = Tk()
root.title("Picninc Bag List")
root.geometry("400x400")
root.configure(background="yellow")
Bag = ['Bottle', 'Tiffin', 'ID Card', 'Chocoloates', 'Chips', 'Tickets', 'Hanky']
listed_items = Label(root)
listed_items.place(relx=0.5, rely=0.4, anchor=CENTER)
put_item = Label(root)
put_item.place(relx=0.5, rely=0.6, anchor=CENTER)
def putInBag():
    randomIndex = random.sample(range(0, 7), 1)
    listed_items["text"]= "Listed Items: " + str(Bag)
    put_item["text"]="Put "  + str(randomIndex) + " in the bag"
button1 = Button(root, text="Which item to put in the bag?", command=putInBag)
button1.configure(bg ="greenyellow", fg="red")
button1.place(relx=0.5, rely=0.5, anchor=CENTER)
listed_items.configure(fg="green")
put_item.configure(fg="red")
root.mainloop()