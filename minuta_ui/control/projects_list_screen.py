from minuta_ui.view.projects_list_screen.projects_list_screen import (
    ProjectsListView,
)
from minuta_ui.model.projects_list_screen import ProjectsListModel


class ProjectsListController:
    """
    The `ProjectsListController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model
        self.view = ProjectsListView(controller=self, model=self.model)

    def get_view(self) -> ProjectsListView:
        return self.view
