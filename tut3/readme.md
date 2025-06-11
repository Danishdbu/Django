
### 1. **What are Django Templates?**
Django templates are text files (usually HTML) that define the structure and layout of the output. They use placeholders and logic (like loops and conditionals) to render dynamic content based on data provided by views. The Django template engine processes these templates to generate the final output.

### 2. **Standard Folder Structure for Templates**
To organize templates in a Django project, follow this standard structure:

```
project_name/
├── project_name/           # Project directory
│   ├── __init__.py
│   ├── settings.py        # Template settings are defined here
│   ├── urls.py
│   └── wsgi.py
├── app_name/              # App directory
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── templates/         # App-specific templates
│   │   ├── app_name/     # Namespace templates with app name
│   │   │   ├── base.html
│   │   │   ├── home.html
│   │   │   └── detail.html
│   └── urls.py
├── templates/             # Project-level templates (optional)
│   ├── base.html
│   └── error.html
├── static/                # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
└── manage.py
```

#### Key Points:
- **App-specific templates**: Place templates in `app_name/templates/app_name/` to avoid naming conflicts and use namespacing (e.g., `blog/home.html`).
- **Project-level templates**: For shared templates (e.g., `base.html`), use a project-level `templates/` directory.
- **Settings configuration**: In `settings.py`, configure the `TEMPLATES` setting to tell Django where to find templates:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Project-level templates directory
        'APP_DIRS': True,  # Automatically look in app_name/templates/
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

- `DIRS`: Specifies project-level template directories (e.g., `project_name/templates/`).
- `APP_DIRS=True`: Enables Django to look for templates in each app’s `templates/` folder.

### 3. **Template Syntax**
Django templates use a special syntax for dynamic content, including variables, tags, and filters.

#### a. **Variables**
Variables display data passed from the view. Syntax: `{{ variable_name }}`
- Example:
  ```html
  <p>Welcome, {{ username }}!</p>
  ```
  - If `username="Alice"` is passed from the view, it renders: `Welcome, Alice!`

#### b. **Tags**
Tags provide logic like loops, conditionals, or template inheritance. Syntax: `{% tag %}`
- Common tags:
  - **If condition**:
    ```html
    {% if user.is_authenticated %}
        <p>Hello, {{ user.username }}!</p>
    {% else %}
        <p>Please log in.</p>
    {% endif %}
    ```
  - **For loop**:
    ```html
    <ul>
    {% for post in posts %}
        <li>{{ post.title }}</li>
    {% endfor %}
    </ul>
    ```
  - **Template inheritance**:
    - Base template (`base.html`):
      ```html
      <!DOCTYPE html>
      <html>
      <head>
          <title>{% block title %}My Site{% endblock %}</title>
      </head>
      <body>
          <header>Site Header</header>
          {% block content %}
          {% endblock %}
          <footer>Site Footer</footer>
      </body>
      </html>
      ```
    - Child template (`home.html`):
      ```html
      {% extends 'base.html' %}
      {% block title %}Home Page{% endblock %}
      {% block content %}
          <h1>Welcome to the Home Page</h1>
      {% endblock %}
      ```

  - **Include**: Reuse template snippets:
    ```html
    {% include 'partial/nav.html' %}
    ```

#### c. **Filters**
Filters modify variables for display. Syntax: `{{ variable|filter }}`
- Examples:
  - `{{ name|lower }}`: Converts `name` to lowercase.
  - `{{ date|date:"Y-m-d" }}`: Formats a date.
  - `{{ text|truncatewords:10 }}`: Truncates text to 10 words.
  - Chaining filters: `{{ name|lower|capfirst }}`

#### d. **Comments**
- Single-line: `{# This is a comment #}`
- Multi-line:
  ```html
  {% comment %}
      This is a multi-line comment.
  {% endcomment %}
  ```

#### e. **Static Files**
Load static files (CSS, JS, images) using the `static` tag:
```html
{% load static %}
<img src="{% static 'images/logo.png' %}" alt="Logo">
```
- Ensure static files are in the `static/` directory and run `python manage.py collectstatic` for production.

### 4. **How Django Processes Templates**
1. **View Passes Data**: A view function or class renders a template and passes a context (a dictionary of data).
   ```python
   from django.shortcuts import render

   def home(request):
       context = {'username': 'Alice', 'posts': ['Post 1', 'Post 2']}
       return render(request, 'app_name/home.html', context)
   ```
2. **Template Loading**: Django’s template engine locates the template in:
   - Project-level `templates/` (if listed in `DIRS`).
   - App-specific `templates/` (if `APP_DIRS=True`).
3. **Template Rendering**: The engine replaces variables and processes tags/filters to generate the final HTML.
4. **Response**: The rendered HTML is returned as an HTTP response to the client.

### 5. **Steps to Create and Use a Template**
1. **Create Template Files**:
   - Create `app_name/templates/app_name/home.html`.
   - Optionally, create a project-level `templates/base.html` for shared layouts.
2. **Write Template Code**:
   - Use variables, tags, and filters as needed.
   - Use inheritance for reusable layouts.
3. **Configure Settings**:
   - Ensure `TEMPLATES` in `settings.py` is set up correctly.
4. **Render in View**:
   ```python
   from django.shortcuts import render

   def home(request):
       return render(request, 'app_name/home.html', {'title': 'Home'})
   ```
5. **Map URL**:
   - In `app_name/urls.py`:
     ```python
     from django.urls import path
     from . import views

     urlpatterns = [
         path('', views.home, name='home'),
     ]
     ```

### 6. **Best Practices**
- **Use Template Inheritance**: Create a `base.html` for shared layouts (header, footer, etc.).
- **Namespace Templates**: Store templates in `app_name/templates/app_name/` to avoid conflicts.
- **Keep Templates Simple**: Avoid complex logic; move it to views or models.
- **Use Static Files Properly**: Store CSS/JS in `static/` and use `{% load static %}`.
- **Enable Debugging**: Set `DEBUG=True` in `settings.py` during development to see template errors.

---

### 8. **Common Issues**
- **TemplateDoesNotExist**: Ensure the template path is correct and `TEMPLATES` settings are properly configured.
- **Variable Not Found**: Verify the context dictionary in the view includes the variable.
- **Static Files Not Loading**: Run `python manage.py collectstatic` and ensure `{% load static %}` is used.

For more details, check the [Django template documentation](https://docs.djangoproject.com/en/stable/topics/templates/). If you have a specific template use case or issue, let me know for a tailored explanation!
