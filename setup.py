# -*- coding: utf-8 -*-
##
## $Id$
##
## This file is part of CDS Indico.
## Copyright (C) 2002, 2003, 2004, 2005, 2006, 2007 CERN.
##
## CDS Indico is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## CDS Indico is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with CDS Indico; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

from setuptools import setup, find_packages

if __name__ == '__main__':

    setup(name = "cds-indico-extras",

          version = '0.2',
          description = "Indico - Extra resources",
          author = "Indico Team",
          author_email = "indico-project@cern.ch",
          url = "http://cern.ch/indico",
          download_url = "http://cern.ch/indico/download-beta.html",
          platforms = ["any"],
          long_description = "Extra resources for Indico, such as fonts",
          license = "Several",
          zip_safe = False,
          packages = find_packages(),
          namespace_packages = ['indico'],
          package_data = {'': ['*.ttf','*.ttc'] },
          include_package_data = True,
          classifiers = ["License :: Other/Proprietary License",
                         "Topic :: Text Processing :: Fonts"]
          )
