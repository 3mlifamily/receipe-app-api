from django.test import TestCase
from django.contriib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successfull"""
        email = 'mli@gmail.com'
        password='test1234'
        user = get_user_model().object.create_user(
         email = email,
         password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_passowrd(password))


    def test_new_user_email_normalized(self):
        """Test email for a new user is normalized"""
        email = "mli@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'test1234')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        ""Test creating user with no email reaises error"""
        with self.assertRaise(ValueError):
            get_user_model.objects.create_user(None, 'test1234')
