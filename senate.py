import urllib, csv
import lxml.html

fp = urllib.urlopen("http://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_112_1.htm")

html= lxml.html.parse(fp)

fp.close()

rows = html.xpath('//table[@class="contenttext"]//table/tr')

outfile = open('tablesenate.csv', 'w')
# newline breaks in 2.7 check that out
csvout = csv.writer(outfile)

for row in rows:
    cols = row.getchildren()

    csvcols = [col.text_content().strip() for col in cols]

    csvout.writerow(csvcols)
outfile.close()
