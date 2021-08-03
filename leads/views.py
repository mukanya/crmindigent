from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.core.files.storage import FileSystemStorage
from .models import Lead, Agent, Category, Book
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm, LeadCategoryUpdateForm, BookForm


  # CRUD+L classes

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class LandingPageView(TemplateView):
    template_name = "landing.html"

# Create your views here.
def landing_page(request):
    return render(request,"landing.html")

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request,"leads/lead_list.html", context)

class LeadListView(LoginRequiredMixin, ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)

class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

def lead_create(request):
   # form = LeadForm()
    form = LeadModelForm()
    if request.method == "POST":
       # form = LeadForm(request.POST)
       form = LeadModelForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)


class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        # TODO send email to notify indigent creation
        send_mail(
            subject="The indigent has been created",
            message="Go to indigent management app to view this indigent",
            from_email="indegentClark@gov.za",
            recipient_list = ["cfo@gov.za"]
        )
        return super(LeadCreateView, self).form_valid(form)

class DocumentUp(TemplateView):
    template_name = "home.html"

class DocumentListView(LoginRequiredMixin, ListView):
    #model = Book
    template_name = "book_list.html"
   # context_object_name = 'books'
    queryset = Book.objects.all()
    form_class = BookForm

def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES('document')
        fs = FileSystemtorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

def BooklistView(request):
    books = Book.objects.all()
    return render(request, 'book_list.html',{
        'books': books,
    })


def UploadbookView(request):
    if request.method == "POST":
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('leads:lead-list')
    else:
          form = BookForm()     
    return render(request, 'upload_book.html', { 
        'form': form
    })


    #def get_success_url(self):
       # return reverse("leads:lead-list")

class UploadView(TemplateView):
     
    template_name = "leads/upload.html"   # check this to correct direction
    
    def get_success_url(self):
        return reverse("leads:lead-list")        # reverse

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
   # form = LeadForm()
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
       # form = LeadForm(request.POST)
       form = LeadModelForm(request.POST, instance=lead)
       if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
         "lead": lead,
         "form": form
    }
    return render(request, "leads/lead_update.html", context)

class CategoryListView(LoginRequiredMixin, ListView):
    template_name = "leads/category_list.html"
    context_object_name = "category_list"
    
    def get_queryset(self):
        user = self.request.user

        if user.is_organisor:
            queryset = Category.objects.filter(
                organisation=user.userprofile
            )
        else:
            queryset = Category.objects.filter(
                organisation=user.agent.organisation
            )
        return queryset


class CategoryDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/category_detail.html"
    context_object_name ="category"

    # def get_context_data(self, **kwargs):
    #     context = super(CategoryDetailView, self).get_context_data(**kwargs)
    #     leads = self.get_object().leads.all()
    #     context.update ({
    #         "leads": leads
    #     })
    #     return context

    def get_queryset(self):
        user = self.request.user

        if user.is_organisor:
            queryset = Category.objects.filter(
                organisation=user.userprofile
            )
        else:
            queryset = Category.objects.filter(
                organisation=user.userprofile       #removed organisation=user.agent.organisation
            )
        return queryset

class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")

class LeadCategoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "leads/lead_category_update.html"
    queryset = Lead.objects.all()
    form_class = LeadCategoryUpdateForm

    def get_success_url(self):
        return reverse("leads:lead-detail", kwargs={"pk": self.get_object().id})


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect("/leads")

#     context = {
#         "lead": lead,
#         "form": form
#     }
#     return render(request, "leads/lead_update.html", context)

# return HttpResponse("here is our Home route")
# return render(request, "leads/")



