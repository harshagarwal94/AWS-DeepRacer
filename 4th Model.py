import math
def reward_function(params):
    # Example of rewarding the agent to follow center line

    # Read input parameters
    
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    
    abs_steering = abs(params['steering_angle'])
    
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    # Calculate 3 markers that are at varying distances away from the center line
    #Distance from centre
    
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward *= 1.8
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3 # likely crashed/ close to off track
    
    #steering angle     
    ABS_STEERING_THRESHOLD = 3
    if abs_steering > ABS_STEERING_THRESHOLD:
        #penalty
        reward *= 0.8
    
    ## Set the speed threshold based your action space
    SPEED_THRESHOLD = 1.0

    if not all_wheels_on_track:
        # Penalize if the car goes off track
        reward *= 1e-3
    elif speed < SPEED_THRESHOLD:
        # Penalize if the car goes too slow
        reward *= 0.7
    else:
        # High reward if the car stays on track and goes fast
        reward *= 2.5
        
        
        
# Initialize the reward with typical value
    reward = 1.0

    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD = 3.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5




## Calculate the distance from each border
    distance_from_border = 0.5 * track_width - distance_from_center

    # Reward higher if the car stays inside the track borders
    if distance_from_border >= 0.25:
        reward *= 2.0
    else:
        reward * = 1e-3 # Low reward if too close to the border or goes off the track

    return float(reward)
