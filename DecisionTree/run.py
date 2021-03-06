#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'run decision tree'

import sys

from ReadData import ReadData
from DecisionTree import DecisionTree

# data_set directory
DATA_DIRECTORY = 'data_sets1'


def main(args):
    # judge input arguments length
    if len(args) != 6:
        print('Should Have Six Input Arguments')
        exit(0)

    # input parameters
    L = int(args[0])
    K = int(args[1])
    training_set_file_name = args[2]
    validation_set_file_name = args[3]
    test_set_file_name = args[4]
    to_print = True if args[5].lower() == 'yes' else False

    path = './' + DATA_DIRECTORY + '/'

    # read data from training set, test set, and validation set
    rd = ReadData()
    labels, training_set = rd.createDataSet(path + training_set_file_name)
    labels, validation_set = rd.createDataSet(path + validation_set_file_name)
    labels, test_set = rd.createDataSet(path + test_set_file_name)

    # build tree
    dt = DecisionTree()

    info_gain_tree_root = dt.buildDT(training_set, labels.copy(), 'information_gain')
    pruned_info_gain_tree_root = dt.pruneTree(info_gain_tree_root, L, K, validation_set, labels)

    variance_impurity_tree_root = dt.buildDT(training_set, labels.copy(), 'variance_impurity')
    pruned_variance_impurity_tree_root = dt.pruneTree(variance_impurity_tree_root, L, K, validation_set, labels)

    print()
    info_accuracy = dt.calAccuracy(test_set, info_gain_tree_root, labels)
    print('Accuracy of decision tree constructed using information gain: %s' % info_accuracy)
    variance_accuracy = dt.calAccuracy(test_set, variance_impurity_tree_root, labels)
    print('Accuracy of decision tree constructed using variance impurity: %s' % variance_accuracy)

    prune_info_accuracy = dt.calAccuracy(test_set, pruned_info_gain_tree_root, labels)
    print('Accuracy of pruned decision tree constructed using information gain: %s' % prune_info_accuracy)

    pruned_variance_accuracy = dt.calAccuracy(test_set, pruned_variance_impurity_tree_root, labels)
    print('Accuracy of pruned decision tree constructed using variance impurity: %s' % pruned_variance_accuracy)

    if (to_print):
        print()
        print('Build Decision Tree By Using Information Gain')
        info_gain_tree_root.printTree()

        print()

        print()
        print('Build Decision Tree By Using Variance Impurity')
        variance_impurity_tree_root.printTree()
        print()


if __name__ == "__main__":
    main(sys.argv[1:])
