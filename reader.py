"""

Anirevo Panelist Spreadsheet Reader

Reads a spreadsheet, eliminates duplicate panelists, determines reimbursement rates, and writes that to a new spreadsheet.

By Michelle Chan and Jeremy Androsoff

"""

import csv
import panelist
import re

file_name = "idols.csv"


def get_file():
    file_name = input("Enter file name: ")

    return file_name


def read_file(a_file):

    file = open(a_file)
    file_reader = csv.reader(file)
    panelist_list = []

    for row in file_reader:
        main_panelist = create_panelist_object(row)

        if search_panelist(main_panelist, panelist_list) is False:
            panelist_list.append(main_panelist)

        if row[6] != '':
            co_panelist = create_co_panelist_object(row)

            if search_panelist(co_panelist, panelist_list) is False:
                panelist_list.append(co_panelist)

    return panelist_list


def search_panelist(a_panelist, a_list):

    for panelist in a_list:
        if panelist.get_badge_number() == a_panelist.get_badge_number():
            return True

    return False


def create_panelist_object(line):
    main_panelist = panelist.Panelist(str(line[0] + " " + line[1]), line[2], line[3], line[5], find_panels(line[0], line[1], file_name))
    return main_panelist


def create_co_panelist_object(line):
    panels = find_panels(line[4], line[6], file_name)
    co_panelist = panelist.Panelist(line[4] + " " + line[6], line[9], line[10], line[8], panels)
    return co_panelist


def find_panels(a_first_name, a_last_name, a_file):

    file = open(a_file)
    file_reader = csv.reader(file)

    panels = []

    first_regex = re.compile(a_first_name)
    last_regex = re.compile(a_last_name)

    for row in file_reader:

        first_match = first_regex.search(str(row))
        last_match = last_regex.search(str(row))
        if first_match and last_match:
            panels.append(row[7])

    return panels


def print_panelist(a_panelist_list):

    for panelist in a_panelist_list:
        print("Name: ", panelist.get_name())
        print("Email: " + panelist.get_email())
        print("Phone: " + panelist.get_phone())
        print("Panels: " + str(panelist.panels_to_string()))
        print("Badge Number: " + panelist.get_badge_number())
        print("Reimbursement: " + panelist.get_reimbursement())
        print("\n")


def write_csv(a_panelist_list):

    fields = ["Full Name", "Email", "Phone", "Panel(s)", "Pass Number", "Status"]

    with open("new_idols.csv", 'w') as csvfile:
        file_writer = csv.writer(csvfile)

        file_writer.writerow(fields)

        file_writer.writerows(a_panelist_list)


def create_csv_lines(a_panelist_list):

    rows = []

    for panelist in a_panelist_list:
        attribute_row  = []
        attribute_row.append(panelist.get_name())
        attribute_row.append(panelist.get_email())
        attribute_row.append(panelist.get_phone())
        attribute_row.append(panelist.get_panels())
        attribute_row.append(panelist.get_badge_number())
        attribute_row.append(panelist.get_reimbursement())

        rows.append(attribute_row)

    return rows


def main():
    list = read_file(file_name)
    list.sort(key=lambda x: x.name)
    lines = create_csv_lines(list)
    write_csv(lines)


if __name__ == "__main__":
    main()