#import
from tkinter import *
import urllib.parse
import webbrowser

#drop down option list
base_type_options=[
    "svg",
    "audio",
    "mixed",
    "video",
    "png"
    ]

#window
form = Tk()
form.geometry("900x650")
form.resizable(False, False)
form.iconbitmap("TNA.ico")
form.title("BASE CODE OG - Offline Generator for RMRK2 BASE-Codes")
form.configure(background="#ffffff")

#headers
basic_input = Label(text="Basic Input:", bg="#030896", fg="#ffffff", width="750", height="1", font=(None, 10, "bold"))
basic_input.pack()
base_parts = Label(text="Create base parts:", anchor="center", bg="#030896", fg="#ffffff", height="1", font=(None, 10, "bold"))
base_parts.place(y=130, relwidth=1.0)
themes_header = Label(text="Themes:", bg="#030896", fg="#ffffff", width="750", height="1", font=(None, 10, "bold"))
save_header = Label(text="Save:", bg="#030896", fg="#ffffff", width="750", height="1", font=(None, 10, "bold"))

#methods
def display():
    part_id_text.place(x=20, y=220)
    part_z_text.place(x=20, y=280)
    part_equippable_text.place(x=20, y=400)
    part_id_box.place(x=25, y=250)
    part_z_box.place(x=25, y=310)
    part_src_box.place(x=25, y=370)
    part_equippable_box.place(x=25, y=430)

def display_fixed():
    display()

    part_src_text.config(text="Input picture cid (eg.: QmR3rK1P4n24PPqvfjGYNXWixPJpyBKTV6rYzAS2TYHLpT):")
    part_src_text.place(x=20, y=340)
    
    part_id_box.delete(0, END)
    part_z_box.delete(0, END)
    part_src_box.delete(0, END)
    part_equippable_box.delete(0, END)
    error_text.place_forget()
    
    part_equippable_box.configure(state="disabled")
    
    part_type.set("fixed")

def display_slot():
    display()

    part_src_text.config(text="Input fallback cid (Optional) (eg.: QmR3rK1P4n24PPqvfjGYNXWixPJpyBKTV6rYzAS2TYHLpT):")
    part_src_text.place(x=20, y=340)
    
    part_id_box.delete(0, END)
    part_z_box.delete(0, END)
    part_src_box.delete(0, END)
    part_equippable_box.delete(0, END)
    error_text.place_forget()
    
    part_equippable_box.configure(state="normal")
    
    part_type.set("slot")

def add_part():
    if ((issuer.get()==(""))or(base_symbol.get()==(""))or(part_id.get()==(""))or(part_z.get()==(""))or((part_type.get()==("fixed"))and(part_src.get()==("")))):
        error_text.place(x=90, y=472)
    else:
        name_n=len(part_name_list)
        
        error_text.place_forget()
        
        done_button.configure(state="normal")
        
        if (name_n!=0):
            part_list.append(",")
            
        if (part_type.get()=="fixed"):
            part_list.append("{\"type\":\""+part_type.get()+"\",\"id\":\""+part_id.get()+"\",\"z\":"+part_z.get()+",\"src\":\"ipfs://ipfs/"+part_src.get()+"\"}")
            fixed_frame_text.configure(state="normal")
            fixed_frame_text.insert(END,part_z.get()+" - "+part_id.get()+"\n")
            fixed_frame_text.configure(state="disabled")
            
        elif (part_type.get()=="slot"):
            x=part_equippable.get()
            x=x.replace(",", "\", \"")
            part_equippable.set(x)
            slot_frame_text.configure(state="normal")
            slot_frame_text.insert(END,part_z.get()+" - "+part_id.get()+"\n")
            slot_frame_text.configure(state="disabled")
                
            if (part_src.get()!=("")):
                part_list.append("{\"type\":\""+part_type.get()+"\",\"id\":\""+part_id.get()+"\",\"z\":"+part_z.get()+",\"src\":\"ipfs://ipfs/"+part_src.get()+"\",\"equippable\":[\""+part_equippable.get()+"\"]}")
                
            else:
                part_list.append("{\"type\":\""+part_type.get()+"\",\"id\":\""+part_id.get()+"\",\"z\":"+part_z.get()+",\"equippable\":[\""+part_equippable.get()+"\"]}")
                
        if (name_n==0):
            part_name_list.append("\""+part_id.get()+"\"")
            
        else:
            part_name_list.append(", \""+part_id.get()+"\"")

        part_number.set(name_n+1)

        part_id_box.delete(0, END)
        part_z_box.delete(0, END)
        part_src_box.delete(0, END)
        part_equippable_box.delete(0, END)

