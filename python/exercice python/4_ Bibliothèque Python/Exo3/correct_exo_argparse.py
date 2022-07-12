import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str, help="nom du fichier à créer")
parser.add_argument("-p", "--path", type=str, help="chemin vers le dossier à scanner")
args = parser.parse_args()

if args.path:
    ls = os.listdir(args.path)
    for i in ls:
        print(i)
        
if args.file:
    with open(args.file, "x"):
        print("le fichier {} a bien été créé".format(args.file))