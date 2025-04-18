storyfunction = 0
Explorer = sprites.create(img("""
        . . . . . . f f f f . . . . . .
        . . . . f f f 2 2 f f f . . . .
        . . . f f f 2 2 2 2 f f f . . .
        . . f f f e e e e e e f f f . .
        . . f f e 2 2 2 2 2 2 e e f . .
        . . f e 2 f f f f f f 2 e f . .
        . . f f f f e e e e f f f f . .
        . f f e f b f 4 4 f b f e f f .
        . f e e 4 1 f d d f 1 4 e e f .
        . . f e e d d d d d d e e f . .
        . . . f e e 4 4 4 4 e e f . . .
        . . e 4 f 2 2 2 2 2 2 f 4 e . .
        . . 4 d f 2 2 2 2 2 2 f d 4 . .
        . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
        . . . . . f f f f f f . . . . .
        . . . . . f f . . f f . . . . .
        """),
    SpriteKind.player)
words = ["", "", "", "", ""]
prompts = ["Enter a place:",
    "Enter a noun:",
    "Enter a verb:",
    "Enter an adjective:",
    "Enter an emotion:"]
while storyfunction <= len(prompts) - 1:
    game.splash(prompts[storyfunction])
    story1 = game.ask_for_string("")
    words[storyfunction] = story1
    storyfunction += 1
story = "Yesterday, I went to the " + words[0] + ". I saw a " + words[1] + " " + words[2] + " a tree. It was a " + words[3] + " day, and I felt " + words[4] + "."
game.splash(story)