from django.apps import AppConfig


class HeytrafficAppConfig(AppConfig):
    name = 'heytraffic'

    def ready(self):
        from heytraffic.signals.post_save import post_save_site
