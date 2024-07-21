# lenovoremap

Provides Vantage-like F12 customization options for the `F4`-`F12` special keys. Python version of https://github.com/csavalas/HotkeyMapper/. The script must be run with administrator rights.

Included program `ahksend.exe` can be used to execute shortcuts, see https://www.autohotkey.com/docs/v2/lib/Send.htm for key reference.

## Usage
```
lenovoremap.py [-h] [-o] [-c] {F4,F5,F6,F7,F8,F9,F10,F11,F12} [program] [params]

positional arguments:
  {F4,F5,F6,F7,F8,F9,F10,F11,F12}
                        the key to remap (F4-F12).
  program               fully qualified path of the program to run
  params                the parameters for the program (optional)

options:
  -h, --help            show this help message and exit
  -o, --old-keycodes    use old keycodes for older thinkpad models
  -c, --clear           clear the remapping for the key
```

## Examples

Remap the F12 special key to media play/pause:
```
python lenovoremap.py F12 "C:\path\ahksend.exe" "-f {Media_Play_Pause}"
```
Remap F11 to open windows terminal, and shift+F11 to open cmd:
```
python lenovoremap.py F11 "C:\path\ahksend.exe" "C:Shift;R:cmd;R:wt"
```
Remap F10 to type 'hello' in your browser searchbar:
```
python lenovoremap.py F10 "C:\path\ahksend.exe" "!d S:100 T:hello"
```

## Usage (ahksend)

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
