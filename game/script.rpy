# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define jar = Character("Jarod Canton")
define dia = Character("Diana")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    "This is where the game starts"

    "Thank you for your contributions   , Buddha, Nait, Malca"

    show jarod base:
        zoom 1.7
        yalign 1.0
    jar "The true monster is inside every human's mind"

    show diana base:
        zoom 1.5
        xalign 0.9
        yalign 1.0

    dia "That is kinda cringe, shine baka!"


    # This ends the game.

    return
