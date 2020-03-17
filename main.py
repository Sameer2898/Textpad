import tkinter as tk
from tkinter import ttk 
from tkinter import font, colorchooser, filedialog, messagebox
import os
root=tk.Tk()
root.geometry("800x400")
root.title("Textpad - By Your Name")
root.wm_iconbitmap("icon.ico")
#Main Menu Functions
#Global Variable
url= ""
#New Function
def new_file(event=None):
    global url
    url=""
    text_editor.delete(1.0, tk.END)
#Open Function
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File", filetype=(("Text File", "*.txt"), ("All files", "*.*")))
    try:
        with open(url, "r") as f:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, f.read())
    except FileNotFoundError:
        return
    except:
        return
    root.title(os.path.basename(url))
#Save Function
def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0, tk.END))
            with open(url, "w", encoding="utf-8") as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
            content1=text_editor.get(1.0, tk.END)
            url.write(content1)
            url.close()
    except:
        return
#Save As Function
def save_as_file(event=None):
    global url
    try:
        content=text_editor.get(1.0, tk.END)
        url=filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
        url.write(content)
        url.close()
    except:
        return
#Exit Function
def exit(event=None):
    global url
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel("Warning", "Do You Want To Save The File?")
            if mbox is True:
                if url:
                    content=text_editor(1.0, tk.END)
                    with open(url, "w", encoding="utf-8") as f:
                        f.write(content)
                        root.destroy()
                else:
                    content1=str(text_editor.get(1.0, tk.END))
                    filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
                    utl.write(content1)
                    url.close()
                    root.destroy()
            elif mbox is False:
                root.destroy()
        else:
            root.destroy()
    except:
        return        
#Edit Menu
#Find Function
def find_replace(event=None):
    def find():
        word=find_input.get()
        text_editor.tag_remove("match", "1.0", tk.END)
        matches=0
        if word:
            start_pos="1.0"
            while True:
                start_pos=text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match", start_pos, end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config("match", foreground="red", background="yellow")
    def replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0, tk.END)
        new_content=content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)
    find_dialogue=tk.Toplevel()
    find_dialogue.geometry("450x250+500+200")
    find_dialogue.title("Find And Replace")
    find_dialogue.resizable(0,0)
    find_frame=ttk.LabelFrame(find_dialogue, text="Find/Replace")
    find_frame.pack(pady=20)
    find_label=ttk.Label(find_frame, text="Find")
    replace_label=ttk.Label(find_frame, text="Replace")
    find_input=ttk.Entry(find_frame, width=30)
    replace_input=ttk.Entry(find_frame, width=30)
    find_button=ttk.Button(find_frame, text="Find", command=find)
    replace_button=ttk.Button(find_frame, text="Replace", command=replace)
    find_label.grid(row=0, column=0, padx=4, pady=4)
    replace_label.grid(row=1, column=0, padx=4, pady=4)
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)
    find_button.grid(row=2, column=0, padx=8, pady=8)
    replace_button.grid(row=2, column=1, padx=8, pady=8)
    find_dialogue.mainloop()
#View function
#Toolbar 
def toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True
#Statusbar Function
def statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False 
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True
#Color Theme Function
def change():
    choosen_theme=theme_choice.get()
    color_tuple=color_dict.get(choosen_theme)
    fg_color, bg_color=color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)
