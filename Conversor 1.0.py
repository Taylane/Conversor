from tkinter import *
from tkinter import font

class Aplicacao:
    def __init__(self, Toplevel):
########Declaracao dos containers#
        corFundo="gray20"
        corEntry="gray38"
        corLetra="white smoke"
        Toplevel.configure(background=corFundo)

        #Container Label, 1 Entry#
        self.containerEsquerdo = Frame(Toplevel, bd=10, background=corFundo)
        self.containerEsquerdo.grid(row=0, column=0)

        #Container Button, 2 Label, Canvas#
        self.containerCentro = Frame(Toplevel, bd=10, background=corFundo)
        self.containerCentro.grid(row=0, column=1)

        #Container Label, 2 Entry, Canvas#
        self.containerDireito = Frame(Toplevel, bd=10, background=corFundo)
        self.containerDireito.grid(row=0, column=2)

########Declaracao Canvas

        #Canvas Entry Radianos
        self.canvasEntry = Canvas(self.containerDireito, width=70, height=1, background="white")
        self.canvasEntry.grid(row=2, column=0)

########Definicao Fontes

        self.fonte = font.Font(family="Comics Sans MS", size=15, underline=0)
        self.fonteU = font.Font(family="Comics Sans MS", size=15, underline=1)

########Declaracao Labels Entrys#

        self.grausLabel = Label(self.containerEsquerdo, text="Graus", font=self.fonte, bg=corFundo, fg=corLetra)
        self.grausLabel.grid(row=0, column=0)

        self.grausEntry = Entry(self.containerEsquerdo, width=10, bg=corEntry)
        self.grausEntry.grid(row=1, column=0)

        self.radianosLabel = Label(self.containerDireito, text="Radianos", font=self.fonte, background=corFundo, fg=corLetra)
        self.radianosLabel.grid(row=0, column=0)

        self.radianosEntry1 = Entry(self.containerDireito, width=10, bg=corEntry)
        self.radianosEntry1.grid(row=1, column=0)

        self.radianosEntry2 = Entry(self.containerDireito, width = 10, bg=corEntry)
        self.radianosEntry2.grid(row=3, column=0)

#Config Converter Button

        self.converterButtom = Button(self.containerCentro, text="Converter", font=self.fonte,\
        command=self.converteFunc, bg=corEntry, fg=corLetra)
        self.converterButtom.focus_force()
        self.converterButtom.bind("<Return>", self.converteFunc_a)
        self.converterButtom.bind("<KP_Enter>", self.converteFunc_a)
        self.converterButtom.grid(row=0, column=0)

        self.resultLabel1 = Label(self.containerCentro, text="", font=self.fonte, bg=corFundo, fg=corLetra)
        self.resultLabel1.grid(row=1, column=0)

        self.resultLabel2 = Label(self.containerCentro, text="", font=self.fonte, bg=corFundo, fg=corLetra)
        self.resultLabel2.grid(row=2, column=0)

    #Declaracao Wraprers

    def converteFunc_a(self,event):
        self.converteFunc()
    
    #Declaracao Funcao Converter
    def converteFunc(self):
        #Se for inserido numero apenas na entrada de graus sera convertido para radianos 
        if((self.radianosEntry1.get()=="" and self.radianosEntry2.get()=="") and self.grausEntry.get()):
            graus=self.grausEntry.get()
            try:
                int(graus)
            except:
                self.resultLabel1["text"] = "Erro!"
                self.resultLabel2["text"] = ""
                return

            if (int(graus) == 0):
                self.resultLabel1["text"] = graus
                self.resultLabel2["text"] = ""
                self.resultLabel1["font"] = self.fonte
                return
    
            rad= int(graus)
            rad2= 180
            divisor = 2
            while( divisor < int(graus) or divisor < rad2 ) :
                if( (rad % divisor)==0 and (rad2 % divisor )==0) :
                    rad = rad/divisor
                    rad2 = rad2/divisor
                    divisor = 2
                else :
                    divisor = divisor +1

            self.resultLabel1["text"] =str(int(rad))
            self.resultLabel2["text"] =str(int(rad2))
            self.resultLabel1["font"] = self.fonteU

        #Se for inserido numero apenas na entrada de radianos sera convertido para graus 
        elif(self.grausEntry.get()==""):
            rad = self.radianosEntry1.get()
            if self.radianosEntry2.get()=="":
                rad2=1
            else:
                rad2 = self.radianosEntry2.get()  
            try:
                int(rad) and int(rad2)
            except:
                self.resultLabel1["text"] = "Erro!"
                self.resultLabel2["text"] = ""
                return
            result=0
            
            if(int(rad)==0 or int(rad2)==0):
                self.resultLabel1["text"] = 0
                self.resultLabel2["text"] = ""
                self.resultLabel1["font"] = self.fonte
                return

            result = int(int(rad)*180)/(int(rad2))

            self.resultLabel1["text"] = str(int(result)) + "\u02da"
            self.resultLabel2["text"] = ""
            self.resultLabel1["font"] = self.fonte
        #Se não for inserido apenas em graus ou apenas em radianos dara Erro
        else:
            self.resultLabel1["text"]="Erro!"
            self.resultLabel1["font"]=self.fonte
            self.resultLabel2["text"]=""

root = Tk()
Aplicacao(root)
root.wm_title("Conversor")
root.mainloop()
