from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmPersegiBujurSangkar:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
    
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        Label(mainFrame, text='Masukan Panjang Sisi:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Persegi atau Bujur Sangkar:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling Persegi atau Bujur Sangkar:").grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.txtPanjangSisi = Entry(mainFrame)
        self.txtPanjangSisi.grid(row=0, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=3, column=1, padx=5, pady=5)
        self.txtKeliling = Entry(mainFrame)
        self.txtKeliling.grid(row=4, column=1, padx=5, pady=5)
        
        self.btnHitung = Button(mainFrame, text='Hitung',
        command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
    
    def onHitung(self):
        panjangsisi = int(self.txtPanjangSisi.get())
        luas, kel = self.luasKeliling(panjangsisi)
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(luas))
        self.txtKeliling.delete(0,END)
        self.txtKeliling.insert(END,str(kel))
        
    def luasKeliling(self, panjangsisi):
        luas = panjangsisi**2
        kel = 4 * panjangsisi
        return luas, kel
    
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmPersegiBujurSangkar(root, "Program Luas dan Keliling Persegi atau Bujur Sangkar")
    root.mainloop() 