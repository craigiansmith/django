from django.core.signing import Signer
from django.test import SimpleTestCase, override_settings
from django.urls import reverse

from .urls import ContactFormViewWithMsg


@override_settings(ROOT_URLCONF='messages_tests.urls')
class SuccessMessageMixinTests(SimpleTestCase):

    def test_set_messages_success(self):
        author = {'name': 'John Doe', 'slug': 'success-msg'}
        add_url = reverse('add_success_msg')
        req = self.client.post(add_url, author)
        self.assertIn(ContactFormViewWithMsg.success_message % author,
                      Signer().decompress_b64(req.cookies['messages'].value, charset='latin-1'))
