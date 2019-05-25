import csv

def parse_codemaat_results(csv_file):
    with open(csv_file) as f:
        csv_reader = csv.DictReader(f)
        if (csv_reader.fieldnames == ['entity', 'n-revs']):
            return parse_codemaat_revisions_analysis(csv_reader)
        else:
            raise Exception('Cannot parse CSV file with header: ' + ",".join(csv_reader.fieldnames))


def parse_codemaat_revisions_analysis(csv_reader):
    result = []
    for row in csv_reader:
        analysis = {
            'file_name': row['entity'],
            'attribute': 'n-revs',
            'value': row['n-revs']
        }
        result.append(analysis)
    return result

if __name__ == "__main__":

    print parse_codemaat_results('/tmp/codemaat-revisions.txt')
