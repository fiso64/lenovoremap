import argparse
import os
import subprocess
import shutil

FKEYS = {
    "F4":  ("Ex_1A", "Ex_1A"),
    "F5":  ("Ex_10", "Ex_10"),
    "F6":  ("Ex_0F", "Ex_0F"),
    "F7":  ("7", "7"),
    "F8":  ("5", "5"),
    "F9":  ("Ex_96", "Ex_1C"),
    "F10": ("Ex_97", "Ex_93"),
    "F11": ("Ex_98", "Ex_94"),
    "F12": ("Ex_90", "Ex_90"),
}

def create_registry_file(key, program, params, use_old_keycodes, clear):
    key_code = FKEYS[key][1] if use_old_keycodes else FKEYS[key][0] 
    reg_fname = os.path.join(os.path.expanduser('~'), "tmp_pyhotkeymapper.reg")
    
    with open(reg_fname, "w", encoding="utf-8") as outfile:
        outfile.write("Windows Registry Editor Version 5.00\n\n")
        
        if clear:
            outfile.write(f"[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Lenovo\\ShortcutKey\\AppLaunch\\{key_code}]\n")
        else:
            program = program.replace("\\", "\\\\").replace('/', '\\\\')
            outfile.write(f"[HKEY_LOCAL_MACHINE\\SOFTWARE\\Lenovo\\ShortcutKey\\AppLaunch\\{key_code}]\n")
            outfile.write(f"\"AppType\"=dword:00000001\n\n")
            outfile.write(f"[HKEY_LOCAL_MACHINE\\SOFTWARE\\Lenovo\\ShortcutKey\\AppLaunch\\{key_code}\\Desktop]\n")
            outfile.write(f"\"File\"=\"{program}\"\n")
            outfile.write(f"\"Parameters\"=\"{params if params else ''}\"\n")
            outfile.write(f"\n")
        
        outfile.write("[HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Teams]\n\n")
    
    subprocess.run(["regedit", "/s", reg_fname], check=True)
    os.remove(reg_fname)

def main():
    parser = argparse.ArgumentParser(description="Remap Lenovo ThinkPad special keys.")
    parser.add_argument("key", choices=FKEYS.keys(), help="The key to remap (F4 - F12).")
    parser.add_argument("program", nargs="?", help="The program to launch. Required unless --clear is used.")
    parser.add_argument("params", nargs="?", default="", help="The parameters for the program (optional).")
    parser.add_argument("-o", "--old-keycodes", action="store_true", help="Use old keycodes for older models.")
    parser.add_argument("-c", "--clear", action="store_true", help="Clear the remapping for the key.")
    
    args = parser.parse_args()

    if args.clear != True and not args.program:
        parser.error("The 'program' argument is required unless --clear is specified.")

    if args.program and not os.path.exists(args.program):
        found_program = shutil.which(args.program)
        if found_program:
            args.program = found_program

    create_registry_file(args.key, args.program, args.params, args.old_keycodes, args.clear)


if __name__ == "__main__":
    main()
