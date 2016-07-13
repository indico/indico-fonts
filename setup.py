# This file is part of Indico.
# Copyright (C) 2002 - 2015 European Organization for Nuclear Research (CERN).
#
# Indico is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# Indico is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Indico; if not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from setuptools import setup

setup(
    name="indico-fonts",
    version='1.0',
    url='http://indico.github.io',
    license='Several',
    author='Indico Team',
    author_email='indico-team@cern.ch',
    description='Indico - Binary fonts',
    platforms=['any'],
    zip_safe=False,
    packages=[b'indico_fonts'],
    package_data={b'indico_fonts': [b'*.otf', b'*.ttc', b'*.ttf']},
    include_package_data=True,
    classifiers=['License :: Other/Proprietary License',
                 'Topic :: Text Processing :: Fonts']
)
