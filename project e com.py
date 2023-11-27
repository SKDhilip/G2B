
from tkinter import *
from tkinter import messagebox
import PIL as p
import PIL.ImageTk as ptk
import os
from datetime import datetime


root=Tk()
root.title("AAVIN - G2B Model")
root.geometry("1360x1000")
Heading=LabelFrame(root,bd=2,font="times 18 bold",relief="solid",bg="light sky blue")
Heading.place(x=0,y=0,width=1380,height=55)

image_logo_tn=p.Image.open("images\logotn.png")
image_logo_tn1=ptk.PhotoImage(image_logo_tn)
label_logo_tn=Label(Heading,image=image_logo_tn1)
label_logo_tn.grid(row=0,column=0)

image_logo_large=ptk.PhotoImage(p.Image.open("Images\logolarge.jpg"))


name=Label(Heading,text="AAVIN - G2B Model",font="times 30 bold",bg="light sky blue",fg="white").place(x=560,y=0)
Products_frame=LabelFrame(root,bd=2,relief="groove",text="Products",font="arial 16 bold",fg="dark blue")
Products_frame.place(x=310,y=60,width=1040,height=620)
label_logo_large=Label(Products_frame,image=image_logo_large,bd=2).place(x=50,y=15)
label_enjoy=Label(Products_frame,text="Enjoy Shopping",font="castellar 20 bold").place(x=370,y=528)
Button_frame=LabelFrame(root,bd=2,relief="groove")
Button_frame.place(x=2,y=60,width=300,height=380)


milk1_image=ptk.PhotoImage(p.Image.open("Images\milk1.jpg"))
milk2_image=ptk.PhotoImage(p.Image.open("Images\milk2.jpg"))
milk3_image=ptk.PhotoImage(p.Image.open("Images\milk3.jpg"))
milk4_image=ptk.PhotoImage(p.Image.open("Images\milk4.jpg"))

icecream1_image=ptk.PhotoImage(p.Image.open("Images\icecream1.jpg"))
icecream2_image=ptk.PhotoImage(p.Image.open("Images\icecream2.jpg"))
icecream3_image=ptk.PhotoImage(p.Image.open("Images\icecream3.jpg"))
icecream4_image=ptk.PhotoImage(p.Image.open("Images\icecream4.jpg"))
icecream5_image=ptk.PhotoImage(p.Image.open("Images\icecream5.jpg"))
icecream6_image=ptk.PhotoImage(p.Image.open("Images\icecream6.jpg"))
icecream7_image=ptk.PhotoImage(p.Image.open("Images\icecream7.jpg"))
icecream8_image=ptk.PhotoImage(p.Image.open("Images\icecream8.jpg"))


#milk pockets variables
clicked_milk1=StringVar()
clicked_milk1.set("220ml - Rs.11")
clicked_milk2=StringVar()
clicked_milk2.set("500ml - Rs.20")
clicked_milk3=StringVar()
clicked_milk3.set("500ml - Rs.19")
clicked_milk4=StringVar()
clicked_milk4.set("500ml - Rs.30")
milk_list=[]




#ice creams variables
clicked_icecream1=StringVar()
clicked_icecream1.set("125ml - Rs.40")
clicked_icecream2=StringVar()
clicked_icecream2.set("125ml - Rs.45")
clicked_icecream3=StringVar()
clicked_icecream3.set("125ml - Rs.45")
clicked_icecream4=StringVar()
clicked_icecream4.set("125ml - Rs.40")
clicked_icecream5=StringVar()
clicked_icecream5.set("10g - Rs.25")
clicked_icecream6=StringVar()
clicked_icecream6.set("10g- Rs.35")
clicked_icecream7=StringVar()
clicked_icecream7.set("10g - Rs.30")
clicked_icecream8=StringVar()
clicked_icecream8.set("10g - Rs.45")
icecream_list=[]



def save_invoice(text):
    op=messagebox.askyesno("Invoice Saving Confirmation","Do you want to save the invoice in a file?")
    if op:
        t=datetime.now()
        s=str(t.day)+str(t.month)+str(t.year)+str(t.hour)+str(t.minute)+str(t.second)
        f=open("Invoices/"+s+".txt","w")
        f.write(text)
        f.close()
        messagebox.showinfo("Invoice Saving Status","Invoice is saved successfully as a text document with name "+s+".txt")
    else:
        messagebox.showinfo("Invoice Saving Status","The invoice is not saved into a file.")
