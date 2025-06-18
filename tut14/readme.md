# Django Custom Authentication System using Function-Based Views


---

## 1. Introduction to Django Authentication

### What is Authentication?
Authentication is the process of verifying a user's identity, ensuring they are who they claim to be. In web applications, this typically involves users providing credentials (like a username and password) to access protected resources, such as a personal dashboard or account settings.

### Why is Authentication Important?
- **Security**: Protects sensitive user data and restricts unauthorized access.
- **User Experience**: Enables personalized experiences, like saving user preferences or tracking activity.
- **Access Control**: Allows different levels of access (e.g., admin vs. regular users).

### Django’s Built-in Authentication System
Django provides a robust authentication system out of the box, which includes:
- A `User` model for storing user data.
- Functions for login, logout, and password management.
- Session management to track logged-in users.
- Tools for permissions and groups.

In this guide, we’ll use Django’s authentication system as a foundation but implement custom Function-Based Views to handle registration, login, logout, and password reset.

---

## 2. Setting Up the Environment

Let’s set up a Django project to build our authentication system.

### Step 1: Install Django
Ensure you have Python installed (version 3.8 or higher recommended). Then, install Django using pip:
```bash
pip install django
```

### Step 2: Create a Django Project
1. Create a new Django project named `auth_project`:
   ```bash
   django-admin startproject auth_project
   cd auth_project
   ```
2. Create a new app called `accounts`:
   ```bash
   python manage.py startapp accounts
   ```

### Step 3: Configure the Project
Update the `auth_project/settings.py` file to include the `accounts` app and configure basic settings.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',  # Add the accounts app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add a templates directory
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Database (using SQLite for simplicity)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Redirect URLs after login/logout
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
```

### Step 4: Create a Templates Directory
Create a `templates` folder in the project root (`auth_project/templates/`) to store HTML templates.

### Step 5: Run Migrations
Apply initial migrations to set up the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 3. Creating User Model

For this guide, we’ll use Django’s default `User` model (from `django.contrib.auth.models`) to keep things simple. However, if you need a custom user model (e.g., to add fields like phone number), follow these steps:

### Using the Default User Model
The default `User` model includes fields like `username`, `email`, `password`, `first_name`, and `last_name`. It’s sufficient for most basic authentication systems.

### Creating a Custom User Model (Optional)
If you want a custom user model:
1. Create a new model in `accounts/models.py`:
   ```python
   from django.contrib.auth.models import AbstractUser

   class CustomUser(AbstractUser):
       phone_number = models.CharField(max_length=15, blank=True)

   ```
2. Update `settings.py`:
   ```python
   AUTH_USER_MODEL = 'accounts.CustomUser'
   ```
3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

**Note**: Define a custom user model at the start of the project, as changing it later can be complex.

---

## 4. Building the Authentication Views

Let’s create Function-Based Views in `accounts/views.py` for registration, login, and logout.

### User Registration View
The registration view allows users to create an account by submitting a form with their details.

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
```

**Explanation**:
- We use Django’s `UserCreationForm` to handle user registration.
- On `POST`, we validate the form and save the user if valid.
- A success message is displayed, and the user is redirected to the login page.
- On `GET`, we render an empty form.

### User Login View
The login view authenticates users and starts a session.

```python
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')
```

**Explanation**:
- The `authenticate()` function checks if the credentials are valid.
- If valid, `login()` creates a session for the user.
- Messages provide feedback, and the user is redirected to the `home` page.

### User Logout View
The logout view terminates the user’s session.

```python
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')
```

**Explanation**:
- The `logout()` function clears the user’s session.
- A success message is shown, and the user is redirected to the `home` page.

### Home View (For Testing)
Create a simple home view to test redirects:

```python
def home(request):
    return render(request, 'accounts/home.html')
```

### URL Configuration
Map these views to URLs in `auth_project/urls.py`:

```python
from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
```

---

## 5. Creating Templates

Create HTML templates in the `templates/accounts/` directory for a clean user interface.

### Home Template (`home.html`)
```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to the Authentication System</h1>
    {% if user.is_authenticated %}
        <p>Hello, {{ user.username }}! <a href="{% url 'logout' %}">Logout</a></p>
    {% else %}
        <p><a href="{% url 'login' %}">Login</a> | <a href="{% url 'register' %}">Register</a></p>
    {% endif %}
    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}
</body>
</html>
```

### Registration Template (`register.html`)
```html
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
    <p>Already have an account? <a href="{% url 'login' %}">Login</a></p>
    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}
</body>
</html>
```

### Login Template (`login.html`)
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="post">
        {% csrf_token %}
        <label>Username:</label>
        <input type="text" name="username" required><br>
        <label>Password:</label>
        <input type="password" name="password" required><br>
        <button type="submit">Login</button>
    </form>
    <p>Don't have an account? <a href="{% url 'register' %}">Register</a></p>
    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}
