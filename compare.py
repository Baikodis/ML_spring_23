# import argparse
#
#
# def download_path(pars):
#     path_head = pars.inputt
#     mass = []
#     with open(f'{path_head}', "r") as main_file:
#         for line in main_file:
#             paths = line.split(" ")
#             paths[1] = paths[1].replace("\n", "")
#             mass.append(paths)
#
#
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#
#     parser.add_argument("inputt")
#     parser.add_argument("scores")


mass = []
with open("head.txt", "r") as main_file:
    for line in main_file:
        paths = line.split(" ")
        paths[1] = paths[1].replace("\n", "")
        mass.append(paths)
print(mass)
with open(f'{mass[0][0]}', "r") as file:
    print(file.read())
