import tkinter as tk
from tkinter import *
import mysql.connector as myconn
from tkinter import ttk
import random,os
from PIL import Image,ImageTk #pip insatll pillow
from tkinter import messagebox
import tempfile
from time import strftime

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def billing(master):
    master.destroy()

    class bill_app:
        def __init__(self,root):
            self.root=root
            self.root.geometry("1530x800+0+0")
            self.root.title("Billing software")


        #-----------------variable-----------------
            self.name=StringVar()
            self.phone=StringVar()
            self.bill=StringVar()
            z=random.randint(1000,9999)
            self.bill.set(z)
            self.email=StringVar()
            self.searchbill=StringVar()
            self.c_product=StringVar()
            self.c_price=IntVar()
            self.c_qty=IntVar()
            self.product_id=IntVar()
            self.c_subtotal=StringVar()
            self.c_taxtinput=StringVar()
            self.c_total=StringVar()





        #categories list

            self.Category=["Select Option","CLOTHING","ELECTRONICS","GENERAL"]

        #subclothing
            self.subclothing=["Select Option","Pant","Shirt","t-shirt"]

            self.pant=["ALLEN SOLLY","RAYMOND","LEVI'S"]
            self.price_allen=699,899,999,1999
            self.price_raymond=500,700,1100
            self.price_levis=1000,2000

            self.shirt=["POLO","PETER ENGLAND","ZODIAC"]
            self.price_polo=600
            self.price_peter=1300
            self.price_zodiac=2000,2500

            self.tshirt=["NIKE","PUMA","H&M"]
            self.price_nike=550
            self.price_puma=900
            self.price_hm=850

        #Electronics

            self.subelectronics=["Select Option","IRON PRESS","LED BULB","INDUCTION"]

            self.iron=["PHILIPS","HAVELS","MORPHY"]
            self.price_philips=1400
            self.price_havels=1000
            self.price_morphy=1200

            self.bulb=["SYSKA","WIPRO","CROMPTON"]
            self.price_syska=300,400,500
            self.price_wipro=200
            self.price_crompton=250,450

            self.induction=["PIEGON","PRESTIGE","BAJAJ"]
            self.price_piegon=3999,4500
            self.price_prestige=4999,6000
            self.price_bajaj=3000,4500

        #subgeneral
            self.subgeneral=["Select Option","BISCUIT","COFFEE","CHIPS"]

            self.sugar=["HIDE N SEEK","PARLE","BRITANIA"]
            self.price_hide=30,100
            self.price_parle=10,20
            self.price_britania=35,60

            self.rice=["LAVAZZA","NESCAFE","PEETS"]
            self.price_lavazza=300,500
            self.price_nescafe=10,100,1000
            self.price_peet=400

            self.dal=["LAYS","NACHOS","UNCLE CHIPS"]
            self.price_lays=10,30,55
            self.price_nachos=35,45
            self.price_unclechips=20,30




        #image1
            img=Image.open("image/s3.jpg")
            img=img.resize((450,150),Image.BOX)
            self.photoimg=ImageTk.PhotoImage(img)

            lbl_img=Label(self.root,image=self.photoimg)
            lbl_img.place(x=0,y=0,width=450,height=150)

        #image2
            img_1=Image.open("image/s2.jpg")
            img_1=img_1.resize((450,150),Image.BOX)
            self.photoimg1=ImageTk.PhotoImage(img_1)
        
            lbl_img_1=Label(self.root,image=self.photoimg1)
            lbl_img_1.place(x=470,y=0,width=450,height=150)

        #image3
            img_2=Image.open("image/s2.jpg")
            img_2=img_2.resize((450,150),Image.BOX)
            self.photoimg2=ImageTk.PhotoImage(img_2)

            lbl_img_2=Label(self.root,image=self.photoimg1)
            lbl_img_2.place(x=940,y=0,width=450,height=150)

            lbl_title=Label(self.root,text="BILLING COUNTER OF ALLMART",font=("arial",30,"bold"),bg="black",fg="yellow")
            lbl_title.place(x=0,y=150,width=1530,height=35)

        #main frame 

            main_frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
            main_frame.place(x=0,y=190,width=1530,height=650)

        #CUSTOMER FRAME =======================

            Cust_frame=LabelFrame(main_frame,text="Customer",font=("times new roman",15,"bold"),bg="white",fg="black")
            Cust_frame.place(x=0,y=0,width=250,height=120)

            self.lbl_mob=Label(Cust_frame,text="Mobile:",font=("garamond",12,"bold"),bg="white",fg="black")
            self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)
            self.entry_mob=ttk.Entry(Cust_frame,textvariable=self.phone,font=("times new roman",12),width=19)
            self.entry_mob.grid(row=0,column=1)

            self.lbl_name=Label(Cust_frame,text="Name:",font=("garamond",12,"bold"),bg="white",fg="black")
            self.lbl_name.grid(row=1,column=0,sticky=W,padx=5,pady=2)
            self.txtname=ttk.Entry(Cust_frame,textvariable=self.name,font=("times new roman",11,"bold"),width=19)
            self.txtname.grid(row=1,column=1)

            self.lblemail=Label(Cust_frame,text="Email:",font=("garamond",12,"bold"),bg="white",fg="black")
            self.lblemail.grid(row=2,column=0,sticky=W,padx=5,pady=2)
            self.emailtxt=ttk.Entry(Cust_frame,textvariable=self.email,font=("times new roman",11,"bold"),width=19)
            self.emailtxt.grid(row=2,column=1)

        #PRODUCT FRAME=======================

            prod_frame=LabelFrame(main_frame,text="Product",font=("times new roman",15,"bold"),bg="white",fg="black")
            prod_frame.place(x=260,y=0,width=610,height=120)

        #CATEGORY

            self.lbl_name=Label(prod_frame,text="Select Catagory",font=("times new roman",12,"bold"),bg="white",fg="black")
            self.lbl_name.grid(row=0,column=0,sticky=W,padx=5,pady=2)
            self.combocategory=ttk.Combobox(prod_frame,values=self.Category,font=("times new roman",11,"bold"),width=19,state="readonly")
            self.combocategory.current(0)
            self.combocategory.grid(row=0,column=1)
            self.combocategory.bind("<<ComboboxSelected>>",self.categories)

        #SUBCATEGORY

            self.lbl_name1=Label(prod_frame,text="Select Subcategory",font=("times new roman",12,"bold"),bg="white",fg="black")
            self.lbl_name1.grid(row=1,column=0,sticky=W,padx=5,pady=2)
            self.combocategory1=ttk.Combobox(prod_frame,values=self.subclothing,font=("times new roman",11,"bold"),width=19,state="readonly")
            self.combocategory1.grid(row=1,column=1)
            self.combocategory1.bind("<<ComboboxSelected>>",self.product)

        #PRODUCT

            self.lbl_name2=Label(prod_frame,text="Select Product",font=("times new roman",12,"bold"),bg="white",fg="black")
            self.lbl_name2.grid(row=2,column=0,sticky=W,padx=5,pady=2)
            self.combocategory2=ttk.Combobox(prod_frame,textvariable=self.c_product,font=("times new roman",11,"bold"),width=19,state="readonly",)
            self.combocategory2.grid(row=2,column=1)
            self.combocategory2.bind("<<ComboboxSelected>>",self.price)

        #PRICE

            self.lbl_name3=Label(prod_frame,text="Select price",font=("times new roman",12,"bold"),bg="white",fg="black")
            self.lbl_name3.grid(row=0,column=2,sticky=W,padx=5,pady=2)
            self.combocategory3=ttk.Combobox(prod_frame,textvariable=self.c_price,font=("times new roman",11,"bold"),width=18,state="readonly",)
            self.combocategory3.grid(row=0,column=3)

        #QUANTITY

            self.lblqty=Label(prod_frame,text="QTY",font=("times new roman",11,"bold"),bg="white",fg="black")
            self.lblqty.grid(row=1,column=2,sticky=W,padx=5,pady=2)
            self.txtqty=ttk.Entry(prod_frame,textvariable=self.c_qty,font=("times new roman",11,"bold"),width=18)
            self.txtqty.grid(row=1,column=3)

        #PRODUCT ID

            self.productid=Label(prod_frame,text="PRODUCT ID",font=("times new roman",11,"bold"),bg="white",fg="black")
            self.productid.grid(row=2,column=2,sticky=W,padx=5,pady=2)
            self.txtproduct=ttk.Entry(prod_frame,textvariable=self.product_id,font=("times new roman",11,"bold"),width=17)
            self.txtproduct.grid(row=2,column=3)

        #BILL SEARCH
            button_frame1=Frame(main_frame,bd=2,bg="white")
            button_frame1.place(x=870,y=4,width=400,height=250)
    
            self.lblqty21=Label(button_frame1,text="Search bill",font=("times new roman",12,"bold"),bg="white",fg="black")
            self.lblqty21.grid(row=0,column=0,sticky=W,padx=2)

            self.bill_search=ttk.Entry(button_frame1,textvariable=self.searchbill,font=("times new roman",11,"bold"),width=19)
            self.bill_search.grid(row=0,column=1)


            self.Btnsearch=Button(button_frame1,command=self.search_bills,text="search",font=("times new roman",9,"bold"),bg="black",fg="white",width=15,cursor="hand2")
            self.Btnsearch.grid(row=0,column=2)

        #RIGHT SIDE FRAME
            Rightlabel=LabelFrame(main_frame,text="BILL RECIEPT",font=("times new roman",15,"bold"),bg="white",fg="black")
            Rightlabel.place(x=870,y=40,width=480,height=460)

        #Scroll bar
            scroll_y=Scrollbar(Rightlabel,orient=VERTICAL)
            self.textarea=Text(Rightlabel,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_y.config(command=self.textarea.yview)
            self.textarea.pack(fill=BOTH,expand=1)

        #BOTTOM FRAME======================
            bott_frame=LabelFrame(main_frame,text="Product",font=("times new roman",20,"bold"),bg="white",fg="black")
            bott_frame.place(x=0,y=350,width=870,height=150)

        #SUBTOTAL

            self.lblqty1=Label(bott_frame,text="SUBTOTAL:",font=("times new roman",12,"bold"),bg="white",fg="black")
            self.lblqty1.grid(row=0,column=0,sticky=W,padx=5,pady=2)
            self.txtqty1=ttk.Entry(bott_frame,textvariable=self.c_subtotal,font=("times new roman",11,"bold"),width=19)
            self.txtqty1.grid(row=0,column=1)

        #GOVERNMENT TAX

            self.lblqty2=Label(bott_frame,text="GST:",font=("times new roman",12,"bold"),bg="white",fg="black")
            self.lblqty2.grid(row=1,column=0,sticky=W,padx=5,pady=2)
            self.txtqty2=ttk.Entry(bott_frame,textvariable=self.c_taxtinput,font=("times new roman",11,"bold"),width=19)
            self.txtqty2.grid(row=1,column=1)


        #TOTAL
            self.lblqty3=Label(bott_frame,text="TOTAL:",font=("times new roman",12,"bold"),bg="white",fg="black")
            self.lblqty3.grid(row=2,column=0,sticky=W,padx=5,pady=2)
            self.txtqty3=ttk.Entry(bott_frame,textvariable=self.c_total,font=("times new roman",11,"bold"),width=19)
            self.txtqty3.grid(row=2,column=1)

        #BUTTON
            button_frame=Frame(bott_frame,bd=2,bg="white")
            button_frame.place(x=270,y=0)

            self.BtnAddToCart=Button(button_frame,command=self.additem,text="Add to cart",font=("times new roman",15,"bold"),bg="black",fg="white",width=15,cursor="hand2")
            self.BtnAddToCart.grid(row=0,column=0)

            self.BtnAddToCart1=Button(button_frame,command=self.generating,text="Generate Bill",font=("times new roman",15,"bold"),bg="black",fg="white",width=15,cursor="hand2")
            self.BtnAddToCart1.grid(row=0,column=1)

            self.BtnAddToCart0=Button(button_frame,command=self.savebill,text="Save Bill",font=("times new roman",15,"bold"),bg="black",fg="white",width=15,cursor="hand2")
            self.BtnAddToCart0.grid(row=0,column=2)

            self.BtnAddToCart2=Button(button_frame,command=self.iprint,text="Print Bill",font=("times new roman",15,"bold"),bg="black",fg="white",width=15,cursor="hand2")
            self.BtnAddToCart2.grid(row=1,column=0)

            self.BtnAddToCart3=Button(button_frame,command=self.clear,text="CLEAR",font=("times new roman",15,"bold"),bg="black",fg="white",width=15,cursor="hand2")
            self.BtnAddToCart3.grid(row=1,column=1)

            self.BtnAddToCart4=Button(button_frame,command=self.back,text="Back",font=("times new roman",15,"bold"),bg="black",fg="white",width=15,cursor="hand2")
            self.BtnAddToCart4.grid(row=1,column=2)
            self.welcome()

    
    
    
    #variable for adding
            self.l=[]
    #ADD TO CART
        def additem(self):
            Tax=1
            self.n=self.c_price.get()
            self.m=self.c_qty.get()*self.n
            self.l.append(self.m)
            if self.c_product.get()=="":
                messagebox.showerror("error","please select the product")
            else:
                self.textarea.insert(END,f"\n {self.c_product.get()}\t\t\t{self.c_qty.get()}\t\t\t{self.m}")
                self.c_subtotal.set(str('Rs.%2f'%(sum(self.l))))
                self.c_taxtinput.set(str('Rs.%2f'%((((sum(self.l))-(self.c_price.get()))*Tax)/100)))
                self.c_total.set(str('Rs.%2f'%(((sum(self.l))+((((sum(self.l))-(self.c_price.get()))*Tax)/100)))))
        def back(self):
            self.root.destroy()
            main()

    #GENERATING BILL
        def generating(self):
            if self.c_product.get()=="":
                messagebox.showerror("error","please select the product")
            else:
                text=self.textarea.get(10.0,(10.0+float(len(self.l))))
                self.welcome()
                self.textarea.insert(END,text)
                self.textarea.insert(END,"\n ==================================================")
                self.textarea.insert(END,f"\n Sub amount:\t\t\t{self.c_subtotal.get()}")
                self.textarea.insert(END,f"\n Tax amount:\t\t\t{self.c_taxtinput.get()}")
                self.textarea.insert(END,f"\n total amount:\t\t\t{self.c_total.get()}")
                self.textarea.insert(END,"\n==================================================")


    #TO SAVE BILL 
        def savebill(self):
            op=messagebox.askyesno("save bill","do you want to save bill")
            if op>0:
                self.bill_data=self.textarea.get(1.0,END)
                f1=open('bills/'+str(self.bill.get())+".txt",'w')
                f1.write(self.bill_data)
                op=messagebox.showinfo("saved",f"bill no:{self.bill.get()} saved succesfully")
                f1.close()

    #To print
        def iprint(self):
            #To update stock 
            y=self.bill.get()
            with open('bills/'+y+".txt","r") as nfile:
                string=nfile.readlines()
                c=[]
                for e in string:
                    a=e.strip()
                    print(a)
                    condition=["ALLEN","RAYMOND","LEVI'S","POLO","PETER","ZODIAC","NIKE","PUMA","H&M","PHILIPS","HAVELS","MORPHY","SYSKA","WIPRO","CROMPTON","PRESTIGE","PIEGON","BAJAJ","HIDE","PARLE","BRITANIA","NESCAFE","PEETS","LAVAZZA","LAYS","NACHOS","UNCLE"]
                    if any(a.startswith(cond) for cond in condition):
                        print(a)
                        b=a.split("\t")
                        print(b)
                        z=b[0]
                        x=b[3]
                        w=[z,x]
                        c+=[w]

            print(c)   

            mydb=myconn.connect(host="localhost",user="root",password="@Ayush4321",database="STOCK")
            mycursor=mydb.cursor()
            for i in c:
                c_name=i[0]
                quan=i[1]
                q="UPDATE STOCK SET QUANTITY =QUANTITY-%s WHERE PRODUCT_NAME=%s"
                data=(quan,c_name)
                mycursor.execute(q,data)
                mydb.commit()
            messagebox.showinfo("Info","Stock Updated Successfully")
            # For Printing Facilities 
            '''q=self.textarea.get(1.0,"end-1c")
            filename=tempfile.mktemp('.txt')
            open(filename,'w').write(q)
            os.startfile(filename,"print")'''

    #To search
        def search_bills(self):
            found="no"
            for i in os.listdir("bills/"):
                if i.split('.')[0]==self.searchbill.get():
                    f1=open(f'bills/{i}','r')
                    self.textarea.delete(1.0,END)
                    for d in f1:
                        self.textarea.insert(END,d)
                    f1.close()
                    found="yes"
            if found=='no':
                messagebox.showerror("Error","INVALID BILL NO")

    #To clear
        def clear(self):
            self.textarea.delete(1.0,END)
            self.name.set("")
            self.phone.set("")
            self.bill.set("")
            z=random.randint(1000,9999)
            self.bill.set(str(z))
            self.email.set("")
            self.searchbill.set("")
            self.c_product.set("")
            self.c_price.set(0)
            self.c_qty.set(0)
            self.l=[0]
            self.c_subtotal.set("")
            self.c_taxtinput.set("")
            self.c_total.set("")
            self.welcome()




    #welcome page
        def welcome(self):
            self.textarea.delete(1.0,END)
            self.textarea.insert(END,"\t\t Welcome to the All mart")
            self.textarea.insert(END,f"\n Bill number:{self.bill.get()}")
            self.textarea.insert(END,f"\n Customer name:{self.name.get()}")
            self.textarea.insert(END,f"\n customer phone number:{self.phone.get()}")
            self.textarea.insert(END,f"\n customer email:{self.email.get()}")
            self.textarea.insert(END,"\n==================================================")
            self.textarea.insert(END,f"\n PRODUCT\t\t\tQUANTITY\t\t\tPRICE")
            self.textarea.insert(END,"\n==================================================\n")
                             


    #CATEGORIES
        def categories(self,event=""):
            if self.combocategory.get()=="CLOTHING":
                self.combocategory1.config(value=self.subclothing)
                self.combocategory1.current(0)
            if self.combocategory.get()=="ELECTRONICS":
                self.combocategory1.config(value=self.subelectronics)
                self.combocategory1.current(0)
            if self.combocategory.get()=="GENERAL":
                self.combocategory1.config(value=self.subgeneral)
                self.combocategory1.current(0)

        def product(self,event=""):
            if self.combocategory1.get()=="Pant":
                self.combocategory2.config(value=self.pant)
                self.combocategory2.current(0)

            if self.combocategory1.get()=="Shirt":
                self.combocategory2.config(value=self.shirt)
                self.combocategory2.current(0)

            if self.combocategory1.get()=="t-shirt":
                self.combocategory2.config(value=self.tshirt)
                self.combocategory2.current(0)

        #Lifestyle

            if self.combocategory1.get()=="IRON PRESS":
                self.combocategory2.config(value=self.iron)
                self.combocategory2.current(0)

            if self.combocategory1.get()=="LED BULB":
                self.combocategory2.config(value=self.bulb)
                self.combocategory2.current(0)

            if self.combocategory1.get()=="INDUCTION":
                self.combocategory2.config(value=self.induction)
                self.combocategory2.current(0)

        #GENERAL

            if self.combocategory1.get()=="BISCUIT":
                self.combocategory2.config(value=self.sugar)
                self.combocategory2.current(0)

            if self.combocategory1.get()=="COFFEE":
                self.combocategory2.config(value=self.rice)
                self.combocategory2.current(0)

            if self.combocategory1.get()=="CHIPS":
                self.combocategory2.config(value=self.dal)
                self.combocategory2.current(0)



    #function3
        def price(self,event=""):
            if self.combocategory2.get()=="ALLEN SOLLY":
                self.combocategory3.config(value=self.price_allen)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1000)

            if self.combocategory2.get()=="RAYMOND":
                self.combocategory3.config(value=self.price_raymond)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1001)

            if self.combocategory2.get()=="LEVI'S":
                self.combocategory3.config(value=self.price_levis)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1002)

            if self.combocategory2.get()=="POLO":
                self.combocategory3.config(value=self.price_polo)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1003)

            if self.combocategory2.get()=="PETER ENGLAND":
                self.combocategory3.config(value=self.price_peter)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1004)

            if self.combocategory2.get()=="ZODIAC":
                self.combocategory3.config(value=self.price_zodiac)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1005)

            if self.combocategory2.get()=="NIKE":
                self.combocategory3.config(value=self.price_nike)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1006)

            if self.combocategory2.get()=="PUMA":
                self.combocategory3.config(value=self.price_puma)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1007)

            if self.combocategory2.get()=="POLO":
                self.combocategory3.config(value=self.price_polo)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1008)

        #electronic price  

            if self.combocategory2.get()=="PHILIPS":
                self.combocategory3.config(value=self.price_philips)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1009)

            if self.combocategory2.get()=="HAVELS":
                self.combocategory3.config(value=self.price_havels)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1010)

            if self.combocategory2.get()=="MORPHY":
                self.combocategory3.config(value=self.price_morphy)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1011)

            if self.combocategory2.get()=="SYSKA":
                self.combocategory3.config(value=self.price_syska)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1012)

            if self.combocategory2.get()=="WIPRO":
                self.combocategory3.config(value=self.price_wipro)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1013)

            if self.combocategory2.get()=="CROMPTON":
                self.combocategory3.config(value=self.price_crompton)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1014)

            if self.combocategory2.get()=="PIEGON":
                self.combocategory3.config(value=self.price_piegon)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1015)

            if self.combocategory2.get()=="PRESTIGE":
                self.combocategory3.config(value=self.price_prestige)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1016)

            if self.combocategory2.get()=="BAJAJ":
                self.combocategory3.config(value=self.price_bajaj)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1017)


        #general price

            if self.combocategory2.get()=="HIDE N SEEK":
                self.combocategory3.config(value=self.price_hide)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1018)

            if self.combocategory2.get()=="PARLE":
                self.combocategory3.config(value=self.price_parle)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1019)

            if self.combocategory2.get()=="BRITANIA":
                self.combocategory3.config(value=self.price_britania)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1020)

            if self.combocategory2.get()=="LAVAZZA":
                self.combocategory3.config(value=self.price_lavazza)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1021)

            if self.combocategory2.get()=="NESCAFE":
                self.combocategory3.config(value=self.price_nescafe)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1022)

            if self.combocategory2.get()=="PEET":
                self.combocategory3.config(value=self.price_peet)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1023)

            if self.combocategory2.get()=="LAYS":
                self.combocategory3.config(value=self.price_lays)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1024)

            if self.combocategory2.get()=="NACHOS":
                self.combocategory3.config(value=self.price_nachos)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1025)

            if self.combocategory2.get()=="UNCLE CHIPS":
                self.combocategory3.config(value=self.price_unclechips)
                self.combocategory3.current(0)
                self.c_qty.set(1)
                self.product_id.set(1026)
        #variable
            self.chirag=self.product_id.get()




      






    if __name__=='__main__' :
        root=Tk()
        obj=bill_app(root)
        root.mainloop()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def salary(master):
    master.destroy()
    ap=tk.Tk()
    ap.geometry('1530x800')
    ap.title('ALLMART-:SALARY')
    ap.configure(background='lightgoldenrod1')

    b_title=tk.Message(text=" AllMart -: Salary List ",relief="raised",width=4900,padx=700,pady=0,fg="darkolivegreen1",bg="gray1",justify="center",anchor="center")
    b_title.config(font=("Bahnschrift Light SemiCondensed","28",))
    b_title.pack(side="top")

    b_title=tk.Message(text="The Employee Salary List is as follows-:",relief="raised",width=1000,padx=100,pady=10,fg="darkolivegreen1",bg="gray1",justify="left",anchor="e")
    b_title.config(font=("Bahnschrift Light SemiCondensed","18",))
    b_title.pack(side="top")

