# Anirevo-Panelist-Extractor
Anirevo Panelist Extractor

This was an tool that I wrote back during my time at Anirevo (anime convention in Vancouver, BC) to help automate the compilation and badge compensation process of approved panelists during the Summer 2019 intake, due to the tedious nature of the former if done by hand. This was also written with intention to use for future intakes, although I resigned from the staff before I was able to reuse the tool. 

The tool takes a CSV file of approved panels (in this case, "idols.csv" since the last file used was a spreadsheet for idol groups), in which the fields are tailored to suit the CSV file obtained from the Wordpress site for the panelist application form.

The tool then goes through the list of approved panels, creates a "profile" for each panelist (and if there is one, co-panelist) containing the following below, and writes it to another CSV file in alphabetical order:

- First and Last Name
- Email
- Phone Number
- All panels done
- Badge Number
- Reimbursement Obtained (either 50% or 100%)

The only limitation is that the script does not consider those eligible for a free pass (subjective to the director himself), and assumes that all panelists in the file are fan panelists eligible for a reimbursement. 

As the main intent was to get the pesky data entry out of the way, this can be resolved by manually replacing their reimbursement rate cell with "FREE BADGE" or something (which is nearly impossible to get wrong compared to a badge number). 
