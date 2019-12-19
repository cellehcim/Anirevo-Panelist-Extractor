# Anirevo-Panelist-Extractor
Anirevo Panelist Extractor

This was a tool that I wrote back during my time at Anirevo (anime convention in Vancouver, BC) after I was asked by my programming director to compile a list of all approved panelists and performers, their contact info, and their badge reimbursement rate for our vice chair. I had plans to reuse this for future intakes, although I resigned from the staff before I could do so. 

The tool takes a CSV file of approved panels (in this case, "idols.csv" since the last file used was a spreadsheet for idol groups), in which the fields are tailored to suit the CSV file obtained from the Wordpress site for the panelist application form. 

It then goes through the list of approved panels, creates a "profile" for each panelist (and if there is one, co-panelist) containing the following below, and writes it to another CSV file in alphabetical order:

- First and Last Name
- Email
- Phone Number
- All panels done
- Badge Number
- Reimbursement Obtained (either 50% or 100%)

The only limitation is that the script does not consider those eligible for a free pass (subjective to the director himself), and assumes that all panelists in the file are fan panelists eligible for a reimbursement. 

As the main intent was to get the pesky data entry out of the way, this can be resolved by manually replacing their reimbursement rate cell with "FREE BADGE" or something (which is nearly impossible to get wrong compared to a badge number). 
