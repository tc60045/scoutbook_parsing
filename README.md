# scoutbook_parsing
Tools for parsing the output of Scoutbook reports for use in analysis and reporting
All of the tools here are intended to give you faster answers and usable data from Scoutbook reports that you generate for your troop.
Instructions on how to create a report can be found on these threads:
- MeritBadge-data-dump:
- Troop-advancement-dump: 

MeritBadge-data-dump tools:
- mbs_summer.py -- gen


- mbs_since.py -- gives you details of which badges were earned by each scount since a certain date
The command is: python3 mbs_since.py filename-you-downloaded-in-csv-format.csv 06/01/23
Note that you can enter 01/01/01 to get every MB each scout has earned

Sample output:
Scout: Lethargic Highschooler
Total MBs Earned: 2
ER MBs earned: 1
Badges earned since 06/01/23:
  Metalwork: ['7/28/23']
  Swimming: ['7/25/23']

Scout: Motivate Middleschooler
Total MBs Earned: 5
ER MBs earned: 2
Badges earned since 06/01/23:
  Emergency Prep.: ['7/28/23']
  Canoeing: ['7/26/23']
  Swimming: ['7/25/23']
  Metalwork: ['7/28/23']
  Pioneering: ['7/28/23']

- 