#CONNECTING DATABASE TO PYTHON BY USING MYSQL.CONNECTOR
    connect = myconn.connect(host='localhost',user='root',password='@Ayush4321',database='Salary')

#SELECTING TABLE FROM DATABASE
    conn= connect.cursor()
    conn.execute('SELECT * FROM Salary.emp1')

#CREATING A TABLE VIEW BY USING TREEEVIEW
    tree= ttk.Treeview(ap) 
    tree['show']= 'headings'
    style = ttk.Style(ap)
    style.theme_use('classic')

    style.configure('.',font=('Helvetica',11))
    style.configure('Treeview.Heading', foreground='black',font=('Helvetica',11,'bold'))

    tree['columns']=  ('EID','Ename','Esalary','Estatus')


    tree.column('EID',width=375, minwidth=50,anchor=tk.CENTER)
    tree.column('Ename',width=375, minwidth=50,anchor=tk.CENTER)
    tree.column('Esalary',width=375, minwidth=50,anchor=tk.CENTER)
    tree.column('Estatus',width=375, minwidth=50,anchor=tk.CENTER)


    tree.heading('EID', text='ID',anchor=tk.CENTER)
    tree.heading('Ename', text='Name',anchor=tk.CENTER)
    tree.heading('Esalary', text='Salary',anchor=tk.CENTER)
    tree.heading('Estatus', text='Status',anchor=tk.CENTER)

