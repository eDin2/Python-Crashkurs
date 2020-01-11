import tkinter
import tkinter.messagebox

class Oberflaeche(tkinter.Frame):
	def __init__(self, master=None):
		tkinter.Frame.__init__(self, master)
		# Groesse des Fensters automatisch anpassen
		self.pack()
		
		# Einen Button erstellen
		self.mach_etwas_button = tkinter.Button(self, text="mach etwas!", command=self.mach_etwas)
		self.mach_etwas_button.pack()
		
		# Einen Button erstellen
		self.beenden = tkinter.Button(self, text="beenden", command=self.close_window)
		self.beenden.pack()

	# Verhalten des ersten Buttons festlegen
	def mach_etwas(self):
		tkinter.messagebox.showinfo("Eine Info-Box", "Habe etwas gemacht!")

	# Verhalten des zweiten Buttons festlegen
	def close_window(self): 
		root.destroy()

# Hauptfenster erstellen
root = tkinter.Tk()
# Eigenschaften fuer das Fenster setzen
root.title("Eine GUI")
root.minsize(width=300, height=100)
# Instanz von Oberflaeche erstellen und Parent-Objekt festlegen
oberflaeche = Oberflaeche(master=root)
# Hauptschleife starten, um auf Klicks etc. zu reagieren
oberflaeche.mainloop()
