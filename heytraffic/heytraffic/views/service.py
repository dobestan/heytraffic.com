from django.views.generic import TemplateView


class ServiceView(TemplateView):
    """
    제공하는 각각의 서비스들( 웹 트래픽, 페이스북, 트위터 등 )에 대해서는
    뷰에서 처리하기로 결정하였습니다.
    """
    pass


class TrafficServiceView(ServiceView):
    template_name = 'services/traffic.html'


class FacebookServiceView(ServiceView):
    template_name = 'services/facebook.html'


class TwitterServiceView(ServiceView):
    template_name = 'services/twitter.html'


class InstagramServiceView(ServiceView):
    template_name = 'services/instagram.html'


class YoutubeServiceView(ServiceView):
    template_name = 'services/youtube.html'