def done():
    basic_input.pack_forget()
    base_parts.place_forget()
    
    issuer_text.place_forget()
    base_type_text.place_forget()
    base_symbol_text.place_forget()
    part_id_text.place_forget()
    part_z_text.place_forget()
    part_equippable_text.place_forget()
    part_src_text.place_forget()

    fixed_button.place_forget()
    slot_button.place_forget()
    add_part_button.place_forget()
    done_button.place_forget()

    part_number_text.place_forget()
    part_number_string.place_forget()

    fixed_frame.place_forget()
    slot_frame.place_forget()
    
    issuer_box.place_forget()
    base_type_box.place_forget()
    base_symbol_box.place_forget()
    part_id_box.place_forget()
    part_z_box.place_forget()
    part_src_box.place_forget()
    part_equippable_box.place_forget()

    error_text.place_forget()

    themes_header.pack()

    theme_name_text.place(x=20, y=45)
    theme_attr_1_text.place(x=20, y=105)
    theme_attr_2_text.place(x=20, y=165)
    theme_attr_3_text.place(x=20, y=225)
    theme_val_1_text.place(x=295, y=105)
    theme_val_2_text.place(x=295, y=165)
    theme_val_3_text.place(x=295, y=225)

    theme_name_box.place(x=25, y=75)
    theme_attr_1_box.place(x=25, y=135)
    theme_attr_2_box.place(x=25, y=195)
    theme_attr_3_box.place(x=25, y=255)
    theme_val_1_box.place(x=300, y=135)
    theme_val_2_box.place(x=300, y=195)
    theme_val_3_box.place(x=300, y=255)

    theme_number_text.place(x=350, y=45)
    theme_number_string.place(x=530, y=45)

    theme_frame.place(x=700,y=40)
    scrollbar_theme.pack(side=RIGHT,fill=Y)
    theme_frame_text.pack(anchor="w")
    theme_frame.pack_propagate(False)

    add_theme_button.place(x=25, y=295)
    finish_button.place(x=25, y=340, height=50, width=90)

def add_theme():
    if ((theme_name.get()==(""))or((theme_attr_1.get()==(""))and(theme_attr_2.get()==(""))and(theme_attr_3.get()==("")))):
        theme_error_text.place(x=110, y=297)
    else:
        theme_error_text.place_forget()

        if not theme_list:
            theme_string.set("],\"themes\":{\"default\":{")
            theme_name_box.configure(state="normal")
        else:
            theme_string.set(",\""+theme_name.get()+"\":{")

        if (theme_attr_1.get()!=("")):
            theme_string.set(theme_string.get()+"\""+theme_attr_1.get()+"\":\""+theme_val_1.get()+"\"")
            if (theme_attr_2.get()!=("")):
                theme_string.set(theme_string.get()+",\""+theme_attr_2.get()+"\":\""+theme_val_2.get()+"\"")
            if (theme_attr_3.get()!=("")):
                theme_string.set(theme_string.get()+",\""+theme_attr_3.get()+"\":\""+theme_val_3.get()+"\"")
        elif (theme_attr_2.get()!=("")):
            theme_string.set(theme_string.get()+"\""+theme_attr_2.get()+"\":\""+theme_val_2.get()+"\"")
            if (theme_attr_3.get()!=("")):
                theme_string.set(theme_string.get()+",\""+theme_attr_3.get()+"\":\""+theme_val_3.get()+"\"")
        else:
            theme_string.set(theme_string.get()+"\""+theme_attr_3.get()+"\":\""+theme_val_3.get()+"\"")
        theme_string.set(theme_string.get()+"}")

        theme_list.append(theme_string.get())

        theme_number.set(len(theme_list))
    
        theme_frame_text.configure(state="normal")
        theme_frame_text.insert(END,theme_name.get()+"\n")
        theme_frame_text.configure(state="disabled")

        theme_name_box.delete(0, END)
        theme_attr_1_box.delete(0, END)
        theme_attr_2_box.delete(0, END)
        theme_attr_3_box.delete(0, END)
        theme_val_1_box.delete(0, END)
        theme_val_2_box.delete(0, END)
        theme_val_3_box.delete(0, END)

