from tkinter import *
window = Tk()

def tombol_klik(item):
    global ekspresi
    ekspresi = ekspresi + str(item)
    input_text.set(ekspresi)

def hapus():
    global ekspresi
    ekspresi = ""
    input_text.set("")

def hasil():
    try:
        global ekspresi
        # Menghitung hasil dengan mengganti "%" dengan "/100" untuk perhitungan persentase
        ekspresi_terhitung = ekspresi.replace("%", "/100")
        total = str(eval(ekspresi_terhitung))
        input_text.set(total)
        ekspresi = total
    except:
        input_text.set("Error")
        ekspresi = ""

def persen():
    global ekspresi
    ekspresi += "%"  # Menambahkan simbol % ke ekspresi tanpa menghitung langsung
    input_text.set(ekspresi)

def negasi():
    global ekspresi
    if ekspresi:
        if ekspresi[0] == '-':
            ekspresi = ekspresi[1:]
        else:
            ekspresi = '-' + ekspresi
        input_text.set(ekspresi)

ekspresi = ""
input_text = StringVar()

frame = Frame(window, bg="Dark green", width=500, height=300)
frame.pack()

frame2 = Frame(window, bg="Black", width=500, height=300)
frame2.pack()

label = Label(frame, width=50, anchor="w", text="Kalkulator Byan", font=("Times New Roman", 10))
label.pack(padx=20, pady=20)

label2 = Label(frame, width=50, anchor="e", textvariable=input_text, font=("Times New Roman", 20))
label2.pack(padx=20, pady=20)

Button(frame2, width=6, height=3, text="AC", fg="gray", bg="orange", command=hapus).grid(row=0, column=0)

Button(frame2, width=6, height=3, text="+/-", fg="black", bg="gray", command=negasi).grid(row=0, column=1)

Button(frame2, width=6, height=3, text="%", bg="gray", command=persen).grid(row=0, column=2, padx=10, pady=10)

Button(frame2, width=6, height=3, text="÷", bg="gray", command=lambda: tombol_klik("/")).grid(row=0, column=3, padx=10, pady=10)

Button(frame2, width=6, height=3, text="×", bg="gray", command=lambda: tombol_klik("*")).grid(row=1, column=3, padx=10, pady=10)

Button(frame2, width=6, height=3, text="-", bg="gray", command=lambda: tombol_klik("-")).grid(row=2, column=3, padx=10, pady=10)

Button(frame2, width=6, height=3, text="+", bg="gray", command=lambda: tombol_klik("+")).grid(row=3, column=3)

Button(frame2, width=6, height=3, text="=", bg="gray", command=hasil).grid(row=4, column=3)

Button(frame2, text=".", width=6, height=3, command=lambda: tombol_klik(".")).grid(row=4, column=2, padx=10, pady=10)

Button(frame2, text="0", width=17, height=3, command=lambda: tombol_klik("0")).grid(row=4, column=0, columnspan=2)

Button(frame2, text="1", width=6, height=3,command=lambda: tombol_klik("1")).grid(row=3, column=0, padx=10, pady=10)

Button(frame2, text="2", width=6, height=3,command=lambda: tombol_klik("2")).grid(row=3, column=1, padx=10, pady=10)

Button(frame2, text="3", width=6, height=3,command=lambda: tombol_klik("3")).grid(row=3, column=2, padx=10, pady=10)

Button(frame2, text="4", width=6, height=3,command=lambda: tombol_klik("4")).grid(row=2, column=0, padx=10, pady=10)

Button(frame2, text="5", width=6, height=3,command=lambda: tombol_klik("5")).grid(row=2, column=1, padx=10, pady=10)

Button(frame2, text="6", width=6, height=3,command=lambda: tombol_klik("6")).grid(row=2, column=2, padx=10, pady=10)

Button(frame2, text="7", width=6, height=3,command=lambda: tombol_klik("7")).grid(row=1, column=0, padx=10, pady=10)

Button(frame2, text="8", width=6, height=3,command=lambda: tombol_klik("8")).grid(row=1, column=1, padx=10, pady=10)

Button(frame2, text="9", width=6, height=3,command=lambda: tombol_klik("9")).grid(row=1, column=2, padx=10, pady=10)

window.mainloop()
