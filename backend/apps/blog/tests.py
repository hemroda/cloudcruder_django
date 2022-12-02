from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from apps.blog.models import Post


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="JSmith", email="jsmith@cloudcruder.com", password="secret"
        )

        cls.post = Post.objects.create(
                    body="Sed ut perspiciatis unde omnis iste natus error sit.",
                    title="Lorem title",
                    author=cls.user,
        )

    def test_model_content(self):
        self.assertEqual(self.post.title, "Lorem title")
        self.assertEqual(self.post.author.username, "JSmith")
        self.assertEqual(self.post.body, "Sed ut perspiciatis unde omnis iste natus error sit.")
        self.assertEqual(str(self.post), "Lorem title - JSmith"),
        self.assertEqual(self.post.get_absolute_url(), "/blog/1/")

    def test_url_exists_at_correct_location_blog_index(self):
        response = self.client.get("/blog")
        self.assertEqual(response.status_code, 200)
    
    def test_index_page(self):
        response = self.client.get(reverse("blog_index_path"))
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, "blog/index.html") 
        self.assertContains(response, "Lorem title")

    def test_url_exists_at_correct_location_blog_detail_view(self):
        response = self.client.get("/blog/1/")
        self.assertEqual(response.status_code, 200)

    def test_blog_detail_view(self):
        response = self.client.get(reverse("blog_detail_path", kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/blog/99999999/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Lorem title")
        self.assertTemplateUsed(response, "blog/detail.html")
