from minuta_ui.view.analysis_screen.analysis_screen import AnalysisScreenView
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime


class AnalysisController:
    """
    The `ProjectsListController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model
        self.view = AnalysisScreenView(controller=self, model=self.model)

    def get_view(self) -> AnalysisScreenView:
        return self.view

    def set_testing_ratio(self, value):
        step_value = round(float(value) / 0.05) * 0.05
        self.model._is_os_ratio = round(step_value, 2)
        self.view.ids.testing_ratio.text = self.model.testing_ratio_str

    def set_testing_period(self, value):
        self.model._testing_period = int(value)
        self.view.ids.testing_period.text = self.model.testing_period_str

    def diff_testing_period(self, value):
        diff_res = self.model._testing_period + value
        if diff_res >= 240 or diff_res <= 40:
            return
        self.model._testing_period = diff_res
        self.view.ids.testing_period.text = self.model.testing_period_str

    def show_date_picker(self):
        date_dialog = MDDatePicker(
            title="Testing Range",
            title_input="Testing Range",
            mode="range",
            min_year=2018,
            max_year=datetime.now().year,
        )
        date_dialog.bind(
            on_save=self.datepicker_save, on_cancel=self.datepicker_cancel
        )
        date_dialog.open()

    def datepicker_save(self, instance, value, date_range):
        try:
            self.model._date_start = date_range[0].strftime("%d-%m-%y")
            self.model._date_start = date_range[-1].strftime("%d-%m-%y")
            self.view.ids.date_start.text = self.model.date_start
            self.view.ids.date_end.text = self.model.date_end
        except IndexError:
            pass

    def datepicker_cancel(self, instance, value):
        self.view.ids.date_start.text = self.model.date_start
        self.view.ids.date_end.text = self.model.date_end