def finish():
    themes_header.pack_forget()
    
    theme_name_text.place_forget()
    theme_attr_1_text.place_forget()
    theme_attr_2_text.place_forget()
    theme_attr_3_text.place_forget()
    theme_val_1_text.place_forget()
    theme_val_2_text.place_forget()
    theme_val_3_text.place_forget()

    theme_name_box.place_forget()
    theme_attr_1_box.place_forget()
    theme_attr_2_box.place_forget()
    theme_attr_3_box.place_forget()
    theme_val_1_box.place_forget()
    theme_val_2_box.place_forget()
    theme_val_3_box.place_forget()

    theme_number_text.place_forget()
    theme_number_string.place_forget()
    theme_frame.place_forget()

    add_theme_button.place_forget()
    finish_button.place_forget()

    theme_error_text.place_forget()

    name_n=len(part_name_list)

    json_base.set("{\"symbol\":\""+base_symbol.get()+"\",\"type\":\""+base_type.get()+"\",\"issuer\":\""+issuer.get()+"\",\"parts\":[")
    for i in range((2*(name_n))-1):
        json_base.set(json_base.get()+part_list[i])

    if not theme_list:
        json_base.set(json_base.get()+"]}")
    else:
        for i in range(len(theme_list)):
            json_base.set(json_base.get()+theme_list[i])
        json_base.set(json_base.get()+"}}")

    for i in range(name_n):
        name_output.set(name_output.get()+part_name_list[i])
    
    json_output.set("RMRK::BASE::2.0.0::"+json_base.get())
    url_output.set(urllib.parse.quote_plus(json_base.get()))
    url_output.set("RMRK::BASE::2.0.0::"+url_output.get())

    save_header.pack()

    json_save_text.place(x=30, y=50)
    url_save_text.place(x=30, y=110)
    name_save_text.place(x=30, y=170)
    
    json_name_box.place(x=35, y=80)
    url_name_box.place(x=35, y=140)
    name_name_box.place(x=35, y=200)
    
    json_save_button.place(x=535, y=76)
    url_save_button.place(x=535, y=136)
    name_save_button.place(x=535, y=196)

def save_json():
    if (json_name.get()==""):
        no_json_name.place(x=605, y=77)
        saved_json.place_forget()
    else:
        no_json_name.place_forget()
        with open(json_name.get()+".txt", "w") as json_file:
            json_file.write(json_output.get())
        saved_json.place(x=605, y=77)
        
def save_url():
    if (url_name.get()==""):
        no_url_name.place(x=605, y=137)
        saved_url.place_forget()
    else:
        no_url_name.place_forget()
        with open(url_name.get()+'.txt', 'w') as url_file:
            url_file.write(url_output.get())
        saved_url.place(x=605, y=137)
        
def save_name():
    if (name_name.get()==""):
        no_name_name.place(x=640, y=197)
        saved_name.place_forget()
    else:
        no_name_name.place_forget()
        with open(name_name.get()+'.txt', 'w') as name_file:
            name_file.write(name_output.get())
        saved_name.place(x=640, y=197)

def open_url(url):
    webbrowser.open_new(url)

#variables
issuer=StringVar()
base_type=StringVar()
base_type.set(base_type_options[0])
base_symbol=StringVar()
part_type=StringVar()
part_id=StringVar()
part_z=StringVar()
part_src=StringVar()
part_equippable=StringVar()

part_name_list=[]
name_n=len(part_name_list)
part_list=[]
part_number=IntVar()
part_number.set(0)

