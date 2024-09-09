import random

def init_weights(num_weights):
    weights = [random.uniform(-1, 1) for i in range(num_weights)]
    return weights

def cal(inputs, weights, bias):
    output = sum(i * w for i, w in zip(inputs, weights)) + bias
    return output

def cal_neuron(num_neuron, inputs):
    outputs = []
    for _ in range(num_neuron):
        weights = init_weights(len(inputs))
        bias = 2.0  # bias 값을 2.0으로 고정
        output = cal(inputs, weights, bias)
        outputs.append(output)
    return outputs

num_neuron = int(input("뉴런 개수 입력: "))

inputs = [1.0, 2.0, 3.0, 4.0]

outputs = cal_neuron(num_neuron, inputs)

print(f"Inputs: {inputs}")
print(f"Outputs: {outputs}")