class ResultObject:
    test_name: str = ""
    test_message: str = ""
    is_pass: bool = False
    is_deviation: bool = False

    def __init__(self, is_passp, test_namep, test_messagep="", is_deviation=False):
        self.test_name = test_namep
        self.test_message = test_messagep
        self.is_pass = is_passp
        self.is_deviation = is_deviation

    def get_pass(self):
        return self.is_pass

    def __str__(self):
        return f"{self.test_name}\n{self.test_message}\n\n-----------------------------------------------------------\n"


class FormatTest(ResultObject):
    def __init__(self, is_passp, test_namep, test_messagep="", is_deviation=False):
        super().__init__(is_passp, test_namep, test_messagep, is_deviation)


class FunctionalityTest(ResultObject):
    def __init__(self, is_pass, test_namep, test_messagep="", is_deviation=False):
        super().__init__(is_pass, test_namep, test_messagep, is_deviation)


class NonScoringTest(ResultObject):
    overview: str = None

    def __init__(self, is_passp, test_namep, test_messagep="", overview=""):
        super().__init__(is_passp, test_namep, test_messagep)
        self.overview = overview

    def get_overview_string(self):
        return f'{self.overview} \r\n'


class ResultArray:
    tests: list[ResultObject] = []

    def __init__(self):
        pass

    def append_test(self, test: ResultObject):
        self.tests.append(test)

    def get_count_basic(self):
        count = 0
        for i in self.tests:
            if isinstance(i, FormatTest):
                count += 1
        return count

    def get_num_basic_passed(self):
        count = 0
        for i in self.tests:
            if isinstance(i, FormatTest) and i.get_pass():
                count += 1
        return count

    def get_count_functionality(self):
        count = 0
        for i in self.tests:
            if isinstance(i, FunctionalityTest):
                count += 1
        return count

    def get_num_functionality_passed(self):
        count = 0
        for i in self.tests:
            if isinstance(i, FunctionalityTest) and i.get_pass():
                count += 1
        return count

    def collect_error_messages(self):
        messages = ""
        for test in self.tests:
            if not test.get_pass():
                messages += str(test)
        messages += "\n ============================================================================"

        return messages

    def get_summary_msgs(self):
        messages = ""
        for test in self.tests:
            if isinstance(test, NonScoringTest) and test.get_overview_string():
                messages += test.get_overview_string()
        return messages

    def get_deviation_status(self):
        for test in self.tests:
            if test.is_deviation and (not test.is_pass):
                return True