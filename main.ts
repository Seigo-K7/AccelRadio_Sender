radio.setGroup(1)
basic.showIcon(IconNames.Yes)
music.playMelody("C6 E6 G6", 200)
basic.forever(function on_forever() {
    // global acc
    // acc = input.acceleration(Dimension.Z)
    // acc =  / 10
    // Math.sqrt(input.acceleration(Dimension.Z)*input.acceleration(Dimension.Z)+input.acceleration(Dimension.Z)*input.acceleration(Dimension.Z))
    radio.sendNumber(Math.round(Math.map(Math.sqrt(input.acceleration(Dimension.Z) * input.acceleration(Dimension.Z) + input.acceleration(Dimension.Z) * input.acceleration(Dimension.Z)), -1023, 1023, -980, 980)))
})
