Run the example
===============

.. highlight:: bash

::

   mkdir jssor_example
   mv django-jssor/example jssor_example
   cd jssor_example
   virtualenv .
   source bin/activate
   pip install django django-jssor Pillow pytz
   cd example
   python manage.py runserver
   
Go to ``http://localhost:8000/``. 

Admin login is ``admin`` and password is ``jssor_example``.
   