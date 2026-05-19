# ESP32 Smart Room Controller V2

---

# Deutsche Version

## Projektbeschreibung

Dieses Projekt demonstriert ein intelligentes Smart-Room-Controller-System mit einem ESP32 Mikrocontroller, einem OLED-Display, einem LDR-Lichtsensor, einem PIR-Bewegungssensor, einem RGB-LED und einem Push Button.

Das System erkennt automatisch die Umgebungshelligkeit und Bewegungen. Zusätzlich zeigt das OLED-Display alle wichtigen Systeminformationen in Echtzeit an, darunter Betriebsmodus, Lichtstatus, Bewegungsstatus und RGB-Zustand.

Abhängig von der Umgebung aktiviert das System automatisch unterschiedliche RGB-Farben. Zusätzlich kann der Benutzer über einen Push Button zwischen verschiedenen Betriebsmodi wechseln.

Dieses Projekt demonstriert wichtige Grundlagen aus den Bereichen:

- IoT
- Smart Home
- Embedded Systems
- Sensorintegration
- PWM-Steuerung
- OLED-Systemanzeigen
- Energieeffiziente Beleuchtung
- Smart Energy Systeme

---

## Hauptfunktionen

- Automatische Lichtsteuerung mit LDR-Sensor
- Bewegungserkennung mit PIR-Sensor
- RGB-Farbsteuerung mit PWM
- OLED Echtzeit-Systemanzeige
- Sanfte Farb- und Helligkeitsübergänge
- AUTO MODE
- MANUAL ON MODE
- MANUAL OFF MODE
- Visuelle RGB-Statusanzeige
- Energieeffiziente Beleuchtungslogik
- Smart Ambient Lighting

---

## Verwendete Komponenten

| Komponente | Beschreibung |
|---|---|
| ESP32 DevKit V1 | Hauptcontroller des Systems |
| OLED SSD1306 | Echtzeit-Systemanzeige |
| LDR Sensor | Misst die Umgebungshelligkeit |
| PIR Motion Sensor | Erkennt Bewegungen |
| RGB LED | Mehrfarbige Status- und Beleuchtungsanzeige |
| Push Button | Umschalten zwischen den Betriebsmodi |
| Widerstände | Schutz für die RGB-LED Kanäle |
| Breadboard | Aufbau der Schaltung |
| Jumper Kabel | Elektrische Verbindungen |

---

## Pin-Verbindungen

### RGB LED

| Komponente | ESP32 Pin |
|---|---|
| RGB Rot | GPIO14 |
| RGB Grün | GPIO26 |
| RGB Blau | GPIO13 |
| RGB Common Anode | 3V3 |

### Sensoren

| Komponente | ESP32 Pin |
|---|---|
| LDR Sensor AO | GPIO34 |
| PIR Sensor OUT | GPIO27 |
| Push Button | GPIO25 |
| Button GND | GND |

### OLED Display

| OLED Pin | ESP32 Pin |
|---|---|
| SCL | GPIO33 |
| SDA | GPIO32 |
| VCC | 3V3 |
| GND | GND |

---

## RGB LED Typ

In diesem Projekt wird ein RGB LED mit Common Anode verwendet.

Das bedeutet:

- Das lange Bein des RGB LEDs wird mit 3V3 verbunden.
- Die drei anderen Beine werden über Widerstände mit GPIO Pins verbunden.
- Die Logik ist invertiert:
  - GPIO LOW bedeutet LED-Kanal EIN.
  - GPIO HIGH bedeutet LED-Kanal AUS.

Im Code wird diese invertierte Logik automatisch über die Funktion `set_color()` korrigiert.

---

## OLED Echtzeit-Anzeige

Das OLED-Display zeigt folgende Informationen in Echtzeit an:

- Aktueller Betriebsmodus
- Lichtsensorwert
- Helligkeitsstatus
- Bewegungserkennung
- RGB-Status

Beispiel:

```text
Smart Room V2
Mode: AUTO
Light: 2960
State: DARK
Motion: YES
RGB: WHITE
```

---

## Farblogik des Systems

| Situation | Farbe | Bedeutung |
|---|---|---|
| Helle Umgebung | AUS | Es ist genug Licht vorhanden |
| Dunkelheit ohne Bewegung | Blau | Nacht-Standby-Modus |
| Dunkelheit mit Bewegung | Weiß | Bewegung erkannt |
| Manual ON | Grün | Beleuchtung manuell eingeschaltet |
| Manual OFF | Rot | System manuell ausgeschaltet |

