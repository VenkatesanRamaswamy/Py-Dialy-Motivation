from tkinter import *
import requests

def get_quote():
    response=requests.get("https://api.kanye.rest")
    quote1=response.json()
    quote2=quote1["quote"]
    canvas1.itemconfigure(text_item, text=quote2 )
    #print(quote2)
    # print1_text(text12=quote2)  

# def print1_text(text12):
#     canvas1.itemconfigure(text_item, text=text12 )
    #print(text12)

#text1=get_quote()
window=Tk()
window.title("Kanye Quotes")
window.configure(bg="grey",padx=25,pady=25)

canvas1=Canvas(width=400,height=450,bg='grey',highlightthickness=0,highlightcolor='grey')
#canvas1.configure()
image1=PhotoImage(file="background.png")
canvas1.create_image(200,200, image=image1)
text_item=canvas1.create_text(200,150, text="",font=(('arial'),20,'bold'), width=275,anchor="center")


canvas1.grid(column=1,row=0)


image2=PhotoImage(file="kanye.png")
button1=Button(image=image2,command=get_quote,bg='white',highlightthickness=0,highlightcolor='grey')
button1.grid(column=1,row=2)








window.mainloop()
























# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)



# window.mainloop()