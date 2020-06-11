# Production Readiness

Project is not production ready.

Now’s a good time to note: don’t use this server in anything resembling a production environment. It’s intended only for use while developing. (We’re in the business of making Web frameworks, not Web servers.)

# Env vars

Allow passing env vars for the database connection

# Dry run of migrations

```
docker-compose run app python manage.py sqlmigrate <app> <migration_number>
```

# `__str__` on Models

It gives you a human readable version of the model printed in the shell and in the Admin console

# `timezone`

Look more into what `timezone.now()` does in Django

# Query through foreign key

In this example `Choice` has a foreign key to `Question`. To find all the `Choice`s that are linked to a question that was published in the current year we can do

```
Choice.objects.filter(question__pub_date__year=current_year)
```

Note how we have `<fk_field_name>__<field_name>__<predicate>`

More info:
- Relations: https://docs.djangoproject.com/en/3.0/ref/models/relations/
- Querying on fields: https://docs.djangoproject.com/en/3.0/topics/db/queries/#field-lookups-intro
- Full on database docs https://docs.djangoproject.com/en/3.0/topics/db/queries/

# Info on urls

https://docs.djangoproject.com/en/3.0/topics/http/urls/

# More about templates

https://docs.djangoproject.com/en/3.0/topics/templates/
How loading happens: https://docs.djangoproject.com/en/3.0/topics/templates/#template-loading

# More about testing

https://docs.djangoproject.com/en/3.0/topics/testing/

# More info on static files

https://docs.djangoproject.com/en/3.0/howto/static-files/
https://docs.djangoproject.com/en/3.0/ref/contrib/staticfiles/
Deployment https://docs.djangoproject.com/en/3.0/howto/static-files/deployment/

# Start command for gunicorn, does not serve static files
```
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi"]
```