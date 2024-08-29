from pprint import pprint

# thresholds
ABS_STEERING_ON_STRAIGHT_PATH_THRESHOLD = 10
MIN_SPEED_ON_STRAIGHT_PATH = 3.5

# optimal racing line for 2022_reinvent_champ_ccw
RACING_LINE = [
    [0.7082, 0.35669, 4.0, 0.0758],
    [0.50682, 0.58334, 4.0, 0.0758],
    [0.30523, 0.8098, 4.0, 0.0758],
    [0.10345, 1.03608, 4.0, 0.0758],
    [-0.09854, 1.26219, 4.0, 0.0758],
    [-0.30044, 1.48836, 4.0, 0.0758],
    [-0.50215, 1.71471, 4.0, 0.0758],
    [-0.70366, 1.94125, 3.76048, 0.08062],
    [-0.90504, 2.16789, 3.20962, 0.09446],
    [-1.10623, 2.3947, 2.80152, 0.10822],
    [-1.30762, 2.62102, 2.46568, 0.12287],
    [-1.51272, 2.84072, 2.22074, 0.13534],
    [-1.72445, 3.04713, 1.89271, 0.15623],
    [-1.94444, 3.23322, 1.66734, 0.17281],
    [-2.17276, 3.39216, 1.46336, 0.1901],
    [-2.40791, 3.51744, 1.46336, 0.18208],
    [-2.64685, 3.60282, 1.46336, 0.17339],
    [-2.88503, 3.64404, 1.46336, 0.16518],
    [-3.11521, 3.63151, 1.46336, 0.15753],
    [-3.32589, 3.55841, 1.46336, 0.15239],
    [-3.4962, 3.41785, 1.57495, 0.14021],
    [-3.61656, 3.23217, 1.741, 0.1271],
    [-3.687, 3.02359, 1.94255, 0.11333],
    [-3.7146, 2.80736, 2.1238, 0.10264],
    [-3.70647, 2.59148, 2.33574, 0.09249],
    [-3.66954, 2.37975, 2.59995, 0.08267],
    [-3.60989, 2.17339, 2.18047, 0.09852],
    [-3.53261, 1.97227, 1.85652, 0.11605],
    [-3.44161, 1.77579, 1.85652, 0.11663],
    [-3.34067, 1.58296, 1.85652, 0.11724],
    [-3.22955, 1.3873, 1.85652, 0.1212],
    [-3.13342, 1.18396, 1.85652, 0.12115],
    [-3.07084, 0.96545, 1.85652, 0.12243],
    [-3.05938, 0.72908, 2.2889, 0.10339],
    [-3.0867, 0.4818, 2.72891, 0.09117],
    [-3.14583, 0.22623, 3.4124, 0.07687],
    [-3.22856, -0.0355, 4.0, 0.06862],
    [-3.32377, -0.30059, 3.7509, 0.07509],
    [-3.42062, -0.5851, 3.33496, 0.09012],
    [-3.51016, -0.87054, 2.98448, 0.10024],
    [-3.58912, -1.15688, 2.6714, 0.11119],
    [-3.65427, -1.44364, 2.3837, 0.12336],
    [-3.70232, -1.72979, 2.11803, 0.13699],
    [-3.72979, -2.01359, 1.84855, 0.15424],
    [-3.73254, -2.29227, 1.64016, 0.16992],
    [-3.7067, -2.56181, 1.4615, 0.18527],
    [-3.64885, -2.81677, 1.3, 0.20111],
    [-3.55642, -3.05001, 1.3, 0.193],
    [-3.42821, -3.25252, 1.3, 0.18437],
    [-3.26462, -3.41175, 1.3, 0.17561],
    [-3.07154, -3.51403, 1.3, 0.16807],
    [-2.86094, -3.54382, 1.3, 0.16361],
    [-2.65603, -3.48169, 1.57114, 0.13628],
    [-2.4724, -3.35674, 1.75714, 0.12641],
    [-2.3174, -3.17987, 2.02011, 0.11641],
    [-2.19397, -2.9623, 2.31808, 0.10791],
    [-2.10256, -2.71347, 2.25093, 0.11777],
    [-2.03903, -2.44333, 1.95759, 0.14176],
    [-1.99508, -2.16083, 1.73585, 0.1647],
    [-1.93091, -1.88357, 1.54009, 0.18478],
    [-1.84297, -1.62483, 1.35786, 0.20126],
    [-1.72779, -1.39217, 1.35786, 0.19119],
    [-1.58367, -1.19448, 1.35786, 0.18017],
    [-1.41199, -1.04121, 1.35786, 0.16949],
    [-1.21778, -0.94162, 1.35786, 0.16073],
    [-1.00951, -0.90729, 1.35786, 0.15545],
    [-0.80444, -0.95529, 1.51867, 0.13869],
    [-0.61973, -1.06791, 1.69845, 0.12737],
    [-0.46385, -1.23178, 1.88341, 0.12008],
    [-0.3419, -1.4371, 2.1024, 0.11359],
    [-0.25626, -1.67487, 1.97415, 0.12801],
    [-0.20502, -1.93572, 1.57649, 0.16863],
    [-0.18393, -2.21209, 1.32407, 0.20934],
    [-0.18806, -2.49836, 1.32407, 0.21623],
    [-0.20839, -2.76169, 1.32407, 0.19947],
    [-0.20068, -3.00958, 1.32407, 0.18731],
    [-0.14731, -3.22864, 1.32407, 0.17028],
    [-0.04123, -3.4066, 1.32407, 0.15647],
    [0.12006, -3.5251, 1.51263, 0.13231],
    [0.31513, -3.59172, 1.73333, 0.11892],
    [0.53346, -3.61069, 1.97446, 0.11099],
    [0.76841, -3.58395, 2.30177, 0.10273],
    [1.01401, -3.51545, 2.62219, 0.09724],
    [1.26587, -3.4786, 2.8126, 0.0905],
    [1.51728, -3.46956, 2.30128, 0.10932],
    [1.768, -3.4839, 1.9517, 0.12867],
    [2.01785, -3.51938, 1.72316, 0.14645],
    [2.2667, -3.57411, 1.54625, 0.16479],
    [2.51429, -3.64868, 1.39786, 0.18498],
    [2.76268, -3.69504, 1.39786, 0.18077],
    [2.99831, -3.70135, 1.39786, 0.16862],
    [3.21491, -3.66237, 1.39786, 0.15744],
    [3.40571, -3.57583, 1.39786, 0.14987],
    [3.5605, -3.43887, 1.39786, 0.14785],
    [3.6589, -3.2479, 1.57057, 0.13679],
    [3.697, -3.02149, 1.75801, 0.1306],
    [3.6732, -2.77674, 1.95405, 0.12584],
    [3.59079, -2.5309, 2.19029, 0.11838],
    [3.45956, -2.29713, 2.41526, 0.11099],
    [3.28918, -2.08231, 2.7052, 0.10136],
    [3.08893, -1.88775, 3.12019, 0.08948],
    [2.86687, -1.71105, 3.64364, 0.07788],
    [2.62895, -1.54879, 4.0, 0.072],
    [2.39269, -1.36641, 4.0, 0.07462],
    [2.16512, -1.17229, 4.0, 0.07478],
    [1.94477, -0.96882, 4.0, 0.07498],
    [1.73043, -0.75783, 4.0, 0.07519],
    [1.52082, -0.54108, 4.0, 0.07538],
    [1.3148, -0.32004, 4.0, 0.07554],
    [1.11133, -0.09598, 4.0, 0.07566],
    [0.90941, 0.1299, 4.0, 0.07574],
    [0.7082, 0.35669, 4.0, 0.0758],
]


