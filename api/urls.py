from django.urls import path
from . import views


urlpatterns = [
    path('', views.viewTools),
    path('addTool/', views.addTools),
    path('getTool/<int:id>', views.getTool),
    path('updateTool/<int:id>', views.updateTool),
    path('deleteTool/<int:id>', views.deleteTool)
]
