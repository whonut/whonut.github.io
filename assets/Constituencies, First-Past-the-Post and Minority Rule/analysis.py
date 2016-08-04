import csv
from collections import namedtuple

Constituency = namedtuple('Constituency',
                          ['name', 'total_electorate', 'valid_votes'])
constituencies = []

with open("/path/to/data",
          encoding="latin-1") as f:
    constituencyreader = csv.reader(f)
    for i, row in enumerate(constituencyreader):
        if i == 0:
            continue
        constituencies.append(Constituency(name=row[1],
                                           total_electorate=int(row[4]),
                                           valid_votes=int(row[5])))

total_electorate_size = sum([c.total_electorate for c in constituencies])

# Analysis assumes a strict two-party system i.e. plurality equals majority.
# Winning party must win 326 seats. To get minimum possible total votes, win
# least populated 326.

# Assuming 100% turnout
constituencies.sort(key=lambda c: c.total_electorate)
total_electorate_votes_won = 0
constituencies_won = constituencies[:326]
for c in constituencies_won:
    # To win a majority, must win half of the vote plus one
    total_electorate_votes_won += int(c.total_electorate * 0.5) + 1

print('Assuming 100% turnout')
print('---------------------')
print('Total electorate size:', total_electorate_size)
print('Votes won:', total_electorate_votes_won)
print('Percentage of all votes:',
      (total_electorate_votes_won / total_electorate_size) * 100)

# Using actual number of valid votes.
constituencies.sort(key=lambda c: c.valid_votes)
valid_votes_won = 0
constituencies_won = constituencies[:326]
for c in constituencies_won:
    # To win a majority, must win half of the vote plus one
    valid_votes_won += int(c.valid_votes * 0.5) + 1

print('\nUsing actual number of votes cast')
print('---------------------------------')
print('Total electorate size:', total_electorate_size)
print('Votes won:', valid_votes_won)
print('Percentage of all votes:',
      (valid_votes_won / total_electorate_size) * 100)
