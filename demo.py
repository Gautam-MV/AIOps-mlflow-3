import os
import mlflow
import argparse

def add_2_num(param1,param2):
    result = param1 + param2
    return result

def main(p1,p2):
    mlflow.log_param("param1",p1)
    mlflow.log_param("param2",p2)
    metric = add_2_num(p1,p2)
    mlflow.log_metric("metric",metric)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("-p1",type=int,default=2)
    args.add_argument("-p2",type=int,default=5)
    parsed_args = args.parse_args()
    main(parsed_args.p1,parsed_args.p2)


