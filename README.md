# lenovoremap

Provides Vantage-like F12 customization options for the `F4`-`F12` keys. Python version of https://github.com/csavalas/HotkeyMapper/. The script must be run with administrator rights.

Included program `ahksend.exe` can be used to execute shortcuts, see https://www.autohotkey.com/docs/v2/lib/Send.htm for key reference.

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

Remap F12 to media play/pause:
```
python lenovoremap.py "F12" "C:\path\ahksend.exe" "-f {Media_Play_Pause}"
```
Remap F9 to open windows terminal, and shift+F9 to open cmd:
```
python lenovoremap.py "F9" "C:\path\ahksend.exe" "C:Shift;R:cmd;R:wt"
```
Remap F10 to type 'hello' in your browser searchbar:
```
python lenovoremap.py "F10" "C:\path\ahksend.exe" "!d S:100 T:hello"
```

### Usage (ahksend)

```
Usage: ahksend [-f] <key> <key>...
 
  <key>               <key> is one of the following:
                        An autohotkey key combo (like ^!a for Ctrl+Shift+a)
                        See https://www.autohotkey.com/docs/v2/lib/Send.htm
 
                        S:<ms> sleep for the specified number of milliseconds
 
                        T:<text> types the specified text
 
                        R:<command> runs the specified command
 
                        C:<keyname>;<truekey>;<falsekey> sends truekey if
                        keyname is held, otherwise falsekey.
                        See https://www.autohotkey.com/docs/v2/KeyList.htm
                        for accepted keynames. To check multiple keys join
                        them with +, e.g Control+Shift. 
 
  -f                  Steal focus. Focused application will not receive
                      and intercept keypresses.
```
