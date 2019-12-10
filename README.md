# Anirevo-Panelist-Extractor
Anirevo Panelist Extractor

This was an tool that I wrote back during my time at Anirevo (anime convention in Vancouver, BC), to help automate the badge compensation process for approved panelists during the Summer 2019 intake. This was also written with intention to use for future intakes, although I resigned from the staff before I could resuse the tool. 

The tool takes a CSV file of approved panels (in this case, "idols.csv" since the last file used was a spreadsheet for idol groups), in which the fields are tailored to suit the CSV file obtained from the Wordpress site for the panelist application form.

The tool then goes through the list of approved panels, creates a "profile" for each panelist (and if there are any, co-panelist) containing the following below, and writes it to another CSV file:

- First and Last Name
- Email
- Phone Number
- All panels done
- Badge Number
- Reimbursement Obtained. 
