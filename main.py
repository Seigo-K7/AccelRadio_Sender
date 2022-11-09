acc = 0
radio.set_group(1)
basic.show_string("Hello!")
music.play_melody("C5 E6 G6", 200)

def on_forever():
    global acc
    acc = input.acceleration(Dimension.Z)
    acc = Math.round(Math.map(acc, 0, 1023, 0, 98)) / 10
    radio.send_number(acc)
basic.forever(on_forever)
