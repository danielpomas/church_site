from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.db.models import Q
from django.urls import reverse_lazy

from accounts.forms import UpdateUserForm
from accounts.models import User
from church_site.views import AdminListView, BaseUpdateView, BaseCreateView


class UsersAdminListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'accounts.view_user'
    model = get_user_model()
    context_object_name = 'users'
    template_name = 'accounts/users-admin-list.html'
    page_title = 'Users - Admin'
    current_page = 'manage'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(Q(member__in=self.request.user.churches.all()) | Q(member__isnull=True)).distinct()


class UsersAdminUpdateView(PermissionRequiredMixin, BaseUpdateView):
    permission_required = 'accounts.change_user'
    model = get_user_model()
    template_name = 'admin-form-view.html'
    form_class = UpdateUserForm
    success_url = reverse_lazy('accounts:users-admin-list')
    page_title = 'Update User - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('accounts:users-admin-list')

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(Q(member__in=self.request.user.churches.all()) | Q(member__isnull=True)).distinct()


class GroupsAdminListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'auth.view_group'
    model = Group
    context_object_name = 'groups'
    template_name = 'accounts/groups-admin-list.html'
    page_title = 'Groups - Admin'
    current_page = 'manage'
    btn_add_href = reverse_lazy('accounts:groups-admin-create')


class GroupsAdminCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = 'auth.add_group'
    model = Group
    fields = ['name', 'permissions']
    template_name = 'admin-form-view.html'
    success_url = reverse_lazy('accounts:groups-admin-list')
    page_title = 'New Group - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('accounts:groups-admin-list')


class GroupsAdminUpdateView(PermissionRequiredMixin, BaseUpdateView):
    permission_required = 'auth.change_group'
    model = Group
    fields = ['name', 'permissions']
    template_name = 'admin-form-view.html'
    success_url = reverse_lazy('accounts:groups-admin-list')
    page_title = 'Update Group - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('accounts:groups-admin-list')