class RewardCalculator(object):
    def __init__(self):
        self.prev_progress = 0

    def calculate_reward(self, params):
        # Read input parameters
        x, y = params["x"], params["y"]
        track_width = params["track_width"]
        speed = params["speed"]
        progress = params["progress"]
        abs_steering = abs(params["steering_angle"])  # Only need the absolute steering angle
        all_wheels_on_track = params['all_wheels_on_track']
        is_offtrack = params['is_offtrack']
        prev_point, next_point = params['closest_waypoints'][0], params['closest_waypoints'][1]
    
        # Get closest indexes for racing line (and distances to all points on racing line)
        closest_index, second_closest_index = closest_2_racing_points_index(
            RACING_LINE, [x, y]
        )
    
        # Get optimal [x, y] for closest and second closest index
        optimals = RACING_LINE[closest_index]
        optimals_second = RACING_LINE[second_closest_index]
    
        # Extract optimal speed
        optimal_speed = optimals[2]
    
        # Calculate distance to optimal racing line to use this one for rewards
        # (instead of distance to track center)
        distance_to_racing_line = dist_to_racing_line(
            optimals[0:2], optimals_second[0:2], [x, y]
        )
        distance_to_racing_line_pct = distance_to_racing_line / (0.5 * track_width)

        prev_progress = self.prev_progress
        self.prev_progress = progress

        # REWARD LOGIC:
        if progress > (prev_progress + 5.0):
            return 0  # immediately discourage buggy laps

        reward = 1e-3 if is_offtrack else 1  # initial value
    
        reward *= (1.0 - distance_to_racing_line_pct)  # affecting reward based on distance from the optimal line
    
        # if not all_wheels_on_track:
        #     reward *= 0.7  # discouraging going out of track even if it's only one wheel
    
        reward *= (1.0 - abs((optimal_speed - speed) / optimal_speed))  # affect reward based on speed
    
        # uncomment if not fast enough (tweak constants at the beginning, and it should probably be proportional)
        # if (
        #     prev_point > 103
        #     or next_point < 12
        # ):
        #     if abs_steering > ABS_STEERING_ON_STRAIGHT_PATH_THRESHOLD:
        #         # Penalize reward if the car is steering too much on straight paths
        #         reward *= 0.6
        #
        #     if speed < MIN_SPEED_ON_STRAIGHT_PATH:
        #         # Heavily penalize reward if the car doesn't go flat out on straight paths
        #         reward *= 0.5
    
        reward = float(reward)
    
        pprint(dict(
            x=x,
            y=y,
            track_width=track_width,
            track_length=params["track_length"],
            speed=speed,
            abs_steering=abs_steering,
            speed_factor=(1.0 - abs((optimal_speed - speed) / optimal_speed)),
            all_wheels_on_track=all_wheels_on_track,
            is_offtrack=is_offtrack,
            prev_point=prev_point,
            next_point=next_point,
            distance_from_center=params["distance_from_center"],
            distance_to_racing_line=distance_to_racing_line,
            distance_to_racing_line_pct=distance_to_racing_line_pct,
            optimals=optimals,
            optimals_second=optimals_second,
            optimal_speed=optimal_speed,
            closest_index=closest_index,
            second_closest_index=second_closest_index,
            reward=reward,
            progress=progress,
        ))
        return reward


#################################### HELPERS ###################################
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


################################# Entry Point ##################################

calculator = RewardCalculator()  # initializing calculator object


def reward_function(params):
    return calculator.calculate_reward(params)
