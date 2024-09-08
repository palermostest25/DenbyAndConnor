import random

def func_called(decorated_func):
    def wrapper(self, *args, **kwargs):
        # Call the method that should run on each method call
        self.__func_called__()
        # Call the original method
        return decorated_func(self, *args, **kwargs)
    return wrapper

class ValParser:
    def __init__(self, value=0):
        self.value = value

class Algorithm:
    def __init__(self, rain_days:list, hectopascals:ValParser, average_hectopascals:ValParser):
        self.rain_days = rain_days
        try:
            self.hectopascals = hectopascals
            self.average_hectopascals = average_hectopascals
        except AttributeError:
            raise TypeError("hectopascals and average_hectopascals must be ValParser instances")

    def __func_called__(self):
        if len(self.rain_days) < 28:
            raise ValueError("rain_days must be at least 28 items long")
        for i in self.rain_days:
            if i != 1 and i != 0:
                raise ValueError(f"all items in rain_days must be either 1 or 0. {i} is not 1 or 0. list:\n{self.rain_days}")
        if len(self.rain_days) % 7 != 0:
            raise ValueError(f"rain_days size must be a multable of 7. {len(self.rain_days)} is not a multable of 7")
        if not isinstance(self.hectopascals, ValParser) or not isinstance(self.average_hectopascals, ValParser):
            raise TypeError("hectopascals and average_hectopascals must be ValParser instances")
        
            
    @func_called
    def calc_pattern_scores(self):
        pattern_scores = []
        for pattern_start in range(0, len(self.rain_days), 7):
            pattern_block = self.rain_days[pattern_start:pattern_start + 7]
            score = 0
            for test_start in range(0, len(self.rain_days), 7):
                test_block = self.rain_days[test_start:test_start + 7]
                for pattern_individual, test_individual in zip(pattern_block, test_block):
                    if pattern_individual == test_individual:
                        score += 1
            pattern_scores.append(score - 7) 
        already_done_pattern_scores = []
        pattern_scores_grouped = []
        for i in pattern_scores:
            if not i in already_done_pattern_scores:
                already_done_pattern_scores.append(i)
                pattern_scores_grouped.append([x for x in pattern_scores if x == i])
        for i in pattern_scores_grouped:
            if len(i) > 1:
                pattern_challengers = []
                for o in [p for p, x in enumerate(pattern_scores) if x == i]:
                    pattern_challengers.append(o) # self.rain_days[(7 * o): (7 * o + 7)] <-- something earlier that i used
                for o in pattern_challengers:
                    pattern_scores_grouped[pattern_scores_grouped.index(i)] = pattern_scores[max(pattern_challengers)]
        return pattern_scores
    
    @func_called
    def calc_pattern_to_use(self, pattern_scores):
        highest_score = max(pattern_scores)
        highest_score_pattern_index = random.choice([i for i, x in enumerate(pattern_scores) if x == highest_score])
        return self.rain_days[(7 * highest_score_pattern_index): (7 * highest_score_pattern_index + 7)]
    
    @func_called
    def calc_rain_forecast(self, pattern):
        num_of_1s = 0
        for i in self.rain_days:
            if i == 1:
                num_of_1s += 1
        seven_day_forecast = [int(f"{round(num_of_1s / len(self.rain_days), 2) * 100}".split(".")[0]) for _ in range(7)]
        for index, value in enumerate(pattern):
            if value == 1:
                seven_day_forecast[index] = round(seven_day_forecast[index] + seven_day_forecast[index] * 0.15)
            elif value == 0:
                seven_day_forecast[index] = round(seven_day_forecast[index] - seven_day_forecast[index] * 0.15)
        seven_day_forecast[0] = round(seven_day_forecast[0] + (seven_day_forecast[0] * (float("0." + f"{round((self.average_hectopascals.value - self.hectopascals.value) / 3)}"))))
        return seven_day_forecast