---

## Betriebsmodi

| Modus | Beschreibung |
|---|---|
| AUTO MODE | Sensoren steuern das Licht automatisch |
| MANUAL ON | RGB LED bleibt manuell eingeschaltet |
| MANUAL OFF | RGB LED zeigt roten Statusmodus |

Der Push Button wechselt bei jedem Tastendruck zwischen den Modi:

```text
AUTO MODE → MANUAL ON → MANUAL OFF → AUTO MODE
```

---

## Systemlogik

1. Der LDR-Sensor misst die Umgebungshelligkeit.
2. Wenn genug Licht vorhanden ist, bleibt das RGB LED ausgeschaltet.
3. Wenn es dunkel ist, prüft der ESP32 den PIR-Bewegungssensor.
4. Wenn keine Bewegung erkannt wird, leuchtet das RGB LED schwach blau.
5. Wenn Bewegung erkannt wird, leuchtet das RGB LED weiß.
6. Das OLED-Display zeigt alle Systemdaten live an.
7. Mit dem Button kann der Benutzer manuell zwischen AUTO, ON und OFF wechseln.
8. Die Farbänderungen erfolgen mit sanften Übergängen.

---

## Nutzen des Projekts

Dieses Projekt kann in vielen praktischen Bereichen verwendet werden:

- Smart-Home-Beleuchtungssysteme
- Energieeffiziente Raumsteuerung
- Automatische Nachtbeleuchtung
- IoT-basierte Gebäudeautomatisierung
- Intelligente Smart-Building-Systeme
- Embedded- und IoT-Lernplattformen
- Prototypen für Smart-Energy-Systeme
- Sicherheitsbeleuchtung
- Bewegungsgesteuerte Beleuchtung
- Renewable-Energy Anwendungen
- Smart-City Beleuchtung

Das Projekt zeigt, wie intelligente Systeme Energie sparen können, indem Licht nur dann aktiviert wird, wenn es wirklich benötigt wird.

---

## Verwendete Technologien

- ESP32
- MicroPython
- Embedded Systems
- IoT
- OLED SSD1306
- PWM RGB Control
- PIR Motion Detection
- Smart Lighting
- Sensor Integration
- Smart Energy Systems

---

#  English Version

## Project Description

This project demonstrates an intelligent Smart Room Controller system using an ESP32 microcontroller, an OLED display, an LDR light sensor, a PIR motion sensor, an RGB LED and a push button.

The system automatically detects ambient light conditions and motion. Additionally, the OLED display provides real-time visualization of all important system information, including operating mode, light status, motion status and RGB state.

Depending on environmental conditions, the system automatically activates different RGB colors. The user can also switch between different operating modes using the push button.

This project demonstrates important concepts related to:

- IoT
- Smart Home
- Embedded Systems
- Sensor Integration
- PWM Control
- OLED System Displays
- Energy-Efficient Lighting
- Smart Energy Systems

---

## Main Features

- Automatic lighting control using an LDR sensor
- Motion detection using a PIR sensor
- RGB color control using PWM
- Real-time OLED system display
- Smooth color and brightness transitions
- AUTO MODE
- MANUAL ON MODE
- MANUAL OFF MODE
- Visual RGB status indication
- Energy-efficient lighting logic
- Smart ambient lighting

---

## Components Used

| Component | Description |
|---|---|
| ESP32 DevKit V1 | Main controller of the system |
| OLED SSD1306 | Real-time system display |
| LDR Sensor | Measures ambient light intensity |
| PIR Motion Sensor | Detects movement |
| RGB LED | Multicolor lighting and status indicator |
| Push Button | Switches between operating modes |
| Resistors | Protect RGB LED channels |
| Breadboard | Circuit assembly |
| Jumper Wires | Electrical connections |

---

## Pin Connections

### RGB LED

| Component | ESP32 Pin |
|---|---|
| RGB Red | GPIO14 |
| RGB Green | GPIO26 |
| RGB Blue | GPIO13 |
| RGB Common Anode | 3V3 |

### Sensors

| Component | ESP32 Pin |
|---|---|
| LDR Sensor AO | GPIO34 |
| PIR Sensor OUT | GPIO27 |
| Push Button | GPIO25 |
| Button GND | GND |

