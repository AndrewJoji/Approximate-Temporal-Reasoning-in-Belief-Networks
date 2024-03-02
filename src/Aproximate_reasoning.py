import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
csv_path = './data/rs_1.csv'  
data = pd.read_csv(csv_path, header=None, names=['Sample_Result'])

# Filter out rejected samples and calculate cumulative counts for accepted samples
accepted_samples = data[data['Sample_Result'] != -1].copy()
accepted_samples['Cumulative_R_T'] = (accepted_samples['Sample_Result'] == 1).cumsum()
accepted_samples['Cumulative_Total'] = np.arange(1, len(accepted_samples) + 1)
accepted_samples['P_r_given_s_w'] = accepted_samples['Cumulative_R_T'] / accepted_samples['Cumulative_Total']

total_accepted_samples_up_to_100000 = accepted_samples['P_r_given_s_w'].iloc[-1]

# Find the number of accepted samples up to the 100,000th generated sample
num_accepted_samples_up_to_100000 = accepted_samples[accepted_samples.index < 100000]['P_r_given_s_w'].count()
approximation_value = accepted_samples.iloc[num_accepted_samples_up_to_100000 - 1]['P_r_given_s_w'] if num_accepted_samples_up_to_100000 else None

plt.figure(figsize=(12, 8))
plt.plot(accepted_samples['Cumulative_Total'], accepted_samples['P_r_given_s_w'], label='P(r|s,w)', color='blue')
plt.xscale('log')  
plt.xlabel('Number of Accepted Samples (N) [Log Scale]')
plt.ylabel('P(r|s,w)')
plt.title('Probability of Rain Given Sprinkler is On and Grass is Wet')
plt.annotate(f'Approximation: {approximation_value:.4f}', 
            xy=(num_accepted_samples_up_to_100000, approximation_value), 
            xytext=(num_accepted_samples_up_to_100000, approximation_value - 0.1),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            horizontalalignment='left', verticalalignment='bottom')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()

# Calculate dynamic delta for confidence bounds
delta_dynamic = 1.3581 * (1 / accepted_samples['Cumulative_Total']**0.5)
accepted_samples['Dynamic_Upper_Confidence_Bound'] = accepted_samples['P_r_given_s_w'] + delta_dynamic
accepted_samples['Dynamic_Lower_Confidence_Bound'] = np.maximum(0, accepted_samples['P_r_given_s_w'] - delta_dynamic)

# Plot with dynamic confidence bounds
plt.figure(figsize=(12, 8))
plt.plot(accepted_samples['Cumulative_Total'], accepted_samples['P_r_given_s_w'], label='P(r|s,w)', color='blue')
plt.fill_between(accepted_samples['Cumulative_Total'], accepted_samples['Dynamic_Lower_Confidence_Bound'], accepted_samples['Dynamic_Upper_Confidence_Bound'], color='lightblue', alpha=0.5, label='Confidence Bounds')
plt.xscale('log') 
plt.xlabel('Number of Accepted Samples (N) [Log Scale]')
plt.ylabel('P(r|s,w) with Dynamic Confidence Bounds')
plt.title('Augmented Probability of Rain with Dynamic Confidence Bounds')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()


csv_path_lw = './data/lw_1.csv'
data_lw = pd.read_csv(csv_path_lw, header=None, names=['Sample_Result', 'Weight'])

# Calculate the weighted probability estimate P(r|s,w)
weighted_sum_r_t_lw = (data_lw['Sample_Result'] == 1) * data_lw['Weight']
total_weight_lw = data_lw['Weight'].sum()
p_r_given_s_w_weighted = weighted_sum_r_t_lw.sum() / total_weight_lw

# Plot for likelihood weighting results
plt.figure(figsize=(12, 8))
plt.plot(np.arange(1, len(data_lw) + 1), np.cumsum(weighted_sum_r_t_lw).cumsum() / np.cumsum(data_lw['Weight']).cumsum(), label='P(r|s,w) Weighted', color='blue')
plt.xscale('log')
plt.xlabel('Number of Samples (N) [Log Scale]')
plt.ylabel('Weighted P(r|s,w)')
plt.title('Weighted Probability of Rain Given Sprinkler is On and Grass is Wet')
plt.annotate(f'Final Weighted Approximation: {p_r_given_s_w_weighted:.4f}', 
             xy=(len(data_lw), p_r_given_s_w_weighted), 
             xytext=(-100, 20), textcoords="offset points",
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3"),
             horizontalalignment='right', verticalalignment='bottom')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()

print(f"The algorithm's approximation of P(r|s,w) using 100,000 samples (weighted): {p_r_given_s_w_weighted:.4f}")