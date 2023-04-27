from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmTrapesium:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
    
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        Label(mainFrame, text='Masukan Panjang Sisi Atas:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Masukan Panjang Sisi Bawah:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Masukan Tinggi Trapesium:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Trapesium:").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        
        self.txtPanjangAtas = Entry(mainFrame)
        self.txtPanjangAtas.grid(row=0, column=1, padx=5, pady=5)
        self.txtPanjangBawah = Entry(mainFrame)
        self.txtPanjangBawah.grid(row=1, column=1, padx=5, pady=5)
        self.txtTinggiTrapesium = Entry(mainFrame)
        self.txtTinggiTrapesium.grid(row=2, column=1, padx=5, pady=5)
        
        
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5)
        
        self.btnHitung = Button(mainFrame, text='Hitung',
        command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
    
    def onHitung(self, event=None):
        panjangAtas = float(self.txtPanjangAtas.get())
        panjangBawah = float(self.txtPanjangBawah.get())
        tinggiTrapesium = float(self.txtTinggiTrapesium.get())
        luas = self.luas(panjangAtas, panjangBawah, tinggiTrapesium)
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(luas))
        
    def luas(self, panjangAtas, panjangBawah, tinggiTrapesium):
        luas = round(0.5 * (panjangAtas + panjangBawah) * tinggiTrapesium,2)
        return luas
    
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmTrapesium(root, "Program Luas Trapesium")
    root.mainloop() 