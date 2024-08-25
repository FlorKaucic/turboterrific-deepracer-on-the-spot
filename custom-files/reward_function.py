from pprint import pprint
from utils import closest_2_racing_points_index, dist_to_racing_line

# thresholds
ABS_STEERING_ON_STRAIGHT_PATH_THRESHOLD = 10
MIN_SPEED_ON_STRAIGHT_PATH = 3.5

# optimal racing line for 2022_reinvent_champ_ccw
racing_line = [
    [0.7082, 0.35669, 4.0, 0.0758],
    [0.50682, 0.58334, 4.0, 0.0758],
    [0.30523, 0.8098, 4.0, 0.0758],
    [0.10345, 1.03608, 4.0, 0.0758],
    [-0.09854, 1.26219, 4.0, 0.0758],
    [-0.30044, 1.48836, 4.0, 0.0758],
    [-0.50215, 1.71471, 4.0, 0.0758],
    [-0.70366, 1.94125, 4.0, 0.0758],
    [-0.90504, 2.16789, 3.70341, 0.08187],
    [-1.10623, 2.3947, 3.23252, 0.09379],
    [-1.30762, 2.62102, 2.84501, 0.10648],
    [-1.51272, 2.84072, 2.5624, 0.11729],
    [-1.72445, 3.04713, 2.18389, 0.1354],
    [-1.94444, 3.23322, 1.92385, 0.14977],
    [-2.17276, 3.39216, 1.6885, 0.16476],
    [-2.40791, 3.51744, 1.6885, 0.1578],
    [-2.64685, 3.60282, 1.6885, 0.15027],
    [-2.88503, 3.64404, 1.6885, 0.14316],
    [-3.11521, 3.63151, 1.6885, 0.13652],
    [-3.32589, 3.55841, 1.6885, 0.13207],
    [-3.4962, 3.41785, 1.81725, 0.12152],
    [-3.61656, 3.23217, 2.00885, 0.11015],
    [-3.687, 3.02359, 2.24141, 0.09822],
    [-3.7146, 2.80736, 2.45054, 0.08895],
    [-3.70647, 2.59148, 2.69509, 0.08016],
    [-3.66954, 2.37975, 2.99994, 0.07164],
    [-3.60989, 2.17339, 2.51593, 0.08538],
    [-3.53261, 1.97227, 2.14213, 0.10058],
    [-3.44161, 1.77579, 2.14213, 0.10108],
    [-3.34067, 1.58296, 2.14213, 0.10161],
    [-3.22955, 1.3873, 2.14213, 0.10504],
    [-3.13342, 1.18396, 2.14213, 0.105],
    [-3.07084, 0.96545, 2.14213, 0.10611],
    [-3.05938, 0.72908, 2.64103, 0.0896],
    [-3.0867, 0.4818, 3.14875, 0.07901],
    [-3.14583, 0.22623, 3.93739, 0.06662],
    [-3.22856, -0.0355, 4.0, 0.06862],
    [-3.32377, -0.30059, 4.0, 0.07042],
    [-3.42062, -0.5851, 3.84803, 0.0781],
    [-3.51016, -0.87054, 3.44363, 0.08687],
    [-3.58912, -1.15688, 3.08238, 0.09636],
    [-3.65427, -1.44364, 2.75042, 0.10692],
    [-3.70232, -1.72979, 2.44388, 0.11873],
    [-3.72979, -2.01359, 2.13295, 0.13368],
    [-3.73254, -2.29227, 1.89249, 0.14726],
    [-3.7067, -2.56181, 1.68634, 0.16057],
    [-3.64885, -2.81677, 1.5, 0.17429],
    [-3.55642, -3.05001, 1.5, 0.16726],
    [-3.42821, -3.25252, 1.5, 0.15979],
    [-3.26462, -3.41175, 1.5, 0.1522],
    [-3.07154, -3.51403, 1.5, 0.14566],
    [-2.86094, -3.54382, 1.5, 0.1418],
    [-2.65603, -3.48169, 1.81285, 0.11811],
    [-2.4724, -3.35674, 2.02747, 0.10955],
    [-2.3174, -3.17987, 2.33089, 0.10089],
    [-2.19397, -2.9623, 2.67471, 0.09353],
    [-2.10256, -2.71347, 2.59723, 0.10206],
    [-2.03903, -2.44333, 2.25876, 0.12286],
    [-1.99508, -2.16083, 2.0029, 0.14274],
    [-1.93091, -1.88357, 1.77703, 0.16015],
    [-1.84297, -1.62483, 1.56676, 0.17442],
    [-1.72779, -1.39217, 1.56676, 0.1657],
    [-1.58367, -1.19448, 1.56676, 0.15615],
    [-1.41199, -1.04121, 1.56676, 0.14689],
    [-1.21778, -0.94162, 1.56676, 0.1393],
    [-1.00951, -0.90729, 1.56676, 0.13473],
    [-0.80444, -0.95529, 1.75231, 0.1202],
    [-0.61973, -1.06791, 1.95975, 0.11039],
    [-0.46385, -1.23178, 2.17316, 0.10407],
    [-0.3419, -1.4371, 2.42585, 0.09844],
    [-0.25626, -1.67487, 2.27787, 0.11095],
    [-0.20502, -1.93572, 1.81903, 0.14614],
    [-0.18393, -2.21209, 1.52777, 0.18142],
    [-0.18806, -2.49836, 1.52777, 0.1874],
    [-0.20839, -2.76169, 1.52777, 0.17288],
    [-0.20068, -3.00958, 1.52777, 0.16233],
    [-0.14731, -3.22864, 1.52777, 0.14758],
    [-0.04123, -3.4066, 1.52777, 0.13561],
    [0.12006, -3.5251, 1.74535, 0.11467],
    [0.31513, -3.59172, 1.99999, 0.10307],
    [0.53346, -3.61069, 2.27822, 0.0962],
    [0.76841, -3.58395, 2.65589, 0.08903],
    [1.01401, -3.51545, 3.0256, 0.08427],
    [1.26587, -3.4786, 3.2453, 0.07843],
    [1.51728, -3.46956, 2.65533, 0.09474],
    [1.768, -3.4839, 2.25196, 0.11151],
    [2.01785, -3.51938, 1.98826, 0.12692],
    [2.2667, -3.57411, 1.78414, 0.14281],
    [2.51429, -3.64868, 1.61291, 0.16031],
    [2.76268, -3.69504, 1.61291, 0.15666],
    [2.99831, -3.70135, 1.61291, 0.14614],
    [3.21491, -3.66237, 1.61291, 0.13645],
    [3.40571, -3.57583, 1.61291, 0.12989],
    [3.5605, -3.43887, 1.61291, 0.12814],
    [3.6589, -3.2479, 1.81219, 0.11855],
    [3.697, -3.02149, 2.02847, 0.11319],
    [3.6732, -2.77674, 2.25468, 0.10906],
    [3.59079, -2.5309, 2.52726, 0.1026],
    [3.45956, -2.29713, 2.78684, 0.09619],
    [3.28918, -2.08231, 3.12138, 0.08784],
    [3.08893, -1.88775, 3.60022, 0.07755],
    [2.86687, -1.71105, 4.0, 0.07094],
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


def reward_function(params):
    # Read input parameters
    x, y = params["x"], params["y"]
    track_width = params["track_width"]
    speed = params["speed"]
    abs_steering = abs(params["steering_angle"]) # Only need the absolute steering angle
    all_wheels_on_track = params['all_wheels_on_track']
    is_offtrack = params['is_offtrack']
    prev_point, next_point = params['closest_waypoints'][0], params['closest_waypoints'][1]

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
        optimals[0:2], optimals_second[0:2], [params["x"], params["y"]]
    )
    distance_to_racing_line_pct = distance_to_racing_line / (0.5 * track_width)

    # REWARD LOGIC:
    reward = 1e-3 if is_offtrack else 1  # initial value

    reward *= (1.0 - distance_to_racing_line_pct)  # affecting reward based on distance from the optimal line

    if not all_wheels_on_track:
        reward *= 0.7  # discouraging going out of track even if it's only one wheel

    reward *= (1.0 - ((optimal_speed - speed) / optimal_speed))  # affect reward based on speed

    # uncomment if not fast enough (tweak constants at the beginning)
    # if (
    #     prev_point > 103
    #     or next_point < 12
    # ):
    #     if speed < MIN_SPEED_ON_STRAIGHT_PATH:
    #         # Heavily penalize reward if the car doesn't go flat out on straight paths
    #         reward *= 0.5
    #     if abs_steering > ABS_STEERING_ON_STRAIGHT_PATH_THRESHOLD:
    #         # Penalize reward if the car is steering too much on straight paths
    #         reward *= 0.6

    reward = float(reward)

    pprint(dict(
        x=x,
        y=y,
        track_width=track_width,
        track_length=params["track_length"],
        speed=speed,
        abs_steering=abs_steering,
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
        progress=params["progress"],
    ))
    return reward
