

if (A_Args.Length == 0) {
	help := "Usage: ahksend [-f] <key> <key>..."
	help .= "`n"
	help .= "`n  <key>               <key> is one of the following:"
	help .= "`n                        An autohotkey key combo (like ^!a for Ctrl+Shift+a)"
	help .= "`n                        See https://www.autohotkey.com/docs/v2/lib/Send.htm"
	help .= "`n"
	help .= "`n                        S:<ms> sleep for the specified number of milliseconds"
	help .= "`n"
	help .= "`n                        T:<text> types the specified text"
	help .= "`n"
	help .= "`n                        R:<command> runs the specified command"
	help .= "`n"
	help .= "`n                        C:<keyname>;<truekey>;<falsekey> sends truekey if"
	help .= "`n                        keyname is held, otherwise falsekey."
	help .= "`n                        See https://www.autohotkey.com/docs/v2/KeyList.htm"
	help .= "`n                        for accepted keynames. To check multiple keys join"
	help .= "`n                        them with +, e.g Control+Shift. "
	help .= "`n"
	help .= "`n  -f                  Steal focus. Focused application will not receive"
	help .= "`n                      and intercept keypresses."
	help .= "`n"
	MsgBox(help)
	return
}
	
steal_focus := 0
	
if (A_Args[1] == "-f") {
	steal_focus := 1
	focusgui := Gui()
	focusgui.Show("x10000 y10000")
}

processArg(arg) {
	o := SubStr(arg, 1, 2)
	
	if (o == "S:") {
		Sleep(SubStr(arg, 3))
	} 
	else if (o == "T:") {
		SendText(SubStr(arg, 3))
	} 
	else if (o == "R:") {
		Run(SubStr(arg, 3))
	}
	else if (o == "C:") {
		arr := StrSplit(SubStr(arg, 3),";", , 3)
		keys := StrSplit(arr[1],"+")
		state := true
		for k in keys {
			state &= GetKeyState(k)
		}
		if (state && Trim(arr[2]) != "") {
			processArg(arr[2])
		}
		else if (!state && arr.Length == 3 && Trim(arr[3]) != "") {
			processArg(arr[3])
		}
	} 
	else {
		SendInput(arg)
	}
}

i := 1 + steal_focus

while i < A_Args.Length + 1 {
	processArg(A_Args[i])
	i += 1
}

if (steal_focus == 1) {
	focusgui.Destroy()	
}