</body>
</html>
```

### UI Design Tips
- **Simplicity**: Keep forms clean and focused on essential fields.
- **Feedback**: Use Django’s `messages` framework to display success or error messages.
- **Accessibility**: Add labels to form fields and ensure forms are keyboard-navigable.
- **Styling**: For production, use CSS frameworks like Bootstrap or Tailwind CSS for better visuals.

---

## 6. Implementing Password Reset Functionality

Django’s built-in password reset views simplify this process, but we’ll create custom Function-Based Views for learning purposes.

### Step 1: Configure Email Settings
Add email settings to `settings.py` (use a dummy SMTP server for testing, like Mailtrap, or Django’s console backend):

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # For testing
# For production, use something like:
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@gmail.com'
# EMAIL_HOST_PASSWORD = 'your-password'
```

### Step 2: Password Reset Request View
Create a view to handle password reset requests:

```python
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.template.loader import render_to_string

def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email).first()
        if user:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = request.build_absolute_uri(f'/reset/{uid}/{token}/')
            subject = 'Password Reset Request'
            message = render_to_string('accounts/password_reset_email.html', {
                'user': user,
                'reset_link': reset_link,
            })
            send_mail(subject, message, 'from@example.com', [user.email])
            messages.success(request, 'Password reset email sent.')
            return redirect('home')
        else:
            messages.error(request, 'No user found with this email.')
    return render(request, 'accounts/password_reset_request.html')
```

### Step 3: Password Reset Confirm View
Handle the password reset form after the user clicks the reset link:

```python
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.forms import SetPasswordForm

def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password has been reset.')
                return redirect('login')
        else:
            form = SetPasswordForm(user)
        return render(request, 'accounts/password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, 'Invalid reset link.')
        return redirect('home')
```

### Step 4: Password Reset Templates
- **Password Reset Request (`password_reset_request.html`)**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Password Reset</title>
</head>
<body>
    <h1>Reset Your Password</h1>
    <form method="post">
        {% csrf_token %}
        <label>Email:</label>
        <input type="email" name="email" required><br>
        <button type="submit">Send Reset Link</button>
    </form>
    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}
</body>
</html>
```

- **Password Reset Email (`password_reset_email.html`)**:
```html
Hello {{ user.username }},

Click the link below to reset your password:
{{ reset_link }}

If you did not request this, ignore this email.
```

- **Password Reset Confirm (`password_reset_confirm.html`)**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Reset Password</title>
</head>
<body>
    <h1>Set New Password</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Reset Password</button>
    </form>
    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}
</body>
</html>
```

### Step 5: Update URLs
Add password reset URLs to `auth_project/urls.py`:

```python
path('password_reset/', views.password_reset_request, name='password_reset'),
path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
```

---

## 7. Testing the Authentication System

Testing ensures your authentication system works reliably. Write tests in `accounts/tests.py`.

### Example Tests
```python
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthenticationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123', email='test@example.com')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass123'})
        self.assertEqual(response.status_code, 302)  # Redirect after login
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_password_reset_request(self):
        response = self.client.post(reverse('password_reset'), {'email': 'test@example.com'})
        self.assertEqual(response.status_code, 302)
```

Run tests with:
```bash
python manage.py test
```

**Tips**:
- Write tests for edge cases (e.g., invalid credentials, non-existent emails).
- Use Django’s `TestCase` for database-related tests and `Client` for simulating HTTP requests.

---

## 8. Securing the Authentication System

### Best Practices
- **Use HTTPS**: Ensure your site uses HTTPS to encrypt data in transit.
- **Password Hashing**: Django automatically hashes passwords using PBKDF2 (or other algorithms based on settings).
- **CSRF Protection**: Django’s `{% csrf_token %}` in forms prevents cross-site request forgery.
- **Limit Login Attempts**: Consider using packages like `django-axes` to prevent brute-force attacks.
- **Validate Inputs**: Use Django forms to sanitize and validate user input.
- **Secure Email**: Use a secure email service for password resets in production.

### Settings for Security
Update `settings.py`:
```python
# Security settings
SECURE_SSL_REDIRECT = True  # Redirect HTTP to HTTPS
SESSION_COOKIE_SECURE = True  # Cookies only sent over HTTPS
CSRF_COOKIE_SECURE = True  # CSRF cookies over HTTPS
SECURE_BROWSER_XSS_FILTER = True  # Prevent XSS attacks
```

---

## 9. Conclusion and Further Learning

### Key Concepts Learned
- Setting up a Django project and app for authentication.
- Using Django’s default `User` model and creating custom views for registration, login, logout, and password reset.
- Designing user-friendly templates and handling forms.
- Implementing secure authentication practices.
- Writing tests to ensure reliability.

### Next Steps
- Explore Django’s class-based views for authentication.
- Learn about Django REST Framework for API-based authentication.
- Implement social authentication using packages like `python-social-auth`.
- Study advanced security topics, such as two-factor authentication.

### Resources
- [Django Official Documentation](https://docs.djangoproject.com/en/stable/topics/auth/)
- [Django Authentication Tutorial](https://learndjango.com/tutorials/)
- [Real Python Django Tutorials](https://realpython.com/django-user-authentication/)

