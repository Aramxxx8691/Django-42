from django.urls import reverse
from django.test import TestCase
from .models import Article
from django.contrib.auth.models import User

class ArticleDeleteTests(TestCase):
    def setUp(self):
        # Create a user and log them in
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        # Create an article by the user
        self.article = Article.objects.create(title='Test Article', author=self.user, content='Some content')

    def test_article_delete_by_author(self):
        response = self.client.post(reverse('article_delete', kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, 302)  # Should redirect to publications
        self.assertFalse(Article.objects.filter(pk=self.article.pk).exists())  # Ensure the article is deleted

    def test_article_delete_view_accessibility_for_non_author(self):
        # Create another user
        other_user = User.objects.create_user(username='otheruser', password='12345')
        self.client.login(username='otheruser', password='12345')
        response = self.client.post(reverse('article_delete', kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, 302)  # Should redirect back (or deny access)
        self.assertTrue(Article.objects.filter(pk=self.article.pk).exists())  # Ensure the article still exists
