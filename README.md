# Django-Rest-Api-Task
Django REST Framework simple API example without model class and db.

# Installation

1. Install python3, then create virtualenv (optional).
2. Clone the repo, then cd to the repo directory.
3. Install requirements:
  
  ```
  pip install requirements.txt
  ```
4. Run the app locally:

  ```
  python3 thomas_murray/manage.py runserver
  ```

# Test

You can run the tests as follows:
```
python3 thomas_murray/manage.py test.
```

# REST API

(example) ip:port/ = 127.0.0.1:8000/

### ip:port/api/currency 
  Get exchange rate for USD/EUR.
  
### ip:port/api/ip
  Get Ipv4 address for server.
  
```python
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thomas_murray.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
```
