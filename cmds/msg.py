from discord import Embed

name = "msg"
aliases = []

async def code(msg):
    try:
        int(msg.args[0])
    except ValueError:
        print(str(args[0])+" could not be converted to a int")
    finally:
        try:
            if msg.args[1] in ('', None): raise IndexError("You didn't provide a message")
        except IndexError:
            print(f"A message must be provided, do 'amount_of_msg{__import__('config').splitter}message_content'")
            return
    try:
        delay = float(msg.args[3])
    except IndexError:
        delay = 0
    for x in range(int(args[0])):
        try:
            if msg.args[2].lower() == "embed":
                await msg.channel.send(embed=Embed(title=f"{str((int(msg.args[0]) - x) - 1)} times left", description=str(args[1])))
                await sleep(delay)
            elif msg.args[2].lower() == "eval":
                msg.args[1] = eval('''f"""'''+str(args[1])+'''"""''')
                raise IndexError("This exception has been raised to send a message after executing eval")
            else:
                raise IndexError("Argument does not exist")
        except IndexError:
            await msg.channel.send(str(msg.args[1]))
            await sleep(delay)
