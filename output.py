import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess
import shutil
import os
import sys



class BareboneBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("txt view")

        # Janela amarela
        self.root.configure(bg='yellow')

        # Área de texto
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=10)

        # Botões
        
        self.run_button = tk.Button(self.root, text="save", command=self.run_kernel)
        self.run_button.pack(pady=5)
        self.text_area.delete(1.0, tk.END)
        ss=""
        for n in sys.stdin:
            ss=ss+n+"\n"
        self.text_area.insert(tk.END,ss)
        

    def execute_command(self, command,show:bool):
        try:
            
            result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
            self.text_area.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            if show:
                self.text_area.insert(tk.END,f"Error executing command:\n{e.output}")

    

        
    def run_kernel(self):
        
        filename = tk.filedialog.asksaveasfilename(title="save file as")
        txts=self.text_area.get("1.0", "end-1c")
        f1=open(filename,"w")
        f1.write(txts)
        f1.close()
        
        




if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
