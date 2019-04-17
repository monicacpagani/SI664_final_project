
from idp_app.models import Situation, Country, Comment
from django.views import View
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from idp_app.util import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.uploadedfile import InMemoryUploadedFile
from idp_app.forms import CommentForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError
from django.db.models import Q


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_situations = Situation.objects.all().count()
    num_countries = Country.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_situations': num_situations,
        'num_countries': num_countries,
        'num_visits': num_visits,
    }


    # Render the HTML template home.html with the data in the context variable
    return render(request, 'home.html', context=context)


class SituationListView(OwnerListView):
    model = Situation
    template_name = "situation_list.html"

class SituationDetailView(OwnerDetailView):
    model = Situation
    template_name = "situation_detail.html"

    def get(self, request, pk) :
        situation = Situation.objects.get(id=pk)
        comments = Comment.objects.filter(situation=situation).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'situation' : situation, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)

class SituationCreateView(OwnerCreateView):
    model = Situation
    fields = ['name', 'country', 'population_estimate', 'focal_point', 'situation_type', 'year', 'aid_provider', 'description']
    template_name = "situation_form.html"

class SituationUpdateView(OwnerUpdateView):
    model = Situation
    fields = ['name', 'country', 'population_estimate', 'focal_point', 'situation_type', 'year', 'aid_provider', 'description']
    template_name = "situation_form.html"

class SituationDeleteView(OwnerDeleteView):
    model = Situation
    template_name = "situation_delete.html"

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Situation, id=pk)
        comment_form = CommentForm(request.POST)

        comment = Comment(text=request.POST['comment'], owner=request.user, situation=f)
        comment.save()
        return redirect(reverse_lazy('situation_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        situation = self.object.situation
        return reverse_lazy('situation_detail', args=[situation.id])

# class CountryListView(OwnerListView):
#     model = Situation
#     template_name = "country_list.html"

# class CountryDetailView(generic.DetailView):
#     model = Situation
#     template_name = "country_detail.html"

#     # def get_queryset(self):
#     #     return Situation.objects.filter(country = self.request.user)

def search(request):
     if request.method == 'GET' and request.GET.get("searchTerm") is not None:
         print(request.GET.get("searchTerm"))
         situation_name = request.GET.get("searchTerm")
         s = Situation.objects.filter(name__icontains=situation_name)
         print(s)
         return render(request,"search.html", {"situation": s})
     else:
         return render(request,"search.html")

