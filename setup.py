from setuptools import setup, find_packages
import sys, os

version = '0.2'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='auth_pubtkt',
      version=version,
      description="This software implements mod_auth_pubtkt authentication for Python world.",
      long_description=read('README.txt'),
      classifiers=[
      'Development Status :: 3 - Alpha',
      'Environment :: Web Environment',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Programming Language :: Python',
      'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware'
      ],
      keywords='mod_auth_pubtkt authentication single-sing-on',
      author='Andrey Plotnikov',
      author_email='plotnikoff@gmail.com',
      url='https://github.com/AndreyPlotnikov/auth_pubtkt',
      license='BSD License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [paste.app_factory]
      authrequest = auth_pubtkt.authrequest:make_app
      """,
      )
