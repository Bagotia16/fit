from setuptools import setup

setup(
   name='fit',
   version='0.0.1',
   description='A timepass project for health purpose',
   license="MIT",
   url = "https://github.com/Bagotia16/fit",
   author='Deepanshu Bagotia',
   author_email='bagotiadeepanshu@gmail.com',
   packages=['fit'], 
   entry_points={
      "console_scripts": [
         "fit=fit.__init__",
      ]
   },
)