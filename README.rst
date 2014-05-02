Geoserver migration helper script
=================================

Give a directory to this script and it'll search the directories for
``datastore.xml`` files and adjust two things, if found:

- A database host that starts with ``s-`` is replaced with one starting with
  ``p-``: we're moving to production.

- The line with the password is emptied. This forces geoserver to ask you for
  the password again. Simply copy/pasting the password between different
  geoservers doesn't work, probably because the encrypted password is hashed
  with some secret key or so.

The script also prints out which files it changed and what it did in them.

Usage::

    $ python migrate.py some/fancy/directory


You can test the script (on linux when you have a ``/tmp`` dir...) by running ``./test.sh``.
