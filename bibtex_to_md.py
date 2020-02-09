

from utils import get_md_entry
import bibtexparser

file_name = 'bibtex.bib'
with open(file_name) as bibtex_file:
    bibtex_str = bibtex_file.read()

bb_db = bibtexparser.loads(bibtex_str)
list_of_dic = bb_db.entries


bb_db = bibtexparser.loads(bibtex_str)
list_of_dic = bb_db.entries

def get_md(DB, item, key):

    all_str = ""

    number_of_entries = len(DB)
    for i in range(number_of_entries):
        if key in DB[i].keys():
            #if conference in DB[i][key]:
            if any(elem in DB[i][key] for elem in item):
                all_str += get_md_entry(DB[i])

    return all_str


def generate_md_file(DB, list_classif, key, plot_title_fct, filename):
    """

    :param DB: list of dictionnary with bibtex inside
    :param list_classif: list with categories we want to put inside md file
    :param key: key allowing to search in the bibtex dictionnary author/ID/year/keyword...
    :param plot_title_fct: function to plot category title
    :param filename: name of the markdown file
    :return: nothing
    """

    all_in_one_str = ""

    for item in list_classif:

        str = get_md(list_of_dic, item, key)

        if str != "":
            all_in_one_str += plot_title_fct(item)
            all_in_one_str += str

    f = open(filename, "w")
    f.write(all_in_one_str.encode('utf8'))
    f.close()


################################### SORT BY CONFERENCE ####################################
def plot_conf_title(conference):
    return '\n' + "## " + conference[-1] + " (" + conference[0] + ")" + '\n'

conferences = [["ICLR", "International Conference on Learning Representations"],
               ["CVPR", "Conference on Computer Vision and Pattern Recognition"],
               ["ICCV", "International Conference on Computer Vision"],
               ["ECCV", "European Conference on Computer Vision"],
               ["NeuriPS", "NIPS", "Neural Information Processing Systems"],
               ["ICML", "International Conference on Machine Learning"]]

generate_md_file(DB=list_of_dic, list_classif=conferences, key="booktitle", plot_title_fct=plot_conf_title, filename= "Conferences_Bibliography.md")


################################### SORT BY AUTHORS ####################################

def plot_years_title(year):
    return '\n' + "## Papers in " + year[0] + '\n'

years = []
for i in range(1950, 2021):
    years.append([str(i)])
years.reverse()
generate_md_file(DB=list_of_dic, list_classif=years, key="year", plot_title_fct=plot_years_title, filename= "Chronological_Bibliography.md")


################################### SORT BY KEYWORDS ####################################


def plot_keyword_title(keyword):
    return '\n' + "## " + keyword[0] + '\n'

keywords = [["Meta-Learning", "Meta"],
               ["Rehearsal"],
               ["Generative Replay"],
               ["Dynamic Architecture"],
               ["Regularization"],
               ["Replay"]]

generate_md_file(DB=list_of_dic, list_classif=keywords, key="keyword", plot_title_fct=plot_keyword_title, filename= "Classification_Bibliography.md")


################################### By ID List ####################################

def plot_by_ID_title(ID_name):
    return '\n' + "## Personnal Selection : " + ID_name[0] + '\n'

IDs = [["Lifelong", "Ramapuram17","hou2018lifelong","Chen2018Lifelong","Soltoggio2019Born"],
       ["Generative Replay", "Shin17","lesort2018generative"]]

generate_md_file(DB=list_of_dic, list_classif=IDs, key="ID", plot_title_fct=plot_by_ID_title, filename= "Selection_Bibliography.md")

################################### MY PAPERS ####################################

def plot_my_papers_title(_):
    return '\n' + "## My Papers" '\n'

authors = [["Lesort"]]

generate_md_file(DB=list_of_dic, list_classif=authors, key="author", plot_title_fct=plot_my_papers_title, filename= "My_Bibliography.md")





