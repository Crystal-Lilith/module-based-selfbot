token = "Put your token here"
prefix = "/" # Replace with your preffered prefix
enabled_by_default = False # Recommened to have this as False, if you wish to enable it in a certain channel do /enablw_channel
splitter = "][" # This is how arguments are made, so for example `/msg 10][Hi` has 2 arguments, which is split by '][' by default

# The code below checks if the code is valid
for i in (token, prefix, splitter):
    if not isinstance(i, str):
        raise SystemExit("token, prefix or splitter is not a string, please make sure they are all strings")

if not isinstance(enabled_by_default, bool): raise SystemExit("'enabled_by_default' must be either True or False")
