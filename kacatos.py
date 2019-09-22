import os
os.system('color')
msg_color_warning = '\x1b[1;33;0m'
msg_color_ok = '\x1b[1;30;0m'
msg_color_end = '\x1b[0m'

print(msg_color_warning + 'warning' + msg_color_end)
print(msg_color_ok+ 'msg_ok' + msg_color_end)
