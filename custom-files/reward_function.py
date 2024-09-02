import time
from pprint import pprint

# thresholds
ABS_STEERING_ON_STRAIGHT_PATH_THRESHOLD = 10
MIN_SPEED_ON_STRAIGHT_PATH = 4.0
TOTAL_NUM_STEPS = 229
OPTIMAL_SPEED = 2.27

# optimal racing line for 2022_reinvent_champ_ccw
racing_line = [
    [0.7082, 0.35669, 5.0, 0.06064],
    [0.50682, 0.58334, 5.0, 0.06064],
    [0.30523, 0.8098, 5.0, 0.06064],
    [0.10345, 1.03608, 5.0, 0.06064],
    [-0.09854, 1.26219, 5.0, 0.06064],
    [-0.30044, 1.48836, 5.0, 0.06064],
    [-0.50215, 1.71471, 4.29334, 0.07062],
    [-0.70366, 1.94125, 3.47122, 0.08734],
    [-0.90504, 2.16789, 2.96272, 0.10233],
    [-1.10623, 2.3947, 2.58602, 0.11724],
    [-1.30762, 2.62102, 2.27601, 0.1331],
    [-1.51272, 2.84072, 2.04992, 0.14662],
    [-1.72445, 3.04713, 1.74711, 0.16925],
    [-1.94444, 3.23322, 1.53908, 0.18722],
    [-2.17276, 3.39216, 1.3508, 0.20595],
    [-2.40791, 3.51744, 1.3508, 0.19725],
    [-2.64685, 3.60282, 1.3508, 0.18784],
    [-2.88503, 3.64404, 1.3508, 0.17895],
    [-3.11521, 3.63151, 1.3508, 0.17066],
    [-3.32589, 3.55841, 1.3508, 0.16509],
    [-3.4962, 3.41785, 1.4538, 0.15189],
    [-3.61656, 3.23217, 1.60708, 0.13769],
    [-3.687, 3.02359, 1.79313, 0.12278],
    [-3.7146, 2.80736, 1.96043, 0.11119],
    [-3.70647, 2.59148, 2.15607, 0.1002],
    [-3.66954, 2.37975, 2.39995, 0.08956],
    [-3.60989, 2.17339, 2.01274, 0.10672],
    [-3.53261, 1.97227, 1.71371, 0.12572],
    [-3.44161, 1.77579, 1.71371, 0.12635],
    [-3.34067, 1.58296, 1.71371, 0.12701],
    [-3.22955, 1.3873, 1.71371, 0.1313],
    [-3.13342, 1.18396, 1.71371, 0.13125],
    [-3.07084, 0.96545, 1.71371, 0.13263],
    [-3.05938, 0.72908, 2.11283, 0.112],
    [-3.0867, 0.4818, 2.519, 0.09876],
    [-3.14583, 0.22623, 3.14991, 0.08328],
    [-3.22856, -0.0355, 3.86221, 0.07107],
    [-3.32377, -0.30059, 3.46237, 0.08135],
    [-3.42062, -0.5851, 3.07843, 0.09763],
    [-3.51016, -0.87054, 2.7549, 0.10859],
    [-3.58912, -1.15688, 2.4659, 0.12045],
    [-3.65427, -1.44364, 2.20034, 0.13364],
    [-3.70232, -1.72979, 1.95511, 0.14841],
    [-3.72979, -2.01359, 1.70636, 0.1671],
    [-3.73254, -2.29227, 1.51399, 0.18408],
    [-3.7067, -2.56181, 1.34907, 0.20071],
    [-3.64885, -2.81677, 1.2, 0.21787],
    [-3.55642, -3.05001, 1.2, 0.20908],
    [-3.42821, -3.25252, 1.2, 0.19973],
    [-3.26462, -3.41175, 1.2, 0.19025],
    [-3.07154, -3.51403, 1.2, 0.18208],
    [-2.86094, -3.54382, 1.2, 0.17725],
    [-2.65603, -3.48169, 1.45028, 0.14764],
    [-2.4724, -3.35674, 1.62198, 0.13694],
    [-2.3174, -3.17987, 1.86471, 0.12611],
    [-2.19397, -2.9623, 2.13977, 0.11691],
    [-2.10256, -2.71347, 2.07778, 0.12758],
    [-2.03903, -2.44333, 1.80701, 0.15358],
    [-1.99508, -2.16083, 1.60232, 0.17843],
    [-1.93091, -1.88357, 1.42162, 0.20018],
    [-1.84297, -1.62483, 1.25341, 0.21803],
    [-1.72779, -1.39217, 1.25341, 0.20712],
    [-1.58367, -1.19448, 1.25341, 0.19519],
    [-1.41199, -1.04121, 1.25341, 0.18361],
    [-1.21778, -0.94162, 1.25341, 0.17413],
    [-1.00951, -0.90729, 1.25341, 0.16841],
    [-0.80444, -0.95529, 1.40185, 0.15024],
    [-0.61973, -1.06791, 1.5678, 0.13798],
    [-0.46385, -1.23178, 1.73853, 0.13009],
    [-0.3419, -1.4371, 1.94068, 0.12305],
    [-0.25626, -1.67487, 1.82229, 0.13868],
    [-0.20502, -1.93572, 1.45523, 0.18268],
    [-0.18393, -2.21209, 1.22222, 0.22678],
    [-0.18806, -2.49836, 1.22222, 0.23424],
    [-0.20839, -2.76169, 1.22222, 0.2161],
    [-0.20068, -3.00958, 1.22222, 0.20292],
    [-0.14731, -3.22864, 1.22222, 0.18447],
    [-0.04123, -3.4066, 1.22222, 0.16951],
    [0.12006, -3.5251, 1.39628, 0.14334],
    [0.31513, -3.59172, 1.59999, 0.12883],
    [0.53346, -3.61069, 1.82258, 0.12024],
    [0.76841, -3.58395, 2.12471, 0.11129],
    [1.01401, -3.51545, 2.42048, 0.10534],
    [1.26587, -3.4786, 2.59624, 0.09804],
    [1.51728, -3.46956, 2.12426, 0.11843],
    [1.768, -3.4839, 1.80157, 0.13939],
    [2.01785, -3.51938, 1.59061, 0.15865],
    [2.2667, -3.57411, 1.42731, 0.17852],
    [2.51429, -3.64868, 1.29033, 0.20039],
    [2.76268, -3.69504, 1.29033, 0.19583],
    [2.99831, -3.70135, 1.29033, 0.18268],
    [3.21491, -3.66237, 1.29033, 0.17056],
    [3.40571, -3.57583, 1.29033, 0.16236],
    [3.5605, -3.43887, 1.29033, 0.16018],
    [3.6589, -3.2479, 1.44976, 0.14818],
    [3.697, -3.02149, 1.62277, 0.14149],
    [3.6732, -2.77674, 1.80374, 0.13633],
    [3.59079, -2.5309, 2.02181, 0.12825],
    [3.45956, -2.29713, 2.22948, 0.12024],
    [3.28918, -2.08231, 2.4971, 0.1098],
    [3.08893, -1.88775, 2.88018, 0.09694],
    [2.86687, -1.71105, 3.36336, 0.08437],
    [2.62895, -1.54879, 3.80956, 0.0756],
    [2.39269, -1.36641, 4.21972, 0.07073],
    [2.16512, -1.17229, 4.70687, 0.06355],
    [1.94477, -0.96882, 5.0, 0.05998],
    [1.73043, -0.75783, 5.0, 0.06015],
    [1.52082, -0.54108, 5.0, 0.06031],
    [1.3148, -0.32004, 5.0, 0.06043],
    [1.11133, -0.09598, 5.0, 0.06053],
    [0.90941, 0.1299, 5.0, 0.0606],
    [0.7082, 0.35669, 5.0, 0.06064]
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
        self.avg_speed = 0
        self.start_time = time.time()
        self.lap_start_time = time.time()

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
        current_step_len = progress - self.prev_progress

        if progress < self.prev_progress:
            self.lap_start_time = time.time()

        step_start_time = time.time()

        # Get closest indexes for racing line (and distances to all points on racing line)
        closest_index, second_closest_index = closest_2_racing_points_index(
            racing_line, [x, y]
        )

        # Get optimal [x, y] for closest and second closest index
        optimals = racing_line[closest_index]
        optimals_second = racing_line[second_closest_index]

        # Extract optimal speed
        optimal_speed = optimals[2]

        # Calculate distance to optimal racing line to use this one for rewards
        # (instead of distance to track center)
        distance_to_racing_line = dist_to_racing_line(
            optimals[0:2], optimals_second[0:2], [x, y]
        )
        distance_to_racing_line_pct = distance_to_racing_line / (0.5 * track_width)

        # REWARD LOGIC:
        reward = 1e-3 if is_offtrack else 1  # initial value

        distance_penalty_factor = 1.0 - distance_to_racing_line_pct
        reward *= distance_penalty_factor  # affecting reward based on distance from the optimal line

        # if not all_wheels_on_track:
        #     reward *= 0.7  # discouraging going out of track even if it's only one wheel

        optimal_speed_penalty_factor = (1.0 - abs((optimal_speed - speed) / optimal_speed))
        reward *= optimal_speed_penalty_factor  # affect reward based on speed

        # Penalize reward if the car pass every 50 steps slower than expected
        expected_progress = (steps / TOTAL_NUM_STEPS) * 100
        progress_penalty_factor = 1
        if (steps % 20) == 0 and progress < expected_progress:
            progress_penalty_factor = 1.0 - ((expected_progress - progress) / 100.0) ** 0.5
            reward *= progress_penalty_factor

        if prev_point > 101 or next_point < 7:
            if speed < MIN_SPEED_ON_STRAIGHT_PATH:
                # Heavily penalize reward if the car doesn't go flat out on straight paths
                reward *= 0.5
            if abs_steering > ABS_STEERING_ON_STRAIGHT_PATH_THRESHOLD:
                # Penalize reward if the car is steering too much on straight paths
                reward *= 0.6

        avg_speed = (track_len * progress / 100) / (step_start_time - self.lap_start_time)
        # if avg_speed < OPTIMAL_SPEED:
        #     avg_speed_penalty_factor = 1.0 - (OPTIMAL_SPEED - avg_speed)/OPTIMAL_SPEED
        #     reward *= avg_speed_penalty_factor

        # Heavily penalize reward if trying to take a shortcut to complete the lap
        progress_reward_factor = 1
        if progress == 100 and self.prev_progress < 95:
            reward = -100
        elif progress > expected_progress:
            # reward if complete faster than expected
            progress_reward_factor = 1.0 + ((progress - expected_progress) / 100.0) ** 0.5
            reward *= progress_reward_factor

        reward = float(reward)

        self.prev_progress = progress

        pprint(dict(
            steps=steps,
            progress=progress,
            expected_progress=expected_progress,
            progress_reward_factor=progress_reward_factor,
            progress_penalty_factor=progress_penalty_factor,
            distance_penalty_factor=distance_penalty_factor,
            optimal_speed_penalty_factor=optimal_speed_penalty_factor,
        ))
        return reward


calculator = RewardCalculator()


def reward_function(params):
    # Read input parameters
    return calculator.calculate_reward(params)
