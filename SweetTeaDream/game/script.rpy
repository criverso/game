# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Train Stwertess")
define p = Character("Wasu Jikan")
define n = Character("Narrator")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene dorm1


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.
    show normalgirl1
    e "Sir..."
    e "sir wake up we've arrived!"

    p "huh.. sorry I must have dosed off"
    p "Wow... the big city looks amazing"
    n ""
    e "You were having lewd dreams again!!"
    p "no I swear I wasn't"

    show doubtgirl1
    e "ahuh sure whatever hurry up were gonna be late"

    # This ends the game.

    return
