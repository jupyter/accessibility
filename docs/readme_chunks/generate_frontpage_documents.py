import os

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
    with open("./docs/readme_chunks/introduction.md") as intro:
        with open("./docs/readme_chunks/getinvolved.md") as getinvolve:
            with open("./docs/readme_chunks/accessibility_standards.md") as standards:
                introlines = intro.readlines()
                involvelines = getinvolve.readlines()
                standard = standards.readlines()
                writefiles(introlines,involvelines,standard)
                

def writefiles(intro,involve,standard):
    with open("./docs/index.md","w") as index:
        index_writer = index.writelines(intro)
        index_writer = index.writelines(involve)
        index_writer = index.writelines(standard)

    with open("./README.md","w") as readme:
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