# Licensed under the MIT license.
# For more information, check the license command.

### Modules ###
from time import sleep
from json import loads

from system import login
from system import setup

from datetime import date
from CLI.parser import parse

from colors import colored, color

from system import initialize
from render import load, clear


### System ###
def startSystem(doBoot=True):

	if doBoot:

		### Variables ###
		REQ_FIRST_TIME_SETUP = False

		### Booting Screen ###
		load()

		print(open("icons/bootLogo.txt", "r").read())

		sleep(1.2)

		### Initialization ###

		REQ_FIRST_TIME_SETUP = initialize(REQ_FIRST_TIME_SETUP)

		clear()

		if REQ_FIRST_TIME_SETUP:

			setup()

	config = loads(open("data/os.json", "r").read())

	### Begin Login ###
	username, password = login(config)

	sleep(2)

	### Dashboard ###
	clear()

	print(
	    colored(
	        f"OofOS v{config['version']} | User: {username} | {date.today()}",
	        "green"))

	print()

	while True:

		try:

			cmd = input(
			    f"{colored(f'{username}@oofosServer', 'yellow')} {colored('$', 'green')} {color('green')}"
			)

		except KeyboardInterrupt:

			cmd = ""

			print(
			    "\n\nIgnoring exit key; in the future this will terminate ZealousOS.\n"
			)

		args = None

		if " " in cmd:

			args = cmd.split(" ")[1:]

			cmd = cmd.split(" ")[0]

		parse(cmd, args, config, startSystem)


startSystem()