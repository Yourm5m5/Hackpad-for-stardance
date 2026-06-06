import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrienation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.tapdance import Tapdance

keyboard = KMKkeyboard()

keyboard.extensions.append(MediaKeys())
tapdance = TapDance()
keyboard.modules.append(tapdance)

keyboard.col_pins = (board.D9)
keyboard.row_pin = (board.D10, board.D11) 
keyboard.diode_orentation = DiodeOrienation.COL2ROW

mute/pause = KC.TD(KC.AUDIO_MUTE. KC.MEDIA_PLAY_PAUSE)
vol_up/foreword = KC.TD(KC.AUDIO_VOL_UP. KC.MEDIA_PLAY_NEXT_TRACK)
vol_down/download = KC.TD(KC.AUDIO_VOL_DOWN. KC.MEDIA_PLAY_PREV_TRACK)

keyboard.keymap = [[
    mute/pause,
    vol_up/foreword,
    vol_down/download
]]

if __name__ == "__main__":
    keyboard.go()