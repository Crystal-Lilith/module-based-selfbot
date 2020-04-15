token = "Your token" # Replace with your user token
prefix = "/" # Replace with your preferred prefix
enabled_by_default = False # Recommened to have this as False, if you wish to enable it in a certain channel do /enablw_channel
splitter = "][" # This is how arguments are made, so for example `/msg 10][Hi` has 2 arguments, which is split by '][' by default
allowed_ids = [] # The account using this selfbot is always allowed to use the commands

# The code below checks if the config is valid
for i in (token, prefix, splitter):
    if not isinstance(i, str):
        raise SystemExit("token, prefix or splitter is not a string, please make sure they are all strings")

if not isinstance(enabled_by_default, bool): raise SystemExit("'enabled_by_default' must be either True or False")

if not isinstance(allowed_ids, list): raise SystemExit("Allowed IDs is not a list, please make it a list containing integers seprated by ',' for every user id")

for id in allowed_ids:
    if not isinstance(id, int): raise SystemExit("'"+id+"' has the type '"+type(id)+"', when it needs to be an integer")
