let acc = 0
radio.setGroup(1)
basic.showString("Hello!")
music.playMelody("C5 E6 G6", 200)
basic.forever(function on_forever() {
    
    acc = input.acceleration(Dimension.Z)
    acc = Math.round(Math.map(acc, 0, 1023, 0, 98)) / 10
    radio.sendNumber(acc)
})
