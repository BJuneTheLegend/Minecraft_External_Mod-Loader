#Thanks to https://stackoverflow.com/a/287944

class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#print(f"""
#{BColors.HEADER} Hello, world!
#{BColors.OKBLUE} Hello, world!
#{BColors.OKCYAN} Hello, world!
#{BColors.OKGREEN} Hello, world!
#{BColors.WARNING} Hello, world!
#{BColors.FAIL} Hello, world!
#{BColors.ENDC} Hello, world!
#{BColors.BOLD} Hello, world!{BColors.ENDC}
#{BColors.UNDERLINE} Hello, world!
#""")