import unittest
from mock import patch


def getMockedRewardFunction():
    import importlib
    rf_module = importlib.import_module("custom-files.reward_function")
    rf_module.racing_line = [[0.50682, 0.58334, 5.0, 0.06064], ]
    return rf_module.reward_function


reward_function = getMockedRewardFunction()


class RewardFunctionTest(unittest.TestCase):
    def setUp(self):
        self.params_baseline = dict(
            x=0.5,
            y=0.5,
            track_width=2,
            speed=5.0,
            progress=2,
            steps=4,
            closest_waypoints=[1, 2],
            steering_angle=0,
        )

        self.reward_baseline = reward_function(self.params_baseline)

    def test_baseline_is_not_zero(self):
        self.assertNotEqual(self.reward_baseline, 0)

    def test_further_away(self):
        params_further_away = dict(
            x=0.45,
            y=0.48,
            track_width=2,
            speed=5.0,
            progress=2,
            steps=4,
            closest_waypoints=[1, 2],
            steering_angle=0,
        )

        reward_further_away = reward_function(params_further_away)
        self.assertNotEqual(params_further_away, 0)
        self.assertTrue(reward_further_away <= self.reward_baseline)

    def test_closer_to_raceline(self):
        params_closer_to_raceline = dict(
            x=0.5,
            y=0.51,
            track_width=2,
            speed=5.0,
            progress=2,
            steps=4,
            closest_waypoints=[1, 2],
            steering_angle=0,
        )

        reward_closer_to_raceline = reward_function(params_closer_to_raceline)
        self.assertNotEqual(params_closer_to_raceline, 0)
        self.assertTrue(reward_closer_to_raceline >= self.reward_baseline)

    def test_slower_speed(self):
        params_speed_slower = dict(
            x=0.5,
            y=0.5,
            track_width=2,
            speed=3.0,
            progress=2,
            steps=4,
            closest_waypoints=[1, 2],
            steering_angle=0,
        )

        reward_speed_slower = reward_function(params_speed_slower)
        self.assertNotEqual(reward_speed_slower, 0)
        self.assertTrue(reward_speed_slower <= self.reward_baseline)

    def test_faster_speed(self):
        params_speed_faster = dict(
            x=0.5,
            y=0.5,
            track_width=2,
            speed=5.5,
            progress=2,
            steps=4,
            closest_waypoints=[1, 2],
            steering_angle=0,
        )

        reward_speed_faster = reward_function(params_speed_faster)
        self.assertNotEqual(reward_speed_faster, 0)
        self.assertTrue(reward_speed_faster >= self.reward_baseline)

    def test_slower_steps(self):
        params_steps_slower = dict(
            x=0.5,
            y=0.5,
            track_width=2,
            speed=5.0,
            progress=2,
            steps=5,
            closest_waypoints=[1, 2],
            steering_angle=0,
        )

        reward_steps_slower = reward_function(params_steps_slower)
        self.assertNotEqual(reward_steps_slower, 0)
        self.assertTrue(reward_steps_slower <= self.reward_baseline)

    def test_faster_steps(self):
        params_steps_faster = dict(
            x=0.5,
            y=0.5,
            track_width=2,
            speed=5.0,
            progress=2,
            steps=3,
            closest_waypoints=[1, 2],
            steering_angle=0,
        )

        reward_steps_faster = reward_function(params_steps_faster)
        self.assertNotEqual(reward_steps_faster, 0)
        self.assertTrue(reward_steps_faster >= self.reward_baseline)

    def test_out_of_bounds_distance(self):
        params_distance_upper = dict(
            x=5,
            y=5,
            track_width=2,
            speed=5.0,
            progress=2,
            steps=4,
            closest_waypoints=[1, 2],
            steering_angle=0,
        )

        params_distance_lower = dict(
            x=-5,
            y=-5,
            track_width=2,
            speed=5.0,
            progress=2,
            steps=4,
            closest_waypoints=[1, 2],
            steering_angle=0,
        )

        reward_distance_upper = reward_function(params_distance_upper)
        reward_distance_lower = reward_function(params_distance_lower)

        self.assertNotEqual(reward_distance_upper, 0)
        self.assertNotEqual(reward_distance_lower, 0)

        self.assertTrue(reward_distance_upper < self.reward_baseline)
        self.assertTrue(reward_distance_lower < self.reward_baseline)

    def test_out_of_bounds_speed(self):
        params_speed_extreme = dict(
            x=0.5,
            y=0.5,
            track_width=2,
            speed=15.0,
            progress=2,
            steps=4,
            closest_waypoints=[1, 2],
            steering_angle=0,
        )

        params_speed_stopped = dict(
            x=0.5,
            y=0.5,
            track_width=2,
            speed=0.0,
            progress=2,
            steps=4,
            closest_waypoints=[1, 2],
            steering_angle=0,
        )

        reward_speed_stopped = reward_function(params_speed_stopped)
        reward_speed_extreme = reward_function(params_speed_extreme)

        self.assertNotEqual(reward_speed_stopped, 0)
        self.assertNotEqual(reward_speed_extreme, 0)

        self.assertTrue(reward_speed_extreme > self.reward_baseline)
        self.assertTrue(reward_speed_stopped < self.reward_baseline)

    def test_out_of_bounds_steps(self):
        params_steps_extreme = dict(
            x=0.5,
            y=0.5,
            track_width=2,
            speed=5.0,
            progress=2,
            steps=50,
            closest_waypoints=[1, 2],
            steering_angle=0,
        )

        reward_steps_extreme = reward_function(params_steps_extreme)
        self.assertNotEqual(reward_steps_extreme, 0)
        self.assertTrue(reward_steps_extreme < self.reward_baseline)

    def test_out_of_bounds_progress(self):
        params_big_progress = dict(
            x=0.5,
            y=0.5,
            track_width=2,
            speed=5.0,
            progress=98,
            steps=4,
            closest_waypoints=[1, 2],
            steering_angle=0,
        )

        reward_big_progress = reward_function(params_big_progress)
        self.assertNotEqual(reward_big_progress, 0)
        self.assertTrue(reward_big_progress > self.reward_baseline)


if __name__ == '__main__':
    unittest.main()
