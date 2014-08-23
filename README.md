protoman 0.1a
=================

Simple django app to help with prototyping.

Running `newprototype` will set up a new TemplateView, and Url mapping along with a django template file for your prototype. This allows you to keep your prototypes inside of the django engine thus giving you all the django goodies, while keeping your code highly re-usable. Also allows your front end 'devs' to stay the heck out of your python code. As a nice bonus to your devs, it creates a usuable list of views that they will need to bang out.

Installation
-----------
1. Download/clone/fetch this repo into your app directory
2. Include `protoman` in your `INSTALLED_APPS`
3. Include url file into app
`url(r'^protoman/', include('protoman.urls')),`

Usage
-------
`manage.py newprototype <name of prototype>`


Required Folders
------------------
1. <root>/raw/tpl/   (currently set up to generate jade files in the project root)


Todo
----
1. Ability to create folders if necessary (see above)
2. Create some variables so you can pass in template names & directories
3. Create a method to turn off/on jade creation
4. Flesh out ability to pass in a dictionary to be returned as context (simple integration complete)