#INSERTING ALL RECORDS ONE AT A TIME BY USING FOR LOOP
    i=0
    for ro in conn:
        tree.insert('',i,text='',values=(ro[0],ro[1],ro[2],ro[3]))
        i= i+1

#CREATING A SCROLLBAR BOTH HORIZONTAL AND VERTICAL
    hsb= ttk.Scrollbar(ap,orient='horizontal')

    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X,side= BOTTOM)


    hsb= ttk.Scrollbar(ap,orient='vertical')

    hsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=hsb.set)
    hsb.pack(fill=Y,side= RIGHT)

    tree.pack()


    img7=tk.PhotoImage(file="back.png")
    myimg7=img7.subsample(1,1)
    b7=tk.Button(image=myimg7,command=lambda: back(ap))   
    b7.image=myimg7
    b7.place(x=100,y=350)
    img8=tk.PhotoImage(file="updsal.png")
    myimg8=img8.subsample(1,1)
    b8=tk.Button(image=myimg8,command=lambda: updatesal(ap))   
    b8.image=myimg8
    b8.place(x=850,y=350)
    ap.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def updatesal(master):
    master.destroy()
    f = ('Times', 14)       
    wsb=tk.Tk()
    wsb.geometry("1030x600")
    wsb.title("ALLMART")
    wsb.configure(background='lightgoldenrod1')
    fr1=tk.Frame(wsb)
    fr1.pack(side="top")
    l_title=tk.Message(text="Welcome To AllMart ",relief="raised",width=4900,padx=700,pady=0,fg="darkolivegreen1",bg="gray1",justify="center",anchor="center")
    l_title.config(font=("Bahnschrift Light SemiCondensed","28",))
    l_title.pack(side="top")
    b_title=tk.Message(text=" AllMart -:Salary Updation ",relief="raised",width=4900,padx=700,pady=0,fg="darkolivegreen1",bg="gray1",justify="center",anchor="center")
    b_title.config(font=("Bahnschrift Light SemiCondensed","28",))
    b_title.pack(side="top")
    b_title=tk.Message(text="please fill the updated details-: ",relief="raised",width=1000,padx=100,pady=10,fg="darkolivegreen1",bg="gray1",justify="left",anchor="e")
    b_title.config(font=("Bahnschrift Light SemiCondensed","18",))
    b_title.pack(side="top")

    var = StringVar()



    var.set('male')
