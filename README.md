# create-license

Easily create license files. Requires Python 3.

# Installation

`pip install create-license`

# Usage

`create-license [license name] [?output]`  
Creates the specified license. If no output file is
specified, it will write to `./LICENSE`.

`create-license list`  
Lists available licenses.

`create-license help`  
Shows additional information.

# Add a License

To add a license to create-license:

* Fork this project
* Add your license template to `create_license/templates/`
* `{{YEAR}}` will be replaced with the year
* `{{NAME}}` will be replaced with the user's name
* Add the appropriate entry to `ENABLED_LICENSES` in `create_license/__init__.py`
