def reward_function(params):
    """
    Example of penalize steering, which helps mitigate zig-zag behaviors
    """

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
                -(a**4)
                + 2 * (a**2) * (b**2)
                + 2 * (a**2) * (c**2)
                - (b**4)
                + 2 * (b**2) * (c**2)
                - (c**4)
            ) ** 0.5 / (2 * a)
        except:
            distance = b

        return distance

    # optimal racing line for 2022_reinvent_champ
    racing_line = [
        [ 0.70819545,  0.35669275],
        [ 0.50681953,  0.58334065],
        [ 0.30522838,  0.80979686],
        [ 0.10344665,  1.0360825 ],
        [-0.09853543,  1.26218789],
        [-0.30044332,  1.48835971],
        [-0.50214832,  1.71471407],
        [-0.70365529,  1.94124631],
        [-0.90503601,  2.16789179],
        [-1.1062326 ,  2.39470207],
        [-1.30761652,  2.6210244 ],
        [-1.51271573,  2.8407219 ],
        [-1.7244521 ,  3.04712955],
        [-1.94444249,  3.23321702],
        [-2.17275734,  3.39216021],
        [-2.40791303,  3.51744224],
        [-2.6468494 ,  3.60282354],
        [-2.88502839,  3.64403827],
        [-3.1152084 ,  3.63151353],
        [-3.32588842,  3.55840935],
        [-3.49620148,  3.41785244],
        [-3.61656491,  3.2321677 ],
        [-3.68699707,  3.02358679],
        [-3.71459624,  2.80735825],
        [-3.70646863,  2.59147901],
        [-3.66953619,  2.37974832],
        [-3.60989115,  2.17338594],
        [-3.5326054 ,  1.97226932],
        [-3.44161262,  1.77578655],
        [-3.34066642,  1.58295594],
        [-3.22954679,  1.38730476],
        [-3.13341554,  1.18395726],
        [-3.07083748,  0.96544814],
        [-3.05938017,  0.72907975],
        [-3.08670016,  0.48180059],
        [-3.14583123,  0.22622581],
        [-3.22855902, -0.03550009],
        [-3.32376556, -0.30059202],
        [-3.42062329, -0.58509968],
        [-3.51015586, -0.87054467],
        [-3.5891213 , -1.1568813 ],
        [-3.65426896, -1.44363757],
        [-3.70232043, -1.72978702],
        [-3.72979204, -2.01359012],
        [-3.73253951, -2.29226512],
        [-3.70669643, -2.56180624],
        [-3.64885473, -2.81676566],
        [-3.55642322, -3.05001364],
        [-3.42821432, -3.2525226 ],
        [-3.2646163 , -3.41175402],
        [-3.07153991, -3.51403329],
        [-2.86094061, -3.54382267],
        [-2.65603147, -3.48169324],
        [-2.47239811, -3.35673913],
        [-2.31740482, -3.17987436],
        [-2.19396788, -2.9622966 ],
        [-2.1025638 , -2.71347242],
        [-2.0390278 , -2.44332812],
        [-1.99507654, -2.16083002],
        [-1.93090827, -1.88357466],
        [-1.84296541, -1.62483409],
        [-1.72778857, -1.39217488],
        [-1.58367055, -1.19448017],
        [-1.41198933, -1.0412109 ],
        [-1.21778483, -0.94161698],
        [-1.00951212, -0.90728926],
        [-0.80443608, -0.95529357],
        [-0.61973436, -1.06791367],
        [-0.46385497, -1.23178304],
        [-0.34189715, -1.43710289],
        [-0.25625952, -1.67487143],
        [-0.20501757, -1.93572323],
        [-0.18393207, -2.2120939 ],
        [-0.18805536, -2.49836107],
        [-0.20838702, -2.76169354],
        [-0.20068361, -3.00958269],
        [-0.14730808, -3.22863612],
        [-0.0412273 , -3.40659853],
        [ 0.12006073, -3.52510106],
        [ 0.31512816, -3.5917227 ],
        [ 0.53345974, -3.61069302],
        [ 0.76840824, -3.58394932],
        [ 1.01401186, -3.51545155],
        [ 1.26586568, -3.47859854],
        [ 1.51727968, -3.46956043],
        [ 1.76799679, -3.48389983],
        [ 2.01784645, -3.51938298],
        [ 2.26670266, -3.57410532],
        [ 2.51428653, -3.64867902],
        [ 2.76268343, -3.6950357 ],
        [ 2.99831073, -3.70134609],
        [ 3.21491463, -3.6623733 ],
        [ 3.40570828, -3.57583022],
        [ 3.56049706, -3.43887474],
        [ 3.65889537, -3.24790347],
        [ 3.69699564, -3.02148621],
        [ 3.6732015 , -2.77674087],
        [ 3.59078927, -2.53089636],
        [ 3.4595594 , -2.29713459],
        [ 3.28917836, -2.08230878],
        [ 3.08892636, -1.88774909],
        [ 2.86687315, -1.71105069],
        [ 2.62895009, -1.54878645],
        [ 2.39268553, -1.36640985],
        [ 2.16511814, -1.1722912 ],
        [ 1.94477373, -0.96881966],
        [ 1.73043455, -0.75782849],
        [ 1.52082155, -0.54107673],
        [ 1.31479605, -0.32003912],
        [ 1.11133415, -0.09597619],
        [ 0.90941009,  0.12990168],
        [ 0.70819545,  0.35669275]
    ]

    # Get closest indexes for racing line (and distances to all points on racing line)
    closest_index, second_closest_index = closest_2_racing_points_index(
        racing_line, [params["x"], params["y"]]
    )

    # Get optimal [x, y] for closest and second closest index
    optimals = racing_line[closest_index]
    optimals_second = racing_line[second_closest_index]

    # Read input parameters
    track_width = params["track_width"]
    speed = params["speed"]
    abs_steering = abs(
        params["steering_angle"]
    )  # Only need the absolute steering angle
    all_wheels_on_track = params['all_wheels_on_track']
    closest_waypoints = params['closest_waypoints']
    prev_point = closest_waypoints[0]
    next_point = closest_waypoints[1]

    # Calculate distance to optimal racing line to use this one for rewards
    # (instead of distance to track center)
    distance_to_racing_line = dist_to_racing_line(
        optimals[0:2], optimals_second[0:2], [params["x"], params["y"]]
    )
    distance_to_racing_line_pct = distance_to_racing_line / (0.5 * track_width)

    if not all_wheels_on_track:
        # Heavily penalize if it goes out of track as it means its disqualified
        reward = 1e-3
        print("#TT# All wheels out of track! Reward: {}.".format(reward))
    else:
        # Give higher reward if the car is closer to center line and vice versa

        # Original:
        # reward = math.exp(-5*distance_to_racing_line_pct)
        reward = 1 - distance_to_racing_line_pct
        print("#TT# Reward after distance to racing line ({}): {}.".format(distance_to_racing_line_pct, reward))

        # Steering penality threshold, change the number based on your action space setting
        ABS_STEERING_THRESHOLD = 20
        SPEED_THRESHOLD = 2.5
        # cambiar los waypoints para la nueva pista
        if (
            False
            or prev_point > 141
            or next_point < 11
            or (prev_point > 21 and next_point < 35)
            or (prev_point > 109 and next_point < 132)
        ):
            if speed < SPEED_THRESHOLD:
                # Heavily penalize reward if the car steers on straight paths
                reward *= 0.5
        elif abs_steering > ABS_STEERING_THRESHOLD:
            # Penalize reward if the car is steering too much
            reward *= 0.8
        print("#TT# Reward after steering compensation ({}): {}.".format(abs_steering, reward))

    return float(reward)