### OLED Display

| OLED Pin | ESP32 Pin |
|---|---|
| SCL | GPIO33 |
| SDA | GPIO32 |
| VCC | 3V3 |
| GND | GND |

---

## RGB LED Type

This project uses a Common Anode RGB LED.

This means:

- The long leg of the RGB LED is connected to 3V3.
- The other three legs are connected to GPIO pins through resistors.
- The logic is inverted:
  - GPIO LOW means LED channel ON.
  - GPIO HIGH means LED channel OFF.

The function `set_color()` automatically handles this inverted logic.

---

## OLED Real-Time Display

The OLED display provides real-time information including:

- Current operating mode
- Light sensor value
- Brightness status
- Motion detection status
- RGB status

Example:

```text
Smart Room V2
Mode: AUTO
Light: 2960
State: DARK
Motion: YES
RGB: WHITE
```

---

## System Color Logic

| Situation | Color | Meaning |
|---|---|---|
| Bright environment | OFF | Enough light is available |
| Dark without motion | Blue | Night standby mode |
| Dark with motion | White | Motion detected |
| Manual ON | Green | Lighting manually enabled |
| Manual OFF | Red | System manually disabled |

---

## Operating Modes

| Mode | Description |
|---|---|
| AUTO MODE | Sensors control the lighting automatically |
| MANUAL ON | RGB LED remains manually enabled |
| MANUAL OFF | RGB LED shows red status mode |

Each button press changes the mode:

```text
AUTO MODE → MANUAL ON → MANUAL OFF → AUTO MODE
```

---

## System Logic

1. The LDR sensor measures ambient brightness.
2. If enough light is available, the RGB LED remains OFF.
3. If the environment becomes dark, the ESP32 checks the PIR motion sensor.
4. If no motion is detected, the RGB LED glows dim blue.
5. If motion is detected, the RGB LED turns white.
6. The OLED display shows all system data in real time.
7. The user can manually switch between AUTO, ON and OFF modes using the push button.
8. Smooth RGB transitions are performed using fade effects.

---

## Project Benefits

This project can be used in many practical real-world applications:

- Smart home lighting systems
- Energy-efficient room control
- Automatic night lighting
- IoT-based building automation
- Intelligent smart building systems
- Embedded and IoT learning platforms
- Smart energy system prototypes
- Security lighting
- Motion-controlled lighting
- Renewable energy applications
- Smart City lighting

The project demonstrates how intelligent systems can save energy by activating lighting only when it is actually needed.

---

## Technologies Used

- ESP32
- MicroPython
- Embedded Systems
- IoT
- OLED SSD1306
- PWM RGB Control
- PIR Motion Detection
- Smart Lighting
- Sensor Integration
- Smart Energy Systems

---

## Complete MicroPython Code

```python
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

# OLED Display Function
def update_oled(mode_text, motion_text, light_value, light_state, rgb_text):
    oled.fill(0)

    oled.text("Smart Room V2", 0, 0)
    oled.text("Mode: " + mode_text, 0, 12)
    oled.text("Light: " + str(light_value), 0, 24)
    oled.text("State: " + light_state, 0, 36)
    oled.text("Motion: " + motion_text, 0, 48)
    oled.text("RGB: " + rgb_text, 0, 56)

    oled.show()

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

print("ESP32 Smart Room Controller V2 Running...")

update_oled("START", "-", "-", "-", "BOOT")

while True:

    button_state = button.value()

    # Button changes mode
    if button_state == 0 and last_button_state == 1:

        mode += 1

        if mode > 2:
            mode = 0

        time.sleep(0.3)

    last_button_state = button_state

    # AUTO MODE
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

        print("Mode:", mode_text)
        print("Light:", light_value)
        print("State:", light_state)
        print("Motion:", motion_text)
        print("RGB:", rgb_status)

    # MANUAL ON MODE
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

    # MANUAL OFF MODE
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
```

## Required Libraries

This project uses the `ssd1306.py` OLED display driver library for controlling the SSD1306 OLED screen with MicroPython on ESP32.

Make sure the file `ssd1306.py` is uploaded to the ESP32 board before running the project.

## Developer

**Ahmad Azroun**  
Renewable Energy Manager | IoT & Smart Energy Systems Developer
