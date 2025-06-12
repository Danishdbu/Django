# Django Template Inheritance: Extends, Block, and Static Files

## 1. Template Inheritance with `extends` and `block` Tags

### Overview
Template inheritance in Django allows you to create a base template with common structure and content, which child templates can extend and customize. The `extends` and `block` tags are key to achieving this.

### Step-by-Step Process

#### Step 1: Create a Base Template
- Create a base template (e.g., `base.html`) in your templates directory (`templates/`).
- Define the common structure (e.g., HTML skeleton, header, footer) and use `{% block %}` tags to mark areas that child templates can override.
  ```html
  <!-- templates/base.html -->
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>{% block title %}My Site{% endblock %}</title>
  </head>
  <body>
      <header>
          <h1>My Website</h1>
          <nav>
              <a href="/">Home</a> | <a href="/about">About</a>
          </nav>
      </header>
      <main>
          {% block content %}
          <!-- Default content, if any -->
          {% endblock %}
      </main>
      <footer>
          <p>&copy; 2025 My Website</p>
      </footer>
  </body>
  </html>
  ```
  - `{% block title %}`: Allows child templates to override the page title.
  - `{% block content %}`: Allows child templates to provide their own main content.

#### Step 2: Create a Child Template
- Create a child template (e.g., `home.html`) that extends the base template using the `{% extends %}` tag.
- Override specific blocks using `{% block %}` tags.
  ```html
  <!-- templates/home.html -->
  {% extends 'base.html' %}

  {% block title %}Home Page{% endblock %}

  {% block content %}
  <h2>Welcome to the Home Page</h2>
  <p>This is the main content of the home page.</p>
  {% endblock %}
  ```
  - `{% extends 'base.html' %}`: Specifies the parent template.
  - The child template only overrides the `title` and `content` blocks, inheriting the rest (header, footer) from `base.html`.

#### Step 3: Configure Template Settings
- Ensure your `settings.py` includes the templates directory:
  ```python
  # settings.py
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'templates'],  # Add templates directory
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
  ```

#### Step 4: Create a View to Render the Template
- Define a view in `views.py` to render the child template.
  ```python
  # app_name/views.py
  from django.shortcuts import render

  def home(request):
      return render(request, 'home.html')
  ```

#### Step 5: Map the View to a URL
- Update `urls.py` to map the view to a URL.
  ```python
  # app_name/urls.py
  from django.urls import path
  from . import views

  urlpatterns = [
      path('', views.home, name='home'),
  ]
  ```

#### Step 6: Test the Template
- Run the development server:
  ```bash
  python manage.py runserver
  ```
- Visit `http://127.0.0.1:8000/` to see the rendered `home.html`, which inherits the structure from `base.html` but uses the overridden `title` and `content` blocks.

### Key Points
- **Reusability**: The base template ensures consistent layout across pages.
- **Flexibility**: Child templates can override specific blocks while keeping the rest unchanged.
- **Multiple Blocks**: You can define multiple blocks (e.g., `{% block sidebar %}`, `{% block scripts %}`) for different sections.
- **Access Parent Block Content**: Use `{{ block.super }}` in a child template to include the parent’s block content.
  ```html
  {% block content %}
  {{ block.super }}
  <p>Additional content</p>
  {% endblock %}
  ```

## 2. Template Inheritance with Static Files

### Overview
Static files (CSS, JavaScript, images) enhance templates with styling and interactivity. Combining template inheritance with static files ensures consistent styling across inherited templates.

### Step-by-Step Process

#### Step 1: Set Up Static Files Directory
- Create a `static` directory in your project or app (e.g., `static/css/`, `static/js/`, `static/images/`).
  ```
  project_name/
  ├── static/
  │   ├── css/
  │   │   └── style.css
  │   ├── js/
  │   │   └── script.js
  │   └── images/
  │       └── logo.png
  ```

#### Step 2: Configure Static Files in Settings
- Update `settings.py`:
  ```python
  # settings.py
  STATIC_URL = '/static/'
  STATICFILES_DIRS = [
      BASE_DIR / "static",
  ]
  STATIC_ROOT = BASE_DIR / "staticfiles"
  ```

#### Step 3: Update the Base Template with Static Files
- Modify `base.html` to include static files using the `{% static %}` tag.
  ```html
  <!-- templates/base.html -->
  {% load static %}
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>{% block title %}My Site{% endblock %}</title>
      <link rel="stylesheet" href="{% static 'css/style.css' %}">
  </head>
  <body>
      <header>
          <img src="{% static 'images/logo.png' %}" alt="Logo" class="logo">
          <h1>My Website</h1>
          <nav>
              <a href="/">Home</a> | <a href="/about">About</a>
          </nav>
      </header>
      <main>
          {% block content %}
          <!-- Default content -->
          {% endblock %}
      </main>
      <footer>
          <p>&copy; 2025 My Website</p>
      </footer>
      <script src="{% static 'js/script.js' %}"></script>
  </body>
  </html>
  ```
  - `{% load static %}`: Loads the static template tag.
  - `{% static 'css/style.css' %}`: References the CSS file.
  - `{% static 'images/logo.png' %}`: References the image.
  - `{% static 'js/script.js' %}`: References the JavaScript file.

#### Step 4: Create Static Files
- **CSS File** (`static/css/style.css`):
  ```css
  body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      margin: 0;
      padding: 0;
  }
  header {
      background-color: #333;
      color: white;
      text-align: center;
      padding: 10px;
  }
  .logo {
      max-width: 100px;
  }
  nav a {
      color: white;
      margin: 0 10px;
      text-decoration: none;
  }
  main {
      padding: 20px;
  }
  footer {
      background-color: #333;
      color: white;
      text-align: center;
      padding: 10px;
      position: fixed;
      bottom: 0;
      width: 100%;
  }
  ```
- **JavaScript File** (`static/js/script.js`):
  ```javascript
  document.addEventListener('DOMContentLoaded', function() {
      console.log('Website loaded with JavaScript!');
      alert('Welcome to My Website!');
  });
  ```
- **Image**: Place an image file (e.g., `logo.png`) in `static/images/`.

#### Step 5: Create a Child Template
- Create `home.html` to extend `base.html`:
  ```html
  <!-- templates/home.html -->
  {% extends 'base.html' %}

  {% block title %}Home Page{% endblock %}

  {% block content %}
  <h2>Welcome to the Home Page</h2>
  <p>This page inherits the base template with CSS, JavaScript, and image static files.</p>
  {% endblock %}
  ```

#### Step 6: Serve Static Files in Development
- Add static file serving to `urls.py`:
  ```python
  # urls.py
  from django.conf import settings
  from django.conf.urls.static import static

  urlpatterns = [
      path('', views.home, name='home'),
  ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  ```
