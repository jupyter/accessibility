import os
import sys

class DocGenerator:
    """A Class to represent a documentation generator

    Attributes: None

    Methods
    _________
    get_chunk_paths()
        returns the chunks that have been made
    """


    #CHUNKED DOCUMENTS
    INTRO_DOC = "./docs/readme_chunks/introduction.md"
    GET_INVOLVED = "./docs/readme_chunks/getinvolved.md"
    ACC_STANDARDS = "./docs/readme_chunks/accessibility_standards.md"

    # INTERNAL MESSAGES
    DIR_ERR = "Error: please call from top directory, docs directory, or readme_chunks directory."

    # PATHS TO WRITE TO
    RTD_INDEX = "./docs/index.md"
    REPO_README = "./README.md"


    def __init__(self):
        """
        Constructs attributes needed for the object.
        Additionally, parses chunk files and writes README files.
        """
        current_path = os.getcwd()
        working_directory = current_path.split("/")[-1]
        if self.__valid_directory(working_directory):
            pass
        else:
            print(self.DIR_ERR)
            sys.exit(0)
        self.__parse_files()
        self.__write_readme_files(self.introlines,self.involvelines,self.standard)


    def get_chunk_paths(self):
        """
        Returns paths to chunked files

        No Parameters.

        Returns: List of file paths
        """
        return[self.INTRO_DOC,self.GET_INVOLVED,self.ACC_STANDARDS]


    def __valid_directory(self,working_directory:str):
        """Checks if the name of the directory is valid

        Args:
            working_directory (str): Last part of a filepath.

        Returns:
            Boolean: Whether the filepath was valid
        """
        if working_directory == "accessibility":
            return True
        if working_directory == "docs":
            os.chdir("../")
            return True
        if working_directory == "readme_chunks":
            os.chdir("../../")
            return True
        return False


    def __parse_files(self):
        """
        Parses chunked files using paths stored in variables

        Saves the contents of a file as a list of strings,
        where each string represents a line in the file.
        Assumes that the files are encoded in utf-8.
        """
        with open(self.INTRO_DOC,encoding="utf-8") as intro:
            with open(self.GET_INVOLVED,encoding="utf-8") as getinvolve:
                with open(self.ACC_STANDARDS,encoding="utf-8") as standards:
                    self.introlines = intro.readlines()
                    self.involvelines = getinvolve.readlines()
                    self.standard = standards.readlines()


    def __write_readme_files(self,intro:list,involve:list,standard:list):
        """_summary_

        Args:
            intro (list): Strings, who each represent one line of the 'intro_doc' chunk
            involve (list):  Strings, who each represent one line of the 'get_involved' chunk
            standard (list):  Strings, who each represent one line of the 'acc_standards' chunk
        """
        with open(self.RTD_INDEX,"w",encoding="utf-8") as index:
            index.writelines(intro)
            index.writelines(involve)
            index.writelines(standard)

        with open(self.REPO_README,"w",encoding="utf-8") as readme:
            readme.writelines(intro)
            readme.writelines(standard)


if __name__ == "__main__":
    dc = DocGenerator()
