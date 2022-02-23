from django.http.response import HttpResponseRedirect
from authapp.models import ShopUser
from adminapp.utils import superuser_required_decorator
from adminapp.forms import ShopUserAdminForm, ShopUserCreateAdminForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator


class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    paginate_by = 5

    @method_decorator(superuser_required_decorator)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user_edit.html'
    form_class = ShopUserCreateAdminForm
    success_url = reverse_lazy('admin:users')

    # fields = '__all__'

    @method_decorator(superuser_required_decorator)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UserEditView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_edit.html'
    form_class = ShopUserAdminForm
    success_url = reverse_lazy('admin:users')

    # fields = '__all__'

    @method_decorator(superuser_required_decorator)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование'
        return context


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin:users')

    @method_decorator(superuser_required_decorator)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить'
        return context
