import tkinter
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(text, text=quote)


window = tkinter.Tk()
window.title("Kanye says...")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(height=414, width=300)
picture = tkinter.PhotoImage(file="background.png")
canvas.create_image(150, 207, image=picture)
text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 18, "bold"))
canvas.grid(column=0, row=0)

get_quote()

kanye_img = tkinter.PhotoImage(file="kanye.png")
button = tkinter.Button(image=kanye_img, highlightthickness=0, command=get_quote)
button.grid(column=0, row=1)

window.mainloop()