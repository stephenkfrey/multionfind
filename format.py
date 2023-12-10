with open('texts/directions.txt', 'r') as file:
    instructions = file.read()

with open('texts/outreach_message.txt', 'r') as file:
    outreach_message = file.read()

formatted_instructions = instructions.format(outreach_message=outreach_message)

print(formatted_instructions)