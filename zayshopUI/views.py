from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from .models import Prodct,Color,Size,ContactUsForm
# Create your views here.


class Home(ListView):
    model = Prodct
    context_object_name = 'context'
    template_name = 'pages/index.html'

    


    

class AboutUs(TemplateView):
    template_name = 'pages/about.html'

class Contact(TemplateView):
    template_name = 'pages/contact.html'


    def post(self,request,*args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactUsForm.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        return redirect('base:home')




class ShopList(ListView):
    model = Prodct
    template_name = 'pages/shop.html'
    context_object_name = 'context'

    def get_queryset(self):
        # prefetch the related objects for the many-to-many fields
        return Prodct.objects.prefetch_related('color', 'size')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # pass the prefetched related objects to the context
        context['colors'] = Color.objects.all()
        context['sizes'] = Size.objects.all()
        return context


class ShopDetail(DetailView):
    model = Prodct
    template_name = 'pages/shop-single.html'
    context_object_name = 'context'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        # retrieve the many-to-many fields
        obj.colors = obj.color.all()
        obj.sizes = obj.size.all()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # retrieve the many-to-many fields
        context['colors'] = self.object.colors
        context['sizes'] = self.object.sizes
        return context
