from setuptools import setup

setup(
    name='indico-fonts',
    version='1.2',
    url='https://getindico.io',
    license='Several',
    author='Indico Team',
    author_email='indico-team@cern.ch',
    description='Indico - Binary fonts',
    platforms=['any'],
    zip_safe=False,
    packages=['indico_fonts'],
    package_data={'indico_fonts': ['*.otf', '*.ttc', '*.ttf']},
    include_package_data=True,
    classifiers=['License :: Other/Proprietary License',
                 'Topic :: Text Processing :: Fonts']
)
