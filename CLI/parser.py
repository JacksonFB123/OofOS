import logging
import CLI.func as CLI

from time import sleep
from render import clear

from flask import Flask
from colors import color

from threading import Thread

def _run(port, text):

  app = Flask(__name__)

  log = logging.getLogger("werkzeug")

  log.disabled = True

  app.logger.disabled = True

  @app.route("/")
  def index():
    return text

  app.run(host = "0.0.0.0", port = port)

def parse(cmd, args, config, startSystem):

  if cmd.lower() in ["sys", "system", "sys-stats"]:

    CLI.system()

  elif cmd.lower() in ["cls", "clear"]:

    clear()

  elif cmd.lower() in ["help", "info"]:

    CLI.help(config)

  elif cmd.lower() in ["license"]:

    CLI.license()

  elif cmd.lower() in ["logout", "lgt"]:

    startSystem(doBoot = False)

  elif cmd.lower() in ["server", "sv"]:

    if not args:

      print("\nUsage: server [host] [port] [text]\n")

    else:

      try:

        host = args[0]

        port = args[1]

        text = ""

        for arg in args[2:]:

          text += arg + " "

        try:

          port = int(port)

          thread = Thread(target = _run, args = [port, text])

          thread.start()

          sleep(.5)

          clear()

          print(f"\nServer now running at {host}:{port}\n")

        except:

          print("\nInvalid port specified.\n")

      except:

        print("\nUsage: server [host] [port] [text]\n")

  elif cmd.lower() in ["echo", "write", "print"]:

    if not args:

      pass

    else:

      text = ""

      for arg in args:

        text += arg + " "

      print(f"\n{text[:-1]}\n")

  elif cmd.lower() in ["reboot", "rbt"]:

    print(f"Rebooting system...{color('reset')}")

    startSystem()

  elif cmd.lower() == "":

    pass

  else:

    print(f"\nCommand \"{cmd}\" not found.\n")