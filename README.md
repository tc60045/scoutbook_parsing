# scoutbook_parsing
Tools for parsing the output of Scoutbook reports for use in analysis and reporting.  


All of the tools here are intended to give you faster answers and usable data from Scoutbook reports that you generate for your troop.

Please review the .output for each utility to see what you can expect AND to see the command convention.  

Also, at the recommendation of Brian D, please note:  dates (when used) are always in mm/dd/yy and not mm/dd/yyyy.  I could / should have been more flexible on these, and will re-visit in the future. 


Instructions on how to create a report can be found on these threads:
- MeritBadge-data-dump: https://www.reddit.com/r/BSA/comments/15t2s5e/more_advancement_chair_tools_mbs_earned_since/
- Troop-advancement-dump: <coming soon>


MeritBadge-data-dump tools:
- mbs_since.py -- gives you details of which badges were earned by each scout since a date
- mbs_counter.py -- tells you comma-separated: scout, MBs, ER MBs earned since a date
- mbs_between.py -- all the details of badges earned between two dates you enter
- mbs_between_counter.py -- like mbs_counter, gives data comma-separated b/t 2 dates
- mbs_json.py -- scout, [array of all badges] earned after a date
- eagle_review.py -- tells you in 1 second how many and which ER badges are missing: EM of X
  (we refer to Life scouts as being EM3 or EM1 = how many they are missing)
- missing.py -- tells you which Scouts are missing an MB (review missing.output for badge name handling)
- who_has -- does the opposite; tells you who has a particular MB (review who_has.output for badge name handling)

Sample output is shown for each of these tools in the corresponding .output files

More goodies to come -- enjoy!!
