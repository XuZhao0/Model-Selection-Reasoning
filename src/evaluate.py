import argparse
from tool import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, required=True)
    parser.add_argument('--dataset_type', type=str,
                        choices=['math', 'date'], required=True)
    args = parser.parse_args()

    input_path = args.input_path
    dataset_type = args.dataset_type

    output_data = jsonlines_load(input_path)

    total = 0
    correct = 0
    error = 0
    for i in range(len(output_data)):
        if dataset_type == 'math':
            if output_data[i]['majority_ans'] is not None:
                if abs(output_data[i]['majority_ans'] - output_data[i]['answer']) < 1e-3:
                    correct += 1
            else:
                error += 1

        else:
            if output_data[i]['final_ans'] == output_data[i]['answer']:
                correct += 1
            else:
                error += 1

        total += 1

    print(
        f'Accuracy: {correct/total}, Total: {total}, Correct: {correct}, Error: {error}')
