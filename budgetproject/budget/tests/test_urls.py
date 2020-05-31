from django.test import SimpleTestCase
from django.urls import reverse, resolve
from budget.views import (project_list, project_detail, ProjectCreateView)

# you can use SimpleTestCase anytime you don't need to interact with the database


class TestUrls(SimpleTestCase):
    def test_list_url_resolves(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func, project_list)

    def test_create_url_resolves(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView)

    def test_detail_url_resolves(self):
        url = reverse('detail', args=['some-slug'])
        self.assertEquals(resolve(url).func, project_detail)
