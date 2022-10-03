# AoI-implementation-for-CMA-and-MMW
Cellular Max Age(CMA) and Multi Cell Max Weight(MMW) implementation in adversarial and stochastic environments

## General Overview of the two algorithms

The following paper [1] [*Optimizing Age-of-Information in Adversarial and Stochastic Environments*](https://arxiv.org/pdf/2011.05563.pdf)
deals with the AoI minimization problem in both adversarial and stochastic environments. In the adversarial framework, adversary has complete knowledge of the scheduling policy and models the channel statistics based on the scheduling decisions. While the scheduling policy only has the causal information of the channel states and user mobility. In the adversarial framework we deal with an important performance metric known as the competitive ratio, which is defined as the worst case ratio of the cost incurred by an online policy to the cost incurred by an optimal offline policy(OPT). The OPT has the knowledge of the complete sequence $\sigma$ over the entire time horizon $T$. Here, $\sigma$ is the sequence representing the channel states and the user's locations. In the adversarial setting the optimality is achieved making no specific assumptions on the channel statistics or user mobility both of which can be dictated by an omniscient adversary. The CMA policy, Base station schedules the user having maximum age in it's cell during each time slot. Results show that CMA is $2N^2$ competitive in average AoI case and $2N$ competitive in peak AoI case against any optimal offline policy. Yao's Minimax principle obtains lower bound to the competitive ratio that any online policy can achieve in both average and peak AoI case. In the stochastic setting, the Multi Cell Max weight(MMW) gives a 2 approximation guarantee in the average age metric for static mobile users located in a single cell and for users with i.i.d uniform mobility. While for the peak AoI metric, the same greedy is optimal. The CMA policy achieves large deviation exponent in which the maximum age stays below a threshold age with high probability. 
	     
# References

[1] [*Optimizing Age-of-Information in Adversarial and Stochastic Environments*](https://arxiv.org/pdf/2011.05563.pdf)

[2] [*Competitive Algorithms for Minimizing the Maximum Age-of-Information*](https://www.tifr.res.in/~abhishek.sinha/files/MAMA2020Sinha.pdf)
