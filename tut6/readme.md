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
---
# Hyperlinks in Django 
---
## What is a Hyperlink in Django?
A hyperlink is a clickable link that takes you to another page in your Django app, like going from a list of notes to a specific note's details. In Django, hyperlinks are created using **templates** and **URL routing** to connect pages.

## Key Ideas
1. **URLs**: Define the web addresses (e.g., `/notes/`) in a file called `urls.py`.
2. **Views**: Python functions that show pages (e.g., a list of notes).
3. **Templates**: HTML files where you add links using Django’s special `{% url %}` tag.
4. **Named URLs**: Give each URL a name to make links easy to use and update.

## Steps to Create Hyperlinks
Let’s build a simple notes app with hyperlinks to:
- Show a list of notes.
- View one note’s details.
- Add a new note.

### Step 1: Set Up Your Django App
1. Create a Django project and an app called `notes`.
2. Add the `notes` app to `INSTALLED_APPS` in `notes_project/settings.py`:
   ```python
   INSTALLED_APPS = [
       ...
       'notes',
   ]
   ```

### Step 2: Create a Model
In `notes/models.py`, define a simple `Note` model:
```python
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
```

Run migrations to create the database table:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Set Up URLs
In `notes/urls.py`, define URLs for your app:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),          # Home page: List all notes
    path('note/<int:id>/', views.note_detail, name='note_detail'),  # Show one note
    path('create/', views.note_create, name='note_create'),  # Create a new note
]
```

In `notes_project/urls.py`, include the app’s URLs:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include('notes.urls')),  # All notes URLs start with /notes/
]
```

- **What this does**: 
  - `/notes/` shows the list of notes.
  - `/notes/note/1/` shows details for note with ID 1.
  - `/notes/create/` shows a form to add a new note.
  - `name='note_list'` gives each URL a name for easy linking.

### Step 4: Create Views
In `notes/views.py`, add functions to show pages:
```python
from django.shortcuts import render
from .models import Note

def note_list(request):
    notes = Note.objects.all()  # Get all notes
    return render(request, 'note_list.html', {'notes': notes})

def note_detail(request, id):
    note = Note.objects.get(id=id)  # Get one note by ID
    return render(request, 'note_detail.html', {'note': note})

def note_create(request):
    return render(request, 'note_create.html')  # Show create form
```

- **What this does**:
  - `note_list`: Shows a page with all notes.
  - `note_detail`: Shows one note’s details.
  - `note_create`: Shows a page to create a new note (form not included for simplicity).

### Step 5: Create Templates with Hyperlinks
Create a folder `notes/templates/` for your HTML files.

**`notes/templates/base.html`** (main layout):
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Notes App{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="{% url 'note_list' %}">Home</a> | 
        <a href="{% url 'note_create' %}">Add Note</a>
    </nav>
    <h1>{% block header %}{% endblock %}</h1>
    {% block content %}
    {% endblock %}
</body>
</html>
```

- **What this does**:
  - Creates a navigation bar with links to "Home" (note list) and "Add Note".
  - Uses `{% url 'note_list' %}` to make links dynamic.
  - Other templates will extend this file.

**`notes/templates/note_list.html`** (list all notes):
```html
{% extends "base.html" %}
{% block title %}All Notes{% endblock %}
{% block header %}My Notes{% endblock %}
{% block content %}
<ul>
    {% for note in notes %}
        <li><a href="{% url 'note_detail' note.id %}">{{ note.title }}</a></li>
    {% empty %}
        <li>No notes yet.</li>
    {% endfor %}
</ul>
<p><a href="{% url 'note_create' %}">Create a new note</a></p>
{% endblock %}
```

- **What this does**:
  - Shows a list of notes.
  - Each note title links to its detail page using `{% url 'note_detail' note.id %}`.
  - Adds a link to create a new note.

**`notes/templates/note_detail.html`** (show one note):
```html
{% extends "base.html" %}
{% block title %}{{ note.title }}{% endblock %}
{% block header %}{{ note.title }}{% endblock %}
{% block content %}
<p>{{ note.content }}</p>
<p><a href="{% url 'note_list' %}">Back to all notes</a></p>
{% endblock %}
```

- **What this does**:
  - Shows the note’s title and content.
  - Adds a "Back to all notes" link.

**`notes/templates/note_create.html`** (create note form):
```html
{% extends "base.html" %}
{% block title %}Create Note{% endblock %}
{% block header %}Create a New Note{% endblock %}
{% block content %}
<p>Form to create a note goes here.</p>
<p><a href="{% url 'note_list' %}">Back to all notes</a></p>
{% endblock %}
```

- **What this does**:
  - Placeholder for a create note form (you can add a form later).
  - Includes a link to go back to the note list.

### Step 6: Test Your App
1. Run the server:
   ```bash
   python manage.py runserver
   ```
2. Visit `http://localhost:8000/notes/`.
3. You’ll see:
   - A navigation bar with "Home" and "Add Note" links.
   - A list of notes (empty at first).
   - Clicking a note title (after adding notes) takes you to its detail page.
   - Links to go back or create a new note.

## Why Use `{% url %}`?
- **Avoid hardcoding**: Don’t write `<a href="/notes/note/1/">`. If the URL changes (e.g., to `/mynotes/`), hardcoded links break.
- **Easy to update**: With `{% url 'note_list' %}`, you only change `urls.py`, and all links update automatically.
- **Safe and simple**: Named URLs keep your app organized.

## Tips for Beginners
1. **Always name URLs**: Add `name='something'` in `urls.py` for every path.
2. **Use `{% url %}` in templates**: It’s the Django way to make links.
3. **Check your URLs**: If a link doesn’t work, check the name in `urls.py` and the `{% url %}` tag.
4. **Start small**: Add a form to `note_create` later when you’re ready.

---
# Template inside Template using Include Tag in Django
---
In Django, `{% include %}` is a **template tag** used to **include one HTML template inside another**. It helps in **breaking templates into reusable components** like headers, footers, navbars, etc.

---

### ✅ Syntax of `{% include %}`

```django
{% include 'relative/path/to/template.html' %}
```

---

### ✅ 1. Example Folder Structure

```
myproject/
├── myapp/
│   └── templates/
│       └── myapp/
│           ├── base.html
│           ├── header.html
│           ├── footer.html
│           └── home.html
```

---

### ✅ 2. Create a Reusable Template (e.g., `header.html`)

**`header.html`**

```html
<header>
    <h1>Welcome to My Website</h1>
</header>
```

---

### ✅ 3. Use `{% include %}` in Another Template

**`home.html`**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>

{% include 'myapp/header.html' %}

<main>
    <p>This is the homepage content.</p>
</main>

{% include 'myapp/footer.html' %}

</body>
</html>
```

---

### ✅ 4. Include with Variables (Optional)

If you want to pass variables:

```html
{% include 'myapp/greeting.html' with name='Danish' %}
```

**`greeting.html`**

```html
<p>Hello, {{ name }}!</p>
```

---

### ✅ Summary

| Feature         | Description                                    |
| --------------- | ---------------------------------------------- |
| `{% include %}` | Embeds another template into current one       |
| `with`          | Passes variables to the included template      |
| Reusability     | Great for components like nav, footer, sidebar |

---

Let me know if you want to combine `{% include %}` with `{% block %}` and `{% extends %}` for full template inheritance!
