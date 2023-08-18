import csv
import sys
from datetime import datetime

er_badges = (
    "Camping", "Citizenship in Society", "Cit. in Comm.", "Cit. in Nation",
    "Cit. in World", "Communication", "Cooking", "Cycling", "Emergency Prep.",
    "Enviro. Science", "Family Life", "First Aid", "Lifesaving", "Pers. Fitness",
    "Personal Mgmt.", "Sustainability", "Swimming", "Hiking"
)

er_criticals = (
    "Camping", "Citizenship in Society", "Cit. in Comm.", "Cit. in Nation",
    "Cit. in World", "Communication", "Cooking", "Family Life", "First Aid",
    "Pers. Fitness", "Personal Mgmt."
)

er_sport = ("Cycling", "Hiking", "Swimming")

er_emerg = ("Emergency Prep.", "Lifesaving")

er_enviro = ("Enviro. Science", "Sustainability")

def parse_csv(filename, eval_date):
    global headers
    eval_date = datetime.strptime(eval_date, '%m/%d/%y')
    scout_data = {}

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames

        if headers[0].lower() != 'scout':
            headers[0] = 'Scout'

        for row in reader:
            scout_name = row['Scout']
            for header, value in row.items():
                if header != 'Scout' and value:
                    try:
                        date = datetime.strptime(value, '%m/%d/%y')
                        if date >= eval_date:
                            if scout_name not in scout_data:
                                scout_data[scout_name] = {}
                            if header not in scout_data[scout_name]:
                                scout_data[scout_name][header] = []
                            scout_data[scout_name][header].append(value)
                    except ValueError:
                        pass  # Not a valid date format

    return scout_data

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <filename> <badge_name>")
        return
    print("To get a list of all BSA badges enter 'all'. If you don't match, we will show a smaller list")

    filename = sys.argv[1]
    badge_name = sys.argv[2]
    eval_date = '01/01/01'
    badges_out = list()
    scout_data = parse_csv(filename, eval_date)
    if badge_name not in headers:
        if badge_name == 'all':
            print("Here is the list the BSA uses - copy exactly")
            badges_out = headers[1:]
            print(badges_out)
            print()
        else:
            print("That badge name wasn't found. Here is the subset that starts with what you entered - copy exactly")
            for badge in headers[1:]:
                if badge.upper()[0:2] == badge_name.upper()[0:2]:
                    badges_out.append(badge)
            print(badges_out)
            print()
    else:
        have_count = 0
        missing_count = 0
        for scout_name in scout_data:
            if badge_name not in scout_data[scout_name]:
                print(f"{scout_name}")
                missing_count = missing_count + 1
            else:
                have_count = have_count + 1
        total_count = have_count + missing_count
        print(f"{missing_count} of {total_count} Scouts are missing the {badge_name} badge")


if __name__ == "__main__":
    main()

