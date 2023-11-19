def on_received_number(receivedNumber):
    if receivedNumber != 0:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # #
            # # . . .
            """)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.set_group(1)
    radio.send_number(1)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(0)
    basic.show_leds("""
        . . . . .
        . . . . .
        . # # # .
        . . . . .
        . . . . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)
