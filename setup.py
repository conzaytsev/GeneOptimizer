from setuptools import setup


setup(
    name="genex", 
    version='0.1.0',
    author="Konstantin Zaytsev",
    url='https://github.com/conzaytsev/GeneOptimizer',
    description='Codon optimization tool',
    long_description='Python module for codon optimization in genes to achieve specific expression levels.',
    packages=['genex'],
    install_requires=[],
    python_requires='>3.9',
    package_data={'genex': ['models/*.pkl']},
    classifiers= [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)