def HideAllFrames():
    for widget in Products_frame.winfo_children():
        widget.destroy()
def Spaces(n,s1=" "):
    s=""
    for i in range(n):
        s+=s1
    return s




def MilkCall():
    HideAllFrames()
    Milk_Label=Label(Products_frame,text="Milk",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)
    
    lf_milk1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_milk1.place(x=5,y=35,width=180,height=280)
    lf_milk2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_milk2.place(x=210,y=35,width=180,height=280)
    lf_milk3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_milk3.place(x=415,y=35,width=180,height=280)
    lf_milk4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_milk4.place(x=620,y=35,width=180,height=280)


    label_milk_1=Label(lf_milk1,image=milk1_image,bd=2).grid(row=0,column=0)
    label_milk_2=Label(lf_milk2,image=milk2_image,bd=2).grid(row=0,column=0)
    label_milk_3=Label(lf_milk3,image=milk3_image,bd=2).grid(row=0,column=0)
    label_milk_4=Label(lf_milk4,image=milk4_image,bd=2).grid(row=0,column=0)
    
    
    name_milk1=Label(lf_milk1,text="Standized - Green",font="arial 9 bold").grid(row=1,column=0)
    name_milk2=Label(lf_milk2,text="Toned - Blue",font="arial 9 bold",justify="center").grid(row=1,column=0,padx=15)
    name_milk3=Label(lf_milk3,text="DoubleToned - Magenta",font="arial 9 bold",justify="center").grid(row=1,column=0)
    name_milk4=Label(lf_milk4,text="FullCream - Orange",font="arial 9 bold",justify="center").grid(row=1,column=0,padx=9)
    
    label_qty_milk1=Label(lf_milk1,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_milk2=Label(lf_milk2,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_milk3=Label(lf_milk3,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_milk4=Label(lf_milk4,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)

    
    options_milk1=["220ml - Rs.11","500ml - Rs.22","5L - Rs.210"]
    options_milk2=["500ml - Rs.20","1L - Rs.40"]
    options_milk3=["500ml - Rs.19"]
    options_milk4=["500ml - Rs.30"]
    
    global clicked_milk1,clicked_milk2,clicked_milk3,clicked_milk4
    drop_milk1=OptionMenu(lf_milk1,clicked_milk1,*options_milk1).place(x=30,y=212)
    drop_milk2=OptionMenu(lf_milk2,clicked_milk2,*options_milk2).place(x=30,y=212)
    drop_milk3=OptionMenu(lf_milk3,clicked_milk3,*options_milk3).place(x=30,y=212)
    drop_milk4=OptionMenu(lf_milk4,clicked_milk4,*options_milk4).place(x=30,y=212)
    

    def MilkPrice(s):
        s1=""
        for i in range(len(s)-1,0,-1):
            if s[i]!='.':
                s1=s1+s[i]
            else:
                break
        return int(s1[::-1])
    def MilkQty(s):
        s1=""
        for i in range(len(s)):
            s1=s1+s[i]
            if s[i]=='g' or s[i]=='L':
                break
        return s1

    def AddM1():
        global milk_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            milk_list.append(["Standized",MilkPrice(clicked_milk1.get()),MilkQty(clicked_milk1.get()),Spaces(40-len("Standized"))])
            messagebox.showinfo("Product Status","Standized - Diet ("+clicked_milk1.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Standized - Diet("+clicked_milk1.get()+") is not added to the cart.")

    add_milk1=Button(lf_milk1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddM1).place(x=60,y=245)

    def AddM2():
        global milk_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            milk_list.append(["Toned",MilkPrice(clicked_milk2.get()),MilkQty(clicked_milk2.get()),Spaces(40-len("Toned"))])
            messagebox.showinfo("Product Status","Toned - Blue ("+clicked_milk2.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Toned - Blue ("+clicked_milk2.get()+") is not added to the cart.")

    add_milk2=Button(lf_milk2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddM2).place(x=60,y=245)

    def AddM3():
        global milk_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            milk_list.append(["DoubleToned",MilkPrice(clicked_milk3.get()),MilkQty(clicked_milk3.get()),Spaces(40-len("DoubleToned"))])
            messagebox.showinfo("Product Status","DoubleToned - Magenta ("+clicked_milk3.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","DoubleToned - Magenta ("+clicked_milk3.get()+") is not added to the cart.")

    add_milk3=Button(lf_milk3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddM3).place(x=60,y=245)

    def AddM4():
        global milk_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            milk_list.append(["FullCream",MilkPrice(clicked_milk4.get()),MilkQty(clicked_milk4.get()),Spaces(40-len("FullCream"))])
            messagebox.showinfo("Product Status","DoubleToned - FullCream ("+clicked_milk4.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","DoubleToned - FullCream ("+clicked_milk4.get()+") is not added to the cart.")

    add_milk3=Button(lf_milk4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddM4).place(x=60,y=245)
    

    







#IceCreamCall
#---------------

def IceCreamCall():
    HideAllFrames()
    IceCream_Label=Label(Products_frame,text="IceCream",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=10)
    
    lf_icecream1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_icecream1.place(x=5,y=35,width=180,height=280)
    lf_icecream2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_icecream2.place(x=210,y=35,width=180,height=280)
    lf_icecream3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_icecream3.place(x=415,y=35,width=180,height=280)
    lf_icecream4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_icecream4.place(x=620,y=35,width=180,height=280)
    lf_icecream5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_icecream5.place(x=825,y=35,width=180,height=280)
    
    lf_icecream6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_icecream6.place(x=5,y=310,width=180,height=280)
    lf_icecream7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_icecream7.place(x=210,y=310,width=180,height=280)
    lf_icecream8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_icecream8.place(x=415,y=310,width=180,height=280)


    label_icecream_1=Label(lf_icecream1,image=icecream1_image,bd=2,justify="center").grid(row=0,column=0)
    label_icecream_2=Label(lf_icecream2,image=icecream2_image,bd=2,justify="center").grid(row=0,column=0)
    label_icecream_3=Label(lf_icecream3,image=icecream3_image,bd=2,justify="center").grid(row=0,column=0)
    label_icecream_4=Label(lf_icecream4,image=icecream4_image,bd=2,justify="center").grid(row=0,column=0)
    label_icecream_5=Label(lf_icecream5,image=icecream5_image,bd=2,justify="center").grid(row=0,column=0)
    label_icecream_6=Label(lf_icecream6,image=icecream6_image,bd=2,justify="center").grid(row=0,column=0)
    label_icecream_7=Label(lf_icecream7,image=icecream7_image,bd=2,justify="center").grid(row=0,column=0)
    label_icecream_8=Label(lf_icecream8,image=icecream8_image,bd=2,justify="center").grid(row=0,column=0)
    
    
    name_icecream1=Label(lf_icecream1,text="Litchi",font="arial 9 bold").grid(row=1,column=0)
    name_icecream2=Label(lf_icecream2,text="BlackCurrant",font="arial 9 bold",justify="center").grid(row=1,column=0)      #padx not given
    name_icecream3=Label(lf_icecream3,text="Chocolate",font="arial 9 bold",justify="center").grid(row=1,column=0)
    name_icecream4=Label(lf_icecream4,text="Butterscotch",font="arial 9 bold",justify="center").grid(row=1,column=0)
    name_icecream5=Label(lf_icecream5,text="KulfiBar",font="arial 9 bold").grid(row=1,column=0)
    name_icecream6=Label(lf_icecream6,text="Kulfi - SugarFree",font="arial 9 bold",justify="center").grid(row=2,column=0)      #padx not given
    name_icecream7=Label(lf_icecream7,text="Cone",font="arial 9 bold",justify="center").grid(row=2,column=0)
    name_icecream8=Label(lf_icecream8,text="Casatta",font="arial 9 bold",justify="center").grid(row=2,column=0)


    
    
    label_qty_icecream1=Label(lf_icecream1,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_icecream2=Label(lf_icecream2,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_icecream3=Label(lf_icecream3,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_icecream4=Label(lf_icecream4,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_icecream5=Label(lf_icecream5,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_icecream6=Label(lf_icecream6,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_icecream7=Label(lf_icecream7,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_icecream8=Label(lf_icecream8,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)

    #yet to complete    
    options_icecream1=["125ml - Rs.40","250ml - Rs.70","500ml - Rs.125"]
    options_icecream2=["125ml - Rs.45","250ml - Rs.75","500ml - Rs.135"]
    options_icecream3=["125ml - Rs.45","250ml - Rs.80","500ml - Rs.145"]
    options_icecream4=["125ml - Rs.40","250ml - Rs.70","500ml - Rs.125"]
    options_icecream5=["10g - Rs.25"]
    options_icecream6=["7g - Rs.35"]
    options_icecream7=["10g - Rs.30"]
    options_icecream8=["10g - Rs.45"]
    
    global clicked_icecream1,clicked_icecream2,clicked_icecream3,clicked_icecream4,clicked_icecream5
    global clicked_icecream6,clicked_icecream7,clicked_icecream8
    drop_icecream1=OptionMenu(lf_icecream1,clicked_icecream1,*options_icecream1).place(x=30,y=212)
    drop_icecream2=OptionMenu(lf_icecream2,clicked_icecream2,*options_icecream2).place(x=30,y=212)
    drop_icecream3=OptionMenu(lf_icecream3,clicked_icecream3,*options_icecream3).place(x=30,y=212)
    drop_icecream4=OptionMenu(lf_icecream4,clicked_icecream4,*options_icecream4).place(x=30,y=212)
    drop_icecream5=OptionMenu(lf_icecream5,clicked_icecream5,*options_icecream5).place(x=30,y=212)
    drop_icecream6=OptionMenu(lf_icecream6,clicked_icecream6,*options_icecream6).place(x=30,y=212)
    drop_icecream7=OptionMenu(lf_icecream7,clicked_icecream7,*options_icecream7).place(x=30,y=212)
    drop_icecream8=OptionMenu(lf_icecream8,clicked_icecream8,*options_icecream8).place(x=30,y=212)
    

    def IcecreamPrice(s):
        s1=""
        for i in range(len(s)-1,0,-1):
            if s[i]!='.':
                s1=s1+s[i]
            else:
                break
        return int(s1[::-1])
    def IcecreamQty(s):
        s1=""
        for i in range(len(s)):
            s1=s1+s[i]
            if s[i]=='g' or s[i]=='L':
                break
        return s1

    def AddI1():
        global icecream_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            icecream_list.append(["Litchi",IcecreamPrice(clicked_icecream1.get()),IcecreamQty(clicked_icecream1.get()),Spaces(40-len("Litchi"))])
            messagebox.showinfo("Product Status","Litchi ("+clicked_icecream1.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Litchi("+clicked_icecream1.get()+") is not added to the cart.")

    add_icecream1=Button(lf_icecream1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddI1).place(x=68,y=245)

    def AddI2():
        global icecream_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            icecream_list.append(["BlackCurrant",IcecreamPrice(clicked_icecream2.get()),IcecreamQty(clicked_icecream2.get()),Spaces(40-len("BlackCurrant"))])
            messagebox.showinfo("Product Status","BlackCurrant ("+clicked_icecream2.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","BlackCurrant ("+clicked_icecream2.get()+") is not added to the cart.")

    add_icecream2=Button(lf_icecream2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddI2).place(x=68,y=245)

    def AddI3():
        global icecream_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            icecream_list.append(["Chocolate",IcecreamPrice(clicked_icecream3.get()),IcecreamQty(clicked_icecream3.get()),Spaces(40-len("Chocolate"))])
            messagebox.showinfo("Product Status","Chocolate ("+clicked_icecream3.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Chocolate ("+clicked_icecream3.get()+") is not added to the cart.")

    add_icecream3=Button(lf_icecream3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddI3).place(x=68,y=245)


    def AddI4():
        global icecream_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            icecream_list.append(["Butterscotch",IcecreamPrice(clicked_icecream4.get()),IcecreamQty(clicked_icecream4.get()),Spaces(40-len("Butterscotch"))])
            messagebox.showinfo("Product Status","Butterscotch ("+clicked_icecream4.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Butterscotch ("+clicked_icecream4.get()+") is not added to the cart.")

    add_icecream4=Button(lf_icecream4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddI4).place(x=68,y=245)


    def AddI5():
        global icecream_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            icecream_list.append(["KulfiBar",IcecreamPrice(clicked_icecream5.get()),IcecreamQty(clicked_icecream5.get()),Spaces(40-len("KulfiBar"))])
            messagebox.showinfo("Product Status","KulfiBar ("+clicked_icecream5.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","KulfiBar ("+clicked_icecream5.get()+") is not added to the cart.")

    add_icecream5=Button(lf_icecream5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddI5).place(x=68,y=245)


    def AddI6():
        global icecream_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            icecream_list.append(["Kulfi Sugarfree",IcecreamPrice(clicked_icecream6.get()),IcecreamQty(clicked_icecream6.get()),Spaces(40-len("Kulfi - SugarFree"))])
            messagebox.showinfo("Product Status","Kulfi - SugarFree ("+clicked_icecream6.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Kulfi - SugarFree ("+clicked_icecream6.get()+") is not added to the cart.")

    add_icecream6=Button(lf_icecream6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddI6).place(x=68,y=245)

    def AddI7():
        global icecream_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            icecream_list.append(["Cone",IcecreamPrice(clicked_icecream7.get()),IcecreamQty(clicked_icecream7.get()),Spaces(40-len("Cone"))])
            messagebox.showinfo("Product Status","Cone ("+clicked_icecream7.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Cone ("+clicked_icecream7.get()+") is not added to the cart.")

    add_icecream7=Button(lf_icecream7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddI7).place(x=68,y=245)


    def AddI8():
        global icecream_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            icecream_list.append(["Casatta",IcecreamPrice(clicked_icecream8.get()),IcecreamQty(clicked_icecream8.get()),Spaces(40-len("Casatta"))])
            messagebox.showinfo("Product Status","Casatta ("+clicked_icecream8.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Casatta ("+clicked_icecream8.get()+") is not added to the cart.")

    add_icecream8=Button(lf_icecream8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddI8).place(x=68,y=245)






    #NavBar button 
    
Milk_button=Button(Button_frame,text="Milk",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=MilkCall)
Milk_button.grid(row=0,column=0,padx=5,pady=5)
icecream_button=Button(Button_frame,text="Ice Creams",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=IceCreamCall)
icecream_button.grid(row=1,column=0,padx=5,pady=5)
sweets_button=Button(Button_frame,text="Sweets",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue")#command=SweetsCall)
sweets_button.grid(row=2,column=0,padx=5,pady=5)
milkproducts_button=Button(Button_frame,text="MilkProducts",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue")#command=MilkProductsCall)
milkproducts_button.grid(row=3,column=0,padx=5,pady=5)
milkproducts_button=Button(Button_frame,text="Fermented",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue")#command=FermentedCall)
milkproducts_button.grid(row=4,column=0,padx=5,pady=5)










Coupon_frame=LabelFrame(root,bd=2,relief="groove",text="COUPON AVAILABLE!!!",fg="green",font="arial 14 bold")
Coupon_frame.place(x=2,y=450,width=300,height=230)
Coupon_1=Label(Coupon_frame,text="Get 15% Off on your purchase(upto Rs.500)",font="times 12",fg="yellow",bg="brown")
Coupon_2=Label(Coupon_frame,text="Get 10% Off on your purchase(upto Rs.750)",font="times 12",fg="yellow",bg="brown")
Coupon_3=Label(Coupon_frame,text="Get 5% Off on your purchase(upto Rs.1000)",font="times 12",fg="yellow",bg="brown")
Coupon_1.grid(row=0,column=0,padx=10,pady=17)
Coupon_2.grid(row=1,column=0,padx=10,pady=17)
Coupon_3.grid(row=2,column=0,padx=10,pady=17)




def Bill():
    op=messagebox.askyesno("Bill Generation Confirmation","Products cannot be added or removed during bill generation. Are you sure that you have finished shopping?")
    if op:
        
        Products_frame.destroy()
        Button_frame.destroy()
        Coupon_frame.destroy()
        bill_gen_button.destroy()
        milk_price=0
        icecream_price=0

        
        
        for i in range(len(milk_list)):
            milk_price+=milk_list[i][1]   
        for i in range(len(icecream_list)):
            icecream_price+=icecream_list[i][1]

       
        total_price=milk_price+icecream_price     #sportsgym_price+furniture_price+appliances_price
        discount=[0,0,0]
        if 0.15*total_price<500:
            discount[0]=0.15*total_price
        else:
            discount[0]=500
        if 0.1*total_price<750:
            discount[1]=0.1*total_price
        else:
            discount[1]=750
        if 0.05*total_price<1000:
            discount[2]=0.05*total_price
        else:
            discount[2]=1000
        max_discount=max(discount)
        if max_discount==discount[0]:
            suggest=Label(root,bd=1,text="Suggested : 15% Off upto Rs.500",font="times 12",fg="blue").place(x=545,y=480)
        elif max_discount==discount[1]:
            suggest=Label(root,bd=1,text="Suggested : 10% Off upto Rs.750",font="times 12",fg="blue").place(x=545,y=480)
        else:
            suggest=Label(root,bd=1,text="Suggested : 5% Off upto Rs.1000",font="times 12",fg="blue").place(x=545,y=480)
        

        def GenBill(d,choice):
            bill_area=LabelFrame(root,bd=2,relief="groove")
            bill_area.place(x=305,y=80,width=750,height=600)
            bill_title=Label(bill_area,text="INVOICE",font="arial 15 bold",bd=4,relief="groove").pack(fill=X)
            scroll_y=Scrollbar(bill_area,orient=VERTICAL)
            bill_txt_area=Text(bill_area,yscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_y.config(command=bill_txt_area.yview)
            bill_txt_area.pack(fill=BOTH,expand=1)
            bill_txt_area.insert(END,Spaces(40)+"Aavin - G2B\n"+Spaces(90,'*')+"\n")
            if len(milk_list)>0:
                bill_txt_area.insert(END,"Milk Product(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Quantity\n")
                for i in milk_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+str(i[1])+Spaces(27-len(str(i[1])))+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal MilkPockets Price : Rs."+str(milk_price)+"\n"+Spaces(90,'*')+"\n")
              
            if len(icecream_list)>0:
                bill_txt_area.insert(END,"Ice Cream Product(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Quantity\n")
                for i in icecream_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+str(i[1])+Spaces(27-len(str(i[1])))+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Icecream Price : Rs."+str(icecream_price)+"\n"+Spaces(90,'*')+"\n")
             
            '''
            for further
            '''
            
            if choice==1:
                bill_txt_area.insert(END,"\nCoupon Applied : 15% Off upto Rs.500")
            elif choice==2:
                bill_txt_area.insert(END,"\nCoupon Applied : 10% Off upto Rs.750")
            else:
                bill_txt_area.insert(END,"\nCoupon Applied : 5% Off upto Rs.1000")
            bill_txt_area.insert(END,"\nDiscount Offered : Rs."+str(d))
            bill_txt_area.insert(END,"\nTotal Price(after discount) = Rs."+str(total_price-d))
            
            save_button=Button(root,text="Save Invoice",font="times 20 bold",bd=6,bg="skyblue",width=10,fg="white",command=lambda:save_invoice(bill_txt_area.get("1.0",END)))
            save_button.place(x=1120,y=600)
       
        Coupon_frame_2=LabelFrame(root,bd=2,relief="groove",text="Apply a Coupon",fg="green",font="arial 16 bold").place(x=500,y=150,width=380,height=300)
        Coupon_apply1=Button(Coupon_frame_2,text="15% Off upto Rs.500",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:GenBill(discount[0],1))
        Coupon_apply1.place(x=540,y=190)
        Coupon_apply2=Button(Coupon_frame_2,text="10% Off upto Rs.750",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:GenBill(discount[1],2))
        Coupon_apply2.place(x=540,y=280)
        Coupon_apply3=Button(Coupon_frame_2,text="5% Off upto Rs.1000",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:GenBill(discount[2],3))
        Coupon_apply3.place(x=540,y=370)
        
    else:
        messagebox.showinfo("Bill Generation Confirmation","You can continue shopping now.")
bill_gen_button=Button(Heading,bd=4,text="Proceed to Checkout",font="times 17 bold",bg="light sky blue",fg="navy blue",activebackground="purple",command=Bill)
bill_gen_button.place(x=1095,y=0)
root.mainloop()










root.mainloop()
