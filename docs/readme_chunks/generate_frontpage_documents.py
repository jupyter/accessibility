import os
from paths import *


def validDirectory(wd):
    if wd == "accessibility":
        return True
    elif wd == "docs":
        os.chdir("../")
        return True
    elif wd == "readme_chunks":
        os.chdir("../../")
        return True
    return False

def parsefiles():
    with open(INTRO_DOC) as intro:
        with open(GET_INVOLVED) as getinvolve:
            with open(ACC_STANDARDS) as standards:
                introlines = intro.readlines()
                involvelines = getinvolve.readlines()
                standard = standards.readlines()
                writefiles(introlines,involvelines,standard)
                

def writefiles(intro,involve,standard):
    with open(RTD_INDEX,"w") as index:
        index_writer = index.writelines(intro)
        index_writer = index.writelines(involve)
        index_writer = index.writelines(standard)

    with open(REPO_README,"w") as readme:
        readme_writer = readme.writelines(intro)
        readme_writer = readme.writelines(standard)

def main():
    pat = os.getcwd()
    wd = pat.split("/")[-1]
    if validDirectory(wd):
        pass
    else:
        print("Error: please call from top directory, docs directory, or readme_chunks directory.")
        exit(0)
    newpat = os.getcwd()
    wd = newpat.split("/")[-1]
    if wd != "accessibility":
        exit(0)
    else:
        parsefiles()

if __name__ == "__main__":
    main()