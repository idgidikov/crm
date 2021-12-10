from django.urls import path
from .views import AgentListView,AgentCreateView,AgentDetailView
app_name = "agent"
urlpatterns = [
    path("",AgentListView.as_view(),name="agent-list"),
    path("create/",AgentCreateView.as_view(),name="agent-create"),
    path("<int:pk>/",AgentDetailView.as_view(),name='agent-detail'),
    # path("<int:pk>/update",LeadUpdateView.as_view(),name='agent-update'),
    # path("<int:pk>/delete/",LeadDeleteView.as_view(),name='agent-delete'),
]
