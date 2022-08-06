from django.test import SimpleTestCase
from projects.views import ProjectCreateView, ProjectDeleteView, ProjectDetailView, ProjectListView, ProjectUpdateView
from django.urls import reverse, resolve

class TestProjectViews(SimpleTestCase):

    def test_project_list_url_resolves(self):
        url=reverse("projects:list")
        self.assertEquals(resolve(url).func.view_class, ProjectListView)

    def test_detail_url_resolves(self):
        url=reverse("projects:detail", args=['1'])
        self.assertEquals(resolve(url).func.view_class, ProjectDetailView)
    
    def test_create_url_resolves(self):
        url=reverse("projects:create")
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView)
    
    def test_update_url_resolves(self):
        url=reverse("projects:update", args=['1'])
        self.assertEquals(resolve(url).func.view_class, ProjectUpdateView)
    
    def test_delete_url_resolves(self):
        url=reverse("projects:delete", args=['1'])
        self.assertEquals(resolve(url).func.view_class, ProjectDeleteView)
    