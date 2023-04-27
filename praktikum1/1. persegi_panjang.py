import tkinter as tk

class FrmPersegiPanjang:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
    
    def aturKomponen(self):
        mainFrame = tk.Frame(self.parent, bd=10)
        mainFrame.pack(fill=tk.BOTH, expand=tk.YES)
        
        tk.Label(mainFrame, text='Masukan Panjang:').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        tk.Label(mainFrame, text="Masukan Lebar:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        tk.Label(mainFrame, text="Luas Persegi Panjang:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        tk.Label(mainFrame, text="Keliling Persegi Panjang:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        
        self.txtPanjang = tk.Entry(mainFrame)
        self.txtPanjang.grid(row=0, column=1, padx=5, pady=5)
        self.txtLebar = tk.Entry(mainFrame)
        self.txtLebar.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuas = tk.Entry(mainFrame)
        self.txtLuas.grid(row=3, column=1, padx=5, pady=5)
        self.txtKeliling = tk.Entry(mainFrame)
        self.txtKeliling.grid(row=4, column=1, padx=5, pady=5)
        
        self.btnHitung = tk.Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
    
    def onHitung(self):
        panjang = int(self.txtPanjang.get())
        lebar = int(self.txtLebar.get())
        luas, keliling = self.luasKeliling(panjang, lebar)
        self.txtLuas.delete(0, tk.END)
        self.txtLuas.insert(tk.END, str(luas))
        self.txtKeliling.delete(0, tk.END)
        self.txtKeliling.insert(tk.END, str(keliling))
    
    def luasKeliling(self, panjang, lebar):
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
        return luas, keliling
    
    def onKeluar(self):
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FrmPersegiPanjang(root, "Program Luas dan Keliling Persegi Panjang")
    root.mainloop()