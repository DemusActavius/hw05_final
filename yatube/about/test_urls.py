from django.contrib.auth import get_user_model
from django.test import TestCase, Client

User = get_user_model()


class AboutURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='UserTest')

    def setUp(self):
        self.guest_client = Client()

    def test_urls_uses_correct_template(self):
        """About: URL-адрес использует соответствующий шаблон."""
        templates_url_names = {
            '/about/author/': 'about/author.html',
            '/about/tech/': 'about/tech.html',
        }
        for address, templates in templates_url_names.items():
            with self.subTest(address=address):
                response = self.guest_client.get(address)
                self.assertTemplateUsed(response, templates)
