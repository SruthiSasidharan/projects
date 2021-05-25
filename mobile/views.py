from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView
from .models import Brand,Mobiles
from .forms import BrandCreateForm,MobileCreateForm,MobileUpdateForm
from django.urls import  reverse_lazy
# Create your views here.
def index(request):
    return render(request,"mobile/base.html")

class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandCreateForm
    template_name = "mobile/brandcreate.html"
    success_url = reverse_lazy("index")

class MobileCreateView(CreateView):
    model = Mobiles
    form_class = MobileCreateForm
    template_name = "mobile/createmobile.html"
    success_url = reverse_lazy("index")

class MobileListView(ListView):
    model = Mobiles
    context_object_name = "mobiles"
    template_name = "mobile/listallmobile.html"

class MobileUpdate(UpdateView):
    model = Mobiles
    form_class = MobileUpdateForm
    template_name = "mobile/update.html"
    success_url = reverse_lazy("list")
