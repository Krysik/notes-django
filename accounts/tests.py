from django.test import TestCase
from .forms import RegisterForm, LoginForm
from django.urls import reverse
from django.core.exceptions import ValidationError
# Forms
class TestRegisterForm(TestCase):
    def setUp(self):
        self.form = RegisterForm()
        self.form.username = 'jdoe123'
        self.form.email = 'jdoe@test.com'
        self.form.password1 = 'zaq1@WSXd'
        self.form.password2 = 'zaq1@WSXd'

    def test_form_labels(self):
        form = self.form
        self.assertEquals(form.fields['username'].label, 'Nazwa użytkownika')
        self.assertTrue(form.fields['email'].label == None or 'Email')
        self.assertEquals(form.fields['password1'].label, 'Hasło')
        self.assertEquals(form.fields['password2'].label, 'Powtórz hasło')

    def test_valid_register_form(self):
        data = {
            'username': self.form.username,
            'email': self.form.email,
            'password1': self.form.password1,
            'password2': self.form.password2,
        }
        form = RegisterForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_register_form(self):
        data = {
            'username': self.form.username,
            'email': self.form.email,
            'password1': self.form.password1,
            'password2': 'passwordDoesntMatch123',
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())
    
    def test_min_len_of_password(self):
        password1 = self.form.password1
        password2 = self.form.password2
        self.assertGreaterEqual(len(password1), 8)
        self.assertGreaterEqual(len(password2), 8)
    def test_email_validation(self):
        data1 = {
            'username': self.form.username,
            'email': self.form.email,
            'password1': self.form.password1,
            'password2': self.form.password2,
        }
        form1 = RegisterForm(data=data1)
        data2 = {
            'username': 'xyz12',
            'email': self.form.email,
            'password1': self.form.password1,
            'password2': self.form.password2,
        }
        form2 = RegisterForm(data=data2)
        self.assertRaisesMessage(ValidationError, 'Taki email już istnieje')

class TestLoginForm(TestCase):
    def setUp(self):
        self.form = LoginForm()
        self.username = 'jdoe123'
        self.password = 'zaq1@WSX'
    
    def test_form_labels(self):
        form = self.form
        self.assertEquals(form.fields['username'].label, 'Użytkownik')
        self.assertEquals(form.fields['password'].label, 'Hasło')

# Views
class TestViews(TestCase):
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
    
    def test_login_view(self):
        response = self.client.get(reverse('login_view'))
        self.assertEqual(response.status_code, 200)
