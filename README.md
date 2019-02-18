# create-license

Easily create license files. Requires PHP.

## Quickstart

1. Download this repo and run `./install.sh` (pcan) or run `mkdir ~/.local/bin && echo export PATH="$HOME/.local/bin:\$PATH" >> ~/.profile && source ~/.profile && wget https://raw.githubusercontent.com/itsmaxymoo/create-license/master/build/create-license -O ~/.local/bin/create-license && chmod +x ~/.local/bin/create-license`.

2. Run `create-license list` to see what licenses are available.
3. Run `create-license {name}` to create a license! Optionally, you can specify a path to the license file after the license name.

When you create a license for the first time, create-license will prompt you for your name. This will be the name that is inserted into generated licenses. You can change it by running `create-license set-name`.

## Contributing

Want to add a license to create-license?

* Add your license txt file to the `templates` directory.
	* `{{NAME}}` will be automatically set to the user's name.
	* `{{YEAR}}` will be automatically set to the current year.
* Add your entry to `licenses.json`
	```
	{
		"code": "License identifier",
		"name": "Long name",
		"file": "Name of text file in templates/"
	}
	```
* You **must** add your entry in alphabetical order by the `code` property.
* You **must** convert your license text file to use `{{NAME}}` and `{{YEAR}}`, if possible.
* Then submit your PR!