#!/bin/bash
rm dist/*
python3 setup.py sdist bdist_wheel
echo "BUILD DONE! Run with argument 'upload' to upload to pypi"

if [ "$1" == "uplaod" ]; then
	python3 -m twine upload dist/*
fi
