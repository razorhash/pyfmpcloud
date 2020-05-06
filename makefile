git:
    git add .
    git commit -m "$m"
    git push -u origin master 

setup:
    python setup.py install
    
dist:
    python setup.py sdist
    python -m twine upload --skip-existing dist/*