# The Whole Page is been divided into 2 parts using frames This is the description of the right frame  ws is the main window,bd border,bg background,relief for special effects.
    right_frame = Frame(wsb,bd=2,bg='#CCCCCC',relief=SOLID,padx=20,pady=20)
# It helps in providing a space to write the details in the page. grid is used to set the geometry of the box
    Label(right_frame,text="How Much Salary to be Updated?????", bg='#CCCCCC',font=f).grid(row=0, column=0, sticky=W, pady=10)

    Label(right_frame, text="Enter Salary Status(Paid/Unpaid)-:", bg='#CCCCCC',font=f).grid(row=2, column=0, sticky=W, pady=10)
    Label(right_frame, text="Enter The Employee ID", bg='#CCCCCC',font=f).grid(row=1, column=0, sticky=W, pady=10)

# Enter is used to take input from the user as the user writes the input in tgose spaces

    register_eid = Entry(right_frame, font=f)

    register_status = Entry(right_frame, font=f)

    register_salary=Entry(right_frame,font=f)

# It is used to create a dropdown list in the window. but it is not suitable for a long list as it doesnot contain a scroll bar
#*states means all states
#states is an empty list in which names would be appended 


    def insert_record():
        check_counter=0
        warn = ""
        if register_salary.get() == "":
            warn = "Salary can't be empty"
        else:
            check_counter += 1
        
        if register_eid.get() == "":
            warn = "Emplyee ID can't be empty"
        else:
            check_counter += 1

        if check_counter == 2:        
            try:
                con=myconn.connect(host='localhost',user='root',password="@Ayush4321",database="SALARY")

                cur = con.cursor()
                print(type(register_salary))
                x=register_salary.get()
                print(type(x))
                q="UPDATE emp1 SET Esalary ="+x+",Estatus=\""+register_eid.get()+"\"where EID="+register_status.get()+";"
                print(q)
                cur.execute(q)
            
                con.commit()

                x=messagebox.showinfo('confirmation', 'Record updated')
                if x=="ok":
                    salary(wsb)
            
