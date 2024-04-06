import numpy as np

def generate_data(num_nodes, average_bytes_per_edge, count):
    
    num_edges = num_nodes * (num_nodes - 1) / 2
    data = []
    
    while count > 0:
        
        count -= 1
        
        row_data = []
        
        # With Chance 95%
        if np.random.uniform(0, 1) < 0.95:
            for i in range(int(num_edges)):
                sample_noise = np.random.normal(0, 1)
                row_data.append(average_bytes_per_edge + average_bytes_per_edge*sample_noise)
        else:
            # Anomalies
            for i in range(int(num_edges)):
                sample_noise = np.random.normal(0, 1)
                row_data.append(average_bytes_per_edge + average_bytes_per_edge*sample_noise + np.random.uniform(0, 1)*3)

        data.append(row_data)
        
    return data