from typing import NoReturn

from kivy.metrics import dp
from minuta_ui.view.base_screen import BaseScreenView
from kivymd.uix.datatables import MDDataTable


class ProjectsListView(BaseScreenView):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.data_tables = MDDataTable(
            column_data=[
                ("Id", dp(10)),
                ("Name", dp(60)),
                ("Status", dp(30)),
                ("Actions", dp(30)),
            ],
            row_data=self.model.projects_list,
        )
        self.add_widget(self.data_tables)
        self.model.add_project("aaa", "bbb")

    def model_is_changed(self) -> NoReturn:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
