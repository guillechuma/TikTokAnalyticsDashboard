
# Convert processing code to function
def process_results(data):

    nested_values = ['video', 'author', 'music', 'stats', 'authorStats', 'challenges', 'duetInfo', 'textExtra', 'stickersOnItem']
    skip_values = ['challenges', 'duetInfo', 'textExtra', 'stickersOnItem']

    # Create blank dictionary
    flattened_data = {}
    
    # Loop through each video (JSON) with an assigned unique key identifier
    for idx, value in enumerate(data):
        # Create new record in flattened data dict
        flattened_data[idx] = {}
        # loop through each property in each video
        for prop_idx, prop_value in value.items():
            # First add flat data (no nested vars)
            # Case the key is nested
            if prop_idx in nested_values:
                # Check if key is in skip list
                if prop_idx in skip_values:
                    pass # Skip
                else: # Is nested and not skip, process it
                    # Unflatten it (loop through it)
                    # Loop through each nested property (prop_value)
                    for nested_idx, nested_value in prop_value.items():
                        flattened_data[idx][prop_idx + '_' + nested_idx] = nested_value
                    
            else: # If not in nested values, go ahead and add it to the flattened dictionary
                flattened_data[idx][prop_idx] = prop_value
    
    return flattened_data