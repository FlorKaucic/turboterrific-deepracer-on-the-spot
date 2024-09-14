from pprint import pprint

OPTIMAL_LINE_BASE_VALUE = 100
STEPS_REWARD_BASE = 1000

# optimal racing line for 2022_may_pro
racing_line = [
    [-0.51133, -5.39399, 5.0, 0.06018],
    [-0.21084, -5.38896, 5.0, 0.06011],
    [0.08914, -5.38183, 5.0, 0.06001],
    [0.38843, -5.37215, 5.0, 0.05989],
    [0.68687, -5.35942, 5.0, 0.05974],
    [0.98426, -5.34313, 5.0, 0.05957],
    [1.28037, -5.32277, 5.0, 0.05936],
    [1.57495, -5.29782, 5.0, 0.05913],
    [1.86774, -5.26776, 5.0, 0.05887],
    [2.15849, -5.23218, 5.0, 0.05858],
    [2.44701, -5.1908, 5.0, 0.05829],
    [2.73321, -5.14364, 5.0, 0.05801],
    [3.01706, -5.09085, 5.0, 0.05774],
    [3.29835, -5.03217, 5.0, 0.05747],
    [3.57685, -4.96731, 4.67362, 0.06119],
    [3.85233, -4.89599, 4.19237, 0.06787],
    [4.12408, -4.81709, 3.76232, 0.07521],
    [4.39107, -4.72898, 3.44501, 0.08161],
    [4.65189, -4.62977, 3.44501, 0.081],
    [4.90468, -4.51733, 3.44501, 0.08031],
    [5.14715, -4.38998, 3.25357, 0.08418],
    [5.38115, -4.25181, 2.925, 0.09291],
    [5.60457, -4.10133, 2.65449, 0.10148],
    [5.81467, -3.93699, 2.3183, 0.11505],
    [6.00754, -3.75703, 2.04071, 0.12926],
    [6.17862, -3.56023, 1.75588, 0.14851],
    [6.31989, -3.34471, 1.75588, 0.14676],
    [6.42102, -3.11026, 1.75588, 0.14541],
    [6.46535, -2.85859, 2.23847, 0.11416],
    [6.47319, -2.59985, 2.58316, 0.10021],
    [6.45218, -2.3367, 3.01081, 0.08768],
    [6.40863, -2.07063, 3.7046, 0.07278],
    [6.34934, -1.80274, 5.0, 0.05488],
    [6.28189, -1.53395, 5.0, 0.05542],
    [6.21706, -1.24903, 5.0, 0.05844],
    [6.1574, -0.9622, 5.0, 0.05859],
    [6.10202, -0.67402, 5.0, 0.05869],
    [6.0504, -0.3848, 5.0, 0.05876],
    [6.00205, -0.09481, 5.0, 0.0588],
    [5.95654, 0.19576, 5.0, 0.05882],
    [5.91353, 0.4868, 5.0, 0.05884],
    [5.87275, 0.77818, 5.0, 0.05885],
    [5.83393, 1.06986, 5.0, 0.05885],
    [5.79689, 1.36175, 5.0, 0.05885],
    [5.76141, 1.65382, 5.0, 0.05884],
    [5.72755, 1.94606, 5.0, 0.05884],
    [5.69539, 2.23842, 5.0, 0.05883],
    [5.66711, 2.51098, 4.51887, 0.06064],
    [5.63595, 2.78081, 3.80061, 0.07147],
    [5.59915, 3.04541, 3.27483, 0.08158],
    [5.55383, 3.30249, 2.82562, 0.09239],
    [5.49726, 3.55019, 2.47553, 0.10263],
    [5.42667, 3.78672, 2.18259, 0.1131],
    [5.33874, 4.00979, 1.94018, 0.12359],
    [5.22999, 4.2167, 1.94018, 0.12048],
    [5.09644, 4.40358, 1.94018, 0.11839],
    [4.93374, 4.56433, 1.96462, 0.11642],
    [4.74472, 4.69705, 2.16683, 0.10659],
    [4.53536, 4.80415, 2.40649, 0.09772],
    [4.31015, 4.8883, 2.64719, 0.09082],
    [4.07212, 4.95167, 2.96092, 0.08319],
    [3.824, 4.99692, 3.31405, 0.0761],
    [3.56788, 5.02658, 3.76753, 0.06844],
    [3.30558, 5.04334, 4.45163, 0.05904],
    [3.03886, 5.05037, 5.0, 0.05336],
    [2.76941, 5.05108, 5.0, 0.05389],
    [2.4856, 5.04809, 5.0, 0.05677],
    [2.20182, 5.04808, 5.0, 0.05675],
    [1.91808, 5.05032, 5.0, 0.05675],
    [1.63435, 5.05423, 5.0, 0.05675],
    [1.35064, 5.05925, 5.0, 0.05675],
    [1.06694, 5.06491, 5.0, 0.05675],
    [0.78858, 5.06923, 4.6056, 0.06045],
    [0.51129, 5.0696, 3.84062, 0.0722],
    [0.23578, 5.06299, 3.32538, 0.08288],
    [-0.0374, 5.0465, 2.77473, 0.09863],
    [-0.3075, 5.01608, 2.77473, 0.09796],
    [-0.5736, 4.9674, 2.77473, 0.09749],
    [-0.83364, 4.89276, 2.98641, 0.09059],
    [-1.08789, 4.79564, 3.35262, 0.08118],
    [-1.33715, 4.68038, 3.83841, 0.07154],
    [-1.58234, 4.55097, 4.53272, 0.06116],
    [-1.82444, 4.41117, 5.0, 0.05591],
    [-2.06453, 4.26473, 5.0, 0.05625],
    [-2.30368, 4.11518, 5.0, 0.05641],
    [-2.54907, 3.96327, 5.0, 0.05772],
    [-2.79518, 3.81235, 5.0, 0.05774],
    [-3.04199, 3.6624, 5.0, 0.05776],
    [-3.28949, 3.51346, 5.0, 0.05777],
    [-3.53767, 3.36554, 5.0, 0.05778],
    [-3.78653, 3.21867, 5.0, 0.05779],
    [-4.03608, 3.07293, 5.0, 0.0578],
    [-4.28639, 2.92844, 5.0, 0.0578],
    [-4.53749, 2.78536, 5.0, 0.0578],
    [-4.78948, 2.64397, 4.3607, 0.06626],
    [-5.03159, 2.51066, 3.45349, 0.08003],
    [-5.26911, 2.37359, 2.91234, 0.09416],
    [-5.49759, 2.22921, 2.49829, 0.10818],
    [-5.71211, 2.07396, 2.18206, 0.12136],
    [-5.90755, 1.90495, 2.18206, 0.11841],
    [-6.07748, 1.72006, 2.18206, 0.11508],
    [-6.21423, 1.51913, 2.19518, 0.11072],
    [-6.32407, 1.30849, 2.05649, 0.11552],
    [-6.40585, 1.09028, 1.84972, 0.12598],
    [-6.45679, 0.86666, 1.65116, 0.13891],
    [-6.47323, 0.64046, 1.47933, 0.15331],
    [-6.44774, 0.41622, 1.47933, 0.15256],
    [-6.37063, 0.2027, 1.47933, 0.15346],
    [-6.23186, 0.01696, 1.69429, 0.13684],
    [-6.04931, -0.13645, 1.88457, 0.12653],
    [-5.83368, -0.25623, 2.09451, 0.11776],
    [-5.59389, -0.34282, 2.32078, 0.10986],
    [-5.33774, -0.39791, 2.56071, 0.10232],
    [-5.07177, -0.42421, 2.8543, 0.09364],
    [-4.8009, -0.42582, 3.09745, 0.08745],
    [-4.52815, -0.40569, 3.34481, 0.08177],
    [-4.25551, -0.36658, 3.60136, 0.07648],
    [-3.98424, -0.31097, 3.86379, 0.07167],
    [-3.71507, -0.24099, 4.11183, 0.06764],
    [-3.44846, -0.15835, 4.33525, 0.06438],
    [-3.1847, -0.06437, 4.55294, 0.0615],
    [-2.92395, 0.03985, 4.79843, 0.05852],
    [-2.66626, 0.15323, 5.0, 0.05631],
    [-2.41156, 0.27477, 5.0, 0.05644],
    [-2.16005, 0.40422, 5.0, 0.05657],
    [-1.91149, 0.54047, 5.0, 0.05669],
    [-1.66571, 0.68271, 5.0, 0.05679],
    [-1.42265, 0.83041, 5.0, 0.05688],
    [-1.18223, 0.98313, 5.0, 0.05696],
    [-0.94485, 1.1412, 4.95596, 0.05755],
    [-0.71101, 1.30502, 3.94717, 0.07233],
    [-0.48173, 1.47533, 2.74953, 0.10388],
    [-0.27491, 1.63926, 2.22329, 0.1187],
    [-0.06481, 1.79027, 1.86217, 0.13894],
    [0.15125, 1.9165, 1.70293, 0.14694],
    [0.37474, 2.00814, 1.70293, 0.14184],
    [0.60592, 2.054, 1.70293, 0.1384],
    [0.84191, 2.04625, 1.89425, 0.12465],
    [1.07757, 1.99362, 2.07225, 0.11653],
    [1.30869, 1.9013, 2.26087, 0.11008],
    [1.53105, 1.77439, 2.44812, 0.10458],
    [1.7408, 1.61828, 2.64113, 0.099],
    [1.93532, 1.43864, 2.80125, 0.09452],
    [2.11309, 1.24006, 2.90671, 0.09169],
    [2.27368, 1.02639, 2.73737, 0.09765],
    [2.41649, 0.80015, 2.73737, 0.09774],
    [2.53859, 0.56232, 2.73737, 0.09766],
    [2.63598, 0.31447, 2.86629, 0.09291],
    [2.71006, 0.06042, 2.92877, 0.09035],
    [2.76185, -0.19708, 2.88598, 0.09101],
    [2.79168, -0.45596, 2.75758, 0.0945],
    [2.79939, -0.71429, 2.59733, 0.0995],
    [2.78483, -0.9701, 2.4279, 0.10554],
    [2.74665, -1.2211, 2.27848, 0.11143],
    [2.68298, -1.46435, 2.03988, 0.12327],
    [2.59167, -1.69618, 1.7904, 0.13917],
    [2.47089, -1.91236, 1.7904, 0.13831],
    [2.31575, -2.10554, 1.7904, 0.13838],
    [2.11945, -2.26276, 2.2641, 0.11108],
    [1.89889, -2.39384, 2.48151, 0.10339],
    [1.65838, -2.50061, 2.77235, 0.09492],
    [1.4019, -2.58573, 3.09054, 0.08744],
    [1.13259, -2.65164, 3.43879, 0.08063],
    [0.85303, -2.70064, 3.92963, 0.07222],
    [0.56584, -2.73568, 4.5358, 0.06379],
    [0.27312, -2.75965, 5.0, 0.05874],
    [-0.02341, -2.77523, 5.0, 0.05939],
    [-0.32246, -2.7848, 5.0, 0.05984],
    [-0.62303, -2.79044, 5.0, 0.06013],
    [-0.92437, -2.79398, 5.0, 0.06027],
    [-1.2259, -2.79699, 5.0, 0.06031],
    [-1.52742, -2.8, 5.0, 0.06031],
    [-1.82895, -2.80302, 5.0, 0.06031],
    [-2.13047, -2.80604, 5.0, 0.06031],
    [-2.432, -2.80906, 5.0, 0.06031],
    [-2.73349, -2.81214, 5.0, 0.0603],
    [-3.03419, -2.81712, 5.0, 0.06015],
    [-3.33314, -2.82599, 4.78163, 0.06255],
    [-3.62933, -2.84068, 4.23244, 0.07007],
    [-3.92149, -2.86323, 3.79088, 0.0773],
    [-4.20816, -2.89566, 3.40658, 0.08469],
    [-4.48763, -2.94002, 3.06066, 0.09245],
    [-4.75792, -2.99821, 2.74887, 0.10058],
    [-5.01672, -3.07205, 2.48771, 0.10818],
    [-5.26122, -3.16334, 2.20274, 0.11848],
    [-5.48806, -3.27365, 1.92868, 0.13078],
    [-5.69355, -3.4039, 1.69859, 0.14323],
    [-5.87219, -3.55531, 1.59053, 0.14723],
    [-6.01625, -3.72832, 1.59053, 0.14155],
    [-6.11624, -3.9208, 1.59053, 0.13637],
    [-6.16666, -4.1256, 1.54078, 0.13689],
    [-6.17602, -4.33397, 1.4, 0.14899],
    [-6.1408, -4.54018, 1.4, 0.14943],
    [-6.05356, -4.73561, 1.4, 0.15287],
    [-5.90245, -4.90264, 1.82815, 0.12321],
    [-5.71371, -5.04367, 2.04262, 0.11535],
    [-5.49392, -5.15784, 2.31907, 0.1068],
    [-5.24945, -5.24616, 2.65375, 0.09795],
    [-4.98592, -5.31087, 3.05321, 0.08888],
    [-4.70814, -5.35503, 3.58542, 0.07845],
    [-4.42029, -5.38258, 4.20698, 0.06873],
    [-4.12547, -5.39707, 5.0, 0.05903],
    [-3.82644, -5.40268, 5.0, 0.05982],
    [-3.52537, -5.40347, 5.0, 0.06021],
    [-3.22383, -5.40316, 5.0, 0.06031],
    [-2.92229, -5.40289, 5.0, 0.06031],
    [-2.62075, -5.40261, 5.0, 0.06031],
    [-2.31922, -5.40233, 5.0, 0.06031],
    [-2.01768, -5.40204, 5.0, 0.06031],
    [-1.71617, -5.40156, 5.0, 0.0603],
    [-1.41473, -5.40076, 5.0, 0.06029],
    [-1.11339, -5.39948, 5.0, 0.06027],
    [-0.81223, -5.39733, 5.0, 0.06023],
    [-0.51133, -5.39399, 5.0, 0.06018],
]


