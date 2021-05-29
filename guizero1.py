from guizero import App, Text,Picture
app = App(title="Hello world")
message = Text(app, text="Welcome to the app")
message.text_size=50
message.font="Comic Sans"
app.bg = "green"
message = Picture(app,image="960x0.jpg")

app.display()
