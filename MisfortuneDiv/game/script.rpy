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
    play music "audio/mellow_ambient_rode.mp3" fadein 0.70
    show bg_inside_car

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "Thank you for your contributions, Buddha, Nait, Malca"
    "It was a particularly sunny afternoon for the dead-middle of autumn."
    "The gentle sunlight shining through the co-pilot’s window made Jarod especially drowsy."
    "Most car rides did, anyways, but since the season called for coats, he couldn’t help himself from getting carried away by the unintentionally snug seating."


    show diana base:
        zoom 1.5
        xalign 0.85
        yalign 1.0

    dia "Dude, sit up,"
    dia "we’re two blocks away. First impressions matter."

    "Jarod recoiled, took a deep breath and started stretching with his eyes half shut, mumbling a very tired"


    show jarod base1:
        zoom 1.8
        yalign 1.0
    jar "yeah"

    # Change of scenery
    # hide diana base
    scene bg_gloomy_city

    show jarod base1:
        zoom 1.8
        yalign 1.0

    "Jarod took moments to appreciate the scenery while regaining his composure."
    "Just a normal city block, buildings were about 3 stories high on average, save for a couple architectural wonders in the skyline."
    "These concrete and glass monsters had started popping up a lot recently, usually built by small businesses that landed a good deal or penetrated the market in such a way they could basically get rich overnight and scale their production immediately."
    "This meant very eccentric looking buildings and sometimes skyscrapers amidst regular old establishments."

    # This ends the game.

    return
