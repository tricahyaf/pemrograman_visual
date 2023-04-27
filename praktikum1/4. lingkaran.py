from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
import math

class FrmLingkaran:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
    
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        Label(mainFrame, text='Masukan Jari-Jari Lingkaran:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Lingkaran:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling Lingkaran:").grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.txtJariJariLingkaran = Entry(mainFrame)
        self.txtJariJariLingkaran.grid(row=0, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=3, column=1, padx=5, pady=5)
        self.txtKeliling = Entry(mainFrame)
        self.txtKeliling.grid(row=4, column=1, padx=5, pady=5)
        
        self.btnHitung = Button(mainFrame, text='Hitung',
        command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
    
    def onHitung(self):
        jarijari = float(self.txtJariJariLingkaran.get())
        luas, kel = self.luasKeliling(jarijari)
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(round(luas,2)))
        self.txtKeliling.delete(0,END)
        self.txtKeliling.insert(END,str(round(kel,2)))
        
    def luasKeliling(self, jarijari):
        luas = math.pi*(jarijari*jarijari)
        kel = 2*math.pi*jarijari
        return luas, kel
    
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmLingkaran(root, "Program Menghitung Keliling Luas Lingkaran")
    root.mainloop() 