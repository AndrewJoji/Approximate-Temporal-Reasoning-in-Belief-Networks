**Analysis of Probabilistic Inference in Belief Networks
**

This project involves the analysis of probabilistic inference within belief networks, focusing on the assessment of two primary sampling techniques: rejection sampling and likelihood weighting. The goal is to interpret and understand the behavior of these anytime algorithms, especially how their results improve with an increasing number of samples.

**Overview**

Given a belief network, we observe two events: the activation of a sprinkler system and the wetness of grass. These observations lead us to estimate the probability of a third event, rain, which is denoted by r. This probability, P(r|s,w), is assessed by analyzing the outcomes of sampling methods.

**Sampling Methods Analysis
**
The analysis is carried out in multiple stages:

Rejection Sampling Visualization: The first task is to visualize the convergence of the rejection sampling method. A dataset containing 100,000 generated samples indicates whether each sample is accepted or rejected, and if accepted, whether the event r is true or false. The visualization plots the cumulative probability estimate of P(r|s,w) as a function of the number of accepted samples, using a logarithmic scale for the x-axis to emphasize behavior at smaller sample sizes.

Confidence Interval Estimation: Using Hoeffding's inequality, a tight bound is derived to estimate the confidence interval around the sample-based probability approximation. The value of this bound, ε, guarantees that the probability of the sample estimate deviating from the true probability by more than ε is less than 5%.

Augmented Visualization: The original plot is augmented with confidence bounds, providing a visual representation of the uncertainty associated with the probability estimate. These bounds are computed dynamically from the cumulative accepted samples.

Likelihood Weighting Analysis: A separate dataset for likelihood weighting contains 100,000 weighted samples. An equivalent analysis is performed, and the results are visualized in a similar manner, incorporating the sample weights into the probability estimate.

**Code Implementation**
Two main scripts are included:

Rejection Sampling and Confidence Intervals: The first script handles the visualization of rejection sampling results and the computation of confidence intervals. It outputs a plot of the estimated probability along with the dynamic confidence bounds.

Likelihood Weighting Visualization: The second script is dedicated to processing and visualizing the results of likelihood weighting, taking into account the weights of the samples to adjust the probability estimate.

**Conclusion**
The completed analysis provides insights into the performance and reliability of approximate inference methods in belief networks. The visualizations demonstrate the convergence properties of the sampling algorithms and quantify the confidence in the probability estimates derived from sample data.
