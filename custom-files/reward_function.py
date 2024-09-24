from pprint import pprint

OPTIMAL_LINE_BASE_VALUE = 100
STEPS_REWARD_BASE = 1000
STRAIGHT_PATH_SPEED_REWARD_BASE = 150
STEERING_ANGLE_REWARD_BASE = 150

OPTIMAL_LINE_WEIGHT = 1
STEPS_WEIGHT = 1
SPEED_WEIGHT = 1
SPEED_ON_STRAIGHT_PATH_WEIGHT = 2
STEERING_ANGLE_WEIGHT = 1

MIN_SPEED_ON_STRAIGHT_PATHS = 4.0
TOP_SPEED = 5.0
HIGHEST_STEERING_ANGLE = 30

# optimal racing line for 2022_may_pro
racing_line = [
    [-0.19668, -5.38338, 5.0, 0.05252],
    [-0.45997, -5.3878, 5.0, 0.05267],
    [-0.72478, -5.39126, 5.0, 0.05297],
    [-0.99164, -5.39399, 5.0, 0.05338],
    [-1.26109, -5.39612, 5.0, 0.05389],
    [-1.5323, -5.39797, 5.0, 0.05424],
    [-1.80569, -5.39958, 5.0, 0.05468],
    [-2.08183, -5.40095, 5.0, 0.05523],
    [-2.36136, -5.40209, 5.0, 0.05591],
    [-2.64349, -5.4031, 5.0, 0.05643],
    [-2.93011, -5.40388, 5.0, 0.05732],
    [-3.22219, -5.40444, 5.0, 0.05842],
    [-3.52371, -5.40475, 5.0, 0.0603],
    [-3.82523, -5.40512, 4.06498, 0.07418],
    [-4.1249, -5.40147, 3.44092, 0.0871],
    [-4.42006, -5.38893, 2.99315, 0.0987],
    [-4.70782, -5.36302, 2.55758, 0.11297],
    [-4.98506, -5.31993, 2.23671, 0.12544],
    [-5.24833, -5.25647, 1.97265, 0.13728],
    [-5.49259, -5.16867, 1.74435, 0.1488],
    [-5.71233, -5.05402, 1.40979, 0.1758],
    [-5.90103, -4.91127, 1.40979, 0.16784],
    [-6.05035, -4.7407, 1.40979, 0.1608],
    [-6.13856, -4.54291, 1.52631, 0.14189],
    [-6.17498, -4.33455, 1.5859, 0.13337],
    [-6.16515, -4.12459, 1.5859, 0.13254],
    [-6.11324, -3.91927, 1.5859, 0.13354],
    [-6.014, -3.72679, 1.76445, 0.12273],
    [-5.87623, -3.55121, 1.93086, 0.11558],
    [-5.70559, -3.39472, 2.11397, 0.10952],
    [-5.5067, -3.25851, 2.29304, 0.10513],
    [-5.28316, -3.14351, 2.51039, 0.10014],
    [-5.0387, -3.04978, 2.79107, 0.0938],
    [-4.77737, -2.97619, 3.15243, 0.08612],
    [-4.50311, -2.92053, 3.58897, 0.07797],
    [-4.21931, -2.88014, 4.13966, 0.06925],
    [-3.92871, -2.85209, 4.81601, 0.06062],
    [-3.63343, -2.83368, 5.0, 0.05917],
    [-3.33495, -2.8226, 5.0, 0.05974],
    [-3.03458, -2.81638, 5.0, 0.06009],
    [-2.73329, -2.81274, 5.0, 0.06026],
    [-2.43178, -2.80973, 5.0, 0.0603],
    [-2.13028, -2.80671, 5.0, 0.0603],
    [-1.82877, -2.80369, 5.0, 0.0603],
    [-1.52727, -2.80067, 5.0, 0.0603],
    [-1.22577, -2.79765, 5.0, 0.0603],
    [-0.92426, -2.79464, 5.0, 0.0603],
    [-0.62276, -2.79161, 5.0, 0.0603],
    [-0.32186, -2.78711, 4.97177, 0.06053],
    [-0.02262, -2.77866, 4.29331, 0.06973],
    [0.27376, -2.76377, 3.79769, 0.07814],
    [0.56579, -2.73973, 3.3964, 0.08627],
    [0.85179, -2.70399, 3.06575, 0.09401],
    [1.12993, -2.65416, 2.76704, 0.10212],
    [1.39813, -2.58792, 2.42079, 0.11412],
    [1.65411, -2.50313, 2.15534, 0.12511],
    [1.89508, -2.39755, 1.87492, 0.14032],
    [2.11637, -2.26737, 1.87492, 0.13694],
    [2.31239, -2.10939, 1.87492, 0.13427],
    [2.47312, -1.91918, 2.0167, 0.12348],
    [2.60078, -1.70495, 2.16121, 0.11539],
    [2.69723, -1.47288, 2.32989, 0.10787],
    [2.76475, -1.22824, 2.46139, 0.1031],
    [2.80472, -0.97508, 2.58535, 0.09914],
    [2.81854, -0.71683, 2.70678, 0.09555],
    [2.80775, -0.45641, 2.81445, 0.09261],
    [2.7738, -0.19625, 2.78177, 0.09431],
    [2.71744, 0.06147, 2.60832, 0.10114],
    [2.63958, 0.31476, 2.60832, 0.10159],
    [2.53846, 0.56071, 2.60832, 0.10195],
    [2.41213, 0.79488, 2.88657, 0.09218],
    [2.26679, 1.017, 2.82155, 0.09408],
    [2.10441, 1.22556, 2.7021, 0.09782],
    [1.92622, 1.41833, 2.50323, 0.10487],
    [1.73373, 1.59297, 2.33181, 0.11146],
    [1.52843, 1.74653, 2.08135, 0.12318],
    [1.3117, 1.87457, 1.86846, 0.13472],
    [1.08586, 1.97299, 1.63574, 0.15061],
    [0.8534, 2.03495, 1.63574, 0.14708],
    [0.61805, 2.05323, 1.63574, 0.14431],
    [0.3853, 2.01592, 1.72682, 0.13651],
    [0.15996, 1.92756, 2.02533, 0.11951],
    [-0.05666, 1.79918, 2.52575, 0.09969],
    [-0.2658, 1.6426, 3.67301, 0.07113],
    [-0.47081, 1.47166, 4.51476, 0.05912],
    [-0.69733, 1.29632, 4.74933, 0.06032],
    [-0.92948, 1.12892, 5.0, 0.05724],
    [-1.16615, 0.96902, 5.0, 0.05712],
    [-1.40667, 0.81631, 5.0, 0.05698],
    [-1.65068, 0.67079, 4.9048, 0.05792],
    [-1.89787, 0.53243, 4.57265, 0.06195],
    [-2.14816, 0.40173, 4.51408, 0.06255],
    [-2.40152, 0.27937, 4.51408, 0.06233],
    [-2.65806, 0.16665, 4.51408, 0.06207],
    [-2.91746, 0.06387, 4.47863, 0.0623],
    [-3.17928, -0.02927, 4.33799, 0.06406],
    [-3.44319, -0.11276, 4.14672, 0.06675],
    [-3.70888, -0.18617, 3.88376, 0.07097],
    [-3.97601, -0.24885, 3.58661, 0.0765],
    [-4.24417, -0.29982, 3.27769, 0.08328],
    [-4.51275, -0.33756, 2.96138, 0.09159],
    [-4.7809, -0.35997, 2.64233, 0.10183],
    [-5.04721, -0.36441, 2.35663, 0.11302],
    [-5.30954, -0.34758, 2.05242, 0.12808],
    [-5.56448, -0.30538, 1.80789, 0.14293],
    [-5.80705, -0.23371, 1.60024, 0.15806],
    [-6.02934, -0.12741, 1.4, 0.176],
    [-6.22076, 0.01671, 1.4, 0.17115],
    [-6.36743, 0.19907, 1.4, 0.16716],
    [-6.44818, 0.41385, 1.65979, 0.13824],
    [-6.4793, 0.63937, 1.79582, 0.12677],
    [-6.46738, 0.86724, 1.9138, 0.11923],
    [-6.41711, 1.09209, 2.04961, 0.11241],
    [-6.33297, 1.31032, 2.19542, 0.10654],
    [-6.21886, 1.5196, 2.22914, 0.10694],
    [-6.07778, 1.71833, 2.22914, 0.10933],
    [-5.9065, 1.90193, 2.49825, 0.10051],
    [-5.71079, 2.07045, 2.84735, 0.0907],
    [-5.4959, 2.22532, 3.33438, 0.07944],
    [-5.26673, 2.36902, 4.11576, 0.06572],
    [-5.02797, 2.50478, 5.0, 0.05493],
    [-4.78438, 2.63642, 5.0, 0.05538],
    [-4.53202, 2.77652, 5.0, 0.05773],
    [-4.28081, 2.91917, 5.0, 0.05778],
    [-4.0306, 3.06401, 5.0, 0.05782],
    [-3.78129, 3.21079, 5.0, 0.05786],
    [-3.53277, 3.35926, 5.0, 0.0579],
    [-3.28498, 3.50928, 5.0, 0.05793],
    [-3.03787, 3.66073, 5.0, 0.05797],
    [-2.79141, 3.81355, 5.0, 0.058],
    [-2.54562, 3.96777, 5.0, 0.05803],
    [-2.30712, 4.11952, 5.0, 0.05654],
    [-2.06799, 4.26909, 4.53815, 0.06215],
    [-1.82752, 4.4141, 3.88178, 0.07234],
    [-1.58498, 4.55197, 3.38381, 0.08245],
    [-1.3396, 4.67996, 2.94686, 0.09392],
    [-1.09047, 4.79478, 2.65224, 0.10343],
    [-0.83665, 4.89264, 2.65224, 0.10257],
    [-0.57703, 4.96853, 2.65224, 0.10198],
    [-0.31082, 5.01736, 3.31598, 0.08162],
    [-0.04065, 5.04867, 3.78313, 0.07189],
    [0.23262, 5.06628, 4.35859, 0.06283],
    [0.50845, 5.07334, 5.0, 0.05518],
    [0.78637, 5.07292, 5.0, 0.05558],
    [1.06574, 5.06805, 5.0, 0.05588],
    [1.34901, 5.06525, 5.0, 0.05666],
    [1.63229, 5.06415, 5.0, 0.05666],
    [1.91557, 5.06429, 5.0, 0.05666],
    [2.19886, 5.06535, 5.0, 0.05666],
    [2.48215, 5.06702, 5.0, 0.05666],
    [2.75795, 5.06666, 4.48024, 0.06156],
    [3.03093, 5.06214, 3.85658, 0.07079],
    [3.30007, 5.05086, 3.3799, 0.0797],
    [3.5647, 5.03029, 3.00385, 0.08836],
    [3.82399, 4.99773, 2.61514, 0.09993],
    [4.07675, 4.95025, 2.31019, 0.11132],
    [4.32126, 4.88485, 2.08187, 0.12158],
    [4.5546, 4.79711, 1.86948, 0.13335],
    [4.77277, 4.68239, 1.86948, 0.13185],
    [4.97045, 4.53638, 1.86948, 0.13146],
    [5.13887, 4.35384, 1.94767, 0.12752],
    [5.27552, 4.13957, 2.27414, 0.11175],
    [5.38528, 3.90298, 2.5928, 0.10059],
    [5.47184, 3.64954, 2.95165, 0.09074],
    [5.53865, 3.3832, 3.38267, 0.08117],
    [5.58913, 3.10714, 4.01409, 0.06991],
    [5.62723, 2.8242, 5.0, 0.0571],
    [5.65712, 2.53692, 5.0, 0.05777],
    [5.68233, 2.24642, 5.0, 0.05832],
    [5.71226, 1.95247, 5.0, 0.05909],
    [5.74597, 1.65878, 5.0, 0.05912],
    [5.78293, 1.36571, 5.0, 0.05908],
    [5.82274, 1.07328, 5.0, 0.05902],
    [5.86513, 0.7815, 5.0, 0.05897],
    [5.90991, 0.49034, 5.0, 0.05892],
    [5.95689, 0.19981, 5.0, 0.05886],
    [6.00599, -0.09011, 5.0, 0.05881],
    [6.05726, -0.37936, 5.0, 0.05875],
    [6.1108, -0.66787, 5.0, 0.05869],
    [6.16684, -0.95552, 5.0, 0.05861],
    [6.22576, -1.24209, 5.0, 0.05851],
    [6.28809, -1.52722, 3.86981, 0.07542],
    [6.35106, -1.79549, 3.05349, 0.09024],
    [6.4071, -2.06285, 2.58031, 0.10587],
    [6.44946, -2.3284, 2.22073, 0.12109],
    [6.47098, -2.59111, 1.83229, 0.14386],
    [6.46496, -2.84973, 1.83229, 0.14118],
    [6.42349, -3.10203, 1.83229, 0.13954],
    [6.33149, -3.34115, 2.04761, 0.12512],
    [6.20004, -3.56451, 2.2655, 0.1144],
    [6.03737, -3.77064, 2.48795, 0.10554],
    [5.85, -3.95916, 2.70992, 0.09808],
    [5.64294, -4.13042, 2.97636, 0.09028],
    [5.42047, -4.28572, 3.1985, 0.08483],
    [5.18538, -4.42605, 3.42804, 0.07987],
    [4.93993, -4.55244, 3.66608, 0.07531],
    [4.68594, -4.66597, 3.90763, 0.07119],
    [4.42494, -4.76762, 4.14379, 0.0676],
    [4.15817, -4.85829, 4.37757, 0.06436],
    [3.88676, -4.93875, 4.61653, 0.06132],
    [3.61173, -5.00973, 4.86726, 0.05836],
    [3.3341, -5.07195, 5.0, 0.0569],
    [3.05485, -5.12611, 5.0, 0.05689],
    [2.77494, -5.17293, 5.0, 0.05676],
    [2.49529, -5.21308, 5.0, 0.0565],
    [2.2167, -5.24727, 5.0, 0.05614],
    [1.93985, -5.27615, 5.0, 0.05567],
    [1.66524, -5.30037, 5.0, 0.05513],
    [1.39317, -5.32052, 5.0, 0.05456],
    [1.12372, -5.33714, 5.0, 0.05399],
    [0.85672, -5.35075, 5.0, 0.05347],
    [0.5918, -5.3618, 5.0, 0.05303],
    [0.32843, -5.37064, 5.0, 0.0527],
    [0.06585, -5.37772, 5.0, 0.05253],
    [-0.19668, -5.38338, 5.0, 0.05252],
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


class Path:
    def __init__(self, first_point, last_point):
        self.first_point = first_point
        self.last_point = last_point

    def is_current_path(self, prev_point, next_point):
        if not self.first_point:
            return next_point <= self.last_point

        if not self.last_point:
            return prev_point >= self.first_point

        return prev_point >= self.first_point and next_point <= self.last_point


class CurvePath(Path):
    pass


class StraightPath(Path):
    pass


STRAIGHT_PATHS = [
    # StraightPath(203, None),
    StraightPath(None, 15),
    StraightPath(39, 50),
    StraightPath(84, 89),
    StraightPath(120, 135),
    StraightPath(143, 152),
    StraightPath(167, 184),
]


CURVED_PATHS = [
    CurvePath(16, 36),
    CurvePath(52, 82),
    CurvePath(98, 118),
    CurvePath(154, 166),
    CurvePath(185, 202),
]


def is_current_path_straight(prev_point, next_point):
    return any([path.is_current_path(prev_point, next_point) for path in STRAIGHT_PATHS])


def is_current_path_a_curve(prev_point, next_point):
    return any([path.is_current_path(prev_point, next_point) for path in CURVED_PATHS])


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
        steering_angle = params["steering_angle"]

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

        is_straight_path = is_current_path_straight(prev_point, next_point)
        is_path_curved = is_current_path_a_curve(prev_point, next_point)

        # REWARD LOGIC:
        # affecting reward based on distance from the optimal line
        distance_penalty_factor = max((track_width - distance_to_racing_line) / track_width, 1e-3)
        optimal_line_reward = OPTIMAL_LINE_BASE_VALUE * distance_penalty_factor * (2 if is_path_curved else 1)

        steps_reward = (progress / steps) * STEPS_REWARD_BASE

        speed_reward = speed ** 2

        min_speed_factor = 1 - (MIN_SPEED_ON_STRAIGHT_PATHS - speed) / TOP_SPEED
        speed_on_straight_paths_extra = (
            STRAIGHT_PATH_SPEED_REWARD_BASE * min_speed_factor
            if is_straight_path
            else 0
        )
        # to avoid zigzag, increase reward if the car uses small steering angles in the straights
        steering_angle_factor = 1 - abs(steering_angle) / HIGHEST_STEERING_ANGLE
        steering_reward = (
            STEERING_ANGLE_REWARD_BASE * steering_angle_factor
            if is_straight_path
            else 0
        )

        combined_reward = (
                OPTIMAL_LINE_WEIGHT * optimal_line_reward
                + STEPS_WEIGHT * steps_reward
                + SPEED_WEIGHT * speed_reward
                + SPEED_ON_STRAIGHT_PATH_WEIGHT * speed_on_straight_paths_extra
                + STEERING_ANGLE_WEIGHT * steering_reward
        )

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
            calculated_is_straight_path=is_straight_path,
            calculated_is_path_curved=is_path_curved,
            calculated_speed_ratio=min_speed_factor,
            # factors
            combined_reward=combined_reward,
            factor_distance_penalty=distance_penalty_factor,
            factor_optimal_line_reward=optimal_line_reward,
            factor_speed_reward=speed_reward,
            factor_steps_reward=steps_reward,
            factor_speed_on_straight_paths_extra=speed_on_straight_paths_extra,
            # given
            given_coordinates=[x, y],
            given_steps=steps,
            given_track_width=track_width,
            # status
            status_accumulated_reward=self.accumulated_reward,
            # weights
            weight_optimal_line=OPTIMAL_LINE_WEIGHT,
            weight_steps=STEPS_WEIGHT,
            weight_speed=SPEED_WEIGHT,
            weight_speed_on_straight_path=SPEED_ON_STRAIGHT_PATH_WEIGHT,
        ))
        return reward


calculator = RewardCalculator()


def reward_function(params):
    # Read input parameters
    return calculator.calculate_reward(params)
