from django.urls import path,include
from home.views import index,person,ClassPerson,PersonViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'person',PersonViewSets,basename='Person')
urlpatterns = router.urls


urlpatterns = [
    path('',include(router.urls)),
    path('index/', index,name='index'),
    path('person/',person,name='person'),
    path('classperson/',ClassPerson.as_view(),name='classperson')
]
