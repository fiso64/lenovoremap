
steal_focus := 0

if (A_Args.Length == 0) {
	help := "Usage: ahksend [-f] <key> <key>..."
	help .= "`n"
	help .= "`n  <key>               An autohotkey key combo (like ^!a for Ctrl-Shift-a)"
	help .= "`n                      S:<ms> sleep for the specified number of milliseconds"
	help .= "`n                      T:<string> send input as raw text"
	help .= "`n                      C:<key>,<true-key>,<false-key> conditional execution"
	help .= "`n                      sends true-key if key is held, otherwise false-key"
	help .= "`n"
	help .= "`n  -f                  Steal focus. Focused application will not receive"
	help .= "`n                      and intercept keypresses."
	help .= "`n"
	MsgBox(help)
	return
}
	
if (A_Args[1] == "-f") {
	steal_focus := 1
	focusgui := Gui()
	focusgui.Show("x10000 y10000")
}

i := 1 + steal_focus
while i < A_Args.Length + 1 {
	a := A_Args[i]
	if (SubStr(a, 1, 2) == "S:") {
		Sleep(SubStr(a, 3))
	} 
	else if (SubStr(a, 1, 2) == "T:") {
		Send(SubStr(a, 3))
	} 
	else if (SubStr(a, 1, 2) == "C:") {
		arr := StrSplit(SubStr(a, 3),",", , 3)
		state := GetKeyState(arr[1])
		if (state && Trim(arr[2]) != "") {
			SendInput(arr[2])
		}
		else if (!state && arr.Length == 3 && Trim(arr[3]) != "") {
			SendInput(arr[3])
		}
	} 
	else {
		SendInput(a)
	}
	i += 1
}

if (steal_focus == 1) {
	focusgui.Destroy()	
}

