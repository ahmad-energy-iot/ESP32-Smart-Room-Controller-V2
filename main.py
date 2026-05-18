from machine import Pin, ADC, PWM, I2C
import ssd1306
import time

# ============================================
# ESP32 Smart Room Controller V2
# OLED + RGB + PIR + LDR + Button
# ============================================

# RGB LED - Common Anode
red = PWM(Pin(14))
green = PWM(Pin(26))
blue = PWM(Pin(13))

red.freq(1000)
green.freq(1000)
blue.freq(1000)

# Sensors
light_sensor = ADC(Pin(34))
light_sensor.atten(ADC.ATTN_11DB)
light_sensor.width(ADC.WIDTH_12BIT)

motion_sensor = Pin(27, Pin.IN)

# Button
button = Pin(25, Pin.IN, Pin.PULL_UP)

# OLED Display
# SCL -> GPIO33
# SDA -> GPIO32
i2c = I2C(0, scl=Pin(33), sda=Pin(32), freq=100000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Variables
mode = 0
last_button_state = 1
motion_timeout = 5
last_motion_time = 0
current_color = (0, 0, 0)

# ============================================
# OLED Display Function
# ============================================

def update_oled(mode_text, motion_text, light_value, light_state, rgb_text):
    oled.fill(0)

    oled.text("Smart Room V2", 0, 0)
    oled.text("Mode: " + mode_text, 0, 12)
    oled.text("Light: " + str(light_value), 0, 24)
    oled.text("State: " + light_state, 0, 36)
    oled.text("Motion: " + motion_text, 0, 48)
    oled.text("RGB: " + rgb_text, 0, 56)

    oled.show()

# ============================================
# RGB Functions
# ============================================

# Common Anode:
# 0 = OFF
# 1023 = FULL Brightness

def set_color(r, g, b):
    red.duty(1023 - r)
    green.duty(1023 - g)
    blue.duty(1023 - b)

def fade_color(start, end, steps=30, delay=0.01):
    for i in range(steps + 1):

        r = int(start[0] + (end[0] - start[0]) * i / steps)
        g = int(start[1] + (end[1] - start[1]) * i / steps)
        b = int(start[2] + (end[2] - start[2]) * i / steps)

        set_color(r, g, b)

        time.sleep(delay)

def go_to_color(target):
    global current_color

    if current_color != target:
        fade_color(current_color, target)
        current_color = target

# ============================================
# Start Message
# ============================================

print("ESP32 Smart Room Controller V2 Running...")

update_oled("START", "-", "-", "-", "BOOT")

# ============================================
# Main Loop
# ============================================

while True:

    button_state = button.value()

    # ========================================
    # Button changes mode
    # ========================================

    if button_state == 0 and last_button_state == 1:

        mode += 1

        if mode > 2:
            mode = 0

        time.sleep(0.3)

    last_button_state = button_state

    # ========================================
    # AUTO MODE
    # ========================================

    if mode == 0:

        mode_text = "AUTO"

        light_value = light_sensor.read()

        motion = motion_sensor.value()

        # Bright Environment
        if light_value < 1800:

            light_state = "BRIGHT"

            motion_text = "YES" if motion == 1 else "NO"

            rgb_status = "OFF"

            go_to_color((0, 0, 0))

        # Dark Environment
        else:

            light_state = "DARK"

            # Motion detected
            if motion == 1:

                last_motion_time = time.time()

                motion_text = "YES"

                rgb_status = "WHITE"

                go_to_color((500, 500, 500))

            # No motion
            else:

                motion_text = "NO"

                elapsed = time.time() - last_motion_time

                # Timeout active
                if elapsed < motion_timeout:

                    rgb_status = "WHITE"

                    go_to_color((500, 500, 500))

                # Timeout finished
                else:

                    rgb_status = "DIM BLUE"

                    go_to_color((0, 0, 120))

        # OLED Update
        update_oled(
            mode_text,
            motion_text,
            light_value,
            light_state,
            rgb_status
        )

        # Serial Monitor
        print("Mode:", mode_text)
        print("Light:", light_value)
        print("State:", light_state)
        print("Motion:", motion_text)
        print("RGB:", rgb_status)

    # ========================================
    # MANUAL ON MODE
    # ========================================

    elif mode == 1:

        mode_text = "MANUAL ON"

        motion_text = "-"

        rgb_status = "GREEN"

        go_to_color((0, 500, 0))

        update_oled(
            mode_text,
            motion_text,
            "-",
            "-",
            rgb_status
        )

        print("MANUAL ON -> Green")

    # ========================================
    # MANUAL OFF MODE
    # ========================================

    elif mode == 2:

        mode_text = "MANUAL OFF"

        motion_text = "-"

        rgb_status = "RED"

        go_to_color((500, 0, 0))

        update_oled(
            mode_text,
            motion_text,
            "-",
            "-",
            rgb_status
        )

        print("MANUAL OFF -> Red")

    print("----------------------")

    time.sleep(0.5)