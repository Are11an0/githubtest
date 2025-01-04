import tkinter as tk

root = tk.Tk()
root.geometry('300x200')

language = tk.StringVar()
language.set('SPA')

f1 = tk.Frame(root)
f1.pack(pady=50, anchor=tk.CENTER)

r1 = tk.Radiobutton(f1, text='English',
                    variable=language, value='ENG')
r2 = tk.Radiobutton(f1, text='Español',
                    variable=language, value='SPA')
r3 = tk.Radiobutton(f1, text='Français',
                    variable=language,  value='FR')

for radio in f1.winfo_children():
    radio.pack()


# var = c1.toggle()
# #Returns: None
# print(f'{var=}\n{type(var)=}')

root.mainloop()

# def callback(event=None):
#     print(language.get())

# b1 = tk.Button(root, text='Click me!', command=callback,
#                activebackground='red', activeforeground='yellow')
# b1.pack(pady=50, anchor=tk.CENTER)


#O/P: 
#Returns: 