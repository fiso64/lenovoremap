import argparse
import os
import subprocess

FKEYS = {
    "F4": ("Ex_1A", "Ex_1A"),
    "F5": ("Ex_10", "Ex_10"),
    "F6": ("Ex_0F", "Ex_0F"),
    "F7": ("7", "7"),
    "F8": ("5", "5"),
    "F9": ("Ex_96", "Ex_1C"),
    "F10": ("Ex_97", "Ex_93"),
    "F11": ("Ex_98", "Ex_94"),
    "F12": ("Ex_90", "Ex_90"),
}

def create_registry_file(key, program, params=None, use_old_keycodes=False, clear=False):
    key_code = FKEYS[key][1] if use_old_keycodes else FKEYS[key][0]
    
    filename = os.path.join(os.path.expanduser('~'), "tmp_pyhotkeymapper.reg")
    
    with open(filename, "w") as outfile:
        outfile.write("Windows Registry Editor Version 5.00\n\n")
        
        if clear:
            outfile.write(f"[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Lenovo\\ShortcutKey\\AppLaunch\\{key_code}]\n")
        else:
            program = program.replace("\\", "\\\\")
            outfile.write(f"[HKEY_LOCAL_MACHINE\\SOFTWARE\\Lenovo\\ShortcutKey\\AppLaunch\\{key_code}]\n")
            outfile.write("\"AppType\"=dword:00000001\n\n")
            outfile.write(f"[HKEY_LOCAL_MACHINE\\SOFTWARE\\Lenovo\\ShortcutKey\\AppLaunch\\{key_code}\\Desktop]\n")
            outfile.write(f"\"File\"=\"{program}\"\n")
            if params: 
                params = params.replace("\\", "\\\\")
                outfile.write(f"\"Parameters\"=\"{params}\"\n")
            else:
                outfile.write(f"\"Parameters\"=-\n")
            outfile.write("\n")
        
        outfile.write("[HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Teams]\n\n")
    
    subprocess.run(["regedit", "/s", filename], check=True)
    os.remove(filename)

def main():
    parser = argparse.ArgumentParser(description="Remap Lenovo ThinkPad special keys.")
    parser.add_argument("key", choices=FKEYS.keys(), help="The key to remap (F4 - F12).")
    parser.add_argument("program", nargs="?", help="The program to launch. Required unless --clear is used.")
    parser.add_argument("params", nargs="?", default="", help="The parameters for the program (optional).")
    parser.add_argument("-o", "--old-keycodes", action="store_true", help="Use old keycodes for older models.")
    parser.add_argument("-c", "--clear", action="store_true", help="Clear the remapping for the key.")
    
    args = parser.parse_args()

    if args.clear:
        create_registry_file(args.key, None, None, args.old_keycodes, clear=True)
    else:
        if args.program is None:
            parser.error("The 'program' argument is required unless --clear is specified.")
        create_registry_file(args.key, args.program, args.params if args.params else None, args.old_keycodes)


if __name__ == "__main__":
    main()
