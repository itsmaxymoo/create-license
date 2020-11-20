import sys
from os import path
import datetime
import pkgutil

PROGRAM_NAME = "create-license"
PROGRAM_VERSION = "2.0"
PROGRAM_AUTHOR = "Max Loiacono"
PROGRAM_URL = "https://github.com/itsmaxymoo/create-license"

ENABLED_LICENSES = [
	("mit", "MIT License")
]

config = ""
config_file_path = path.expanduser("~") + "/.create-license"
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

			print("Created " + license_name.lower() + " license at " + filename)
		except:
			print("ERROR: Could not create file: " + filename)
	else:
		print("ERROR: License \"" + license_name.lower() + "\" not found!")


def show_help():
	print(PROGRAM_NAME + " version " + PROGRAM_VERSION + " by " + PROGRAM_AUTHOR)
	print("See at: " + PROGRAM_URL + "\n")
	print("Usage:\t" + path.basename(__file__) + " [option]")
	print("\t" + path.basename(__file__) + " [license]")
	print("\t" + path.basename(__file__) + " [license] [file]")
	print("Options:")
	print("\thelp\t\t\tshow help text")
	print("\tlist\t\t\tlist all licenses")
	print("\tset-name\t\tset your name")
	print("\t[license]\t\tcreate a new [license] file")
	print("\t[license] [file]\tcreate a new [license] with filename [file]")


def list_licenses():
	print("License\tDescription\n")

	for l in ENABLED_LICENSES:
		print(l[0] + "\t" + l[1])


def set_name():
	name = input("Your name: ")
	print("Hi, " + name)
	f = open(config_file_path, mode="w", encoding="utf-8")
	f.write(name)


if __name__ == "__main__":
	main()
