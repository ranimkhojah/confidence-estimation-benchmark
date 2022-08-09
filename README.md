# Confidence estimation benchmark for Natural Language Understanding (NLU)

This repository contains benchmarks that have been used to evaluate confidence estimation in NLU for dialogue systems. In detail, benchmarks are provided to measure the calibration and performance of NLUs on model and rank level.

## About
The benchmark is further described in R. Khojah, A. Berman and S. Larsson, "_Evaluating N-best Calibration of Natural Language Understanding for Dialogue Systems_" (Proceedings of SIGDIAL 2022, forthcoming) and Ranim Khojah, "_Evaluating Confidence Estimation of NLUs for Dialogue Systems_" (Master's thesis in Language Technology (Spring 2022), supervised by Staffan Larsson and Alexander Berman).

## Resources
The evaluation involves 5 NLU Services, namely IBM's Watson Assistant, Language Understanding Intelligent Service (LUIS), Snips, Rasa (Sklearn Classifier) and Rasa (DIET Classifier). 

We train the NLUs on intent classification tasks using the dataset proposed by Liu et al. (2021).

## Content
The repository contains:
  1. Subset of the dataset that have been used in the evaluation.
  2. Scripts to reformat the training set to an acceptable format in regard to the NLU.
  3. Scripts to train Snips and Rasa.
  4. Scripts to test Watson, LUIS, Snips and Rasa.
  5. Script to evaluate NLU performance.
  6. Script to evaluate the calibration on model and rank level.
  7. Results of the evaluation study.

## Requirements
NLU requirements:
```
Rasa 2.4.3
ibm-watson==6.0.0
ibm-cloud-sdk-core==3.15.1
snips_nlu==0.20.2
```
Env. requirements are in [requirements.txt](requirements.txt) and Rasa-related requirements in [rasa-requirements.txt](models/rasa/requirements.txt).

## Contact 🦦
Please contact rankhojah@gmail.com if you have any questions.





### References
Liu, X., Eshghi, A., Swietojanski, P., & Rieser, V. (2021). Benchmarking natural language understanding services for building conversational agents. In _Increasing Naturalness and Flexibility in Spoken Dialogue Interaction_ (pp. 165-183). Springer, Singapore.