#Main Menu
main_menu=tk.Menu()
#file Icons
new_icon=tk.PhotoImage(file="icons/new.png")
open_icon=tk.PhotoImage(file="icons/open.png")
save_icon=tk.PhotoImage(file="icons/save.png")
save_as_icon=tk.PhotoImage(file="icons/save_as.png")
exit_icon=tk.PhotoImage(file="icons/exit.png")
file=tk.Menu(main_menu, tearoff=False)
file.add_command(label="New", image=new_icon, compound=tk.LEFT, accelerator="CTRL+N", command=new_file)
file.add_command(label="Open", image=open_icon, compound=tk.LEFT, accelerator="CTRL+O", command=open_file)
file.add_command(label="Save", image=save_icon, compound=tk.LEFT, accelerator="CTRL+S", command=save_file)
file.add_command(label="Save As", image=save_as_icon, compound=tk.LEFT, accelerator="CTRL+ALT+S", command=save_as_file)
file.add_command(label="Exit", image=exit_icon, compound=tk.LEFT, accelerator="CTRL+Q", command=exit)
main_menu.add_cascade(label="File", menu=file)
#Edit Menu
cut_icon=tk.PhotoImage(file="icons/cut.png")
copy_icon=tk.PhotoImage(file="icons/copy.png")
paste_icon=tk.PhotoImage(file="icons/paste.png")
clear_all_icon=tk.PhotoImage(file="icons/clear_all.png")
find_icon=tk.PhotoImage(file="icons/find.png")
edit=tk.Menu(main_menu, tearoff=False)
edit.add_command(label="Cut", image=cut_icon, compound=tk.LEFT, accelerator="CTRL+X", command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="Copy", image=copy_icon, compound=tk.LEFT, accelerator="CTRL+C", command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste", image=paste_icon, compound=tk.LEFT, accelerator="CTRL+V", command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Clear All", image=clear_all_icon, compound=tk.LEFT, accelerator="CTRL+ALT+X",command=lambda:text_editor.delete(1.0, tk.END))
edit.add_command(label="Find & Replace", image=find_icon, compound=tk.LEFT, accelerator="CTRL+F", command=find_replace)
main_menu.add_cascade(label="Edit", menu=edit)
#View Menu
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)
tool_bar_icon=tk.PhotoImage(file="icons/tool_bar.png")
status_bar_icon=tk.PhotoImage(file="icons/status_bar.png")
view=tk.Menu(main_menu, tearoff=False)
view.add_checkbutton(label="Tool Bar", onvalue=True, offvalue=False, variable=show_toolbar, image=tool_bar_icon, compound=tk.LEFT, command=toolbar)
view.add_checkbutton(label="Status Bar", onvalue=True, offvalue=False, variable=show_statusbar, image=status_bar_icon, compound=tk.LEFT, command=statusbar)
main_menu.add_cascade(label="View", menu=view)
#Color Theme
color_theme=tk.Menu(main_menu, tearoff=False)
light_default_icon=tk.PhotoImage(file="icons/light_default.png")
light_plus_icon=tk.PhotoImage(file="icons/light_plus.png")
dark_icon=tk.PhotoImage(file="icons/dark.png")
red_icon=tk.PhotoImage(file="icons/red.png")
monokai_icon=tk.PhotoImage(file="icons/monokai.png")
night_blue_icon=tk.PhotoImage(file="icons/night_blue.png")
theme_choice=tk.StringVar()
color_icons=(light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)
color_dict={
    "Light Default":("#000000", "#ffffff"),
    "Light Plus":("#474747", "#e0e0e0"),
    "Dark":("#c4c4c4", "#2d2d2d"),
    "Red":("#2d2d2d", "#ffe8e8"),
    "Monokai":("#d3b774", "#474747"),
    "Night Blue":("#ededed", "#6b9dc2")
}
count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change)
    count+=1
