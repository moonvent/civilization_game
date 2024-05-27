from kivy.uix.label import Label
from entities import Community


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

from game.services.entities.community import CommunityService
from game.services.entities.perks.start_community import StartCommunityPerk


class UiApp(App):
    __community: Community
    __layout: FloatLayout

    __community_info: Label
    __create_community_button: Button

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__community = None

    def build(self):
        # Создание FloatLayout
        self.__layout = layout = FloatLayout()

        # Создание кнопки 1
        self.__create_community_button = btn1 = Button(
            text="Создать комьюнити",
            size_hint=(
                0.2,
                0.1,
            ),  # Процентное указание размера кнопки относительно родителя
            pos_hint={
                'center_x': 0.5,
                'center_y': 0.55,
            },  # Позиционирование в центре экрана
        )

        btn1.on_press = self.__create_new_community

        # Создание кнопки 2
        btn2 = Button(
            text="Прокачать первый перк",
            size_hint=(0.2, 0.1),
            pos_hint={
                'center_x': 0.5,
                'center_y': 0.45,
            },  # Сдвиг вниз относительно первой кнопки
        )

        btn2.on_press = lambda: print('sex 2')

        # Добавление кнопок в layout
        layout.add_widget(btn1)
        layout.add_widget(btn2)

        return layout

    def __create_new_community(self):

        if not self.__community:
            community_service = CommunityService()
            self.__community = community_service.start_new_community()
            self.__community_info = community_data = Label(text='Новое комьюнити')
            self.__community_info.size_hint = self.__create_community_button.size_hint
            self.__community_info.pos_hint = self.__create_community_button.pos_hint
            self.__layout.add_widget(community_data)
            self.__layout.remove_widget(self.__create_community_button)

    def __level_up_start_community(self):
        StartCommunityPerk(community=self.__community)


def start_game():
    UiApp().run()
