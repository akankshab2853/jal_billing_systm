from django.urls import path
from .views import StaffViewset

urlpatterns = [
    path("allstaff/", StaffViewset.as_view({"get": "list"}), name="staff-list"),
    path("staffdetails/<int:pk>/",StaffViewset.as_view({"get": "retrieve"}),name="staff-retrieve",),
    path("addstaff/", StaffViewset.as_view({"post": "create"}), name="vendor-create"),
    path("updatestaff/<int:pk>/",StaffViewset.as_view({"put": "update"}),name="staff-update",),
    path("deletestaff/<int:pk>/",StaffViewset.as_view({"delete": "destroy"}),name="staff-delete",)]
