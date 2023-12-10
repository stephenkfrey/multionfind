import multion 
multion.login()

### Load Upwork job ### 
upwork_url = "https://www.upwork.com/ab/applicants/1733701623681265664/suggested"

with open('texts/instructions.txt', 'r') as file:
    instructions = file.read()

with open('texts/outreach_message.txt', 'r') as file:
    outreach_message = file.read()

formatted_instructions = instructions.format(outreach_message=outreach_message)

### Run talent search and review ###    
r = multion.new_session({"input": formatted_instructions, "url": upwork_url}) 
# returns a dict with {session_id, status, message, url}

print (r['session_id'], r['status'], r['message'], r['url'])
session_id = r['session_id']
multion.close_session(session_id)