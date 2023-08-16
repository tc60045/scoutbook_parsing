import csv
import sys
from datetime import datetime

er_badges = (
    "Camping", "Citizenship in Society", "Cit. in Comm.", "Cit. in Nation",
    "Cit. in World", "Communication", "Cooking", "Cycling", "Emergency Prep.",
    "Enviro. Science", "Family Life", "First Aid", "Lifesaving", "Pers. Fitness",
    "Personal Mgmt.", "Sustainability", "Swimming", "Hiking"
)

def parse_csv(filename, eval_date):
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
        print("Usage: python script.py <filename> <eval_date>")
        return

    filename = sys.argv[1]
    eval_date = sys.argv[2]
    scout_data = parse_csv(filename, eval_date)

    for scout_name, data in scout_data.items():
        total_badge_count = len(data)
        er_badge_count = sum(1 for badge in er_badges if badge in data)
        print(f'{scout_name}, {total_badge_count}, {er_badge_count}')
        #print()


if __name__ == "__main__":
    main()

