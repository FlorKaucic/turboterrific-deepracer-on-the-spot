import time
from pprint import pprint

# thresholds
ABS_STEERING_ON_STRAIGHT_PATH_THRESHOLD = 5
MIN_SPEED_ON_STRAIGHT_PATH = 4.0
TOTAL_NUM_STEPS = 380
OPTIMAL_SPEED = 2.27

# optimal racing line for 2022_reinvent_champ_ccw
racing_line = [
    [-0.19668, -5.38338, 5.0, 0.05252],
    [-0.45997, -5.3878, 5.0, 0.05267],
    [-0.72478, -5.39126, 5.0, 0.05297],
    [-0.99164, -5.39399, 5.0, 0.05337],
    [-1.26109, -5.39612, 5.0, 0.05389],
    [-1.5323, -5.39797, 5.0, 0.05424],
    [-1.80569, -5.39958, 5.0, 0.05468],
    [-2.08183, -5.40095, 5.0, 0.05523],
    [-2.36136, -5.40209, 5.0, 0.05591],
    [-2.64349, -5.4031, 5.0, 0.05643],
    [-2.93011, -5.40388, 5.0, 0.05732],
    [-3.22219, -5.40444, 5.0, 0.05842],
    [-3.52371, -5.40475, 5.0, 0.0603],
    [-3.82523, -5.40512, 4.06424, 0.07419],
    [-4.1249, -5.40147, 3.44025, 0.08711],
    [-4.42006, -5.38893, 2.99367, 0.09868],
    [-4.70782, -5.36302, 2.55761, 0.11297],
    [-4.98506, -5.31993, 2.23657, 0.12545],
    [-5.24833, -5.25647, 1.97281, 0.13727],
    [-5.49259, -5.16867, 1.74435, 0.1488],
    [-5.71233, -5.05402, 1.40971, 0.17582],
    [-5.90103, -4.91127, 1.40971, 0.16784],
    [-6.05035, -4.7407, 1.40971, 0.16081],
    [-6.13856, -4.54291, 1.52641, 0.14188],
    [-6.17498, -4.33455, 1.58578, 0.13338],
    [-6.16515, -4.12459, 1.58578, 0.13255],
    [-6.11324, -3.91927, 1.58578, 0.13355],
    [-6.014, -3.72679, 1.76441, 0.12274],
    [-5.87623, -3.55121, 1.93121, 0.11556],
    [-5.70559, -3.39472, 2.11346, 0.10955],
    [-5.5067, -3.25851, 2.29348, 0.10511],
    [-5.28316, -3.14351, 2.5104, 0.10014],
    [-5.0387, -3.04978, 2.79095, 0.09381],
    [-4.77737, -2.97619, 3.15212, 0.08613],
    [-4.50311, -2.92053, 3.58891, 0.07798],
    [-4.21931, -2.88014, 4.14138, 0.06922],
    [-3.92871, -2.85209, 4.81255, 0.06066],
    [-3.63343, -2.83368, 5.0, 0.05917],
    [-3.33495, -2.8226, 5.0, 0.05974],
    [-3.03458, -2.81638, 5.0, 0.06009],
    [-2.73329, -2.81274, 5.0, 0.06026],
    [-2.43178, -2.80973, 5.0, 0.06031],
    [-2.13028, -2.80671, 5.0, 0.0603],
    [-1.82877, -2.80369, 5.0, 0.06031],
    [-1.52727, -2.80067, 5.0, 0.0603],
    [-1.22577, -2.79765, 5.0, 0.0603],
    [-0.92426, -2.79464, 5.0, 0.06031],
    [-0.62276, -2.79161, 5.0, 0.0603],
    [-0.32186, -2.78711, 4.97081, 0.06054],
    [-0.02262, -2.77866, 4.2938, 0.06972],
    [0.27376, -2.76377, 3.79793, 0.07814],
    [0.56579, -2.73973, 3.39559, 0.08629],
    [0.85179, -2.70399, 3.06589, 0.09401],
    [1.12993, -2.65416, 2.76767, 0.1021],
    [1.39813, -2.58792, 2.42031, 0.11414],
    [1.65411, -2.50313, 2.1553, 0.12511],
    [1.89508, -2.39755, 1.87514, 0.1403],
    [2.11637, -2.26737, 1.87514, 0.13692],
    [2.31239, -2.10939, 1.87514, 0.13426],
    [2.47312, -1.91918, 2.01646, 0.1235],
    [2.60078, -1.70495, 2.16151, 0.11537],
    [2.69723, -1.47288, 2.32974, 0.10787],
    [2.76475, -1.22824, 2.46149, 0.1031],
    [2.80472, -0.97508, 2.58525, 0.09914],
    [2.81854, -0.71683, 2.70666, 0.09555],
    [2.80775, -0.45641, 2.81475, 0.0926],
    [2.7738, -0.19625, 2.78154, 0.09432],
    [2.71744, 0.06147, 2.60854, 0.10113],
    [2.63958, 0.31476, 2.60854, 0.10158],
    [2.53846, 0.56071, 2.60854, 0.10194],
    [2.41213, 0.79488, 2.88742, 0.09215],
    [2.26679, 1.017, 2.82097, 0.0941],
    [2.10441, 1.22556, 2.70262, 0.0978],
    [1.92622, 1.41833, 2.50271, 0.10489],
    [1.73373, 1.59297, 2.33189, 0.11146],
    [1.52843, 1.74653, 2.08164, 0.12316],
    [1.3117, 1.87457, 1.86825, 0.13474],
    [1.08586, 1.97299, 1.63577, 0.1506],
    [0.8534, 2.03495, 1.63577, 0.14707],
    [0.61805, 2.05323, 1.63577, 0.14431],
    [0.3853, 2.01592, 1.727, 0.13649],
    [0.15996, 1.92756, 2.02506, 0.11952],
    [-0.05666, 1.79918, 2.52575, 0.0997],
    [-0.2658, 1.6426, 3.67398, 0.07111],
    [-0.47081, 1.47166, 4.51653, 0.0591],
    [-0.69733, 1.29632, 4.74839, 0.06033],
    [-0.92948, 1.12892, 5.0, 0.05724],
    [-1.16615, 0.96902, 5.0, 0.05712],
    [-1.40667, 0.81631, 5.0, 0.05698],
    [-1.65068, 0.67079, 4.90663, 0.0579],
    [-1.89787, 0.53243, 4.57364, 0.06194],
    [-2.14816, 0.40173, 4.5126, 0.06257],
    [-2.40152, 0.27937, 4.5126, 0.06235],
    [-2.65806, 0.16665, 4.5126, 0.0621],
    [-2.91746, 0.06387, 4.48057, 0.06227],
    [-3.17928, -0.02927, 4.33852, 0.06405],
    [-3.44319, -0.11276, 4.14443, 0.06679],
    [-3.70888, -0.18617, 3.88564, 0.07094],
    [-3.97601, -0.24885, 3.58604, 0.07651],
    [-4.24417, -0.29982, 3.27741, 0.08329],
    [-4.51275, -0.33756, 2.96185, 0.09157],
    [-4.7809, -0.35997, 2.64187, 0.10185],
    [-5.04721, -0.36441, 2.35688, 0.11301],
    [-5.30954, -0.34758, 2.05242, 0.12808],
    [-5.56448, -0.30538, 1.80785, 0.14294],
    [-5.80705, -0.23371, 1.60029, 0.15806],
    [-6.02934, -0.12741, 1.4, 0.176],
    [-6.22076, 0.01671, 1.4, 0.17115],
    [-6.36743, 0.19907, 1.4, 0.16716],
    [-6.44818, 0.41385, 1.65971, 0.13825],
    [-6.4793, 0.63937, 1.79589, 0.12677],
    [-6.46738, 0.86724, 1.91397, 0.11922],
    [-6.41711, 1.09209, 2.04943, 0.11242],
    [-6.33297, 1.31032, 2.1954, 0.10654],
    [-6.21886, 1.5196, 2.22898, 0.10694],
    [-6.07778, 1.71833, 2.22898, 0.10934],
    [-5.9065, 1.90193, 2.49866, 0.10049],
    [-5.71079, 2.07045, 2.84667, 0.09073],
    [-5.4959, 2.22532, 3.33515, 0.07942],
    [-5.26673, 2.36902, 4.1162, 0.06572],
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
    [-2.06799, 4.26909, 4.53768, 0.06216],
    [-1.82752, 4.4141, 3.88291, 0.07232],
    [-1.58498, 4.55197, 3.38308, 0.08247],
    [-1.3396, 4.67996, 2.94713, 0.09391],
    [-1.09047, 4.79478, 2.65218, 0.10343],
    [-0.83665, 4.89264, 2.65218, 0.10257],
    [-0.57703, 4.96853, 2.65218, 0.10199],
    [-0.31082, 5.01736, 3.31614, 0.08162],
    [-0.04065, 5.04867, 3.7835, 0.07189],
    [0.23262, 5.06628, 4.35631, 0.06286],
    [0.50845, 5.07334, 5.0, 0.05518],
    [0.78637, 5.07292, 5.0, 0.05558],
    [1.06574, 5.06805, 5.0, 0.05588],
    [1.34901, 5.06525, 5.0, 0.05666],
    [1.63229, 5.06415, 5.0, 0.05666],
    [1.91557, 5.06429, 5.0, 0.05666],
    [2.19886, 5.06535, 5.0, 0.05666],
    [2.48215, 5.06702, 5.0, 0.05666],
    [2.75795, 5.06666, 4.47789, 0.06159],
    [3.03093, 5.06214, 3.85849, 0.07076],
    [3.30007, 5.05086, 3.37926, 0.07971],
    [3.5647, 5.03029, 3.00411, 0.08836],
    [3.82399, 4.99773, 2.61545, 0.09992],
    [4.07675, 4.95025, 2.30965, 0.11135],
    [4.32126, 4.88485, 2.08206, 0.12156],
    [4.5546, 4.79711, 1.86958, 0.13334],
    [4.77277, 4.68239, 1.86958, 0.13184],
    [4.97045, 4.53638, 1.86958, 0.13145],
    [5.13887, 4.35384, 1.94767, 0.12752],
    [5.27552, 4.13957, 2.274, 0.11176],
    [5.38528, 3.90298, 2.59287, 0.10059],
    [5.47184, 3.64954, 2.9513, 0.09074],
    [5.53865, 3.3832, 3.38327, 0.08116],
    [5.58913, 3.10714, 4.01439, 0.06991],
    [5.62723, 2.8242, 5.0, 0.0571],
    [5.65712, 2.53692, 5.0, 0.05777],
    [5.68233, 2.24642, 5.0, 0.05832],
    [5.71226, 1.95247, 5.0, 0.05909],
    [5.74597, 1.65878, 5.0, 0.05912],
    [5.78293, 1.36571, 5.0, 0.05908],
    [5.82274, 1.07328, 5.0, 0.05903],
    [5.86513, 0.7815, 5.0, 0.05897],
    [5.90991, 0.49034, 5.0, 0.05892],
    [5.95689, 0.19981, 5.0, 0.05886],
    [6.00599, -0.09011, 5.0, 0.05881],
    [6.05726, -0.37936, 5.0, 0.05875],
    [6.1108, -0.66787, 5.0, 0.05869],
    [6.16684, -0.95552, 5.0, 0.05861],
    [6.22576, -1.24209, 5.0, 0.05851],
    [6.28809, -1.52722, 3.87016, 0.07541],
    [6.35106, -1.79549, 3.05312, 0.09026],
    [6.4071, -2.06285, 2.58031, 0.10587],
    [6.44946, -2.3284, 2.22097, 0.12108],
    [6.47098, -2.59111, 1.83224, 0.14386],
    [6.46496, -2.84973, 1.83224, 0.14119],
    [6.42349, -3.10203, 1.83224, 0.13955],
    [6.33149, -3.34115, 2.04769, 0.12512],
    [6.20004, -3.56451, 2.26512, 0.11442],
    [6.03737, -3.77064, 2.48833, 0.10553],
    [5.85, -3.95916, 2.71015, 0.09807],
    [5.64294, -4.13042, 2.97575, 0.0903],
    [5.42047, -4.28572, 3.19914, 0.08481],
    [5.18538, -4.42605, 3.42768, 0.07988],
    [4.93993, -4.55244, 3.66645, 0.0753],
    [4.68594, -4.66597, 3.90652, 0.07122],
    [4.42494, -4.76762, 4.145, 0.06757],
    [4.15817, -4.85829, 4.37799, 0.06436],
    [3.88676, -4.93875, 4.61508, 0.06134],
    [3.61173, -5.00973, 4.86814, 0.05835],
    [3.3341, -5.07195, 5.0, 0.0569],
    [3.05485, -5.12611, 5.0, 0.05689],
    [2.77494, -5.17293, 5.0, 0.05676],
    [2.49529, -5.21308, 5.0, 0.0565],
    [2.2167, -5.24727, 5.0, 0.05614],
    [1.93985, -5.27615, 5.0, 0.05567],
    [1.66524, -5.30037, 5.0, 0.05514],
    [1.39317, -5.32052, 5.0, 0.05456],
    [1.12372, -5.33714, 5.0, 0.05399],
    [0.85672, -5.35075, 5.0, 0.05347],
    [0.5918, -5.3618, 5.0, 0.05303],
    [0.32843, -5.37064, 5.0, 0.0527],
    [0.06585, -5.37772, 5.0, 0.05254],
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


class RewardCalculator:
    def __init__(self):
        self.prev_progress = 0
        self.total_time = 0
        self.progress_incentive = []

    def calculate_reward(self, params):
        # Read input parameters
        x, y = params["x"], params["y"]
        track_width = params["track_width"]
        speed = params["speed"]
        abs_steering = abs(params["steering_angle"])  # Only need the absolute steering angle
        all_wheels_on_track = params['all_wheels_on_track']
        is_offtrack = params['is_offtrack']
        progress = params["progress"]
        steps = params["steps"]
        track_len = params['track_length']
        prev_point, next_point = params['closest_waypoints'][0], params['closest_waypoints'][1]

        if progress < self.prev_progress:
            self.prev_progress = 0
            self.total_time = 0
            self.progress_incentive = []

        current_step_progress = progress - self.prev_progress
        current_step_len = current_step_progress * track_len / 100
        current_step_time = current_step_len / speed
        self.total_time += current_step_time

        distance_achieved = progress * track_len / 100
        avg_speed = distance_achieved / self.total_time

        # Get closest indexes for racing line (and distances to all points on racing line)
        closest_index, second_closest_index = closest_2_racing_points_index(
            racing_line, [x, y]
        )

        # Get optimal [x, y] for closest and second closest index
        optimals = racing_line[closest_index]
        optimals_second = racing_line[second_closest_index]

        # REWARD LOGIC:

        # Calculate distance to optimal racing line to use this one for rewards
        # (instead of distance to track center)
        distance_to_racing_line = dist_to_racing_line(
            optimals[0:2], optimals_second[0:2], [x, y]
        )

        distance_to_racing_line_pct = distance_to_racing_line / track_width
        distance_reward = 1.0 - distance_to_racing_line_pct ** 0.4
        # reward *= distance_penalty_factor  # affecting reward based on distance from the optimal line

        max_speed_diff = 0.7
        optimal_speed = optimals[2]
        speed_diff = abs(optimal_speed - speed)
        optimal_speed_reward = max(1e-3, 1 - ((speed_diff / max_speed_diff) ** 0.4))

        # optimal_speed = 2.2  # calculated based on track len (33 m) and time goal (15 s)
        # speed_diff = optimal_speed - avg_speed
        # speed_diff_pct = speed_diff / 5.0
        # optimal_speed_reward = 1.0 - speed_diff_pct

        # optimal_speed_reward = 1.0 - (optimal_speed - speed) / optimal_speed
        # reward *= optimal_speed_penalty_factor  # affect reward based on speed

        expected_progress = (steps / TOTAL_NUM_STEPS) * 100
        progress_reward = 1.0 + ((progress - expected_progress) / 100.0)

        # extra reward for progress every 10% of track complete
        extra_progress_reward = 0
        pi = int(progress // 10)
        if pi != 0 and pi not in self.progress_incentive:
            self.progress_incentive.append(pi)
            extra_progress_reward = (10 * progress / steps) ** (avg_speed + 0.7 * pi)

        reward = 1e-3 if is_offtrack else (distance_reward + optimal_speed_reward + progress_reward + extra_progress_reward)

        reward = float(reward)

        self.prev_progress = progress

        pprint(dict(
            a_steps=steps,
            a_progress=progress,
            a_progress_expected=expected_progress,
            a_progress_reward=progress_reward,
            a_step_progress=current_step_progress,
            a_extra_step_progress=extra_progress_reward,
            b_speed_reward=optimal_speed_reward,
            b_speed_optimal=optimal_speed,
            b_speed_avg=avg_speed,
            b_speed=speed,
            c_distance_to_racing_line=distance_to_racing_line,
            c_distance_reward=distance_reward,
            c_distance_expected1=optimals[0:2],
            c_distance_expected2=optimals_second[0:2],
            c_distance_actual=[x, y],
            d_track_width=track_width,
            d_track_len=track_len,
            d_total_time=self.total_time,
        ))

        return reward


calculator = RewardCalculator()


def reward_function(params):
    # Read input parameters
    return calculator.calculate_reward(params)