#ek button banana hoga message box mai jo entry le
            except Exception as ep:
                messagebox.showerror('', ep) 
        else:
            messagebox.showerror('Error', warn)


# Button is used to trigger some activity 
    register_btn = Button(right_frame,width=15,text='Update',font=f,relief=SOLID,cursor='hand2',command=insert_record)

    register_eid.grid(row=2, column=1, pady=10, padx=20)
    register_status.grid(row=1, column=1, pady=10, padx=20) 
    register_salary.grid(row=0,column=1,padx=20,pady=10)
    register_btn.grid(row=7, column=1, pady=10, padx=20)
    right_frame.place(x=250, y=150)

    # infinite loop
    wsb.mainloop()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def pending(master):
    master.destroy()
    app=tk.Tk()
    app.geometry('1530x800')
    app.title('ALLMART-:Pending Orders')

    app.configure(background='lightgoldenrod1')

    b_title=tk.Message(text=" AllMart -:Pending Orders ",relief="raised",width=4900,padx=700,pady=0,fg="darkolivegreen1",bg="gray1",justify="center",anchor="center")
    b_title.config(font=("Bahnschrift Light SemiCondensed","28",))
    b_title.pack(side="top")

    b_title=tk.Message(text="The pending Orders are as follows:",relief="raised",width=1000,padx=100,pady=10,fg="darkolivegreen1",bg="gray1",justify="left",anchor="e")
    b_title.config(font=("Bahnschrift Light SemiCondensed","18",))
    b_title.pack(side="top")

