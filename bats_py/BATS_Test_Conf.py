class BATSTestConf:
    is_basic: bool = False
    is_functionality: bool = False
    is_non_scoring: bool = False
    score: int = 1 # The number of points the test is worth
    is_deviation: bool = False

    def __init__(self, is_basicp = False, is_functionalityp = False, is_non_scoring = False, score = 1, is_deviation = False):
        self.is_basic = is_basicp
        self.is_functionality = is_functionalityp
        self.is_non_scoring = is_non_scoring
        self.score = score
        self.is_deviation = is_deviation

        # If the test is not associated with one of the two primary categories return a non-scoring test
        if (not self.is_basic) and (not self.is_functionality):
            self.is_non_scoring = True

        if self.is_non_scoring:
            self.score = 0