"""
    This module finds burnout rate of the student
"""


class BurnoutCalculator:
    @classmethod
    def burnout_calculator(cls, d_scores: list, e_scores: list):
        """
            Burnout calculator, constants based on average of
            10 datasets of mean and std dev based of the scores of 100 students
        :param d_scores:
        :param e_scores:
        :return:
        """
        # std_mean = 54.295
        # std_dev = 30.893
        up_div = 85.188
        low_div = 23.402
        student_score = sum(d_scores) + sum(e_scores)

        if student_score <= low_div:
            return {
                'score': student_score,
                'burnout_level': 'low'
            }
        elif low_div < student_score <= up_div:
            return {
                'score': student_score,
                'burnout_level': 'Medium'
            }
        elif student_score > up_div:
            return {
                'score': student_score,
                'burnout_level': 'High'
            }
