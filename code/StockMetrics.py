
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        """pt1
        """
        averages = []
        for row in self.data:
            valid_prices = []
            sum = 0
            for price in row[1:]:
                if not (price == " " or price == ""):
                    valid_prices.append(float(price))
                    sum += float(price)
            average = round(sum / len(valid_prices), 3)
            averages.append(average)
        return averages

    def median02(self):
        """pt2
        """
        medians = []
        for row in self.data:
            valid_prices = []
            for price in row[1:]:
                if not (price == " " or price == ""):
                    valid_prices.append(float(price))
            medians.append(stats.median(valid_prices))
        return medians

    def stddev03(self):
        """pt3
        """
        ...
