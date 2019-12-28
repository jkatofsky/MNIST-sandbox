from tkinter import *
from PIL import Image, ImageDraw


class Drawing:
    def __init__(self, parent):

        self.width = 450
        self.height = 450

        self.thickness = 50

        self.drawing_frame = Frame(parent, borderwidth=2, relief=RIDGE)
        self.drawing_frame.pack()

        self.canvas_frame = Frame(self.drawing_frame, borderwidth=2, relief=RIDGE)
        self.canvas_frame.pack(side=TOP)

        self.canvas = Canvas(self.canvas_frame, bg='white', width=self.width, height=self.height)
        self.canvas.pack()

        self.image = Image.new("L", (self.width, self.height), 255)
        self.image_draw = ImageDraw.Draw(self.image)

        self.canvas_controls_frame = Frame(self.drawing_frame)
        self.canvas_controls_frame.pack(side=BOTTOM)

        self.clear_canvas_button = Button(self.canvas_controls_frame, text="CLEAR", command=self.clear)
        self.clear_canvas_button.pack(side=LEFT)

        self.tickness_slider_label = Label(self.canvas_controls_frame, text="Width:")
        self.tickness_slider_label.pack(side=LEFT)
        self.thickness_slider = Scale(self.canvas_controls_frame, from_=20, to=80, orient='horizontal',
                                      length=150, command=self.update_width)
        self.thickness_slider.set(self.thickness)
        self.thickness_slider.pack(side=LEFT)

        self.alpha_slider_label = Label(self.canvas_controls_frame, text="Alpha:")
        self.alpha_slider_label.pack(side=LEFT)
        self.alpha_slider = Scale(self.canvas_controls_frame, from_=0, to=255, orient='horizontal',
                                  length=150, command=self.update_color_vars)
        self.alpha_slider.pack(side=LEFT)

        self.update_color_vars(None)

        self.canvas.bind('<B1-Motion>', self.dot)
        self.canvas.bind('<Button-1>', self.dot)

    def update_width(self, event):
        self.thickness = self.thickness_slider.get()

    def update_color_vars(self, event):
        alpha = self.alpha_slider.get()
        self.alpha = int(alpha)
        self.color = "#%02x%02x%02x" % (alpha, alpha, alpha)

    def clear(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (self.width, self.height), 255)
        self.image_draw = ImageDraw.Draw(self.image)

    def dot(self, event):
        radius = self.thickness / 2
        self.canvas.create_oval(event.x - radius, event.y - radius,
                                event.x + radius, event.y + radius, fill=self.color, outline="")
        self.image_draw.ellipse((event.x - radius, event.y - radius,
                                 event.x + radius, event.y + radius), fill=self.alpha)

    def get_pixel_list(self):
        copy = self.image.copy()
        smaller = copy.resize((28, 28))
        pixels = list(smaller.getdata())
        return pixels