#CONNECTING DATABASE TO PYTHON BY USING MYSQL.CONNECTOR
    connect = myconn.connect(host='localhost',user='root',password='@Ayush4321',database='pending')

    #SELECTING TABLE FROM DATABASE
    conn= connect.cursor()
    conn.execute('SELECT * FROM pending.bill')

#CREATING A TABLE VIEW BY USING TREEEVIEW
    tree= ttk.Treeview(app) 
    tree['show']= 'headings'
    style = ttk.Style(app)
    style.theme_use('classic')

    style.configure('.',font=('Helvetica',11))
    style.configure('Treeview.Heading', foreground='black',font=('Helvetica',11,'bold'))

    tree['columns']=  ('billno','items')


    tree.column('billno',width=575, minwidth=50,anchor=tk.CENTER)
    tree.column('items',width=975, minwidth=50,anchor=tk.CENTER)



    tree.heading('billno', text='Bill No',anchor=tk.CENTER)
    tree.heading('items', text='Items List[["PRODUCT NAME","QUANTITY"]]',anchor=tk.CENTER)


#INSERTING ALL RECORDS ONE AT A TIME BY USING FOR LOOP
    i=0
    for ro in conn:
        tree.insert('',i,text='',values=(ro[0],ro[1]))
        i= i+1

