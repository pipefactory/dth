# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('???', color="#c8ffc8")


# The game starts here.
label start:

    scene white

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    e "let's go into Character Workspace"

label character_workspace:

    window hide None

    scene black
    with dissolve

    python:
        ui.add(CharacterWorkspace())
        end = ui.interact(suppress_overlay=True, suppress_underlay=True)

    scene white
    with dissolve

    e "You've returned"

    return
