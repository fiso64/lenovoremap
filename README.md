# lenovoremap

Provides Vantage-like F12 customization options for the `F4`-`F12` keys. Python version of https://github.com/csavalas/HotkeyMapper/. The script must be run with administrator rights.

Included program `ahksend.exe` can be used to execute shortcuts, see https://www.autohotkey.com/docs/v2/KeyList.htm and https://www.autohotkey.com/docs/v1/Hotkeys.htm for key reference.

### Usage
```
usage: lenovoremap.py [-h] [-o] [-c] {F4,F5,F6,F7,F8,F9,F10,F11,F12} [program] [params]

Remap Lenovo ThinkPad special keys.

positional arguments:
  {F4,F5,F6,F7,F8,F9,F10,F11,F12}
                        The key to remap (F4 - F12).
  program               The program to launch. Required unless --clear is used.
  params                The parameters for the program (optional).

options:
  -h, --help            show this help message and exit
  -o, --old-keycodes    Use old keycodes for older models.
  -c, --clear           Clear the remapping for the key.
```

### Examples

Remap F12 to media play/pause
```
python lenovoremap.py "F12" "C:\path\ahksend.exe" "-f {Media_Play_Pause}"
```
Remap F10 to type 'hello' in your browser searchbar
```
python lenovoremap.py "F10" "C:\path\ahksend.exe" "!d S:100 T:hello"
```
Remap F9 to type 'a' and shift+F9 to type 'b'
```
python lenovoremap.py "F9" "C:\path\ahksend.exe" "C:Shift,b,a"
```

### Usage (ahksend)

```
Usage: ahksend [-f] <key> <key>...

 <key>               An autohotkey key combo (like ^!a for Ctrl-Shift-a)
                     S:<ms> sleep for the specified number of milliseconds
                     T:<string> send input as raw text
                     C:<key>,<true-key>,<false-key> conditional execution
                     sends true-key if key is held, otherwise false-key

 -f                  Steal focus. Focused application will not receive
                     and intercept keypresses.
```
