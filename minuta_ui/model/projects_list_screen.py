from minuta_ui.model.base_model import BaseScreenModel
from minuta_ui.db import Project
from datetime import datetime


class ProjectsListModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """

    def __init__(self) -> None:
        super().__init__()
        self.projects_list = [
            (p.id, p.name, p.status, "nnnn")
            for p in Project.select().order_by(Project.created_date.desc())
        ]

    def add_project(self, name, path):
        Project.create(
            name=name, path=path, status=False, created_date=datetime.now()
        )
