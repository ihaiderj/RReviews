{% load static wagtailcore_tags wagtailuserbar %}

<!DOCTYPE html>
<html class="no-js" lang="en">
    <head>
        <meta charset="utf-8" />
        <title>
            {% block title %}
                {% if page.seo_title %}{{ page.seo_title }}{% else %}{{ page.title }}{% endif %}
            {% endblock %}
            {% block title_suffix %}
                {% wagtail_site as current_site %}
                {% if current_site and current_site.site_name %}- {{ current_site.site_name }}{% endif %}
            {% endblock %}
        </title>
        <meta name="description" content="" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />

        {# Global stylesheets #}
        <link rel="stylesheet" type="text/css" href="{% static 'css/RReviews.css' %}">

        {% block extra_css %}
            {# Override this in templates to add extra stylesheets #}
        {% endblock %}
    </head>

    <body class="{% block body_class %}{% endblock %}">
        {% wagtailuserbar %}

        {% block content %}{% endblock %}

        {# Global javascript #}
        <script type="text/javascript" src="{% static 'js/RReviews.js' %}"></script>

        {% block extra_js %}
            {# Override this in templates to add extra javascript #}
        {% endblock %}
    </body>
</html>
