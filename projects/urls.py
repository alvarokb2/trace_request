from django.urls import path
from .views import ProjectListView, ProjectCreateView,ProjectDetailView, ProjectUpdateView,ProjectDeleteView

app_name = "projects"

urlpatterns = [
    path('', ProjectListView.as_view(), name="home"),
    path('create/', ProjectCreateView.as_view(), name="create"),
    path('<int:pk>/', ProjectDetailView.as_view(), name="detail"),
    path('update/<int:pk>', ProjectUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', ProjectDeleteView.as_view(), name="delete"),
]