main_menu.add_cascade(label="Color Theme", menu=color_theme)
#Tool Bar
#Fonts
tool_bar=ttk.Label(root)
tool_bar.pack(side=tk.TOP, fill=tk.X)
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar, width=30, textvariable=font_family, state="readonly")
font_box["values"]=font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0, column=0, padx=5)
#Size Box
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar, width=15, textvariable=size_var, state="readonly")
font_size["values"]=tuple(range(8,100,2))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)
#Bold Button
bold_icon=tk.PhotoImage(file="icons/bold.png")
bold_btn=ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)
#Italic Button
italic_icon=tk.PhotoImage(file="icons/italic.png")
italic_btn=ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)
#Under Line Button
underline_icon=tk.PhotoImage(file="icons/underline.png")
underline_btn=ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)
#Strike Through Button
strike_through_icon=tk.PhotoImage(file="icons/strikethrough.png")
strike_through_btn=ttk.Button(tool_bar, image=strike_through_icon)
strike_through_btn.grid(row=0, column=5, padx=5)
#Font Color Button
font_color_icon=tk.PhotoImage(file="icons/font_color.png")
font_color_btn=ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=6, padx=5)
#Align Left Button
align_left_icon=tk.PhotoImage(file="icons/align_left.png")
align_left_btn=ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=7, padx=5)
#Align Center Button
align_center_icon=tk.PhotoImage(file="icons/align_center.png")
align_center_btn=ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=8, padx=5)
#Align Right Button
align_right_icon=tk.PhotoImage(file="icons/align_right.png")
align_right_btn=ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=9, padx=5)
root.config(menu=main_menu)
#Textarea OR Text Editor
text_editor=tk.Text(root)
text_editor.config(wrap="word", relief=tk.FLAT)
scroll_bar=tk.Scrollbar(root)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
#Status Bar
status_bar=ttk.Label(root, text="Status Bar")
status_bar.pack(side=tk.BOTTOM)
#Creating Functions For Our Application
#Font Family Function
current_font_family="Arial"
current_font_size=12
def change_font(event=None):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))
#Font Size Function
def change_fontsize(event=None):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))
font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)
text_editor.configure(font=("Arial", 12))
#Button's Functions
#Bold Button Function
def change_bold():
    text_bold=tk.font.Font(font=text_editor["font"])
    if text_bold.actual()["weight"]=="normal":
        text_editor.configure(font=(current_font_family, current_font_size, "bold"))
    if text_bold.actual()["weight"]=="bold":
        text_editor.configure(font=(current_font_family, current_font_size, "normal"))
bold_btn.configure(command=change_bold)
#Italic Button Function
def change_italic():
    text_italic=tk.font.Font(font=text_editor["font"])
    if text_italic.actual()["slant"]=="roman":
        text_editor.configure(font=(current_font_family, current_font_size, "italic"))
    if text_italic.actual()["slant"]=="italic":
        text_editor.configure(font=(current_font_family, current_font_size, "normal"))
italic_btn.configure(command=change_italic)
#Underline Button Function
def change_underline():
    text_underline=tk.font.Font(font=text_editor["font"])
    if text_underline.actual()["underline"]==0:
        text_editor.configure(font=(current_font_family, current_font_size, "underline"))
    if text_underline.actual()["underline"]==1:
        text_editor.configure(font=(current_font_family, current_font_size, "normal"))
underline_btn.configure(command=change_underline)
#Strike Through Button Function
def change_strikethrough():
    text_strikethrough=tk.font.Font(font=text_editor["font"])
    if text_strikethrough.actual()["overstrike"]==0:
        text_editor.configure(font=(current_font_family, current_font_size, "overstrike"))
    if text_strikethrough.actual()["overstrike"]==1:
        text_editor.configure(font=(current_font_family, current_font_size,"normal"))
strike_through_btn.configure(command=change_strikethrough)
#Change Font Color Function
def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
font_color_btn.configure(command=change_font_color)
#Left Allignment Function
def left_align():
    text_content=text_editor.get(1.0, "end")
    text_editor.tag_config("left", justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "left")
align_left_btn.configure(command=left_align)
#Center Allignment Function
def center_align():
    text_content=text_editor.get(1.0, "end")
    text_editor.tag_config("center", justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "center")
align_center_btn.configure(command=center_align)
#Right Allignment Function
def right_align():
    text_content=text_editor.get(1.0, "end")
    text_editor.tag_config("right", justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "right")
align_right_btn.configure(command=right_align)
#Status Bar Function
text_changed=False
def change_status(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0, "end-1c").split())
        characters=len(text_editor.get(1.0, "end-1c"))#If don't want to count spaces use:-.replace(" ", "")
        status_bar.config(text=f"Characters: {characters} Words: {words}")
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>", change_status)
#Bind Short Cut Keys Functions
root.bind("<Control-n>", new_file)
root.bind("<Control-o>", open_file)
root.bind("<Control-s>", save_file)
root.bind("<Control-Alt-s>", save_as_file)
root.bind("<Control-q>", exit)
root.bind("<Control-f>", find_replace)
root.mainloop()