from django.urls import path

from .views import(
todo_list,
todo_create,
todo_details,
todo_update,
todo_update,
todo_delete,
)
app_name='Todos'

urlpatterns = [
    path('',todo_list),
    path('create/', todo_create),
    path('<id>/', todo_details),
    path('<id>/update/', todo_update),
    path('<id>/delete/', todo_delete),

]