def dist_2_points(x1, x2, y1, y2):
    return abs(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5


def closest_2_racing_points_index(racing_coords, car_coords):
    # Calculate all distances to racing points
    distances = []
    for i in range(len(racing_coords)):
        distance = dist_2_points(
            x1=racing_coords[i][0],
            x2=car_coords[0],
            y1=racing_coords[i][1],
            y2=car_coords[1],
        )
        distances.append(distance)

    # Get index of the closest racing point
    closest_index = distances.index(min(distances))

    # Get index of the second closest racing point
    distances_no_closest = distances.copy()
    distances_no_closest[closest_index] = 999
    second_closest_index = distances_no_closest.index(min(distances_no_closest))

    return [closest_index, second_closest_index]


def dist_to_racing_line(closest_coords, second_closest_coords, car_coords):
    # Calculate the distances between 2 closest racing points
    a = abs(
        dist_2_points(
            x1=closest_coords[0],
            x2=second_closest_coords[0],
            y1=closest_coords[1],
            y2=second_closest_coords[1],
        )
    )

    # Distances between car and closest and second closest racing point
    b = abs(
        dist_2_points(
            x1=car_coords[0],
            x2=closest_coords[0],
            y1=car_coords[1],
            y2=closest_coords[1],
        )
    )
    c = abs(
        dist_2_points(
            x1=car_coords[0],
            x2=second_closest_coords[0],
            y1=car_coords[1],
            y2=second_closest_coords[1],
        )
    )

    # Calculate distance between car and racing line (goes through 2 closest racing points)
    # try-except in case a=0 (rare bug in DeepRacer)
    try:
        distance = abs(
            -(a ** 4)
            + 2 * (a ** 2) * (b ** 2)
            + 2 * (a ** 2) * (c ** 2)
            - (b ** 4)
            + 2 * (b ** 2) * (c ** 2)
            - (c ** 4)
        ) ** 0.5 / (2 * a)
    except:
        distance = b

    return distance


class StraightPath:
    def __init__(self, first_point, last_point):
        self.first_point = first_point
        self.last_point = last_point

    def is_current_path(self, prev_point, next_point):
        if not self.first_point:
            return next_point <= self.last_point

        if not self.last_point:
            return prev_point >= self.first_point

        return prev_point >= self.first_point and next_point <= self.last_point


STRAIGHT_PATHS = [
    StraightPath(198, None),
    StraightPath(None, 11),
    StraightPath(34, 50),
    StraightPath(80, 94),
    StraightPath(115, 130),
    StraightPath(162, 182),
]


def is_current_path_straight(prev_point, next_point):
    return any([path.is_current_path(prev_point, next_point) for path in STRAIGHT_PATHS])


class RewardCalculator:
    def __init__(self):
        self.accumulated_reward = 0
        self.prev_progress = 0

    def calculate_reward(self, params):
        # Read input parameters
        x, y = params["x"], params["y"]
        track_width = params["track_width"]
        speed = params["speed"]
        progress = params["progress"]
        steps = params["steps"]
        prev_point, next_point = params['closest_waypoints'][0], params['closest_waypoints'][1]

        # Get closest indexes for racing line (and distances to all points on racing line)
        closest_index, second_closest_index = closest_2_racing_points_index(
            racing_line, [x, y]
        )

        # Get optimal [x, y] for closest and second closest index
        optimals = racing_line[closest_index]
        optimals_second = racing_line[second_closest_index]

        # Calculate distance to optimal racing line to use this one for rewards
        # (instead of distance to track center)
        distance_to_racing_line = dist_to_racing_line(
            optimals[0:2], optimals_second[0:2], [x, y]
        )

        # REWARD LOGIC:
        # affecting reward based on distance from the optimal line
        distance_penalty_factor = max((track_width - distance_to_racing_line) / track_width, 1e-3)
        optimal_line_reward = OPTIMAL_LINE_BASE_VALUE * distance_penalty_factor

        steps_reward = (progress / steps) * STEPS_REWARD_BASE

        speed_reward = speed ** 2

        combined_reward = optimal_line_reward + steps_reward + speed_reward

        isBug = (progress == 100 and self.prev_progress < 95)
        reward = self.accumulated_reward * -1 if isBug else combined_reward

        if progress == 100:
            self.accumulated_reward = 0

        reward = float(reward)

        self.prev_progress = progress
        self.accumulated_reward += reward

        pprint(dict(
            # calculated
            calculated_distance=distance_to_racing_line,
            calculated_is_bug=isBug,
            calculated_optimals=optimals,
            # factors
            combined_reward=combined_reward,
            factor_distance_penalty=distance_penalty_factor,
            factor_optimal_line_reward=optimal_line_reward,
            factor_speed_reward=speed_reward,
            factor_steps_reward=steps_reward,
            # given
            given_coordinates=[x, y],
            given_steps=steps,
            given_track_width=track_width,
            # status
            status_accumulated_reward=self.accumulated_reward,
        ))
        return reward


calculator = RewardCalculator()


def reward_function(params):
    # Read input parameters
    return calculator.calculate_reward(params)


def another_reward_test(params):
    if params["steps"] > 0:
        reward = ((params["progress"] / params["steps"]) * 100) + (params["speed"] ** 2)
    else:
        reward = 0.01

    return float(reward)


def test2():
    params_baseline = dict(
        speed=5,
        progress=5,
        steps=10,
    )

    params_less_speed = dict(
        speed=4.5,
        progress=5,
        steps=10,
    )

    params_less_progress = dict(
        speed=5,
        progress=3,
        steps=10,
    )

    params_more_steps = dict(
        speed=5,
        progress=5,
        steps=12,
    )

    params_more_speed = dict(
        speed=5.5,
        progress=5,
        steps=10,
    )

    params_more_progress = dict(
        speed=5,
        progress=7,
        steps=10,
    )

    params_less_steps = dict(
        speed=5,
        progress=5,
        steps=8,
    )

    baseline = another_reward_test(params_baseline)
    less_speed = another_reward_test(params_less_speed)
    less_progress = another_reward_test(params_less_progress)
    more_steps = another_reward_test(params_more_steps)
    more_speed = another_reward_test(params_more_speed)
    more_progress = another_reward_test(params_more_progress)
    less_steps = another_reward_test(params_less_steps)

    print("baseline", baseline)
    print("less_speed", less_speed)
    print("less_progress", less_progress)
    print("more_steps", more_steps)
    print("more_speed", more_speed)
    print("more_progress", more_progress)
    print("less_steps", less_steps)

    assert (baseline > less_speed)
    assert (baseline > less_progress)
    assert (baseline > more_steps)
    assert (baseline < more_speed)
    assert (baseline < more_progress)
    assert (baseline < less_steps)

    params_baseline = dict(
        speed=5,
        progress=95,
        steps=200,
    )

    params_less_speed = dict(
        speed=4.5,
        progress=95,
        steps=200,
    )
    params_less_progress = dict(
        speed=5,
        progress=93,
        steps=200,
    )

    params_more_steps = dict(
        speed=5,
        progress=95,
        steps=205,
    )

    params_more_speed = dict(
        speed=5.5,
        progress=95,
        steps=200,
    )

    params_more_progress = dict(
        speed=5,
        progress=97,
        steps=200,
    )

    params_less_steps = dict(
        speed=5,
        progress=95,
        steps=195,
    )

    baseline = another_reward_test(params_baseline)
    less_speed = another_reward_test(params_less_speed)
    less_progress = another_reward_test(params_less_progress)
    more_steps = another_reward_test(params_more_steps)
    more_speed = another_reward_test(params_more_speed)
    more_progress = another_reward_test(params_more_progress)
    less_steps = another_reward_test(params_less_steps)

    print("baseline", baseline)
    print("less_speed", less_speed)
    print("less_progress", less_progress)
    print("more_steps", more_steps)
    print("more_speed", more_speed)
    print("more_progress", more_progress)
    print("less_steps", less_steps)

    assert (baseline > less_speed)
    assert (baseline > less_progress)
    assert (baseline > more_steps)
    assert (baseline < more_speed)
    assert (baseline < more_progress)
    assert (baseline < less_steps)


def test():
    """
    To run tests:
    import importlib
    mod = importlib.import_module("custom-files.reward_function")
    mod.test()
    """
    # BASELINE
    params_baseline = dict(
        x=0.5,
        y=0.5,
        track_width=2,
        speed=5.0,
        progress=2,
        steps=4,
        closest_waypoints=[1, 2],
    )

    # BASED ON DISTANCE
    params_further_away = dict(
        x=0.45,
        y=0.48,
        track_width=2,
        speed=5.0,
        progress=2,
        steps=4,
        closest_waypoints=[1, 2],
    )

    params_closer_to_raceline = dict(
        x=0.5,
        y=0.55,
        track_width=2,
        speed=5.0,
        progress=2,
        steps=4,
        closest_waypoints=[1, 2],
    )

    reward_baseline = reward_function(params_baseline)

    reward_further_away = reward_function(params_further_away)
    reward_closer_to_raceline = reward_function(params_closer_to_raceline)

    assert (reward_further_away <= reward_baseline <= reward_closer_to_raceline)

    # BASED ON DISTANCE
    params_speed_slower = dict(
        x=0.5,
        y=0.5,
        track_width=2,
        speed=3.0,
        progress=2,
        steps=4,
        closest_waypoints=[1, 2],
    )

    params_speed_faster = dict(
        x=0.5,
        y=0.5,
        track_width=2,
        speed=5.5,
        progress=2,
        steps=4,
        closest_waypoints=[1, 2],
    )

    reward_speed_slower = reward_function(params_speed_slower)
    reward_speed_faster = reward_function(params_speed_faster)

    assert (reward_speed_slower <= reward_baseline <= reward_speed_faster)

    # BASED ON STEPS
    params_steps_slower = dict(
        x=0.5,
        y=0.5,
        track_width=2,
        speed=5.0,
        progress=2,
        steps=5,
        closest_waypoints=[1, 2],
    )

    params_steps_faster = dict(
        x=0.5,
        y=0.5,
        track_width=2,
        speed=5.0,
        progress=2,
        steps=3,
        closest_waypoints=[1, 2],
    )

    reward_steps_slower = reward_function(params_steps_slower)
    reward_steps_faster = reward_function(params_steps_faster)

    assert (reward_steps_slower <= reward_baseline <= reward_steps_faster)

    # OUT OF BOUNDS?
    # BASED ON DISTANCE
    params_distance_upper = dict(
        x=5,
        y=5,
        track_width=2,
        speed=5.0,
        progress=2,
        steps=4,
        closest_waypoints=[1, 2],
    )

    params_distance_lower = dict(
        x=-5,
        y=-5,
        track_width=2,
        speed=5.0,
        progress=2,
        steps=4,
        closest_waypoints=[1, 2],
    )

    reward_distance_upper = reward_function(params_distance_upper)
    reward_distance_lower = reward_function(params_distance_lower)

    assert (reward_distance_upper < reward_further_away)
    assert (reward_distance_lower < reward_further_away)

    # BASED ON SPEED
    params_speed_extreme = dict(
        x=0.5,
        y=0.5,
        track_width=2,
        speed=15.0,
        progress=2,
        steps=4,
        closest_waypoints=[1, 2],
    )

    reward_speed_extreme = reward_function(params_speed_extreme)

    assert (reward_speed_extreme > reward_speed_faster)

    params_speed_stopped = dict(
        x=0.5,
        y=0.5,
        track_width=2,
        speed=0.0,
        progress=2,
        steps=4,
        closest_waypoints=[1, 2],
    )

    reward_speed_stopped = reward_function(params_speed_stopped)

    assert (reward_speed_stopped < reward_speed_slower)

    # BASED ON STEPS
    params_steps_extreme = dict(
        x=0.5,
        y=0.5,
        track_width=2,
        speed=5.0,
        progress=2,
        steps=50,
        closest_waypoints=[1, 2],
    )
    reward_steps_extreme = reward_function(params_steps_extreme)

    assert (reward_steps_extreme < reward_steps_slower)

    # BASED ON PROGRESS
    params_big_progress = dict(
        x=0.5,
        y=0.5,
        track_width=2,
        speed=5.0,
        progress=98,
        steps=4,
        closest_waypoints=[1, 2],
    )

    reward_big_progress = reward_function(params_big_progress)
    assert (reward_big_progress > reward_baseline)

    # assert none is 0
    assert (reward_baseline != 0)
    assert (params_further_away != 0)
    assert (params_closer_to_raceline != 0)
    assert (reward_speed_slower != 0)
    assert (reward_speed_faster != 0)
    assert (reward_steps_slower != 0)
    assert (reward_steps_faster != 0)
    assert (reward_distance_upper != 0)
    assert (reward_distance_lower != 0)
    assert (reward_speed_extreme != 0)
    assert (reward_speed_stopped != 0)
    assert (reward_steps_extreme != 0)
    assert (reward_big_progress != 0)

    print("All done!")


if __name__ == '__main__':
    test()
    test2()
    print("All tests ran.")
