from setuptools import setup

setup(
    name="indico-fonts",
    version='1.1',
    url='https://getindico.io',
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
