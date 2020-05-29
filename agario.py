from tkinter import *
import random
def dots():
    x=random.randint(0,1500)
    y=random.randint(0,1500)
    colors = ['blue', 'red', 'orange', 'yellow','green']
    c1.create_oval(x,y,x+5,y+5, fill = random.choice(colors))
root = Tk()
c1 = Canvas(root, width=1500, height=1500)
c1.pack()
i=0
while i<500:
    dots()
    i+=1
root.mainloop()