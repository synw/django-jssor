Runing the example
==================

.. highlight:: bash

::

   mkdir jssor_example
   mv django-jssor/example jssor_example
   cd jssor_example
   virtualenv .
   source bin/activate
   pip install django django-jssor Pillow pytz
   cd example
   python manage.py migrate
   python manage.py runserver
   