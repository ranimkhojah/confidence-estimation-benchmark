import os
import argparse

def main(args):
    version = args.version
    config_file = args.config_file
    extra = args.extra
    nlu_name = 'rasa-sklearn'
    train_set = '../../datasets/' + nlu_name + '/v' + str(version) + '/' + nlu_name +'_split_6_train_v' + str(version) +'.yml'
    test_set = '../../datasets/' + nlu_name + '/v' + str(version) + '/' + nlu_name + '_split_6_test_v' + str(version) + '.csv'
    output_file = '../../results/' + nlu_name + '/v' + str(version) + '/' + nlu_name + '_split_6_results_v' + str(version) + '.json'
    # train
    model_name = 'nlu_model_v' + str(version) + extra
    model_path = 'models/' + model_name + '.tar.gz'
    os.system("rasa train nlu --nlu " + train_set + " --config " + config_file + " --fixed-model-name " + model_name)
    # test
    os.system("python rasa_opensource.py --model "+ model_path + " -t " + test_set + " -o " + output_file)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help = "version of the dataset", default=1)
    parser.add_argument("-x", "--extra", help = "extra feature name", default="")
    parser.add_argument("-c", "--config_file", help = "pipeline config file for training rasa", default="config.yml")

    args = parser.parse_args()
    
    main(args)