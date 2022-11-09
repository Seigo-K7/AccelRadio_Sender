radio.set_group(1)
basic.show_icon(IconNames.YES)
music.play_melody("C6 E6 G6", 200)

def on_forever():
    #global acc
    #acc = input.acceleration(Dimension.Z)
    #acc =  / 10
    #Math.sqrt(input.acceleration(Dimension.Z)*input.acceleration(Dimension.Z)+input.acceleration(Dimension.Z)*input.acceleration(Dimension.Z))
    radio.send_number(Math.round(Math.map(Math.sqrt(input.acceleration(Dimension.Z)*input.acceleration(Dimension.Z)+input.acceleration(Dimension.Z)*input.acceleration(Dimension.Z)), -1023, 1023, -980, 980)))
basic.forever(on_forever)
