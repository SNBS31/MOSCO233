def reward_function(params):
    
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    abs_steering_angle = abs(params['steering_angle']) # First change
    
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3
        
    ABS_STEERING_THRESHOLD = 15                       # Second change
    if abs_steering_angle > ABS_STEERING_THRESHOLD:
        reward *= 0.8                               # That is, assigning a penalty for excessiive steering angle
            
    return float(reward)                