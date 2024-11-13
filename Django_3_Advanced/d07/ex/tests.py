from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Article, UserFavouriteArticle

User = get_user_model()

class ArticleTests(TestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.article_data = {
            'title': 'Test Article',
            'synopsis': 'This is a test synopsis.',
            'content': 'This is the content of the test article.'
        }
        self.article = Article.objects.create(
            title='Existing Article',
            author=self.user,
            synopsis='Test synopsis for an existing article.',
            content='Test content for an existing article.'
        )

    def test_article_create(self):
        # Test if article creation works correctly
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('article_publish'), self.article_data)
        self.assertEqual(response.status_code, 302)  # Should redirect to publications
        self.assertEqual(Article.objects.count(), 2)  # There should be two articles

    def test_article_publish_view(self):
        # Test if the article publication page is accessible for the logged-in user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('publications'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Publish')

    def test_article_edit(self):
        # Test editing an article
        self.client.login(username='testuser', password='testpassword')
        edit_url = reverse('article_edit', kwargs={'pk': self.article.id})
        updated_data = {
            'title': 'Updated Article',
            'synopsis': 'Updated synopsis.',
            'content': 'Updated content.'
        }
        response = self.client.post(edit_url, updated_data)
        self.article.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.article.title, 'Updated Article')

    def test_article_delete(self):
        # Test deleting an article
        self.client.login(username='testuser', password='testpassword')
        delete_url = reverse('article_delete', kwargs={'pk': self.article.id})
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)  # Should redirect after deletion
        self.assertEqual(Article.objects.count(), 0)  # Article should be deleted

    def test_article_delete_by_author(self):
        # Ensure the author can delete the article
        self.client.login(username='testuser', password='testpassword')
        delete_url = reverse('article_delete', kwargs={'pk': self.article.id})
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Article.objects.count(), 0)  # Article should be deleted

    def test_article_delete_non_author(self):
        # Test non-authors cannot delete an article
        non_author = User.objects.create_user(username='nonauthor', password='testpassword')
        self.client.login(username='nonauthor', password='testpassword')  # Correct the username here
        delete_url = reverse('article_delete', kwargs={'pk': self.article.id})
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 404)  # Should not be allowed to delete
    

class FavouriteTests(TestCase):
    def setUp(self):
        # Create a user and an article for the favorite tests
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.article = Article.objects.create(
            title='Test Article to Favorite',
            author=self.user,
            synopsis='A test article for the favorite feature.',
            content='Test content for the favorite feature.'
        )

    def test_favorite_article_add(self):
        # Test adding an article to favorites
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('favorite', kwargs={'article_id': self.article.id, 'action': 'add'}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(UserFavouriteArticle.objects.count(), 1)

    def test_favorite_article_remove(self):
        # Test removing an article from favorites
        self.client.login(username='testuser', password='testpassword')
        UserFavouriteArticle.objects.create(user=self.user, article=self.article)
        response = self.client.post(reverse('favorite', kwargs={'article_id': self.article.id, 'action': 'remove'}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(UserFavouriteArticle.objects.count(), 0)

    def test_favorite_article_not_authenticated(self):
        # Test access to favorite actions when not authenticated
        response = self.client.post(reverse('favorite', kwargs={'article_id': self.article.id, 'action': 'add'}))
        self.assertEqual(response.status_code, 403)  # Should return forbidden if not authenticated

    def test_favorite_article_invalid_action(self):
        # Test handling invalid favorite actions
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('favorite', kwargs={'article_id': self.article.id, 'action': 'invalid'}))
        self.assertEqual(response.status_code, 400)  # Should return bad request for invalid action

class UserAuthTests(TestCase):
    def test_login_logout(self):
        # Test user login and logout functionality
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Should redirect to home after successful login
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Should redirect after logout
