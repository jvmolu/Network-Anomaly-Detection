import numpy as np

def generate_data(num_nodes, average_bytes_per_edge, count, multiplier=3):
    
    num_edges = num_nodes * (num_nodes - 1) / 2
    data = []
    
    while count > 0:
        
        count -= 1
        
        row_data = []
        
        # With Chance 95%
        if np.random.uniform(0, 1) < 0.95:
            for i in range(int(num_edges)):
                sample_noise = np.random.normal(0, 1)
                sample_noise = min(sample_noise, 1) # Cap the noise to 1
                row_data.append(max(average_bytes_per_edge + average_bytes_per_edge*sample_noise, 0))
        else:
            # Anomalies
            for i in range(int(num_edges)):
                row_data.append(3*average_bytes_per_edge + np.random.uniform(3, 4)*multiplier)

        data.append(row_data)
        
    return data