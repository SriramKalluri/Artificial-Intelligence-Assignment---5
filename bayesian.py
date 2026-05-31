# bayesian.py
# Simple Bayesian Network 

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


# Create the network structure
# Flu causes Fever and Cough

model = DiscreteBayesianNetwork([
    ('Flu', 'Fever'),
    ('Flu', 'Cough')
])


# Probability of Flu
# 0 = No
# 1 = Yes

cpd_flu = TabularCPD(
    variable='Flu',
    variable_card=2,
    values=[
        [0.9],
        [0.1]
    ]
)


# Probability of Fever given Flu

cpd_fever = TabularCPD(
    variable='Fever',
    variable_card=2,

    values=[
        [0.7, 0.2],
        [0.3, 0.8]
    ],

    evidence=['Flu'],
    evidence_card=[2]
)


# Probability of Cough given Flu

cpd_cough = TabularCPD(
    variable='Cough',
    variable_card=2,

    values=[
        [0.8, 0.3],
        [0.2, 0.7]
    ],

    evidence=['Flu'],
    evidence_card=[2]
)


# Add CPTs to model
model.add_cpds(
    cpd_flu,
    cpd_fever,
    cpd_cough
)


# Check if model is valid
if model.check_model():

    print("Bayesian Network created successfully\n")

else:

    print("Model is invalid")


# Print CPT tables
print("Probability Table for Flu")
print(cpd_flu)

print("\nProbability Table for Fever")
print(cpd_fever)

print("\nProbability Table for Cough")
print(cpd_cough)


# Inference
infer = VariableElimination(model)


# Query 1
print("\nP(Flu | Fever = Yes)\n")

result1 = infer.query(
    variables=['Flu'],
    evidence={'Fever': 1}
)

print(result1)


# Query 2
print("\nP(Flu | Fever = Yes, Cough = Yes)\n")

result2 = infer.query(
    variables=['Flu'],
    evidence={
        'Fever': 1,
        'Cough': 1
    }
)

print(result2)


# Query 3
print("\nP(Flu)\n")

result3 = infer.query(
    variables=['Flu']
)

print(result3)
