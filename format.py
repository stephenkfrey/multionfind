with open('texts/instructions.txt', 'r') as file:
    instructions = file.read()

with open('texts/outreach_message.txt', 'r') as file:
    outreach_message = file.read()

formatted_instructions = instructions.format(outreach_message=outreach_message)

print(formatted_instructions)



Extra = """
We are iterating through each profile to see if there is a match. Go through each profile. Click on the profile to open the side pane. See if the profile matches the "cool" criteria and avoids the "pass" criteria. If they met "cool" and didn't have "pass" criteria, then 1) click the heart icon and add them to the list "web app dev" and 2) Click "Invite" to "Invite to Job" to send them a message to invite them to the job. Then look inside of the modal, find the "Profile Header" div section (DO NOT click "open in new window", STAY INSIDE THE MODAL), and click the 24x24 svg image of the "back" arrow to return to the main candidate list. Then move to repeat ont he next candidate. 

-----

We are iterating through each profile to see if there is a match. Go through each profile.  DO NOT click the "Hire" or "Open in external Window" or "More Options" links. Click on the profile picture to open the side pane. 

Click the "More" expansion text underneath the "text body" profile description to read the full  profile description. See if the profile matches the "cool" criteria and avoids the "pass" criteria.  

If they met "cool" and didn't have "pass" criteria, then: 2) Click "Invite" button (it's labelled "invite <name> to job"), wait for the messaging modal to open, and click the "Send Invitation button". 

After either inviting or passing, you must go back from the profile modal and return to the main page--do this by pressing the "Escape" key, which returns you to the main list of candidates. After you've reviewed a profile, Press the "Escape" key to close the modal. DO NOT click the next profile image until after you have pressed the "ESCAPE" key to close the modal. 

Ensure the profile modal is closed before continuing. 

Then move to repeat on the next candidate. 
----
"""