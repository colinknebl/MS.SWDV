import re
from datetime import datetime
from Queue import Queue


class DocSearch:
    """A class for managing the searching of the workout log data set"""

    class WorkoutLog:
        """A class used for parsing and easier access to the workout data

        static:
        Columns - valid data points to search for

        Public methods:
        get - returns the specified data point
        """

        Columns = ['date', 'title', 'description', 'best_result_raw',
             'best_result_display', 'score_type', 'barbell_lift',
             'set_details', 'notes', 'rx_or_scaled', 'pr']


        def __init__(self, log):
            """Creates a new WorkoutLog"""
            try:
                # The data is not easily parsed because it has multiple forms.
                # This sequence of splits seems to reliably split the data.
                (date, title, rest) = log.strip().split(',', 2)
                (description, rest) = rest.split('",', 1)
                (best_result, best_result_display, rest) = rest.split(',', 2)
                (score_type, barbell_lift, set_details, rest) = rest.split('","', 3)
                (notes, rest) = rest.split('",')
                (scaled, pr) = rest.split(',')

                self.log = [date, title, description, best_result,
                            best_result_display, score_type, barbell_lift,
                            set_details, notes, scaled, pr]
            except:
                self.log = log

        def get(self, item):
            """Get a specific data point"""
            if item in DocSearch.WorkoutLog.Columns:
                index = DocSearch.WorkoutLog.Columns.index(item)
                return self.log[index]
            else:
                return False

    class Dates:
        """A class for working with the dates"""

        message_prompt = 'What dates would you like to search? Separate multiple dates with a comma. (MM/DD/YYYY) '
        valid_date_regex = '[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]'

        @staticmethod
        def _parse_date_input(user_input):
            """Parses the dates from the user input, and return an array of dates"""
            dates = []
            for date in user_input.split(','):
                dates.append(date.strip())
            return dates

        @staticmethod
        def init_date(date_str):
            """Returns a datetime instance of the date for easier, more accurate comparisons"""
            split_date = date_str.split('/')
            return datetime(int(split_date[2]), int(split_date[0]), int(split_date[1]))

        def verify_dates(self, dates):
            """Compares each date entered to the regular expression to ensure the date is properly formatted"""
            valid = False
            for date in dates:
                valid = re.fullmatch(self.valid_date_regex, date) != None
            return valid

        def get_dates(self):
            """Returns an array of dates to search for"""
            return self._parse_date_input(
                input(self.message_prompt)
            )

    def __init__(self, file_path):
        file = open(file_path, 'r')
        file.readline() # remove the heading row
        self.file_contents = file.readlines()
        file.close()
        self.dates_queue = Queue()
        self.num_of_logs = len(self.file_contents)

    def run_search(self):
        """Initiates and manages the search sequence"""
        self._get_dates()
        while len(self.dates_queue) > 0:
            target = self._binary_search(self.Dates().init_date(self.dates_queue.dequeue()), self.file_contents)
            self._print_details(target)

    def _binary_search(self, target_date, content, num=0):
        """Performs a binary search on the data"""
        # calculate the mid point of the data
        mid = len(content) // 2

        # create a WorkoutLog instance of the logged workout at the mid point
        logged = self.WorkoutLog(content[mid])

        # get the mid point date for comparisons
        mid_date = self.Dates().init_date(logged.get('date'))

        if len(content) < 0:
            return
        elif target_date == mid_date:
            # if the target_date equals the mid_date, return the workout because that is
            # the one the user is searching for
            return logged
        elif target_date < mid_date:
            # if the target date is smaller than the mid date,
            # perform the search again on the first half of the data
            return self._binary_search(target_date, content[:mid], num + 1)
        else:
            # if here, the target date is larger than the mid date,
            # perform the search again on the last half of the data
            return self._binary_search(target_date, content[mid + 1:], num + 1)

    def _get_dates(self):
        """Prompts the user for the dates to search for, and adds each of the dates to the queue"""
        dates = self.Dates().get_dates()
        if self.Dates().verify_dates(dates):
            self._add_dates_to_queue(dates)
        else:
            print('Dates entered did match the required formatting, closing search.')
            exit(0)

    def _add_dates_to_queue(self, dates):
        """Adds the dates the user specified to a queue

        dates - an array of dates in MM/DD/YYYY format
        """
        for date in dates:
            self.dates_queue.enqueue(date)

    def total(self, data_point, comparator):
        """Performs a linear search over the file contents

        data_point - the specific data point to be searched (i.e. 'pr', 'title', etc.)
        comparator - a function that takes in the data point value found
        """
        num = 0
        for line in self.file_contents:
            line = DocSearch.WorkoutLog(line)
            if comparator(line.get(data_point)):
                num += 1
        return num

    @staticmethod
    def _print_details(logged):
        """Prints out a formatted message containing the searched for workout details"""
        print("""
        Workout Summary for {0}:

            Title: 
            {1}

            Description:
            {2}

            Set Details:
            {4}

            Best Result(s):
            {3}

            Scaled or Rx:
            {5}

            Pr:
            {6}
        """.format(
            logged.get('date'),
            logged.get('title'),
            logged.get('description'),
            logged.get('best_result_display'),
            logged.get('set_details'),
            logged.get('rx_or_scaled'),
            True if logged.get('pr') == 'PR' else False
        ))

def is_pr(val):
    return True if val == 'PR' else False

def is_scaled(val):
    return True if val == 'SCALED' else False

def print_summary(search):
    print('Total number of logged workouts:', search.num_of_logs)
    print('Total Number of PRs:', search.total('pr', is_pr))
    total_scaled = search.total('rx_or_scaled', is_scaled)
    print('{0:0.0f}% of workouts performed Rx'.format(((search.num_of_logs - total_scaled) / search.num_of_logs) * 100))
    print()



def main():

    search = DocSearch('./workouts.csv')

    print_summary(search)

    # run the binary search
    search.run_search()


if __name__ == '__main__':
    main()