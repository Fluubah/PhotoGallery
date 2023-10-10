from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_file("PhotoGallery.kv")


class PhotoGalleryApp(App):
    pass


class Display(Screen):
    def display_image(self):
        pass


PhotoGalleryApp().run()
