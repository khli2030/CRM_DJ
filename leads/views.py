from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Lead, User, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreation

# CRUD+L Create, Retrieve, Update, Delete, and List


class SignupView(LoginRequiredMixin, generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreation

    def get_success_url(self):
        # Reverse takes works by the URL name convention
        return reverse('leads:leads-list')


class LandingTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'landing.html'


def landing_page(request):
    return render(request, 'landing.html')


class LeadListView(LoginRequiredMixin, ListView):
    template_name = 'leads/leads_list.html'
    # This must be set to bring all data pass it to the context
    queryset = Lead.objects.all()
    # This for the context goes to the Template HTML file
    context_object_name = "leads"


def leads_list(request):
    leads = Lead.objects.all()
    # return render(request,'leads/home_page.html')
    print(leads)
    context = {
        "leads": leads
    }
    return render(request, 'leads/leads_list.html', context)


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = 'leads/lead_details.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


def lead_details(request, pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    print(lead)
    context = {
        "lead": lead
    }

    return render(request, 'leads/lead_details.html', context)


class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        print('done')
        # Reverse takes works by the URL name convention
        return reverse('leads:leads-list')

    def form_valid(self, form):
        print('email has been sent')
        send_mail(subject='This is just for a new lead created sub',
                  message='please notes we had created your acount',
                  from_email='test@test.com',
                  recipient_list=['whilist@test.com'])

        return super(LeadCreateView, self).form_valid(form)


def create_lead(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()  # Create object base on the model defined

            return redirect('/leads')
    context = {
        "form": form
    }
    return render(request, 'leads/lead_create.html', context)


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-update')


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()  # related to ModelForm will save the data auto

            return redirect('/leads')
    context = {
        'form': form,
        'lead': lead
    }
    return render(request, 'leads/lead_update.html', context)


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:leads-list')


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()

    return redirect('/leads')
# def create_lead(request):
#     form = LeadModelForm()
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save() # Create object base on the model defined

#             return redirect('/leads')
#     context = {
#         "form" : form
#     }
#     return render(request,'create_lead.html',context)
