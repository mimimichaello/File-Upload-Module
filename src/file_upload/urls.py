from django.urls import path
from .views import FileUploadView, UploadedFilesListView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='upload_file'),
    path('files/', UploadedFilesListView.as_view(), name='uploaded_files_list'),
]
