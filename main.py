from tkinter import *
import pyperclip

alphabets = "abcdefghijklmnopqrstuvwxyz"

root = Tk()
root.title("Cryptogaphy")

Label(root, text="Enter string plaintext: ", padx=5, pady=5).grid(row=0, column=0, columnspan=3)
pt = Entry(root, width=50)
pt.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

l = Label(root, text="Ciphertext appears here: ")
l.grid(row=4, column=0, columnspan=3)


def caesar(pt):
    l.grid_forget()
    win = Tk()
    win.title("Caesar cipher-key")
    Label(win, text="Enter a key: ").grid(row=0, column=0, pady=5)
    k = Entry(win)
    k.grid(row=0, column=1)
    Button(win, text="Submit", command=lambda: submit(int(k.get()), pt)).grid(row=1, column=0, pady=5, columnspan=2)

    def submit(key, pt):
        global l
        l.grid_forget()
        cipher = ""
        for i in pt:
            p = alphabets.index(i)
            c = (p + key) % 26
            c_val = alphabets[c]
            cipher += c_val
        l = Label(root, text=cipher, padx=5, pady=5)
        l.grid(row=4, column=0, columnspan=3)

        Button(root, text="Copy", command=pyperclip.copy(cipher)).grid(row=5, column=0, columnspan=3)


def affine(pt):
    l.grid_forget()

    win = Tk()
    win.title("Affine cipher-key")

    Label(win, text="Enter a multiplicative key: ").grid(row=0, column=0, pady=5)
    Label(win, text="Enter an additive key: ").grid(row=1, column=0, pady=5)

    k1 = Entry(win)
    k1.grid(row=0, column=1)
    k2 = Entry(win)
    k2.grid(row=1, column=1)

    Button(win, text="Submit", command=lambda: submit(int(k1.get()), int(k2.get()), pt)).grid(row=2, column=0,
                                                                                              columnspan=2, pady=5)

    def submit(mul_key, add_key, pt):
        global l
        l.grid_forget()
        cipher = ""
        for i in pt:
            p = alphabets.index(i)
            c = ((p * mul_key) + add_key) % 26
            c_val = alphabets[c]
            cipher += c_val
        l = Label(root, text=cipher, padx=5, pady=5)
        l.grid(row=4, column=0, columnspan=3)
        Button(root, text="Copy", command=pyperclip.copy(cipher)).grid(row=5, column=0, columnspan=3)


def auto_key(pt):
    l.grid_forget()
    win = Tk()
    win.title("Autokey cipher-key")

    Label(win, text="Enter a key: ").grid(row=0, column=0, pady=5)
    key = Entry(win)
    key.grid(row=0, column=1)
    Button(win, text="Submit", command=lambda: submit(int(key.get()), pt)).grid(row=2, column=0, pady=5, columnspan=2)

    def submit(key, pt):
        global l
        l.grid_forget()
        cipher = ""
        p = []
        k = []
        for i in pt:
            p.append(alphabets.index(i))
            k.append(alphabets.index(i))
        k.insert(0, key)
        for i in range(len(p)):
            c = (p[i] + k[i]) % 26
            c_val = alphabets[c]
            cipher += c_val
        l = Label(root, text=cipher, padx=5, pady=5)
        l.grid(row=4, column=0, columnspan=3)
        Button(root, text="Copy", command=pyperclip.copy(cipher)).grid(row=5, column=0, columnspan=3)


def railfence(pt):
    global l
    l.grid_forget()
    l.grid_forget()
    cipher1 = ""
    cipher2 = ""
    for i in range(len(pt)):
        if i % 2 == 0:
            c1 = "".join(pt[i])
            cipher1 += c1
        else:
            c2 = "".join(pt[i])
            cipher2 += c2
    l = Label(root, text=cipher1 + cipher2, padx=5, pady=5)
    l.grid(row=4, column=0, columnspan=3)
    Button(root, text="Copy", command=pyperclip.copy(cipher1 + cipher2)).grid(row=5, column=0, columnspan=3)


def vignere(plaintext):
    l.grid_forget()
    win = Tk()
    win.title("Vignere cipher-key")

    Label(win, text="Enter a string key: ").grid(row=0, column=0, pady=5)
    key = Entry(win)
    key.grid(row=0, column=1, pady=5)
    Button(win, text="Submit", command=lambda: submit(plaintext, key.get())).grid(row=1, column=0, columnspan=2, pady=5)

    def submit(plaintext, key):
        global l
        l.grid_forget()
        pt = []
        kt = []
        for i in key:
            kt.append(alphabets.index(i))
        for i in plaintext:
            pt.append(alphabets.index(i))
        if len(kt) < len(pt):
            for i in key:
                kt.append(alphabets.index(i))
        cipher = ""
        for i in range(len(pt)):
            ct = (pt[i] + kt[i]) % 26
            c = alphabets[ct]
            cipher += c
        l = Label(root, text=cipher, padx=5, pady=5)
        l.grid(row=4, column=0, columnspan=3)
        Button(root, text="Copy", command=pyperclip.copy(cipher)).grid(row=5, column=0, columnspan=3)


def rsa(plaintext):
    l.grid_forget()
    win = Tk()
    win.title("Rsa p and q")
    Label(win, text="Enter prime number p: ").grid(row=0, column=0, pady=5)
    p = Entry(win)
    p.grid(row=0, column=1)
    Label(win, text="Enter prime number q: ").grid(row=1, column=0, pady=5)
    q = Entry(win)
    q.grid(row=1, column=1)
    Button(win, text="Submit", command=lambda: submit(int(p.get()), int(q.get()))).grid(row=2, column=0, columnspan=2,
                                                                                        pady=5)

    def submit(p, q):
        global l
        l.grid_forget()
        n = p * q
        phi_n = (p - 1) * (q - 1)
        pt = []
        for i in plaintext:
            pt.append(ord(i))

        def gcd(e, phi_n):
            while phi_n != 0:
                r = e % phi_n
                e = phi_n
                phi_n = r
            return e

        for i in range(2, phi_n):
            if gcd(i, phi_n) == 1:
                e = i
                break

        ct = []
        for i in pt:
            ct.append((i ** e) % n)

        l = Label(root, text=ct, padx=5, pady=5)
        l.grid(row=4, column=0, columnspan=3)


Button(root, text="Caesar", padx=12, pady=5, command=lambda: caesar(pt.get())).grid(row=2, column=0, padx=20, pady=10)
Button(root, text="Affine", padx=13, pady=5, command=lambda: affine(pt.get())).grid(row=2, column=1, padx=20)
Button(root, text="Autokey", padx=7, pady=5, command=lambda: auto_key(pt.get())).grid(row=2, column=2, padx=20)
Button(root, text="Railfence", padx=5, pady=5, command=lambda: railfence(pt.get())).grid(row=3, column=0, padx=20,
                                                                                         pady=10)
Button(root, text="Vignere", padx=9, pady=5, command=lambda: vignere(pt.get())).grid(row=3, column=1, padx=20)
Button(root, text="RSA", padx=19, pady=5, command=lambda: rsa(pt.get())).grid(row=3, column=2, padx=20)

root.mainloop()
