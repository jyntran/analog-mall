# The script of the game goes in this file.

define p = Character("Me")
define h = Character("Her")

init:
    $ center    = Position(xalign=0.5, yalign=0.0)
    $ left      = Position(xalign=0.1, yalign=0.0)
    $ right     = Position(xalign=0.9, yalign=0.0)

label start:

    jump story