theme_name=StringVar()
theme_name.set("default")
theme_attr_1=StringVar()
theme_attr_2=StringVar()
theme_attr_3=StringVar()
theme_val_1=StringVar()
theme_val_2=StringVar()
theme_val_3=StringVar()

theme_string=StringVar()
theme_list=[]
theme_number=IntVar()
theme_number.set(0)

json_base=StringVar()
json_output=StringVar()
url_output=StringVar()
name_output=StringVar()

json_name=StringVar()
url_name=StringVar()
name_name=StringVar()

#print text
issuer_text=Label(text="Input Issuer:", bg="#ffffff")
base_type_text=Label(text="Choose base type:", bg="#ffffff")
base_symbol_text=Label(text="Input base name:", bg="#ffffff")
part_id_text=Label(text="Input part name:", bg="#ffffff")
part_z_text=Label(text="Input z index:", bg="#ffffff")
part_equippable_text=Label(text="Input equippable collection id (Multiple collections ONLY seperated by a comma):", bg="#ffffff")
part_src_text=Label(text="", bg="#ffffff")

theme_name_text=Label(text="Theme name:", bg="#ffffff")
theme_attr_1_text=Label(text="Theme attribute 1:", bg="#ffffff")
theme_attr_2_text=Label(text="Theme attribute 2:", bg="#ffffff")
theme_attr_3_text=Label(text="Theme attribute 3:", bg="#ffffff")
theme_val_1_text=Label(text="Attribute 1 value:", bg="#ffffff")
theme_val_2_text=Label(text="Attribute 2 value:", bg="#ffffff")
theme_val_3_text=Label(text="Attribute 3 value:", bg="#ffffff")

json_save_text=Label(text="Input filename for .txt file containing the minified json:", bg="#ffffff")
url_save_text=Label(text="Input filename for .txt file containing the url encoded base:", bg="#ffffff")
name_save_text=Label(text="Input filename for .txt file containing the list of parts:", bg="#ffffff")

#auto update print
part_number_text=Label(text="Current number of parts: ", bg="#ffffff")
part_number_string=Label(textvariable=part_number, bg="#ffffff")

fixed_frame=LabelFrame(form, text="Fixed", width = 175, height = 390, borderwidth=1, relief="sunken", bg="#ffffff")
slot_frame=LabelFrame(form, text="Slot", width = 175, height = 390, borderwidth=1, relief="sunken", bg="#ffffff")
scrollbar_fix = Scrollbar(fixed_frame)
scrollbar_slot = Scrollbar(slot_frame)
fixed_frame_text=Text(fixed_frame, width = 175, height = 390, font="lucida 10", state="disabled")
slot_frame_text=Text(slot_frame, width = 175, height = 390, font="lucida 10", state="disabled")

theme_number_text=Label(text="Current number of themes: ", bg="#ffffff")
theme_number_string=Label(textvariable=theme_number, bg="#ffffff")

theme_frame=LabelFrame(form, text="Theme", width = 200, height = 540, borderwidth=1, relief="sunken", bg="#ffffff")
scrollbar_theme = Scrollbar(theme_frame)
theme_frame_text=Text(theme_frame, width = 200, height = 540, font="lucida 10", state="disabled")

#checks
error_text=Label(text="MISSING INPUT", fg="red", bg="#ffffff")

theme_error_text=Label(text="MISSING INPUT", fg="red", bg="#ffffff")

no_json_name=Label(text="INPUT FILENAME", fg="red", bg="#ffffff")
no_url_name=Label(text="INPUT FILENAME", fg="red", bg="#ffffff")
no_name_name=Label(text="INPUT FILENAME", fg="red", bg="#ffffff")

saved_json=Label(text="SAVED", fg="green", bg="#ffffff")
saved_url=Label(text="SAVED", fg="green", bg="#ffffff")
saved_name=Label(text="SAVED", fg="green", bg="#ffffff")

#hyperlink
sign_text=Label(text="Created by: ", bg="#ffffff")
hyperlink_text=Label(text="Tricky-NFT.art", bg="#ffffff", fg="#030896", cursor="hand2")
hyperlink_text.bind("<ButtonRelease-1>", lambda e: open_url("http://www.Tricky-NFT.art"))

