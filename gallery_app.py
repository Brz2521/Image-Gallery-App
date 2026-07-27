import tkinter as tk
from tkinter import filedialog, simpledialog, Menu
from PIL import Image, ImageTk

from image_item import ImageItem
from gallery import Gallery


class GalleryApp:

    THUMBNAIL_SIZE = (150, 150)

    def __init__(self, root):

        self.root = root
        self.root.title("Image Gallery")

        self.gallery = Gallery()

        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        post_button = tk.Button(
            root,
            text="Post Image",
            command=self.post_image
        )

        post_button.pack()

        self.refresh_gallery()

    def post_image(self):

        filename = filedialog.askopenfilename(
            filetypes=[
                ("Images", "*.png *.jpg *.jpeg *.gif *.bmp")
            ]
        )

        if not filename:
            return

        title = simpledialog.askstring(
            "Image Title",
            "Enter a title:"
        )

        if not title:
            title = "Untitled"

        image = ImageItem(title, filename)

        self.gallery.post_image(image)

        self.refresh_gallery()

    def refresh_gallery(self):

        for widget in self.frame.winfo_children():
            widget.destroy()

        for image in self.gallery.get_images():

            pil = Image.open(image.filepath)
            pil.thumbnail(self.THUMBNAIL_SIZE)

            photo = ImageTk.PhotoImage(pil)

            button = tk.Button(
                self.frame,
                image=photo,
                text=image.title,
                compound="top"
            )

            button.image = photo

            button.bind(
                "<Button-3>",
                lambda event, img=image: self.show_menu(event, img)
            )

            button.pack(side="left", padx=10, pady=10)

    def show_menu(self, event, image):

        menu = Menu(self.root, tearoff=0)

        menu.add_command(
            label="Duplicate",
            command=lambda: self.duplicate(image)
        )

        menu.add_command(
            label="Delete",
            command=lambda: self.delete(image)
        )

        menu.add_command(
            label="Save As",
            command=lambda: self.save(image)
        )

        menu.post(event.x_root, event.y_root)

    def duplicate(self, image):

        self.gallery.duplicate_image(image)
        self.refresh_gallery()

    def delete(self, image):

        self.gallery.delete_image(image)
        self.refresh_gallery()

    def save(self, image):

        filename = filedialog.asksaveasfilename()

        if filename:
            image.save_as(filename)