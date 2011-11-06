import urllib.request, csv
import lxml.html

fp = urllib.request.urlopen("http://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_112_1.htm")

html= lxml.html.parse(fp)

fp.close()

rows = html.xpath('//table[@class="contenttext"]//table/tr')

outfile = open('tablesenate.csv', 'w', newline="")

csvout = csv.writer(outfile)

for row in rows:
    cols = row.getchildren()

    csvcols = [col.text_content().strip() for col in cols]

    csvout.writerow(csvcols)
outfile.close()
