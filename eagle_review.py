#!/usr/bin/python3
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

def parse_csv(filename, arb_date):
    arb_date = datetime.strptime(arb_date, '%m/%d/%y')
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
                        if date >= arb_date:
                            if scout_name not in scout_data:
                                scout_data[scout_name] = {}
                            if header not in scout_data[scout_name]:
                                scout_data[scout_name][header] = []
                            scout_data[scout_name][header].append(value)
                    except ValueError:
                        pass  # Not a valid date format

    return scout_data

def has_satisfied_eagle(requirements):
    badges_earned = set(requirements.keys())
    criticals_satisfied = all(badge in badges_earned for badge in er_criticals)
    sport_satisfied = any(badge in badges_earned for badge in er_sport)
    emerg_satisfied = any(badge in badges_earned for badge in er_emerg)
    enviro_satisfied = any(badge in badges_earned for badge in er_enviro)
    total_badge_count = len(badges_earned)
    
    return criticals_satisfied and sport_satisfied and emerg_satisfied and enviro_satisfied and total_badge_count >= 21

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename> <eval_date>")
        return

    filename = sys.argv[1]
    arb_date = '01/01/01' # kept this vestige of eval_date, just easier for parsing data 
    scout_data = parse_csv(filename, arb_date)

    for scout_name, data in scout_data.items():
        life_flag = False
        star_flag = False
        print(f"Scout: {scout_name}")
        total_badge_count = len(data)
        er_badge_count = sum(1 for badge in er_badges if badge in data)
        print(f"MBs: {total_badge_count}")
        print(f"ER MBs: {er_badge_count}")

        if er_badge_count >= 4 and total_badge_count >= 6:
            print("MBs Satisfy Star")
            star_flag = True
        else:
            print("MBs Don't Satisfy Star")

        if er_badge_count >= 7 and total_badge_count >= 11:
            print("MBs Satisfy Life")
            life_flag = True
        else:
            print("MBs Don't Satisfy Life")

        if has_satisfied_eagle(data):
            print("MBs Satisfy Eagle")
        elif not life_flag:
            print("MBs not evaluated for Eagle")
        else:
            print("MBs Don't Satisfy Eagle")
            if not all(badge in data for badge in er_criticals):
                print("  Missing:", ", ".join(badge for badge in er_criticals if badge not in data))
            if not any(badge in data for badge in er_sport):
                print("  Missing one of:" , ", ".join(badge for badge in er_sport if badge not in data))
            if not any(badge in data for badge in er_emerg):
                print("  Missing one of:", ", ".join(badge for badge in er_emerg if badge not in data))
            if not any(badge in data for badge in er_enviro):
                print("  Missing one of:", ", ".join(badge for badge in er_enviro if badge not in data))
            if total_badge_count < 21:
                print("  Total badge count less than 21")
        print()


if __name__ == "__main__":
    main()

