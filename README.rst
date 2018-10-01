=====
Store Lite
=====

Store Lite is a drop-in store for your Django web application. It consists of Orders and Products.

Detailed documentation is in the "docs" directory. Coming soon.

Install
---------

1. Install "store-lite" from Github like this::

    $ pip install https://github.com/wboka/django-store-lite.git


Quick start
-----------

1. Add "store-lite" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'store-lite',
    ]

2. Include the store-lite URLconf in your project urls.py like this::

    url(r'^store/', include('store-lite.urls')),

3. Run `python manage.py migrate` to create the store-lite models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create an order with products (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/store/ to view the store.

Uninstall
---------

1. Remove "store-lite" like this::

    $ pip uninstall django-store-lite
