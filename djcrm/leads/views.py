from django.shortcuts import render,redirect,reverse
from .models import Agent, Lead
from django.http import HttpResponse
from .forms import LeadModelForm,LeadForm
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.
class LandingPageView(TemplateView):
    template_name = "leads/landing.html"

def landing_page(request):
    return render(request,"leads/landing.html")

class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset=Lead.objects.all()
    context_object_name = "leads"

# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         "leads" : leads
#     }
#     return render(request,"leads/lead_list.html",context)

class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset=Lead.objects.all()
    context_object_name = "lead"

# def lead_detail(request,pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         "lead" : lead
#     }
#     return render(request, "leads/lead_detail.html",context)

class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    def get_success_url(self) -> str:
        return reverse("leads:lead-list")
# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             # if use models form there is no need of this but for update is need:
#             # first_name = form.cleaned_data["first_name"]
#             # last_name = form.cleaned_data["last_name"]
#             # age = form.cleaned_data["age"]
#             # agent = form.cleaned_data["agent"]
#             # Lead.objects.create(
#             #     first_name = first_name,
#             #     last_name = last_name,
#             #     age= age,
#             #     agent = agent
#             # )
#             form.save()
#             print("lead has been created")
#             return redirect("/leads")
#     context = {
#         "form":form
#     }
#     return render(request,"leads/lead_create.html",context)
class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    def get_success_url(self) -> str:
        return reverse("leads:lead-list")

# def lead_update(request,pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == "POST":
#         form = LeadModelForm(request.POST,instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {
#          "lead" : lead,
#          "form":form,
#      }
#     return render(request,"leads/lead_update.html",context)
#     return render(request,"leads/lead_update.html",context)
# def lead_update(request,pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data["first_name"]
#             last_name = form.cleaned_data["last_name"]
#             age = form.cleaned_data["age"]
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect("/leads")
#     context = {
#         "lead" : lead,
#         "form":form,
#     }
#     return render(request,"leads/lead_update.html",context)
class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    def get_success_url(self) -> str:
        return reverse("leads:lead-list")

# def lead_delete(request,pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect("/leads")