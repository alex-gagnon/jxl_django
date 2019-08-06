from django.test import TestCase

from .forms import JXLForm
from django.test import TestCase

from .forms import JXLForm


class HomeViewTest(TestCase):

    def test_index_redirects_and_renders_template(self):
        """Index page should redirect to JXL app"""
        # follow=True is required to follow the redirect chain in order to check template used
        response = self.client.get('/', follow=True)
        self.assertRedirects(response=response, expected_url='/jxl/',
                             status_code=302, target_status_code=200,
                             fetch_redirect_response=True)
        self.assertTemplateUsed(response, 'jxl/home.html')


class JXLFormTest(TestCase):
    def test_form_renders_fields(self):
        form = JXLForm()
        [self.assertIn(f'id="{ids}"', form.as_p()) for ids in 'id_project id_filter_by id_version'.split()]
        self.assertIn('placeholder="Enter version number (e.g. 10.2)', form.as_p())

