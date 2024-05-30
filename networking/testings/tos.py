TOS_VALUES = {
    0x00: "Routine", 0x04: "Routine", 0x08: "Routine", 0x0C: "Routine",
    0x10: "Routine", 0x20: "Priority", 0x28: "Priority", 0x30: "Priority",
    0x38: "Priority", 0x40: "Immediate", 0x48: "Immediate", 0x50: "Immediate",
    0x58: "Immediate", 0x60: "Flash", 0x68: "Flash", 0x70: "Flash", 0x78: "Flash",
    0x80: "FlashOverride", 0x88: "FlashOverride", 0x90: "FlashOverride", 0x98: "FlashOverride",
    0xA0: "Critical", 0xB0: "Critical", 0xB8: "Critical", 0xC0: "InterNetwork Control",
    0xE0: "Network Control"
}

def generate_tos(tos_input):
    try:
        tos_value = int(tos_input, 16)
        if tos_value in TOS_VALUES:
            return tos_value, TOS_VALUES[tos_value], None  # Return integer and description
        else:
            return None, None, f"Invalid TOS value. Please choose from the provided options."
    except ValueError:
        return None, None, "Invalid TOS value. Please enter a valid hexadecimal value."

def append_tos_to_main(tos_value):
    try:
        with open("main.py", "r") as f:
            main_content = f.read()
            tos_replacement = f"tos = {hex(tos_value)}  # Manually set Type of Service (leave as None to use random)"
            main_content = main_content.replace("tos = None  # Manually set Type of Service (leave as None to use random)", tos_replacement)

        with open("main.py", "w") as f:
            f.write(main_content)
        return None
    except Exception as e:
        return str(e)

print("Available TOS values:")
for key, value in TOS_VALUES.items():
    print(f"{hex(key)}: {value}")

tos_input = input("Enter the TOS value in hexadecimal format: ")
tos_value, _, error = generate_tos(tos_input)

if error:
    print(error)
else:
    error = append_tos_to_main(tos_value)
    if error:
        print("Error:", error)
    else:
        print("TOS value has been successfully appended to main.py.")
