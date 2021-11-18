from django.test import TestCase
from django.shortcuts import reverse
# .client in test file acts as request in veiw which has the CRUD (get, put, post, and delete)


class LandingViewTest(TestCase):
    def test_get_view(self):
        # TODO some sort of test
        response = self.client.get(reverse('landing-page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing.html')
