from .base_page import BasePage


# В данный момент функционал главной страницы пока дублирует BasePage
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
