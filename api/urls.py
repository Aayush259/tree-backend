from django.urls import path
from .views import TreeView

urlpatterns = [
    path('tree/', TreeView.as_view(), name='tree-operations'),
]
