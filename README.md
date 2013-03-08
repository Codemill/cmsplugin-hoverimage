# Flexible Video
Hover Image is a plugin for Django CMS that let's you include a picture
that changes to another picture on hover.

## Requirements
django-cms >= 2.1

## Installation
Hover Image can be installed with pip:

	pip install cmsplugin-hoverimage

## Usage
- Add cmsplugin\_hoverimage to INSTALLED\_APPS in your settings.py file:

		INSTALLED_APPS = (
			...
			'cmsplugin\_hoverimage',
			...
		)

- Run ./manage.py syncdb to add tables

- Use the plugin like any other CMS plugin

