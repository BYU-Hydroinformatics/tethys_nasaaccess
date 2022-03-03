import os
import sys
from setuptools import setup, find_packages
# from tethys_apps.app_installation import custom_develop_command, custom_install_command
from tethys_apps.app_installation import find_resource_files

### Apps Definition ###
app_package = 'nasaaccess'
release_package = 'tethysapp-' + app_package
# app_class = 'nasaaccess.app:Nasaaccess'
# app_package_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tethysapp', app_package)

### Python Dependencies ###
dependencies = []

# -- Get Resource File -- #
resource_files = find_resource_files('tethysapp/' + app_package + '/templates', 'tethysapp/' + app_package)
resource_files += find_resource_files('tethysapp/' + app_package + '/public', 'tethysapp/' + app_package)
resource_files += find_resource_files('tethysapp/' + app_package + '/workspaces', 'tethysapp/' + app_package)


setup(
    name=release_package,
    version='1.0.0',
    # tags='&quot;Hydrology&quot;, &quot;GLDAS&quot;, &quot;GPM&quot;, &quot;SWAT&quot;',
    description='Web interface for downloading precipitation and air temperature data from NASA&#39;s EarthData website',
    long_description='',
    keywords='',
    author='Spencer McDonald, Ibrahim Mohammed',
    author_email='ibrahim.mohammed@nasa.gov',
    url='',
    license='NASA OPEN SOURCE AGREEMENT VERSION 1.3',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    # namespace_packages=['tethysapp', 'tethysapp.' + app_package],
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies
    # cmdclass={
    #     'install': custom_install_command(app_package, app_package_dir, dependencies),
    #     'develop': custom_develop_command(app_package, app_package_dir, dependencies)
    # }
)