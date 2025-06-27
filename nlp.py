def process_command(command):
    command = command.lower()
    if "time" in command:
        return "time"
    elif "hello" in command:
        return "greet"
    elif "stop" in command or "exit" in command:
        return "exit"
    else:
        return "unknown"
