emogis = {
    "grinning face": "\U0001F600",
    "grinning face with big eyes": "\U0001F603",
    "grinning face with smiling eyes": "\U0001F604",
    "beaming face with smiling eyes": "\U0001F601",
    "grinning squinting face": "\U0001F606",
    "grinning face with sweat": "\U0001F605",
    "rolling on the floor laughing": "\U0001F923",
    "face with tears of joy": "\U0001F602",
    "slightly smiling face": "\U0001F642",
    "upside-down face": "\U0001F643",
    "winking face": "\U0001F609",
    "smiling face with smiling eyes": "\U0001F60A",
    "smiling face with halo": "\U0001F607",
    "smiling face with 3 hearts": "\U0001F970",
    "smiling face with heart-eyes": "\U0001F60D",
    "star-struck": "\U0001F929",
    "face blowing a kiss": "\U0001F618",
    "kissing face": "\U0001F617",
    "kissing face with closed eyes": "\U0001F61A",
    "kissing face with smiling eyes": "\U0001F619",
    "face savoring food": "\U0001F60B",
    "face with tongue": "\U0001F61B",
    "winking face with tongue": "\U0001F61C",
    "zany face": "\U0001F92A",
    "squinting face with tongue": "\U0001F61D",
    "money-mouth face": "\U0001F911",
    "hugging face": "\U0001F917",
    "face with hand over mouth": "\U0001F92D",
    "shushing face": "\U0001F92B",
    "thinking face": "\U0001F914",
    "zipper-mouth face": "\U0001F910",
    "face with raised eyebrow": "\U0001F928",
    "neutral face": "\U0001F610",
    "expressionless face": "\U0001F611",
    "face without mouth": "\U0001F636",
    "smirking face": "\U0001F60F",
    "unamused face": "\U0001F612",
    "face with rolling eyes": "\U0001F644",
    "grimacing face": "\U0001F62C",
    "lying face": "\U0001F925",
    "relieved face": "\U0001F60C",
    "pensive face": "\U0001F614",
    "sleepy face": "\U0001F62A",
    "drooling face": "\U0001F924",
    "sleeping face": "\U0001F634",
    "face with medical mask": "\U0001F637",
    "face with thermometer": "\U0001F912",
    "face with head-bandage": "\U0001F915",
    "nauseated face": "\U0001F922",
}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[39m'

message = "amit: how are you $happy$ $happy$ $happy$ $happy$ $happy$, I find that $sleeping face$ $thinking face$ and $thinking face$ $sleeping face$."

for emogi in emogis:
    # print(emogi)
    if(message.find(emogi)!=-1):
        # print("entered")
        message = message.replace(emogi, emogis[emogi], message.count(emogi))

print(message)
print(" ","\t",end='')
for i in range(44):
    print(bcolors.OKGREEN+"-", end='')
print("")
for emogi in emogis:
    print("\t", bcolors.OKGREEN+"|", bcolors.WHITE+' {:<33}'.format(emogi),": ", emogis[emogi], bcolors.OKGREEN +" |")
print(" ", "\t",end='')
for i in range(44):
    print(bcolors.OKGREEN+"-", end='')
print("")