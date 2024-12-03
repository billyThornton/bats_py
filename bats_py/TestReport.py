"""
Class for creating test report objects.
Heavily relies on ResultsArray to gather the data for use in the report.

"""
from bats_py.ResultsArray import ResultArray

class TestReport:
    max_basic_mark = 100
    max_functionality_mark = 100
    filename = "marker_report.txt"

    results_array = None
    def __init__(self, results_arrayp: ResultArray, max_basic_markp:int, max_functionality_markp:int):
        """
        Requires a results array object,
        The maximum mark available for all the basic format specific tests. I.e. Function names, return values etc.
        The maximum mark for functionality tests. I.e. the code that solves the problem.
        Score is determined as a percentage of tests which pass.
        """
        self.results_array = results_arrayp
        self.max_basic_mark = max_basic_markp
        self.max_functionality_mark = max_functionality_markp

    def data_summary(self):
        basic_tests_passed = self.results_array.get_num_basic_passed()
        functionality_tests_passed = self.results_array.get_num_functionality_passed()
        try:
            basic_mark = str((basic_tests_passed/self.results_array.get_count_basic())*self.max_basic_mark)
        except ZeroDivisionError:
            basic_mark = 0

        try:
            functionality_mark = str((functionality_tests_passed/self.results_array.get_count_functionality())
                                     *self.max_functionality_mark)
        except ZeroDivisionError:
            functionality_mark = 0

        deviated = self.results_array.get_deviation_status()
        summary_string = (f"Marker Report\n ======================================================================== \r\n"
               f"Basic Tests Passed: {basic_tests_passed} \r\n"
               f"Functionality Tests Passed: {functionality_tests_passed}\r\n"
               f"Basic Mark: {basic_mark} \r\n"
               f"Functionality Mark: {functionality_mark}\r\n"
               f"Deviate from Spec?: {deviated} \r\n"
               f"{self.results_array.get_summary_msgs()}"
               f"Failed Test Reports:\r\n"
               f"===============================================\r\n\n")
        return  summary_string

    def create_report(self):
        if self.results_array is None:
            print("No tests have been run")
            return
        try:
            with open(self.filename, 'w') as f:
                f.write(self.data_summary())
                f.write(self.results_array.collect_error_messages())
                f.close()
        except FileNotFoundError:
            print("Marker Report File Not Found")