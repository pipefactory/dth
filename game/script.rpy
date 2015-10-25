﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.

define e = Character('???', color="#c8ffc8")
image white = "#fff"
image black = "#000"

screen skill_workbanch_button:

    textbutton "Skill Workbanch" id "tbtn_skill_workbanch" action ui.callsinnewcontext("lbl_character_workspace") xalign 0.01 yalign 0.01

## ==================================================================
## before_main_menu
## ==================================================================

label before_main_menu:

    "before main menu"

    return

# The game starts here.
label start:

    show white

    e "You've created a new Ren'Py game."

label roll_in_workspace:

    show screen skill_workbanch_button

    "roll_in_workspace"

    "roll_in_workspace..."

    jump roll_in_workspace