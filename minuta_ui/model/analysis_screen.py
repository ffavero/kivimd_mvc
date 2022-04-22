from minuta_ui.model.base_model import BaseScreenModel


class AnalysisModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """

    def __init__(self):
        self._date_start = "1-1-2021"
        self._date_end = "31-12-2021"
        self._is_os_ratio = 0.25
        self._testing_period = 40

    @property
    def testing_period(self):
        return self._testing_period

    @property
    def testing_period_str(self):
        return str(self._testing_period)

    @property
    def testing_ratio(self):
        return self._is_os_ratio

    @property
    def testing_ratio_str(self):
        return str(self._is_os_ratio)

    @property
    def date_start(self):
        return self._date_start

    @property
    def date_end(self):
        return self._date_end
