# Anirevo-Panelist-Extractor

## The Big Idea

This was a tool that I wrote back during my time at Anime Revolution ("Anirevo", a Japanese pop culture event in Vancouver BC) after I was asked by my programming director to compile a list of all approved presenters and performers ("panelists"), the respective events hosted by them ("panels"), their contact info, and their badge reimbursement rate for our vice chair. 

To summarize the goals at the time:
1. Automate the corresponding data entry for future intakes (whether it's me or another staffer), since I've personally found it tedious manually typing in panelists' information.
2. Increase chances of accuracy when it comes to entering in badge numbers. The badge number is key, since it's evidence of a panelist paying for their badge. If I mistype one digit, the panelist is less likely to be initially compensated by our vice chair and will have to wait longer. 

## How It Works

The tool takes a CSV file of approved panels (in this case, "idols.csv" since the last file used was a spreadsheet for idol groups), in which the fields are tailored to suit the CSV file obtained from the Wordpress site for the panelist application form. 

It then goes through the list of approved panels, creates a "profile" for each panelist (and if there is one, co-panelist) containing the following below, and writes it to another CSV file in alphabetical order:

- First and Last Name
- Email
- Phone Number
- All panels done
- Badge Number
- Reimbursement Obtained - either 50% or 100%. Anirevo's policy is that panelists who do one hour's worth of programming is reimbursed for half of their badge, while panelists who do two hours' worth of programming has the full cost of their badge reimbursed. 

## Limitations

The script does not consider those eligible for a free pass (subjective to the director himself), and assumes that all panelists in the file are fan panelists eligible for a reimbursement. 

As the end goal was to get the pesky data entry out of the way, this can be resolved by manually replacing their reimbursement rate cell with "FREE BADGE" or something. This should be something that's nearly impossible to butcher compared to a five-digit badge number. 

## What Could Have Been Done Better and How?

As this was written back following Term 1 at BCIT (ie. basic programming), there's a couple things that I could have improved on now that I've learned more programming concepts following my departure. In no particular order:
1. Use Pandas to process the files, so I don't have to convert .xlsx files into .csv and back again.
2. 3. Create separate variables for the columns, so I can easily reassign the values should I make changes to the main form on the Anirevo website. 
3. Use command args to take the name of the file being converted, so I don't have to hard-code that file in or rely on an input() function.
4. Possibly turn this into a GUI for anyone who's not capable of code, should I leave Anirevo.
5. Remove the "get" functions, since I realized that it doesn't do much in Python (compared to Java). 

## The Future

I doubt I'd be making changes to this, since I'm no longer at Anirevo and don't see myself taking on a programming staff position elsewhere. 

If you're still at Anirevo, feel free to steal this. Data entry is painful!
