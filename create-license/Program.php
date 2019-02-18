<?php

namespace CreateLicense;

class Program {
	private static $config = array(
		'firstRun' => true,
		'name' => ''
	);
	private static $home;
	private static $licenses;

	public static function Main(array $cliArgs) {
		\PHPCanner::log(\PHPCanner::NAME . ' version ' . \PHPCanner::VERSION . PHP_EOL);
		self::$home = getenv('HOME') . DIRECTORY_SEPARATOR . '.config' . DIRECTORY_SEPARATOR . 'create-license';
		self::$licenses = json_decode(\PHPCanner::get_file('licenses.json'), true)['list'];

		if (self::configRead() === false) {
			self::configWrite();
		}

		if (empty($cliArgs[1]) || strtolower($cliArgs[1]) == 'help') {
			self::helpText();
		}
		elseif (strtolower($cliArgs[1]) == 'list') {
			self::listLicenses();
		}
		elseif (strtolower($cliArgs[1]) == 'set-name') {
			self::setName();
			\PHPCanner::end('Your name is now: "' . self::$config['name'] . '".');
		}
		elseif (!empty($cliArgs[1])) {
			if (empty($cliArgs[2])) {
				$cliArgs[2] = getcwd() . DIRECTORY_SEPARATOR . 'LICENSE';
			}

			self::create(strtolower($cliArgs[1]), $cliArgs[2]);
		}
		else {
			self::helpText();
		}
	}

	private static function create($licenseCode, $file): void {
		if (self::$config['firstRun']) {
			self::setName();
		}

		$l = null;

		foreach (self::$licenses as $li) {
			if (strtolower($li['code']) === strtolower($licenseCode)) {
				$l = $li;
			}
		}

		if ($l == null) {
			\PHPCanner::log('ERROR: License ' . $licenseCode . ' not found!' . PHP_EOL);
			self::listLicenses();
		}
		else {
			$license = \PHPCanner::get_file('templates/' . $l['file']);
			$license = str_replace('{{YEAR}}', date('Y'), $license);
			if (self::$config['name'] != '') {
				$license = str_replace('{{NAME}}', self::$config['name'], $license);
			}

			if (@file_put_contents($file, $license)) {
				\PHPCanner::end('Created ' . $l['name'] . ' License at ' . $file);
			}
		}
	}

	private static function setName(): void {
		\PHPCanner::log('Please input the name to be used in license files.');
		self::$config['name'] = readline('Name=');
		self::$config['firstRun'] = false;

		self::configWrite();
	}

	private static function configWrite(): void {
		if (!file_exists(self::$home)) {
			if (!@mkdir(self::$home, 0755, true)) {
				\PHPCanner::end('ERROR: Could not create ' . self::$home);
			}
		}

		$file = self::$home . DIRECTORY_SEPARATOR . 'config.json';

		if (!@file_put_contents($file, json_encode(self::$config))) {
			\PHPCanner::end('ERROR: Could not create ' . $file);
		}
	}

	private static function configRead(): bool {
		$file = @file_get_contents(self::$home . DIRECTORY_SEPARATOR . 'config.json');

		if ($file === false) {
			return false;
		}

		self::$config = json_decode($file, true);

		return isset(self::$config['firstRun'])
			&& isset(self::$config['name']);
	}

	private static function helpText(): void {
		\PHPCanner::log('Run create-license {license code}');
		\PHPCanner::log('or create-license {license code} {file}' . PHP_EOL);
		\PHPCanner::log('Run create-license set-name to set your name.');
		\PHPCanner::end('Run create-license list to show available licenses.');
	}

	private static function listLicenses(): void {
		\PHPCanner::log('Available licenses:');
		\PHPCanner::log("Name\t\tLicense" . PHP_EOL);

		foreach (self::$licenses as $l) {
			\PHPCanner::log($l['code'] . "\t\t" . $l['name'] . ' License');
		}

		\PHPCanner::end(PHP_EOL . 'Need help picking? See https://choosealicense.com');
	}
}
