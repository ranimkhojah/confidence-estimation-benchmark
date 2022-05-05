import os
import os.path
from os import path
import argparse

def main(args):
    num_splits = args.splits
    version = args.version
    config_file = args.config_file
    extra = args.extra
    
    if 'spacy' in config_file:
        nlu_name = 'rasa-sklearn'
    else:
        nlu_name = 'rasa-diet'
        
    for split in range(num_splits):
        split_num = split + 1
        
        # get files names
        train_set = '../../datasets/' + nlu_name + '/v' + str(version) + '/' + nlu_name +'_split_' + str(split_num) + '_train_v' + str(version) +'.yml'
        test_set = '../../datasets/' + nlu_name + '/v' + str(version) + '/' + nlu_name + '_split_' + str(split_num) + '_test_v' + str(version) + '.csv'
        output_file = '../../results/' + nlu_name + '/v' + str(version) + '/' + nlu_name + '_split_' + str(split_num) + '_results_v' + str(version) + '.json'
        
        if not path.exists('../../results/' + nlu_name):
            os.mkdir('../../results/' + nlu_name)
        if not path.exists('../../results/' + nlu_name + '/v' + str(version)):
            os.mkdir('../../results/' + nlu_name + '/v' + str(version))
            
        # train
        model_name = nlu_name + '_nlu_model_' + str(split_num) + '_v' + str(version) 
        model_path = 'models/' + nlu_name + '_nlu_model_' + str(split_num) + '_v' + str(version) + '.tar.gz'
        os.system("rasa train nlu --nlu " + train_set + " --config " + config_file + " --fixed-model-name " + model_name)
        
        # test
        os.system("python rasa_opensource.py --model "+ model_path + " -t " + test_set + " -o " + output_file)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help = "version of the dataset", default=1)
    parser.add_argument("-c", "--config_file", help = "pipeline config file for training rasa", default="config.yml")
    parser.add_argument("-s", "--splits", help = "number of splits/ iterations to run in repeated random subsampling", default=10)
    parser.add_argument("-x", "--extra", help = "extra feature name", default="")

    args = parser.parse_args()
    
    main(args)