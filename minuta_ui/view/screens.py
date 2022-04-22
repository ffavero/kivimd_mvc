# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.

from minuta_ui.model.projects_list_screen import ProjectsListModel
from minuta_ui.control.projects_list_screen import ProjectsListController

from minuta_ui.model.analysis_screen import AnalysisModel
from minuta_ui.control.analysis_screen import AnalysisController

screens = {
    "analysis": {
        "model": AnalysisModel,
        "controller": AnalysisController,
        "text": "Strategy Optimization",
        "icon": "chart-timeline",
    },
    "projects list": {
        "model": ProjectsListModel,
        "controller": ProjectsListController,
        "text": "Open recent Projects",
        "icon": "history",
    },
}
