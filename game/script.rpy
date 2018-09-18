# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# This is the countdown timer. Currently hardcoded to have a length of 7.0 seconds.
image countdown = DynamicDisplayable (countdown, length = 7.0)

# Initialize small versions of the in-game portraits. These will be the standard dialogue.
image hinako happy small = ProportionalScale("hinako happy.png", 700, 1000)
image hinako upset small = ProportionalScale("hinako upset.png", 700,1000)
image hinako surprised small = ProportionalScale("hinako surprised.png", 700,1000)
image hinako sad small = ProportionalScale("hinako sad.png", 700, 1000)
image hinako blush small = ProportionalScale("hinako blush.png", 700, 1000)

# This is the current start screen. You can change it by editing screens.rpy:358
image wallpaper:
    "bg dorm night.png" with Dissolve (5.0)
    pause 10.0
    "bg dorm glow.png" with Dissolve (5.0)
    pause 8.0
    repeat

# Define our characters. Currently just Hinako.
define h = Character("Hinako", who_color="#ffffff",who_outlines=[( 1, "#b1d9ef", 1, 1 )])

#Define some other variables. Note that screen variables are defined in screens.rpy:124
define num_wrong_clicks = 0

# The game starts here.

label start:

    scene bg black

    "The silent wind gently blows throughout the town, whispering in each and every alley it trespasses through."
    "In one particular residence, a lone high school girl is hard at work on her school duties, toiling away the hours of the night, and her youth."
    "After working long past the hours of daylight, she finally puts her pencil down and relaxes."

    #Play some music and a fade-in for the first background.
    play music "black starlight.ogg"

    scene bg dorm glow with Dissolve (1.8)

    # This shows a character sprite. We align it to (0.1, 0.0) on the coordinate system.
    show hinako happy small with Dissolve(1.0):
        xalign 0.1 yalign 0.0


    # These display lines of dialogue.

    h "...And that's that. All in a day's work."

    show hinako upset:

    h "Wasn't very fun, though."

    show hinako sad small with Dissolve(0.5):


    h "..."
    h "Well... while I'm not really used to it, I suppose I can't say I truly hate it."

    show hinako happy small:

    h "I guess some part of me likes tinkering around with something unfamiliar. In the end, it wasn't all bad."

    show hinako happy:

    h "Alright, looks like I'll have to give it a hundred and ten percent!"

    show hinako sad small with Dissolve (0.3)

    h "...Yikes, I didn't realize how late it's gotten. Time really flies when you're hard at work."

    show hinako happy small with Dissolve (0.2)

    h "I should probably hit the hay soon."



#    show hinako happy small with Dissolve (0.2)
    window hide
    pause (0.3)

    stop music fadeout 0.1
    pause 0.1
    play sound "knock.ogg"
    pause (1.5)
    window show

    h "..."

    # Here's the code to make Hinako "jump". Recall we initially set xalign to 0.1 and yalign to 0.0. This movement happens in 0.1 seconds.
    show hinako surprised small:
        linear 0.05 xalign 0.1 yalign 0.1
        linear 0.05 xalign 0.1 yalign 0.0

    play sound "sfx-lightbulb.wav"
    h "...!!"

    show hinako upset small

    h "...Was that the door? Who could it be at this hour, though?"

    play music "decision.ogg" fadein 2.6
    label decision:
    h "..."

    h "...What should I do...?"

    # We show the countdown timer for choices at the bottom left.
    show countdown at Position(xalign=0.9, yalign = 0.9)
    $ ui.timer(7.0, ui.jumps("slow"))

    # Dialogue choice. The choices don't matter, since all jump to doorchoiceend.
    menu:
        "Go check it out":
            jump yes
        "Ignore it":
            jump no

    label slow:
        hide countdown
        h "That was too slow! I need to think faster!"
        jump decision
    label yes:
        hide countdown

        h "Alright, let's see who it is."
        scene bg black with Dissolve (2.0)
        pause 1.0
        scene bg dorm glow
        show hinako happy small:
            xalign 0.1 yalign 0.0
        stop music fadeout 0.1
        h "Just kidding!"
        jump doorchoiceend
    label no:
        hide countdown
        h "I shouldn't open the door. There's no telling what could be out there."
        show hinako happy
        h "Good on you, player!"
        show hinako blush happy with Dissolve (0.3)
        h "It's nice to know you care for my safety."
        show hinako happy small with Dissolve (0.5)
        stop music fadeout 0.1

    # After the choice.
    label doorchoiceend:
    play music "black starlight.ogg" fadein 1.0

    show hinako happy small
    h "This is the end of the choices."
    h "Not like the choices actually mattered or anything, since I'd be stupid to open the door regardless."
    show hinako sad small
    h "..."
    show hinako happy small
    h "Alright, let's continue with this showcase."
    show hinako sad small
    h "Hm, let's see here..."

    window hide
    show hinako happy small:
        linear 1.0 xalign 0.01
    pause 1.0
    $ show_pointclick1 = True

    window show

    #Bootleg method of forcing the player to click on the lamp.
    label before_lamp:


    h "Go ahead and try clicking on that lamp."
#    jump before_lamp

    if not clicked_on_lamp:
        if num_wrong_clicks < 4:
            h "That's not the lamp. Try again please!"
            $ num_wrong_clicks = num_wrong_clicks + 1
            jump before_lamp
        else:
            $ show_pointclick1 = False
            show hinako upset with Dissolve (0.3)
            h "..."
            h "...Not cool, dude. Not cool at all."
            show hinako happy small with Dissolve (0.3)
            jump failed_to_click
#    else:
#        $ clicked_on_lamp = True
    label lamp_pressed:
    $ show_pointclick1 = False
    show hinako happy small
    h "You did it! Grats!"
    h "The implementation wasn't very pretty, but the important thing is that it works!"

    show hinako happy small:
        linear 1.0 xalign 0.1

    label failed_to_click:
    h "Next up, we can try out timed point-and-clicks."

    window hide
    show hinako happy small:
        linear 1.0 xalign 0.01
    pause 1.0
    window show

    # This ends the game.

    return
