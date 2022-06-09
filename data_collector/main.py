import json

from curler import Curler

if __name__ == '__main__':
    vendor_code = '3e59v2'
    curler = Curler()
    extract_comments = curler.extract_all_comments(vendor_code)
    output_file = open('comments/' + vendor_code + '.json', 'w')
    output_file.write(json.dumps(extract_comments))
