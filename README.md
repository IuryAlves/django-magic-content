# django-magic-content

[![Build Status](https://drone.io/github.com/DjenieLabs/django-magic-content/status.png)](https://drone.io/github.com/DjenieLabs/django-magic-content/latest)

Works for Django1.6 and Django1.7

A flexible content application

## Documentation

django-magic-content provides a flexible content engine that you can extends
on your project, also there are a lot of built-in contents that you can attach,
following the Django's contrib structure.


## Quickstart

Install django-magic-content

    `pip install -e https://github.com/DjenieLabs/django-magic-content.git#egg=django-magic-content`

If you are going to contribute to this project, install this way

    `git clone git@github.com:DjenieLabs/django-magic-content.git`
    `pip install -e django-magic-content/`


## Usage

Before to add magiccontent itself to INSTALLED_APPS, you must add its dependencies
in INSTALLED_APPS

    `'easy_thumbnails',
    'floppyforms',
    'image_cropping',
    'multisitesutils',
    'magicgallery',`

And of course, the magiccontent itself

   `'magiccontent',`


At your urls.py, add the following

    `url(r'^magiccontent/', include('magiccontent.urls')),`


If you are going to use contrib apps is pretty simple, just choose which ones
that you want to use, install them in INSTALLED_APPS

    `'magiccontent.contrib.simplecontent',
    'magiccontent.contrib.background',
    'magiccontent.contrib.iconcontent',
    'magiccontent.contrib.imagecontent',
    'magiccontent.contrib.longcontent',
    'magiccontent.contrib.pagelink',`


And include the urls in urls.py:

    `url(r'^contrib/', include('magiccontent.contrib.simplecontent.urls')),
    url(r'^contrib/', include('magiccontent.contrib.background.urls')),
    url(r'^contrib/', include('magiccontent.contrib.iconcontent.urls')),
    url(r'^contrib/', include('magiccontent.contrib.imagecontent.urls')),
    url(r'^contrib/', include('magiccontent.contrib.longcontent.urls')),
    url(r'^contrib/', include('magiccontent.contrib.pagelink.urls')),`


## Testing

To run the tests, create a empty virtualenv like "magiccontent" and install tox:

    `pip install tox`

Then, run the tests:

    `tox`

If you are going to contribute to the code, you may want a faster way to run your
tests, to do that, install all dependencies listed on requirements-test.txt and the
django1.6, after that run:

    `py.test tests/`

Beware, this is not a replacement of tox, the reason to use py.test directly is only
to save some time during the development, but you must run tox when you pull the code
and just before you commit your code.