import re

pattern = re.compile(r"\[(on|off)\]")
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))
print(re.search(pattern, "Nothing...:-("))