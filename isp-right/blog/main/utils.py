from main.models import *


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        section = Section.objects.all()
        context['section'] = section
        if 'sect_selected' not in context:
            context['sect_seslected'] = 0
        return context