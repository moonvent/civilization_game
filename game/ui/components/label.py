from kivy.uix.label import Label

from game.services.aliases import Alias
from game.services.utils.observer import Observer


class CustomLabel(Label, Observer):
    _meta_info: Alias.WidgetKivyMetaInfo

    def __init__(self, *arg, meta_label_name: str, **kwargs):
        super().__init__(**kwargs)
        self._meta_info = Alias.WidgetKivyMetaInfo(title=meta_label_name)

    def update_by_publisher(self, data: Alias.WidgetUpdateData):
        if self._meta_info.title == data.widget_title:
            self.text = str(data.value)
