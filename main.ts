radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        basic.showLeds(`
            . . . . .
            . . # . .
            . . # . .
            . . # . .
            . . . . .
            `)
    } else {
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            . . . . .
            . . . . .
            `)
    }
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(1)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(0)
    basic.showLeds(`
        . . . . .
        . . . . .
        . # # # .
        . . . . .
        . . . . .
        `)
})
radio.onReceivedValue(function (name, value) {
	
})
