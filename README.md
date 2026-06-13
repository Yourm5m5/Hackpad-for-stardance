# Hackpad — 3-Key Media Macropad

Hackpad is an ultra-compact, custom-built 3-key mechanical macropad powered by the **Seeed Studio XIAO RP2040** and running **KMK Firmware**. It features custom Tap Dance functionality, allowing you to seamlessly control volume, track navigation, and media playback with only three physical switches.

---

## Features

* **Compact Form Factor:** Designed around the tiny Seeed XIAO RP2040 footprint.
* **Tap Dance Controls:** Get 6 different media functions out of just 3 physical keys.
* **Premium Build Hardware:** Uses durable M3 heatset inserts for a robust, reusable 3D-printed case assembly.
* **Custom PCB Design:** Clean, reliable hardware routing (no messy hand-wiring birds-nests!).

---

## Design & Gallery

### Render of Macropad
![Render of Macropad](https://github.com/user-attachments/assets/31a828e8-2b13-4715-b19d-785a1a69d9b7)

### 3D Model of Case
![3D model of Case](https://github.com/user-attachments/assets/404f1bad-b3b0-47c0-9345-67d14bc2bc9d)

### PCB Layout
![PCB layout](https://github.com/user-attachments/assets/df20df70-f5af-4cbe-b86b-80ac6ba3b6a2)

### Schematic Diagram
![Schematic](https://github.com/user-attachments/assets/4b82a4d8-8efa-4747-b0eb-5d2521c19c76)

---

## Bill of Materials (BOM)

| Component | Description | Estimated Price (AUD) | Link |
| :--- | :--- | :---: | :--- |
| **Microcontroller** | Seeed XIAO RP2040 Development Board | ~$16.00 | [Aliexpress](https://www.aliexpress.com/item/1005007427287029.html) |
| **Switches** | MX-style mechanical switches (Linear/Tactile) | ~$11.00 | [Aliexpress](https://www.aliexpress.com/item/1005008904106530.html) |
| **Keycaps** | Blank DSA Profile PBT Keycaps | ~$5.00 | [Aliexpress](https://www.aliexpress.com/item/1005002976015114.html) |
| **Screws** | M3 × 16mm socket head screws | ~$9.00 | [Aliexpress](https://www.aliexpress.com/item/1005005041733771.html) |
| **Threaded Inserts**| M3 × 5mm (OD) × 4mm (L) brass heatset inserts | ~$5.00 | [Aliexpress](https://www.aliexpress.com/item/1005004701945081.html) |

---

## Default Keymap Layout (Tap Dance)

Thanks to KMK's `TapDance` module, every switch has two distinct functions based on how many times you press it:

| Switch | Single Tap Action | Double Tap Action |
| :---: | :--- | :--- |
| **Key 1** | 🔇 Mute / Unmute | Play / Pause Video |
| **Key 2** | 🔊 Volume UP | kip Forward (Next Track) |
| **Key 3** | 🔉 Volume DOWN |  Skip Backward (Previous Track) |

---

## Software & Firmware Setup

The Hackpad runs on **CircuitPython** paired with the **KMK Keyboard Firmware framework**. 

### 1. Flash CircuitPython
1. Download the latest `.uf2` stable firmware for the **Seeed XIAO RP2040** from [circuitpython.org](https://circuitpython.org/downloads).
2. Connect your XIAO to your computer while holding down the **BOOT** button.
3. A new flash drive named `RPI-RP2` will appear. Drag and drop the downloaded `.uf2` file onto it.
4. The board will reboot automatically as a USB drive named **`CIRCUITPY`**.

### 2. Install KMK Library
1. Download the KMK Firmware source code from the official [KMK GitHub Repository](https://github.com/KMKfw/kmk_firmware).
2. Copy the folder named `kmk` from the ZIP directly onto your `CIRCUITPY` drive root.

### 3. Add the Configuration Script
Save the following production code to your `CIRCUITPY` drive as **`code.py`**:

```python
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()

# Enable media controls and Tap Dance features
keyboard.extensions.append(MediaKeys())
tapdance = TapDance()
tapdance.tap_time = 250  # Double-tap window in milliseconds
keyboard.modules.append(tapdance)

# Matrix hardware layout pins for Hackpad
keyboard.col_pins = (board.D9,)
keyboard.row_pins = (board.D10, board.D11)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Configure Tap Dance Macros (Single Tap, Double Tap)
MUTE_PAUSE = KC.TD(KC.AUDIO_MUTE, KC.MEDIA_PLAY_PAUSE)
VOL_UP_FORWARD = KC.TD(KC.AUDIO_VOL_UP, KC.MEDIA_NEXT_TRACK)
VOL_DOWN_BACK = KC.TD(KC.AUDIO_VOL_DOWN, KC.MEDIA_PREV_TRACK)

# Apply configuration to keys mapping
keyboard.keymap = [
    [
        MUTE_PAUSE,       # Key 1
        VOL_UP_FORWARD,   # Key 2
        VOL_DOWN_BACK     # Key 3
    ]
]

if __name__ == "__main__":
    keyboard.go()
```

## Credits
I use AI to help me structure my repo






