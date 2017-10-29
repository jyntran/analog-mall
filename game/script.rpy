# The script of the game goes in this file.

define u = Character("User")

label start:

    scene black

    python:
        u.name = renpy.input("What is your name?", length=32) or u.name
        u.name = u.name.strip()

        renpy.call_screen("confirm", message="Your name will be [u].", yes_action=Return(), no_action=Jump("start"))

    "Welcome to Macintosh, [u]."

    return