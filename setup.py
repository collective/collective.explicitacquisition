from setuptools import find_packages, setup

version = '1.2.dev0'
description = open("README.rst").read() + "\n" + open("CHANGES.rst").read()

setup(
    name='collective.explicitacquisition',
    version=version,
    description="Disallow access to acquired content outside the current path.",  # noqa
    long_description=description,
    classifiers=[
        "Framework :: Zope",
        "Framework :: Zope :: 4",
        "Framework :: Zope :: 5",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Environment :: Web Environment",
    ],
    keywords='traversal acquisition',
    author='Godefroid Chapelle, Johannes Raggam',
    author_email='raggam-nl@adm.at',
    url='https://github.com/collective/collective.explicitacquisition',
    license='GPL',
    packages=find_packages(),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.CMFCore',
    ],
    extras_require={
        'test': [
            'plone.app.testing[robot]'
        ]
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """
)
