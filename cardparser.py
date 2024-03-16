import csv


input_filename = "cardindex.csv" 
output_filename = "ondatra.xml"


header = """<?xml version="1.0" encoding="UTF-8"?>
<cockatrice_carddatabase version="4">
    <sets>
        <set>
            <name>ondrahra</name>
            <longname>ondatra ondrahra</longname>
            <settype>Custom</settype>
            <releasedate>2024-03-15</releasedate>
        </set>
    </sets>
    
     
"""

cards_tag_open = "    <cards>"
cards_tag_close = "\n    </cards>"

file_end = "\n</cockatrice_carddatabase>"

def process_row(row, line_count):
    if line_count == 0:
        print("reading card index...")
        return ""
    else:
        card_id = row[0]
        card_name = row[1]
        card_type = row[2]
        card_rc = row[3]
        card_color = row[4]
        card_pt = row[5]
        card_text = row[6]

        return f"""
        <card>
            <name>{card_name}</name>
            <text>{card_text}</text>
            <prop>
                <type>{card_type}</type>
                <manacost>{card_rc}</manacost>
                <pt>{card_pt}</pt>
                <colors>{card_color}</colors>
            </prop>
            <set>ondrahra</set>
        </card>"""




def main():
    csv_f = open(input_filename)
    csv_r = csv.reader(csv_f, delimiter=",")

    out = open(output_filename, 'w')
    out.write(header)
    out.write(cards_tag_open)

    line_count = 0

    for row in csv_r:
        row_output = process_row(row, line_count)
        if row_output != "":
            out.write(row_output)
        line_count += 1
    

    out.write(cards_tag_close)
    out.write(file_end)
    out.close()

    print("finished.")



if __name__ == "__main__":
    main()
