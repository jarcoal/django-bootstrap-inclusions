from setuptools import setup

setup(
    name="bootstrap-inclusions",
    version="0.0.1",
    description="Library of template tags to help integrate with Bootstrap",
    long_description="Library of template tags to help integrate with Bootstrap",
    keywords="django, bootstrap",
    author="Jared Morse <jarcoal@gmail.com>",
    author_email="jarcoal@gmail.com",
    url="https://github.com/jarcoal/django-bootstrap-inclusions",
    license="BSD",
    packages=["bootstrap-inclusions"],
    zip_safe=False,
    install_requires=[],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)
