
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
        """
        Calculates the average of stock prices and returns a list.

        The function converts strings to floats and ignores empty and white 
        space strings, to create a list of valid numerics. It calculates 
        the sum for the row, divides by the length of the list of numerics, 
        and rounds the result to the third decimal place. It appends this 
        value to the averages list.
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
        """
        Calculates the median of stock prices and returns a list.
        
        The function converts strings to floats and ignores empty and white 
        space strings, to create a list of valid numerics. It utilizes the 
        median function in the statistics module to calculate the median for 
        the row. It does not round the result and appends this value to the 
        median list.
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
        """
        Calculates the standard deviation of stock prices and returns a list.
        
        The function converts strings to floats and ignores empty and white 
        space strings, to create a list of valid numerics. It utilizes the 
        stdev function in the statistics module to calculate the standard 
        deviation for the row. It does not round the result and appends this 
        value to the std_devs list.
        """
        std_devs = []
        for row in self.data:
            valid_prices = []
            for price in row[1:]:
                if not (price == " " or price == ""):
                    valid_prices.append(float(price))
            std_devs.append(round(stats.stdev(valid_prices), 3))
        return std_devs
