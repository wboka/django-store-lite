=====
Store Lite
=====

Store Lite is a drop-in store for your Django web application. It consists of Orders and Products.

Detailed documentation is in the "docs" directory. Coming soon.

Install
---------

1. Install "storefront" from Github like this::

    $ pip install https://github.com/wboka/django-storefront.git


Quick start
-----------

1. Add "storefront" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'storefront',
    ]

2. Include the storefront URLconf in your project urls.py like this::

    url(r'^store/', include('storefront.urls')),

3. Run `python manage.py migrate` to create the storefront models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create an order with products (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/store/ to view the store.

Uninstall
---------

1. Remove "storefront" like this::

    $ pip uninstall django-storefront
