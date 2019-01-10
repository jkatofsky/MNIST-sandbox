from tkinter import *
from PIL import Image, ImageDraw


class Drawing:
    def __init__(self, parent):

        self.width = 450
        self.height = 450

        self.thickness = 50

        self.drawingFrame = Frame(parent, borderwidth=2, relief=RIDGE)
        self.drawingFrame.pack()

        self.canvasFrame = Frame(self.drawingFrame, borderwidth=2, relief=RIDGE)
        self.canvasFrame.pack(side=TOP)

        self.canvas = Canvas(self.canvasFrame, bg='white', width=self.width, height=self.height)
        self.canvas.pack()

        self.image = Image.new("L", (self.width, self.height), 255)
        self.imageDraw = ImageDraw.Draw(self.image)

        self.canvasControlsFrame = Frame(self.drawingFrame)
        self.canvasControlsFrame.pack(side=BOTTOM)

        self.clearCanvasButton = Button(self.canvasControlsFrame, text="CLEAR", command=self.clear)
        self.clearCanvasButton.pack(side=LEFT)

        self.thicknessSliderLabel = Label(self.canvasControlsFrame, text="Width:")
        self.thicknessSliderLabel.pack(side=LEFT)
        self.thicknessSlider = Scale(self.canvasControlsFrame, from_=20, to=80, orient='horizontal',
                                     length=150, command=self.updateWidth)
        self.thicknessSlider.set(self.thickness)
        self.thicknessSlider.pack(side=LEFT)

        self.alphaSliderLabel = Label(self.canvasControlsFrame, text="Alpha:")
        self.alphaSliderLabel.pack(side=LEFT)
        self.alphaSlider = Scale(self.canvasControlsFrame, from_=0, to=255, orient='horizontal',
                                 length=150, command=self.updateColorVariables)
        self.alphaSlider.pack(side=LEFT)

        self.updateColorVariables(None)

        self.canvas.bind('<B1-Motion>', self.dot)
        self.canvas.bind('<Button-1>', self.dot)

    def updateWidth(self, event):
        self.thickness = self.thicknessSlider.get()

    def updateColorVariables(self, event):
        alpha = self.alphaSlider.get()
        self.alpha = int(alpha)
        self.color = "#%02x%02x%02x" % (alpha, alpha, alpha)

    def clear(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (self.width, self.height), 255)
        self.imageDraw = ImageDraw.Draw(self.image)

    def dot(self, event):
        radius = self.thickness/2
        self.canvas.create_oval(event.x - radius, event.y - radius,
                                event.x + radius, event.y + radius, fill=self.color, outline="")
        self.imageDraw.ellipse((event.x - radius, event.y - radius,
                                event.x + radius, event.y + radius), fill=self.alpha)

    def getDrawingPixelList(self):
        copy = self.image.copy()
        smaller = copy.resize((28, 28))
        pixels = list(smaller.getdata())
        return pixels
