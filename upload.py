import os
import shutil
from pathlib import Path


def submit():
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    shutil.rmtree('dist')
    shutil.rmtree('build')
    for d in Path(__file__).parent.glob('*.egg-info'):
        shutil.rmtree(d)


if __name__ == '__main__':
    submit()
