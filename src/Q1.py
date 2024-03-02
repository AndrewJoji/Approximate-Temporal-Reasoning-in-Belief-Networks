import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
csv_path = './rs_1.csv'  
data = pd.read_csv(csv_path, header=None, names=['Sample_Result'])

# Filter out rejected samples and calculate cumulative counts for accepted samples
accepted_samples = data[data['Sample_Result'] != -1].copy()
accepted_samples['Cumulative_R_T'] = (accepted_samples['Sample_Result'] == 1).cumsum()
accepted_samples['Cumulative_Total'] = np.arange(1, len(accepted_samples) + 1)
accepted_samples['P_r_given_s_w'] = accepted_samples['Cumulative_R_T'] / accepted_samples['Cumulative_Total']

# Calculate dynamic delta for confidence bounds
delta_dynamic = 1.3581 * (1 / accepted_samples['Cumulative_Total']**0.5)
accepted_samples['Dynamic_Upper_Confidence_Bound'] = accepted_samples['P_r_given_s_w'] + delta_dynamic
accepted_samples['Dynamic_Lower_Confidence_Bound'] = np.maximum(0, accepted_samples['P_r_given_s_w'] - delta_dynamic)

# Plotting with dynamic confidence bounds
plt.figure(figsize=(12, 8))
plt.plot(accepted_samples['Cumulative_Total'], accepted_samples['P_r_given_s_w'], label='P(r|s,w)', color='blue')
plt.fill_between(accepted_samples['Cumulative_Total'], accepted_samples['Dynamic_Lower_Confidence_Bound'], accepted_samples['Dynamic_Upper_Confidence_Bound'], color='lightblue', alpha=0.5, label='Confidence Bounds')
plt.xscale('log')  # Using logarithmic scale for x-axis
plt.xlabel('Number of Accepted Samples (N) [Log Scale]')
plt.ylabel('P(r|s,w) with Dynamic Confidence Bounds')
plt.title('Augmented Probability of Rain with Dynamic Confidence Bounds')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()
