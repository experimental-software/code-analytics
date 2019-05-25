import unittest

from enrich_codecharta_data import *

# https://docs.python.org/2/library/unittest.html
class EnrichCodechartaDataTest(unittest.TestCase):

    def test_find_node_for_ksch_file(self):
        source_code_root = get_source_code_data('t/sonar-ksch.json')
        example_file_name = 'reporting/reporting-impl/src/main/java/ksch/event/EventEntity.java'

        file_node = find_node(source_code_root, example_file_name.split("/"))

        self.assertTrue(file_node)

    def test_find_node_for_wicket_file(self):
        source_code_root = get_source_code_data('t/sonar-wicket.json')
        example_file_name = 'wicket-request/src/main/java/org/apache/wicket/request/http/WebRequest.java'

        file_node = find_node(source_code_root, example_file_name.split("/"))

        self.assertTrue(file_node)

if __name__ == '__main__':
    unittest.main()
