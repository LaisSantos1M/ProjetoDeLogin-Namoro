from tkinter import*
import random

root  =Tk()
root.title("QUER NOMORAR COMIGO?")
root.geometry("400x200")
root.resizable(False,False)
root.configure(bg="#F0F0F0")

def move_Button(event):
    x = random.randint(50,350)#garar uma nova posição de x aleatória entre 50 e 350
    y = random.randint(50,150)#garar uma nova posição de y aleatória entre 50 e 350
    
    #verificar se a nova posicão x e y não colidem com o botão sim 
    if(x < sim_button.winfo_x() - 50 or x > sim_button.winfo_x() + 50) or ( y < sim_button.winfo_y() - 50 or y > sim_button.winfo_y() + 50):
        nao_button.place(x=x, y=y)#posicionar o botão nao na nova piosição

def show_response(response):
    if response == "sim":
        label_response.config(text="VOCÊ DISSE SIM!", fg="#32CD32")
    elif response == "nao":
        label_response.config(text="VOCÊ DISSE NÃO!", fg= "#FF6347")

sim_button = Button(root, text="SIM",width=10,command=lambda:show_response("sim"))
nao_button = Button(root, text="NÃO",width=10,command=lambda:show_response("nao"))

sim_button.configure(bg='#32CD32',fg=  '#ffffff',font=('Helvetica',12))
nao_button.configure(bg='#FF6347',fg=  '#ffffff',font=('Helvetica',12))

label_question = Label(root, text="QUER NOMORAR COMIGO?", font=('Helvetica',14), bg=("#f0f0f0"))
label_response = Label(root, text="", font=('Helvetica',14), bg=("#f0f0f0"))

sim_button.place(x=100, y=75)
nao_button.place(x=250, y=75)
label_question.place(x=50, y=20)
label_response.place(x=120, y=130)

nao_button.bind("<Motion>", move_Button)
root.mainloop()