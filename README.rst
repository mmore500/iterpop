============
iterpop
============


.. image:: https://img.shields.io/pypi/v/iterpop.svg
        :target: https://pypi.python.org/pypi/iterpop

.. image:: https://img.shields.io/travis/mmore500/iterpop.svg
        :target: https://travis-ci.com/mmore500/iterpop

.. image:: https://readthedocs.org/projects/iterpop/badge/?version=latest
        :target: https://iterpop.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




iterpop makes popping the value out of a singleton container safe and fun


* Free software: MIT license
* Documentation: https://iterpop.readthedocs.io.


.. code-block:: python3

  from iterpop import iterpop as ip

  # returns 'a'
  ip.popsingleton(['a'])
  ip.popsingleton({'a'})
  ip.popsingleton('a')

  # throws
  ip.popsingleton([])
  ip.popsingleton(set())
  ip.popsingleton('')

  # throws
  ip.popsingleton(['a', 'b'])
  ip.popsingleton({'a', 'b'})
  ip.popsingleton('ab'})

  # returns 'a'
  ip.pop homogeneous(['a'])
  ip.pop homogeneous({'a'})
  ip.pop homogeneous('a')

  # also returns 'a'
  ip.pop homogeneous(['a', 'a'])
  ip.pop homogeneous('aaa')
  ip.pop homogeneous('a' for __ in range(100))

  # throws
  ip.pop homogeneous([])
  ip.pop homogeneous(set())
  ip.pop homogeneous('')

  # throws
  ip.pop homogeneous(['a', 'b'])
  ip.pop homogeneous({'a', 'b'})
  ip.pop homogeneous('ab'})


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
