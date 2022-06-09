import sys
try:
    from tkinter import Button, mainloop
except:
    print('No tkinter')

x = Button(
    text='Press me',
    command=(lambda: sys.stdout.write('Spam\n')))
x.pack()
mainloop()
    
input()
