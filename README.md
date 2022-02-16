# Anirevo-Panelist-Extractor

## The Big Idea

This was a tool that I wrote back during my time at Anime Revolution ("Anirevo", a Japanese pop culture event in Vancouver BC) after I was asked by my programming director to compile a list of all approved presenters and performers ("panelists"), their events ("panels"), their contact info, and their badge reimbursement rate for our vice chair. 

To summarize the goals at the time:
1. Automate the corresponding data entry for future intakes, as manually typing in panelists' information is tedious.
2. Increase accuracy while inputting badge numbers. This is key because it's evidence of a panelist buying their badge. Mistyping one digit may have the vice chair overlooking them during the first round of compensation.

## How It Works

The tool takes a CSV file of approved panels ("idols.csv"; the last file used was a spreadsheet for idol groups). Its fields are tailored to suit the CSV file exported from the website's panelist application form. 

It then goes through the list of approved panels, creates a "profile" for each panelist (and if there is one, co-panelist) containing the following below, and writes it to another CSV file in alphabetical order:

- First and Last Name
- Email
- Phone Number
- All panels done
- Badge Number
- Reimbursement  - either 50% or 100%. Anirevo's policy is that panelists who do one hour's worth of programming is reimbursed for half of their badge, while panelists who do two hours' worth of programming have the full cost of their badge reimbursed. 

## Limitations

The script does not consider those eligible for a free pass (subjective to the director himself), and assumes that all panelists in the file are fan panelists eligible for a reimbursement. 

This can be resolved by manually replacing their reimbursement rate cell with (say) "FREE BADGE". 

## What Could Have Been Done Better and How?

As I wrote this after Term 1 at BCIT (ie. basic programming), there's a couple things that I could have improved on now that I've learned more programming concepts following my departure. In no particular order:
1. Use Pandas to process the files, so I don't have to convert .xlsx files into .csv and back again.
2. Create separate variables for the columns, so I can easily reassign the values should I make changes to the main form on the Anirevo website. 
3. Use command args to take the name of the file being converted, so I don't have to hard-code that file in or rely on an input() function.
4. Turn this into a GUI for anyone who's not capable of code, should I leave Anirevo.
5. Write cleaner code, so someone within the department (or within our sister con, International Fan Festival Toronto) can mantain or upgrade it. 
6. Remove the "get" functions, since I realized that it doesn't do much in Python (compared to Java). 

## The Future

I doubt I'd be making changes to this, since I'm no longer at Anirevo and don't see myself taking on a programming staff position elsewhere. 

If you're still at Anirevo (...or International Fan Festival Toronto), feel free to steal this. Data entry is painful!