#CREATING A SCROLLBAR BOTH HORIZONTAL AND VERTICAL
    hsb= ttk.Scrollbar(app,orient='horizontal')

    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X,side= BOTTOM)


    hsb= ttk.Scrollbar(app,orient='vertical')

    hsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=hsb.set)
    hsb.pack(fill=Y,side= RIGHT)

    tree.pack()

    img7=tk.PhotoImage(file="back.png")
    myimg7=img7.subsample(1,1)
    b7=tk.Button(image=myimg7,command=lambda: back(app))   
    b7.image=myimg7
    b7.place(x=100,y=350)
    img8=tk.PhotoImage(file="compbill.png")
    myimg8=img8.subsample(1,1)
    b8=tk.Button(image=myimg8,command=lambda: compbill(app))   
    b8.image=myimg8
    b8.place(x=850,y=350)
    app.mainloop()


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def comments(master):
    master.destroy()
#CREATING AN INTERFACE USING TKINTER
    app=tk.Tk()
    app.geometry('1530x800')
    app.title('ALLMART-:Comments')

    app.configure(background='lightgoldenrod1')

    b_title=tk.Message(text=" AllMart -: Reviews ",relief="raised",width=4900,padx=700,pady=0,fg="darkolivegreen1",bg="gray1",justify="center",anchor="center")
    b_title.config(font=("Bahnschrift Light SemiCondensed","28",))
    b_title.pack(side="top")

    b_title=tk.Message(text="Reviews are as follows:",relief="raised",width=1000,padx=100,pady=10,fg="darkolivegreen1",bg="gray1",justify="left",anchor="e")
    b_title.config(font=("Bahnschrift Light SemiCondensed","18",))
    b_title.pack(side="top")

#CONNECTING DATABASE TO PYTHON BY USING MYSQL.CONNECTOR
    connect = myconn.connect(host='localhost',user='root',password='@Ayush4321',database='Reviews')

    #SELECTING TABLE FROM DATABASE
    conn= connect.cursor()
    conn.execute('SELECT * FROM Reviews.rev')

#CREATING A TABLE VIEW BY USING TREEEVIEW
    tree= ttk.Treeview(app) 
    tree['show']= 'headings'
    style = ttk.Style(app)
    style.theme_use('classic')

    style.configure('.',font=('Helvetica',11))
    style.configure('Treeview.Heading', foreground='black',font=('Helvetica',11,'bold'))

    tree['columns']=  ('Reviews','Ratings')


    tree.column('Reviews',width=975, minwidth=50,anchor=tk.CENTER)
    tree.column('Ratings',width=575, minwidth=50,anchor=tk.CENTER)



    tree.heading('Reviews', text='Reviews',anchor=tk.CENTER)
    tree.heading('Ratings', text='Ratings(Out Of 5)',anchor=tk.CENTER)


#INSERTING ALL RECORDS ONE AT A TIME BY USING FOR LOOP
    i=0
    for ro in conn:
        tree.insert('',i,text='',values=(ro[0],ro[1]))
        i= i+1

#CREATING A SCROLLBAR BOTH HORIZONTAL AND VERTICAL
    hsb= ttk.Scrollbar(app,orient='horizontal')

    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X,side= BOTTOM)


    hsb= ttk.Scrollbar(app,orient='vertical')

    hsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=hsb.set)
    hsb.pack(fill=Y,side= RIGHT)

    tree.pack()


    img7=tk.PhotoImage(file="back.png")
    myimg7=img7.subsample(1,1)
    b7=tk.Button(image=myimg7,command=lambda: back(app))   
    b7.image=myimg7   
    b7.place(x=100,y=350)
    app.mainloop()


#-----------------------------------------------------------------------------------------------------------------------------------------------------

def compbill(master):
    master.destroy()
    #Create interface window and 'e' variable to entry review
    root = tk.Tk()
    mess= Label(root,text="Enter The Bill Number",anchor='center')
    mess.pack()
    e = Entry(root, width=40, borderwidth=10)
    e.pack()

#Connecting database to python code
    conn = myconn.connect(host='localhost',user='root',password='@Ayush4321',database='pending',)
    db_cursor=conn.cursor()

    #Function for sending review to database and printing message after submitting
    def insertdata():
        billno = e.get()
        query="DELETE FROM bill where ORDERID="+billno+";"
        db_cursor.execute(query)
        conn.commit()
        response = messagebox.showinfo('Confirmation','Order Deletion Completed')
        button.config(command=response)
        root.destroy()
        main()

