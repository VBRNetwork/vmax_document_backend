from django.apps import AppConfig


class DaysoffConfig(AppConfig):
    name = 'daysoff'

    def ready(self) -> None:
        import daysoff.receivers