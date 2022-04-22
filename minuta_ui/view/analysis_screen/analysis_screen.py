from typing import NoReturn

from minuta_ui.view.base_screen import BaseScreenView


class AnalysisScreenView(BaseScreenView):
    def model_is_changed(self) -> NoReturn:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        print("hi")
