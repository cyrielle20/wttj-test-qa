#!/usr/bin/env python
import csv
import sys

def list_category_id(file):

    file = open(file, "r")
    reader=csv.DictReader(file)
    cat_id = {}
    for row in reader:
        if (row['category_name'] not in cat_id.keys()):
            cat_id[row['category_name']] = [row['id']]
        else:
            cat_id[row['category_name']].append(row['id'])
    return cat_id


def count_job_contract_type(file, ids):
    file_job = open(file, "r")
    reader=csv.DictReader(file_job)
    contract_type_count = {}
    total = 0
    for row in reader:
        if (row['profession_id'] in ids):
            total = total + 1
            if (row['contract_type'] not in contract_type_count):
                contract_type_count[row['contract_type']] = 1
            else:
               contract_type_count[row['contract_type']] = contract_type_count[row['contract_type']] + 1
    file_job.close()
    return contract_type_count, total

def list_contract_by_category(file1, file2):
    cat_id=list_category_id(file1)
    for key in cat_id.keys():
        count, total = count_job_contract_type(file2,  cat_id[key])
        import ipdb; ipdb.set_trace()
        print(key, total, count)


list_contract_by_category(sys.argv[1], sys.argv[2])
