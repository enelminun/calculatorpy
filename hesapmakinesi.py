import tkinter as tk
import webbrowser

def toplama():
    try:
        sayi1 = float(sayi1_entry.get())
        sayi2 = float(sayi2_entry.get())
        sonuc_label.config(text="Sonuç: " + str(sayi1 + sayi2))
    except ValueError:
        sonuc_label.config(text="Hatalı giriş!")

def cikarma():
    try:
        sayi1 = float(sayi1_entry.get())
        sayi2 = float(sayi2_entry.get())
        sonuc_label.config(text="Sonuç: " + str(sayi1 - sayi2))
    except ValueError:
        sonuc_label.config(text="Hatalı giriş!")

def carpma():
    try:
        sayi1 = float(sayi1_entry.get())
        sayi2 = float(sayi2_entry.get())
        sonuc_label.config(text="Sonuç: " + str(sayi1 * sayi2))
    except ValueError:
        sonuc_label.config(text="Hatalı giriş!")

def open_minun(event):
    webbrowser.open_new("https://www.github.com/hminun")

def cikis():
    root.destroy()

root = tk.Tk()
root.title("Hesap Makinesi")

sayi1_label = tk.Label(root, text="Sayı 1:")
sayi1_label.grid(row=0, column=0, padx=5, pady=5)

sayi1_entry = tk.Entry(root)
sayi1_entry.grid(row=0, column=1, padx=5, pady=5)

sayi2_label = tk.Label(root, text="Sayı 2:")
sayi2_label.grid(row=1, column=0, padx=5, pady=5)

sayi2_entry = tk.Entry(root)
sayi2_entry.grid(row=1, column=1, padx=5, pady=5)

toplama_button = tk.Button(root, text="Toplama", command=toplama)
toplama_button.grid(row=2, column=0, padx=5, pady=5)

cikarma_button = tk.Button(root, text="Çıkarma", command=cikarma)
cikarma_button.grid(row=2, column=1, padx=5, pady=5)

carpma_button = tk.Button(root, text="Çarpma", command=carpma)
carpma_button.grid(row=2, column=2, padx=5, pady=5)

sonuc_label = tk.Label(root, text="")
sonuc_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

imza_label = tk.Label(root, text="Minun", fg="blue", cursor="hand2")
imza_label.grid(row=4, column=2, padx=5, pady=5)
imza_label.bind("<Button-1>", open_minun)

cikis_button = tk.Button(root, text="Çıkış", command=cikis)
cikis_button.grid(row=4, column=1, columnspan=3, padx=5, pady=5)


root.resizable(False, False)
root.geometry("300x300")
root.mainloop()