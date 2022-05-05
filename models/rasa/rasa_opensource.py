from rasa.cli.utils import get_validated_path
from rasa.model import get_model, get_model_subdirectories
from rasa.nlu.model import Interpreter

import argparse
import csv
import json
from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def load_interpreter(model_path):
    model = get_validated_path(model_path, "model")
    model_path = get_model(model)
    _, nlu_model = get_model_subdirectories(model_path)
    return Interpreter.load(nlu_model)
    
    
def main(args):
    model_path = args.model
    test_data = args.test_data
    output_file = args.output_file
    nlu_interpreter = load_interpreter(model_path)
    # read test file
    file = open(test_data)
    reader = csv.reader(file, delimiter=',')

    parsed_utterances = []
    for row in reader:
        intent = row[1]
        utterance = row[0]
        
        # parse an utterance
        res = nlu_interpreter.parse(utterance)
        res['correct_intent'] = intent
        
        # useful to get performance measurements 
        if res['intent']['name'] == intent:
            res['is_correct'] = True
        else:
            res['is_correct'] = False
        
        parsed_utterances.append(res)
        
        
    with open(output_file, 'w') as out:
        json.dump(parsed_utterances, out, indent=2)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model", help = "Path to the Rasa NLU model's file (ends with *.tar.gz)")
    parser.add_argument("-t", "--test_data", help = "Path to the test utterances' csv file")
    parser.add_argument("-o", "--output_file", help = "Path of the output file with the parsing results, default is ../../results/rasa_results.json", default="../../results/rasa_results.json")

    args = parser.parse_args()
    
    main(args)