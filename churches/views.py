from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from church_site.views import AdminListView, BaseCreateView, BaseUpdateView

from churches.models import Church, Person
from churches.forms import SpeakerCreateForm


# Admin Pages

class AdminSpeakersCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = 'churches.add_speaker'
    page_title = 'New Speaker - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('churches:admin-speakers-list')
    model = Person
    template_name = 'admin-form-view.html'
    form_class = SpeakerCreateForm
    success_url = reverse_lazy('churches:admin-speakers-list')


class AdminSpeakerListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'churches.view_speaker'
    page_title = 'Speakers - Admin'
    current_page = 'manage'
    btn_add_href = reverse_lazy('churches:admin-speakers-create')
    model = Person
    context_object_name = 'speakers'
    template_name = 'churches/admin-speakers-list.html'
    queryset = Person.objects.all_speakers()


class ChurchesAdminListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'churches.view_church'
    page_title = 'Churches - Admin'
    current_page = 'manage'
    btn_add_href = reverse_lazy('churches:churches-admin-create')
    model = Church
    context_object_name = 'churches'
    template_name = 'churches/churches-admin-list.html'


class ChurchesAdminCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = 'churches.add_church'
    page_title = 'New Church - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('churches:churches-admin-list')
    model = Church
    template_name = 'admin-form-view.html'
    fields = ('name', 'street', 'city', 'province_state', 'country', 'mixlr_url')
    success_url = reverse_lazy('churches:churches-admin-list')


class ChurchesAdminUpdateView(PermissionRequiredMixin, BaseUpdateView):
    permission_required = 'churches.change_church'
    page_title = 'Update Church - Admin'
    current_page = 'manage'
    btn_back_href = reverse_lazy('churches:churches-admin-list')
    model = Church
    template_name = 'admin-form-view.html'
    fields = ('name', 'street', 'city', 'province_state', 'country', 'mixlr_url')
    success_url = reverse_lazy('churches:churches-admin-list')

    def get_queryset(self):
        return self.model.objects.get_member_churches(user=self.request.user)
