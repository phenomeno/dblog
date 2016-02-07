from django.test import TestCase

# Create your tests here.
import datetime

from django.utils import timezone
from .models import Post

class PostMethodTests(TestCase):
    def test_has_tag_as_test(self):
        """ Post's tag should not be test. Cause testing. """
        post = Post(post_category="test")
        self.assertTrue(post.post_category=="test")
