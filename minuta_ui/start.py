"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""
import os
from typing import NoReturn

from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.card.card import MDSeparator

from minuta_ui.view.screens import screens
from minuta_ui.__config__ import images
from minuta_ui.db import create_tables


KV = """
#:import images_path minuta_ui.__config__.images


<ItemDrawer>:
    theme_text_color: "Custom"
    on_press:
        self.parent.set_color_item(self)
        app.root.ids.manager_screens.current = self.ref_id
        app.root.ids.toolbar.title = self.text
        app.root.ids.nav_drawer.set_state("close")
    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color

<MinutaScreen>:
    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Open recent Project"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
    MDNavigationLayout:
        x: toolbar.height
        size_hint_y: 1.0 - toolbar.height/root.height
        ScreenManager:
            id: manager_screens
        MDNavigationDrawer:
            id: nav_drawer
            MDBoxLayout:
                id: content_drawer
                screen_manager: manager_screens
                nav_drawer: nav_drawer
                orientation: "vertical"
                padding: "8dp"
                spacing: "8dp"

                AnchorLayout:
                    anchor_x: "left"
                    size_hint_y: None
                    height: avatar.height

                    Image:
                        id: avatar
                        size_hint: None, None
                        size: "56dp", "56dp"
                        source: f"{images_path}/logo_black.png"

                MDLabel:
                    text: "Minuta"
                    font_style: "Button"
                    adaptive_height: True

                MDLabel:
                    text: "from Calidris"
                    font_style: "Caption"
                    adaptive_height: True
                ScrollView:
                    DrawerList:
                        id: md_list
"""


class MinutaScreen(MDScreen):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))
    ref_id = StringProperty()


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class Minuta(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_string(KV)
        self.load_all_kv_files(self.directory)
        create_tables()

        # This is the screen manager that will contain all the screens of your
        # application.
        self.theme_cls.material_style = "M3"
        self.icon = os.path.join(images, "logo.png")
        self.title = "Minuta"
        self.app = MinutaScreen()
        self.manager_screens = self.app.ids.manager_screens

    def build(self):
        """
        Initializes the application; it will be called only once.
        If this method returns a widget (tree), it will be used as the root
        widget and added to the window.

        :return:
            None or a root :class:`~kivy.uix.widget.Widget` instance
            if no self.root exists.
        """

        self.theme_cls.primary_palette = "Cyan"
        self.generate_application_screens()
        # return self.manager_screens
        return self.app

    def generate_application_screens(self) -> NoReturn:
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """
        len_screens = len(screens)
        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)
            self.app.ids.md_list.add_widget(
                ItemDrawer(
                    icon=screens[name_screen]["icon"],
                    text=screens[name_screen]["text"],
                    ref_id=name_screen,
                )
            )
            # Add a line above the last 3 screens - Settings and other stuff
            if i < len_screens - 3:
                self.app.ids.md_list.add_widget(MDSeparator())


Minuta().run()