#input boxes
issuer_box=Entry(textvariable=issuer, width="80", bg="#ffffff", selectbackground="#030896")
base_type_box=OptionMenu(form, base_type, *base_type_options)
base_type_box.config(activebackground="#c1c1c1", bg="#c1c1c1", relief="groove", highlightthickness=0)
base_type_box["menu"].config(bg="#ffffff", activebackground="#030896")
base_symbol_box=Entry(textvariable=base_symbol, width="80", bg="#ffffff", selectbackground="#030896")
part_id_box=Entry(textvariable=part_id, width="80", bg="#ffffff", selectbackground="#030896")
part_z_box=Entry(textvariable=part_z, width="10", bg="#ffffff", selectbackground="#030896")
part_src_box=Entry(textvariable=part_src, width="80", bg="#ffffff", selectbackground="#030896")
part_equippable_box=Entry(textvariable=part_equippable, width="80", bg="#ffffff", selectbackground="#030896")

theme_name_box=Entry(textvariable=theme_name, width="40", bg="#ffffff", selectbackground="#030896", state="disabled")
theme_attr_1_box=Entry(textvariable=theme_attr_1, width="40", bg="#ffffff", selectbackground="#030896")
theme_attr_2_box=Entry(textvariable=theme_attr_2, width="40", bg="#ffffff", selectbackground="#030896")
theme_attr_3_box=Entry(textvariable=theme_attr_3, width="40", bg="#ffffff", selectbackground="#030896")
theme_val_1_box=Entry(textvariable=theme_val_1, width="40", bg="#ffffff", selectbackground="#030896")
theme_val_2_box=Entry(textvariable=theme_val_2, width="40", bg="#ffffff", selectbackground="#030896")
theme_val_3_box=Entry(textvariable=theme_val_3, width="40", bg="#ffffff", selectbackground="#030896")

json_name_box=Entry(textvariable=json_name, width="80", bg="#ffffff", selectbackground="#030896")
url_name_box=Entry(textvariable=url_name, width="80", bg="#ffffff", selectbackground="#030896")
name_name_box=Entry(textvariable=name_name, width="80", bg="#ffffff", selectbackground="#030896")

#buttons
fixed_button=Button(text="Fixed part", command=lambda:display_fixed(), bg="#c1c1c1")
slot_button=Button(text="Slot part", command=lambda:display_slot(), bg="#c1c1c1")
add_part_button=Button(text="Add part", command=lambda:add_part(), bg="#c1c1c1")
done_button=Button(text="Done", state="disabled", command=lambda:done(), bg="#c1c1c1")

add_theme_button=Button(text="Add theme", command=lambda:add_theme(), bg="#c1c1c1")
finish_button=Button(text="Finish", command=lambda:finish(), bg="#c1c1c1")

json_save_button=Button(text="Save json", command=lambda:save_json(), bg="#c1c1c1")
url_save_button=Button(text="Save url", command=lambda:save_url(), bg="#c1c1c1")
name_save_button=Button(text="Save part names", command=lambda:save_name(), bg="#c1c1c1")

#placement
issuer_text.place(x=20, y=35)
base_type_text.place(x=20, y=65)
base_symbol_text.place(x=20, y=95)

issuer_box.place(x=200, y=35)
base_type_box.place(x=200, y=61)
base_symbol_box.place(x=200, y=95)

fixed_button.place(x=270, y=175)
slot_button.place(x=400, y=175)
add_part_button.place(x=25, y=470)
done_button.place(x=25, y=515, height=50, width=90)

part_number_text.place(x=530, y=178)
part_number_string.place(x=690, y=178)

fixed_frame.place(x=530,y=230)
slot_frame.place(x=715,y=230)
scrollbar_fix.pack(side=RIGHT,fill=Y)
scrollbar_slot.pack(side=RIGHT,fill=Y)
fixed_frame_text.pack(anchor="w")
slot_frame_text.pack(anchor="w")
fixed_frame.pack_propagate(False) 
slot_frame.pack_propagate(False)

sign_text.place(x=745, y=624)
hyperlink_text.place(x=810, y=624)

mainloop()
