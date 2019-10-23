from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='gdeck',
      version='0.1',
      description='Cards',
      url='https://github.com/damiiegregorio/gdeck',
      author='damiiegregorio',
      author_email='damiiekeith@gmail.com',
      license='MIT',
      packages=['gdeck'],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Operating System :: Microsoft :: Windows',
        'Development Status :: 3 - Alpha'
      ],
      keywords='Cards',
      include_package_data=True,
      zip_safe=False)