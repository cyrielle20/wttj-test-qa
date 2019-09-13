#!/usr/bin/env python
import csv
import sys


def list_profession_id(profession_file):

    file = open(profession_file, "r")
    reader=csv.DictReader(file)
    profession_ids = {}

    for row in reader:
        if (row['category_name'] not in profession_ids.keys()):
            profession_ids[row['category_name']] = [row['id']]
        else:
            profession_ids[row['category_name']].append(row['id'])
    file.close()
    return profession_ids


def count_jobs_by_profession_and_contract(profession_file, job_file):

    profession_ids=list_profession_id(profession_file)
    file = open(job_file, "r")
    reader=csv.DictReader(file)
    profession_id_contract_type_count = {}

    for row in reader:
        for key, values in profession_ids.items():
            if row['profession_id'] in values:
                category_name = key
        if category_name not in profession_id_contract_type_count:
            profession_id_contract_type_count[category_name] = {}

        if (row['contract_type']) not in profession_id_contract_type_count[category_name]:
            profession_id_contract_type_count[category_name][row['contract_type']] = 1
        else:
            profession_id_contract_type_count[category_name][row['contract_type']] += 1

    file.close()
    return profession_id_contract_type_count


def print_jobs_by_profession_and_contract(profession_file, job_file):

        map = count_jobs_by_profession_and_contract(profession_file, job_file)
        for key, values in map.items():
            total = 0
            print(key)
            for val in sorted(values):
                print("    ", val, values[val])
                total = total + values[val]
            print(" "+"TOTAL", total)


print_jobs_by_profession_and_contract(sys.argv[1], sys.argv[2])
