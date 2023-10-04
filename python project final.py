from tkinter import *
from tkinter import messagebox
import threading
import time
nw = Tk()


def easy():
    global fn
    fn = 'easy.txt'
    nw.destroy()


def medium():
    global fn
    fn = 'medium.txt'
    nw.destroy()


def hard():
    global fn
    fn = 'hard.txt'
    nw.destroy()
nw.title('Difficulty Level Window')
dlbl = Label(nw, text='Select the Difficulty Level', font=('Verdana', 15))
dlbl.pack()
var = IntVar()
vari = IntVar()
varia = IntVar()
R1 = Radiobutton(nw, text="Easy", variable=var, command=easy)
R1.configure(font=('Verdana', 15), fg='green')
R1.pack(anchor='w')
R2 = Radiobutton(nw, text="Medium", variable=vari, command=medium)
R2.configure(font=('Verdana', 15), fg='orange')
R2.pack(anchor='w')
R3 = Radiobutton(nw, text="Hard", variable=varia, command=hard)
R3.configure(font=('Verdana', 15), fg='red')
R3.pack(anchor='w')
nw.mainloop()
fo = open(fn)
root = Tk()
root.geometry('1000x2000')
root.title('Typing Speed Test Window')
tlbl = Label(root, text='Time Left:', font=('Verdana', 20))
clbl1 = Label(root, text='Coming Up Next', font=('Verdana', 15))
sec = 60
lines = []
ilines = []
word = []
tim = StringVar()
timerdis = Label(root, text='01:00', fg='green', font=('Times New Roman', 25))
lbl = Label(root, text='Enter the following text', font=('Verdana', 15))
otxt_var = StringVar()
for line in fo:
    words = line.split(' ')
    for i in range(0, len(words)):
        if words[i] == '':
            continue
        ilines.append(words[i])
        if words[i] == '\n' or words[i] == ' ':
            continue
        words[i] = words[i].strip()
        word.append(words[i])
    line = line.strip()
    lines.append(line)
clbl2 = Text(root, height=23, width=80)
clbl2.configure(font=("Courier", 13))
clbl2.insert(INSERT, lines[0] + '\n')
clbl2.insert(INSERT, lines[1] + '\n')
a = "1" + '.' + str(len(word[0]))
clbl2.tag_add("start", "1.0", a)
clbl2.tag_config("start", foreground="blue")
itxt = Label(root, text=word[0], font=("Courier", 13), fg='blue')
disp = word[0]
l = 0
k = 0
j = 1
m = 1
x = 1
ps = 0
countc = 0
countw = 0
lettercount = 0
lcount = 0
wordcount = 0
pe = len(word[0])
add = ''
y = ''
z = ''
d = '1.0'
e = '1' + '.' + str(len(word[0]))


def countdown():
    global sec
    if sec > 0:
        sec = sec - 1
        mins = sec // 60
        m = str(mins)
        if mins < 10:
            m = '0' + str(mins)
        se = sec - (mins*60)
        s = str(se)
        tim.set(m + ':' + s)
        timerdis.config(textvariable=tim)
        if se < 10:
            s = '0' + str(se)
            tim.set(m + ':' + s)
            timerdis.config(textvariable=tim, fg='red')
            tlbl.configure(fg='red')
        root.after(1000, countdown)
    elif sec == 0:
        messagebox.showinfo('Message', 'Time is completed')


def spellcheck(inp):
    global disp, itxt, l, countc, countw, k, j, m, x, ps, pe, y, z, d, e
    if(inp == disp):
        out.configure(text='Correct', fg='green', font=30)
        countc += 1
        clbl2.tag_add("correct", d, e)
        clbl2.tag_config("correct", foreground="green")
    else:
        out.configure(text='Wrong', fg='red', font=30)
        countw += 1
        clbl2.tag_add("wrong", d, e)
        clbl2.tag_config("wrong", foreground="red")
    try:
        l = l + 1
        disp = word[l]
        itxt.configure(text=disp)
        otxt_var.set("")
        ps = pe
        pe = (len(word[l])) + pe + 1
        y = str(x) + '.' + str(ps)
        z = str(x) + '.' + str(pe)
        clbl2.tag_add("start", y, z)
        clbl2.tag_config("start", foreground="blue")
        k = k + 1
        if (ilines[k] == '\n'):
            j = j + 1
            k = k + 1
            m = m + 1
            x = x + 1
            ps = 0
            pe = 0
            pe = (len(word[l])) + pe + 1
            y = str(x) + '.' + str(ps)
            z = str(x) + '.' + str(pe)
            clbl2.tag_add("start", y, z)
            clbl2.tag_config("start", foreground="blue")
            d = y
            e = z
            if j > (len(lines) - 1):
                return
            else:
                clbl2.insert(INSERT, lines[j] + '\n')
        d = y
        e = z
    except:
        itxt.configure(text='end of the check session')
        otxt_var.set('NA')


def timefunc():
    print('the number of right words is:', countc)
    print('the number of wrong words is:', countw)
    print('the typing speed is {0} charcters/min'.format(lettercount))
    print('the typing speed is {0} words/min'.format(countc))
    itxt.configure(text='end of the check session')
    otxt_var.set('NA')
    time.sleep(5)
    root.destroy()


def endcheck(label):
    global value, add, wordcount, lettercount, lcount
    value = label.char
    if (wordcount == 0):
        timer.start()
        countdown()
        wordcount += 1
    if (value != ' '):
        add = add + value
        lettercount += 1
        lcount += 1
        if lcount == 2:
            out.configure(text='')
        return
    else:
        spellcheck(add)
        add = ''
        lcount = 0
timer = threading.Timer(60.0, timefunc)
otxt = Entry(root, textvariable=otxt_var)
root.bind('<Key>', lambda i: endcheck(i))
out = Label(root)
tlbl.place(x=820, y=10)
timerdis.place(x=840, y=45)
clbl1.pack()
clbl2.pack(anchor='w')
lbl.pack()
itxt.pack()
lbl1 = Label(root, text='Type Here', font=('Verdana', 15)).pack()
otxt.pack()
out.pack()
root.mainloop()
