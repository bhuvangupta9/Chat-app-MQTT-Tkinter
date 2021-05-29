import paho.mqtt.client as mqtt
import tkinter as tk

root = tk.Tk()

root.title("Chat Room")

canvas = tk.Canvas(root, width=600, height=700)
canvas.grid(columnspan=3, rowspan=5)

nick = tk.StringVar()

nickname = tk.Entry(root, textvariable= nick, width=50)
nickname.grid(row=0, column=1, padx=45, pady=10)

txtMessages = tk.Text(root, width=50)
txtMessages.grid(row=2, column=1, padx=45, pady=10)
txtMessages.configure(state='disabled')

txtyour = tk.StringVar()

txtYourMessage = tk.Entry(root, textvariable= txtyour, width=50)
txtYourMessage.grid(row=3, column=1, padx=45, pady=10)
txtYourMessage.insert(tk.END, "Your Message")

def sendMessage():
    nn = nick.get()
    msg = txtyour.get()
    client.publish("home", nn+": "+msg)
    txtYourMessage.delete(0, "end")

btnSendMessage = tk.Button(root, text="Send Message", width=20, command=sendMessage)
btnSendMessage.grid(row=4, column=1, padx=10, pady=10)

def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    print("message received " , msg)
    txtMessages.configure(state='normal')
    txtMessages.insert(tk.END, msg+"\n")
    txtMessages.configure(state='disabled')

broker_address="mqtt.eclipseprojects.io"

print("creating new instance")
client = mqtt.Client()
client.on_message=on_message

print("connecting to broker")
client.connect(broker_address)

print("Subscribing to topic","home")
client.subscribe("home")

client.loop_start()

root.mainloop()