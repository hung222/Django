from django.test import TestCase
from .models import Post

class BlogTest(TestCase):
    def setUp(self):
        Post.objects.create(
            title="My Title",
            content="This is a just test"
        )
    def test_string_representation(self):
        post = Post(title="My entry title")
        self.assertEqual(str(post), post.title)
    def test_post_list_view(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Title')
        self.assertTemplateUsed(response, 'blog/blog.html')
    def test_post_detail_view(self):
        response = self.client.get("/blog/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Title')
        self.assertTemplateUsed(response, 'blog/post.html')
    
