from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView



urlpatterns = [
    path('', views.index, name='home'),
    path('situations', views.SituationListView.as_view(), name='situations'),
    path('situation/<int:pk>', views.SituationDetailView.as_view(), name='situation_detail'),
    path('situation/create', views.SituationCreateView.as_view(success_url=reverse_lazy('situations')), name='situation_create'),
    path('situation/<int:pk>/update', views.SituationUpdateView.as_view(success_url=reverse_lazy('situations')), name='situation_update'),
    path('situation/<int:pk>/delete', views.SituationDeleteView.as_view(success_url=reverse_lazy('situations')), name='situation_delete'),
    path('situation/<int:pk>/comment', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(success_url=reverse_lazy('situations')), name='comment_delete'),
    # path('countries', views.CountryListView.as_view(), name='countries'),
    # path('country/<int:pk>', views.CountryDetailView.as_view(), name='country_detail'),
    path('search', views.search, name='search'),
]
