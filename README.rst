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




iterpop makes popping the value out of a singleton container or a homogeneous container safe & fun


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
  ip.pophomogeneous(['a'])
  ip.pophomogeneous({'a'})
  ip.pophomogeneous('a')

  # also returns 'a'
  ip.pophomogeneous(['a', 'a'])
  ip.pophomogeneous('aaa')
  ip.pophomogeneous('a' for __ in range(100))

  # throws
  ip.pophomogeneous([])
  ip.pophomogeneous(set())
  ip.pophomogeneous('')

  # throws
  ip.pophomogeneous(['a', 'b'])
  ip.pophomogeneous({'a', 'b'})
  ip.pophomogeneous('ab'})

  # returns 'a'
  ip.poursingleton(['a'])
  ip.poursingleton({'a'})
  ip.poursingleton('a')

  # returns None
  ip.poursingleton([])
  ip.poursingleton(set())
  ip.poursingleton('')

  # throws
  ip.poursingleton(['a', 'b'])
  ip.poursingleton({'a', 'b'})
  ip.poursingleton('ab'})

  # returns 'a'
  ip.pourhomogeneous(['a'])
  ip.pourhomogeneous({'a'})
  ip.pourhomogeneous('a')

  # also returns 'a'
  ip.pourhomogeneous(['a', 'a'])
  ip.pourhomogeneous('aaa')
  ip.pourhomogeneous('a' for __ in range(100))

  # returns None
  ip.pourhomogeneous([])
  ip.pourhomogeneous(set())
  ip.pourhomogeneous('')

  # throws
  ip.pourhomogeneous(['a', 'b'])
  ip.pourhomogeneous({'a', 'b'})
  ip.pourhomogeneous('ab'})


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
