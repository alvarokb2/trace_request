from django.test import TestCase, Client
from django.urls import reverse
from projects.models import User, Project

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        
        self.user = User.objects.create(username='alvaro', email='alvaro.cabedov@gmail.com', password='xxxxxxx')
        self.project = Project.objects.create(name='proyecto de prueba', description='description de prueba', owner = self.user)

        self.projects_list_url = reverse('projects:list')
        self.projects_create_url = reverse('projects:create')
        self.projects_detail_url = reverse('projects:detail', args=[self.project.id])
        self.projects_update_url = reverse('projects:update', args=[self.project.id])
        self.projects_delete_url = reverse('projects:delete', args=[self.project.id])

    def test_projects_list_get(self):
        response = self.client.get(self.projects_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/index.html')

    def test_projects_create_get(self):
        response = self.client.get(self.projects_create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/create.html')

    def test_projects_create_post(self):
        data={
            "name":"n prueba",
            "description":"d prueba",
            }
        response = self.client.post(self.projects_create_url, params=data)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/create.html')

    def test_projects_detail_get(self):
        response = self.client.get(self.projects_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/detail.html')

    def test_projects_update_get(self):
        response = self.client.get(self.projects_update_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/update.html')

    def test_projects_update_post(self):
        data={
            "name":"n prueba editada",
            "description":"d prueba editada",
            }
        response = self.client.post(self.projects_update_url, params=data)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/update.html')

    def test_projects_delete_get(self):
        response = self.client.get(self.projects_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/delete.html')

    def test_projects_delete_post(self):
        response = self.client.post(self.projects_delete_url)
        self.assertEquals(response.status_code, 302)
        