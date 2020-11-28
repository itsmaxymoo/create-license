import sys
from os import path
import datetime
import pkgutil

PROGRAM_NAME = "create-license"
PROGRAM_CMD = "create-license"
PROGRAM_VERSION = "2.0.5"
PROGRAM_AUTHOR = "Max Loiacono"
PROGRAM_URL = "https://github.com/itsmaxymoo/create-license"

ENABLED_LICENSES = [
	("apache-2", "Apache License, version 2.0"),
	("bsd-3", "BSD License 3.0 (\"New/Revised BSD License\")"),
	("bsd-2", "BSD License 2.0 (\"Free BSD License\")"),
	("gpl-3", "GNU General Public License 3.0"),
	("lgpl-3", "GNU Lesser General Public License 3.0"),
	("mit", "MIT License"),
	("mpl-2", "Mozilla Public License, version 2.0"),
	("none", "Public domain (+liability, warranty)")
]

config = ""
config_file_path = path.expanduser("~") + "/.create_license"
f = open(config_file_path, mode="a", encoding="utf-8")


def main():
	# Configuration file
	global f, config
	f = open(config_file_path, mode="r", encoding="utf-8")
	config = f.read().replace("\n", "").replace("\r", "")
	if len(config) == 0:
		print("Please set the name to be automatically inserted into licenses.")
		set_name()

	# Command line arguments
	cli_opt = ""
	if len(sys.argv) > 1:
		cli_opt = sys.argv[1]

	if cli_opt in ["", "-h", "--help", "help"]:
		show_help()
	elif cli_opt == "list":
		list_licenses()
	elif cli_opt == "set-name":
		set_name()
	elif len(sys.argv) > 2:
		create_license(sys.argv[1], sys.argv[2])
	elif len(sys.argv) > 1:
		create_license(sys.argv[1])

	exit(0)


def create_license(license_name, filename="LICENSE"):
	current_year = str(datetime.date.today().year)
	license_text = ""

	try:
		license_text = str(pkgutil.get_data(__name__, "templates/" + license_name.lower() + ".txt").decode())
	except:
		pass

	if license_text != "":
		license_text = license_text.replace("{{YEAR}}", current_year)
		license_text = license_text.replace("{{NAME}}", config)

		try:
			license_file = open(filename, mode="x", encoding="utf-8")
			license_file.write(license_text)

			print("Created \"" + license_name.lower() + "\" license at " + filename)
		except:
			print("ERROR: Could not create file: " + filename)
	else:
		print("ERROR: License \"" + license_name.lower() + "\" not found!")


def show_help():
	print(PROGRAM_NAME + " version " + PROGRAM_VERSION + " by " + PROGRAM_AUTHOR)
	print("See at: " + PROGRAM_URL + "\n")
	print("Usage:\t" + PROGRAM_CMD + " [option]")
	print("\t" + PROGRAM_CMD + " [license]")
	print("\t" + PROGRAM_CMD + " [license] [file]")
	print("Options:")
	print("\thelp\t\t\tshow help text")
	print("\tlist\t\t\tlist all licenses")
	print("\tset-name\t\tset your name")
	print("\t[license]\t\tcreate a new [license] file")
	print("\t[license] [file]\tcreate a new [license] with filename [file]")


def list_licenses():
	print("License\t\tDescription\n")

	for l in ENABLED_LICENSES:
		tabs = "\t\t" if len(l[0]) < 8 else "\t"
		print(l[0] + tabs + l[1])

	print("\nNeed help deciding? See:")
	print("https://opensource.org/licenses")
	print("https://choosealicense.com/licenses")


def set_name():
	name = input("Your name: ")
	print("Hi, " + name)
	f = open(config_file_path, mode="w", encoding="utf-8")
	f.write(name)


main()
