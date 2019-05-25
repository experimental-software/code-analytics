import csv
import json


def get_json_data(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)

def get_source_code_root(data):
    project_name = data['projectName']
    root_node = data['nodes'][0]
    if (":" in project_name):
        return root_node['children'][0]['children'][0]
    else:
        return root_node['children'][0]

def find_node(parent_node, path_elements):
    next_step = path_elements.pop(0)
    for child_node in parent_node['children']:
        if (child_node['name'] == next_step):
            if (len(child_node['children']) > 0):
                return find_node(child_node, path_elements)
            else:
                return child_node
    return None

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

    json_data = get_json_data('/tmp/sonar.json')
    source_code_root = get_source_code_root(json_data)

    # Enrich data
    codemaat_analysis = parse_codemaat_results('/tmp/codemaat-revisions.txt')
    for analysis in codemaat_analysis:
        file_node = find_node(source_code_root, analysis['file_name'].split("/"))
        if (file_node):
            file_attributes = file_node['attributes']
            file_attributes[analysis['attribute']] = analysis['value']

    # Write out modified JSON file
    with open('/tmp/sonar.json', 'w') as outfile:
        json.dump(json_data, outfile)