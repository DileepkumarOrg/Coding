from tkinter import *
root = Tk()
root.title("Logic Gates")
root.geometry("1200x900")
bg_color = "#00FF00"
fg_color = "white"
lbl_color = 'white'
title = Label(root,text = "Logic Gtaes",bd = 12,relief = GROOVE,bg = bg_color,font=("times new roman",30,"bold").grid(row =0,column = 4))
label1 = Label(root,text="AND GATE",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0)
