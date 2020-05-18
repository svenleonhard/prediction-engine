from machine_learning.model.ml_travel_time_benchmark import MLTravelTimeBenchmark
from machine_learning.prepsocessing.data_map_benchmark import DataMapBenchmark
from machine_learning.prepsocessing.data_map_categories_benchmark import DataMapCategoriesBenchmark

class Benchmark(object):

    def __init__(self, data_map):
        benchmark = []
        if isinstance(data_map, DataMapBenchmark) or isinstance(data_map, DataMapCategoriesBenchmark):
            benchmark = data_map.valid_benchmark
        self.benchmark = benchmark