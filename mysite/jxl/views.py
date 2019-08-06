from django.utils import timezone
from django.views.generic import FormView

from .forms import JXLForm


class HomeView(FormView):
    form_class = JXLForm
    template_name = 'jxl/home.html'

    def get_queryset(self):
        """Return the last five published questions, not including those set to be published in the future."""
        return JXLForm.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
