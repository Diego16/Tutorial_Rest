from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)
schema_view = get_schema_view(title='Pastebin API')
urlpatterns = [
	url(r'^', include(router.urls)),
	url('^schema/$', schema_view),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]