#Creating button for submitting and canceling 
    button = Button(root, text='Submit', fg='red',command=insertdata)
    buttonext = Button(root, text='Back', fg='red',command=lambda: pending(root))

    button.pack()
    buttonext.pack()
    
    root.mainloop()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def stock(master):
    master.destroy()
    ap=tk.Tk()
    ap.geometry('1530x800')
    ap.title('ALLMART-STOCK')
    ap.configure(background='lightgoldenrod1')

    connect = myconn.connect(host='localhost',user='root',password='@Ayush4321',database='STOCK')
    conn= connect.cursor()
    conn.execute('SELECT * FROM STOCK;')
    tree= ttk.Treeview(ap) 
    tree['show']= 'headings'
    style = ttk.Style(ap)
    style.theme_use('classic')

    b_title=tk.Message(text=" AllMart -: Stock List ",relief="raised",width=4900,padx=700,pady=0,fg="darkolivegreen1",bg="gray1",justify="center",anchor="center")
    b_title.config(font=("Bahnschrift Light SemiCondensed","28",))
    b_title.pack(side="top")

    b_title=tk.Message(text="The Stock List is as follows-:",relief="raised",width=1000,padx=100,pady=10,fg="darkolivegreen1",bg="gray1",justify="left",anchor="e")
    b_title.config(font=("Bahnschrift Light SemiCondensed","18",))
    b_title.pack(side="top")


    style.configure('.',font=('Helvetica',11))
    style.configure('Treeview.Heading', foreground='black',font=('Helvetica',11,'bold'))

    tree['columns']=  ('PRODUCT ID','PRODUCT NAME','QUANTITY')


    tree.column('PRODUCT ID',width=500, minwidth=50,anchor=tk.CENTER)
    tree.column('PRODUCT NAME',width=500, minwidth=50,anchor=tk.CENTER)
    tree.column('QUANTITY',width=500, minwidth=50,anchor=tk.CENTER)


    tree.heading('PRODUCT ID', text='PRODUCT ID',anchor=tk.CENTER)
    tree.heading('PRODUCT NAME', text='PRODUCT NAME',anchor=tk.CENTER)
    tree.heading('QUANTITY', text='QUANTITY',anchor=tk.CENTER)
    i=0
    for ro in conn:
        tree.insert('',i,text='',values=(ro[0],ro[1],ro[2]))
        i= i+1

    hsb= ttk.Scrollbar(ap,orient='horizontal')

    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X,side= BOTTOM)


    hsb= ttk.Scrollbar(ap,orient='vertical')

    hsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=hsb.set)
    hsb.pack(fill=Y,side= RIGHT)

    tree.pack()

    img7=tk.PhotoImage(file="back.png")
    myimg7=img7.subsample(1,1)
    b7=tk.Button(image=myimg7,command=lambda: back(ap))   
    b7.image=myimg7
    b7.place(x=100,y=350)
    ap.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

def logout(master):
	master.destroy()

def back(master):
    master.destroy()
    main()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
def main():
    rootwn=tk.Tk()
    rootwn.geometry("1530x800")
    rootwn.title("ALL MART -:User Inteface")
    rootwn.configure(background='lightgoldenrod1')
    fr1=tk.Frame(rootwn)
    fr1.pack(side="top")
    l_title=tk.Message(rootwn,text="ALL MART",relief="raised",width=2000,padx=600,pady=0,fg="darkolivegreen1",bg="gray1",justify="center",anchor="center")
    l_title.config(font=("Arial","50","bold"))
    l_title.pack(side="top")
    label=tk.Label(text="Welcome to all AllMart ",relief="raised",bg="gray1",font=("Times",16),fg="darkolivegreen1",anchor="center",justify="center")
    label.pack(side="top")
    def upd():
        str1=strftime('%H:%M:%S %p')
        label.config(text="Time-:"+str1)
        rootwn.after(1000,upd)    
    label=tk.Label(relief="raised",bg="gray1",font=("Times",16),fg="darkolivegreen1",anchor="center",justify="center")
    label.pack(side="top")
    upd()
    img=(Image.open("logo1.jpeg"))
    reimg=img.resize((100,80),Image.ANTIALIAS)
    new=ImageTk.PhotoImage(reimg)
    img_label=tk.Label(rootwn,image=new)
    img_label.place(x=0,y=0)

    img1=(Image.open("trolly.jpeg"))
    reimg1=img1.resize((450,170),Image.ANTIALIAS)
    new1=ImageTk.PhotoImage(reimg1)
    img_label1=tk.Label(rootwn,image=new1)
    img_label1.place(x=810,y=130)

    img2=(Image.open("sto.jpeg"))
    reimg2=img2.resize((450,170),Image.ANTIALIAS)
    new2=ImageTk.PhotoImage(reimg2)
    img_label2=tk.Label(rootwn,image=new2)
    img_label2.place(x=100,y=350)

    img3=(Image.open("po.png"))
    reimg3=img3.resize((450,170),Image.ANTIALIAS)
    new3=ImageTk.PhotoImage(reimg3)
    img_label3=tk.Label(rootwn,image=new3)
    img_label3.place(x=810,y=550)

    img2=tk.PhotoImage(file="billing.png")
    myimg2=img2.subsample(1,1)
    img3=tk.PhotoImage(file="salary.png")
    myimg3=img3.subsample(1,1)
    img4=tk.PhotoImage(file="comments.png")
    myimg4=img4.subsample(1,1)
    img5=tk.PhotoImage(file="stock.png")
    myimg5=img5.subsample(1,1)
    img7=tk.PhotoImage(file="pending.png")
    myimg7=img7.subsample(1,1)
    b2=tk.Button(image=myimg2,command=lambda: billing(rootwn))
    b2.image=myimg2
    b3=tk.Button(image=myimg3,command=lambda:salary(rootwn))
    b3.image=myimg3
    b4=tk.Button(image=myimg4,command=lambda: comments(rootwn))
    b4.image=myimg4
    b5=tk.Button(image=myimg5,command=lambda: stock(rootwn))
    b5.image=myimg5
    b7=tk.Button(image=myimg7,command=lambda: pending(rootwn))
    b7.image=myimg7

    img6=tk.PhotoImage(file="exit.png")
    myimg6=img6.subsample(1,1)
    b6=tk.Button(image=myimg6,relief="raised",command=lambda: logout(rootwn))
    b6.image=myimg6
	
    b2.place(x=100,y=150)
    b3.place(x=100,y=250)
    b4.place(x=900,y=350)
    b5.place(x=900,y=450)
    b6.place(x=100,y=650)
    b7.place(x=100,y=550)
    rootwn.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
main()

def link():
    print("hii")