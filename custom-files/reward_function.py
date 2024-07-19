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

    # optimal racing line for 2022_may_open
    racing_line = [
        [5.04608283e00, 8.61460574e-01],
        [5.03925822e00, 1.16054809e00],
        [5.02821898e00, 1.45790395e00],
        [5.01187937e00, 1.75301202e00],
        [4.98907970e00, 2.04528526e00],
        [4.95854952e00, 2.33403774e00],
        [4.91880418e00, 2.61841765e00],
        [4.86796774e00, 2.89728438e00],
        [4.80398170e00, 3.16925571e00],
        [4.72428100e00, 3.43246118e00],
        [4.62575474e00, 3.68437236e00],
        [4.50486544e00, 3.92163167e00],
        [4.35631742e00, 4.13844924e00],
        [4.17535546e00, 4.32670210e00],
        [3.97021669e00, 4.48961366e00],
        [3.74615139e00, 4.62997975e00],
        [3.50733254e00, 4.75082543e00],
        [3.25645607e00, 4.85415157e00],
        [2.99573227e00, 4.94170163e00],
        [2.72709102e00, 5.01496661e00],
        [2.45218298e00, 5.07482209e00],
        [2.17295879e00, 5.12278464e00],
        [1.89099898e00, 5.15979221e00],
        [1.60770194e00, 5.18667666e00],
        [1.32424369e00, 5.20409708e00],
        [1.04159084e00, 5.21253034e00],
        [7.60524221e-01, 5.21234040e00],
        [4.81646432e-01, 5.20386454e00],
        [2.05383295e-01, 5.18747126e00],
        [-6.80005262e-02, 5.16356263e00],
        [-3.38322393e-01, 5.13244758e00],
        [-6.05585775e-01, 5.09465365e00],
        [-8.69624493e-01, 5.05021360e00],
        [-1.13016806e00, 4.99890519e00],
        [-1.38693214e00, 4.94045201e00],
        [-1.63928778e00, 4.87393326e00],
        [-1.88651654e00, 4.79830193e00],
        [-2.12738960e00, 4.71168586e00],
        [-2.36049947e00, 4.61209580e00],
        [-2.58436929e00, 4.49783557e00],
        [-2.79725547e00, 4.36759603e00],
        [-2.99827469e00, 4.22204790e00],
        [-3.18604495e00, 4.06150028e00],
        [-3.35720395e00, 3.88473997e00],
        [-3.50534931e00, 3.68963942e00],
        [-3.62245655e00, 3.47609117e00],
        [-3.69603630e00, 3.24672587e00],
        [-3.72342938e00, 3.01094993e00],
        [-3.71703097e00, 2.77574425e00],
        [-3.67419065e00, 2.54505304e00],
        [-3.58820525e00, 2.32515148e00],
        [-3.44911278e00, 2.12871509e00],
        [-3.27356074e00, 1.95610158e00],
        [-3.06869141e00, 1.80746415e00],
        [-2.84042122e00, 1.68154142e00],
        [-2.59432940e00, 1.57541571e00],
        [-2.33426607e00, 1.48659777e00],
        [-2.06393170e00, 1.41169557e00],
        [-1.78644592e00, 1.34717479e00],
        [-1.50486406e00, 1.28889129e00],
        [-1.22385703e00, 1.23392443e00],
        [-9.46500803e-01, 1.17412319e00],
        [-6.75021980e-01, 1.10659090e00],
        [-4.11523411e-01, 1.02876660e00],
        [-1.58229595e-01, 9.38285828e-01],
        [8.20227841e-02, 8.32611744e-01],
        [3.06013065e-01, 7.09559067e-01],
        [5.08558649e-01, 5.66095619e-01],
        [6.83849996e-01, 4.00445517e-01],
        [8.23499955e-01, 2.11838045e-01],
        [9.30908999e-01, 7.58095266e-03],
        [1.00146778e00, -2.09700319e-01],
        [1.02584130e00, -4.36158234e-01],
        [9.88552959e-01, -6.60721079e-01],
        [9.03330444e-01, -8.72392047e-01],
        [7.79650289e-01, -1.06715285e00],
        [6.24954322e-01, -1.24399964e00],
        [4.40059419e-01, -1.39925398e00],
        [2.30347767e-01, -1.53315706e00],
        [-2.07611962e-04, -1.64624973e00],
        [-2.48305151e-01, -1.73933276e00],
        [-5.10512895e-01, -1.81419813e00],
        [-7.83979001e-01, -1.87271219e00],
        [-1.06627444e00, -1.91682389e00],
        [-1.35523154e00, -1.94875767e00],
        [-1.64922009e00, -1.97040831e00],
        [-1.94715148e00, -1.98297602e00],
        [-2.24060536e00, -2.00570388e00],
        [-2.52833948e00, -2.03983908e00],
        [-2.80896004e00, -2.08691184e00],
        [-3.08084944e00, -2.14850420e00],
        [-3.34208459e00, -2.22625273e00],
        [-3.59074970e00, -2.32131374e00],
        [-3.82318690e00, -2.43637940e00],
        [-4.03498317e00, -2.57360574e00],
        [-4.22057159e00, -2.73447141e00],
        [-4.37103089e00, -2.91999469e00],
        [-4.48781561e00, -3.12290690e00],
        [-4.56900903e00, -3.33881469e00],
        [-4.61280257e00, -3.56299030e00],
        [-4.61538396e00, -3.79007236e00],
        [-4.57905863e00, -4.01409121e00],
        [-4.50628819e00, -4.23034354e00],
        [-4.39636406e00, -4.43359942e00],
        [-4.24630323e00, -4.61603197e00],
        [-4.06179111e00, -4.77392776e00],
        [-3.85048551e00, -4.90799764e00],
        [-3.61717757e00, -5.01896801e00],
        [-3.36590805e00, -5.10816519e00],
        [-3.10011559e00, -5.17725063e00],
        [-2.82303560e00, -5.22858212e00],
        [-2.53763938e00, -5.26517654e00],
        [-2.24621966e00, -5.28984722e00],
        [-1.95040390e00, -5.30484304e00],
        [-1.65167790e00, -5.31273222e00],
        [-1.35116184e00, -5.31581299e00],
        [-1.04970199e00, -5.31613708e00],
        [-7.47950315e-01, -5.31556010e00],
        [-4.46316441e-01, -5.31467944e00],
        [-1.44971978e-01, -5.31304874e00],
        [1.55831599e-01, -5.31003940e00],
        [4.55820113e-01, -5.30499614e00],
        [7.54675156e-01, -5.29719222e00],
        [1.05205513e00, -5.28589026e00],
        [1.34757828e00, -5.27030958e00],
        [1.64080402e00, -5.24959661e00],
        [1.93119310e00, -5.22275606e00],
        [2.21811409e00, -5.18869445e00],
        [2.50079659e00, -5.14615962e00],
        [2.77844774e00, -5.09399292e00],
        [3.04964122e00, -5.03004650e00],
        [3.31244904e00, -4.95167335e00],
        [3.56463355e00, -4.85626341e00],
        [3.80323508e00, -4.74080510e00],
        [4.02408303e00, -4.60163796e00],
        [4.22075577e00, -4.43406588e00],
        [4.38582089e00, -4.23515325e00],
        [4.52583883e00, -4.01499147e00],
        [4.64355372e00, -3.77780912e00],
        [4.74130326e00, -3.52670637e00],
        [4.82124391e00, -3.26416234e00],
        [4.88541147e00, -2.99223116e00],
        [4.93577262e00, -2.71266584e00],
        [4.97421404e00, -2.42697075e00],
        [5.00255600e00, -2.13644630e00],
        [5.02252506e00, -1.84220241e00],
        [5.03593389e00, -1.54525019e00],
        [5.04434769e00, -1.24637543e00],
        [5.04896814e00, -9.46137295e-01],
        [5.05101736e00, -6.45034856e-01],
        [5.05159712e00, -3.43466744e-01],
        [5.05157495e00, -4.17148415e-02],
        [5.05122514e00, 2.59913350e-01],
        [5.04971949e00, 5.61101137e-01],
        [5.04608283e00, 8.61460574e-01],
    ]

    # Get closest indexes for racing line (and distances to all points on racing line)
    closest_index, second_closest_index = closest_2_racing_points_index(
        racing_line, [params["x"], params["y"]]
    )

    # Get optimal [x, y] for closest and second closest index
    optimals = racing_line[closest_index]
    optimals_second = racing_line[second_closest_index]

    distance_to_racing_line = dist_to_racing_line(
        optimals[0:2], optimals_second[0:2], [params["x"], params["y"]]
    )

    # Read input parameters
    # distance_from_center = params['distance_from_center']
    track_width = params["track_width"]
    abs_steering = abs(
        params["steering_angle"]
    )  # Only need the absolute steering angle
    all_wheels_on_track = params['all_wheels_on_track']

    # Calculate 3 marks that are farther and father away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    # Give higher reward if the car is closer to center line and vice versa
    if distance_to_racing_line <= marker_1:
        reward = 1.0
    elif distance_to_racing_line <= marker_2:
        reward = 0.5
    elif distance_to_racing_line <= marker_3:
        reward = 0.1
    else:
        reward = (1e-3,)  # likely crashed/ close to off track
    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15
    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    if not all_wheels_on_track:
        # Heavily penalize if it goes out of track as it means its disqualified
        reward *= 1e-3

    return float(reward)
