# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.

define e = Character('???', color="#c8ffc8")
image white = Solid("#fff")
image black = Solid("#000")

screen character_workspace_button:

    vbox xalign 0.01 yalign 0.01:

        textbutton "Character Workspace" action ui.callsinnewcontext("character_workspace")

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

    show screen character_workspace_button

    "roll_in_workspace"

    jump roll_in_workspace