from utils import generate_md_file
import bibtexparser
import os

repository_url = "https://github.com/TLESORT/Automatic_Awesome_Bibliography"
bibfile_name = 'bibtex.bib'
folder_name = "Mardown_Files"
add_comments = False

with open(bibfile_name) as bibtex_file:
    bibtex_str = bibtex_file.read()

bib_db = bibtexparser.loads(bibtex_str)


################################### SORT BY CONFERENCE ####################################
def plot_conf_title(conference):
    return '\n' + "## " + conference[-1] + " (" + conference[0] + ")" + '\n'


conferences_list = [["ICLR", "International Conference on Learning Representations"],
               ["CVPR", "Conference on Computer Vision and Pattern Recognition"],
               ["ICCV", "International Conference on Computer Vision"],
               ["ECCV", "European Conference on Computer Vision"],
               ["NeuriPS", "NIPS", "Neural Information Processing Systems"],
               ["ICML", "International Conference on Machine Learning"],
               ["IJCAI", "International Joint Conference on Artificial Intelligence"],
               ["IJCNN", "International Joint Conference on Neural Networks"],
               ["ICANN", "International Conference on Artificial Neural Networks"]]

output_file = os.path.join("Mardown_Files", "Conferences_Bibliography.md")
generate_md_file(DB=bib_db,
                 list_classif=conferences_list,
                 key="booktitle",
                 plot_title_fct=plot_conf_title,
                 filename=output_file,
                 url=repository_url,
                 bibfile=bibfile_name,
                 add_comments=add_comments)


################################### SORT BY AUTHORS ####################################

def plot_years_title(year):
    return '\n' + "## Papers in " + year[0] + '\n'


years = []
for i in range(1950, 2021):
    years.append([str(i)])
years.reverse()

output_file = os.path.join(folder_name, "Chronological_Bibliography.md")
generate_md_file(DB=bib_db,
                 list_classif=years,
                 key="year",
                 plot_title_fct=plot_years_title,
                 filename=output_file,
                 url=repository_url,
                 bibfile=bibfile_name,
                 add_comments=add_comments)


################################### SORT BY KEYWORDS ####################################


def plot_keyword_title(keyword):
    return '\n' + "## " + keyword[0] + '\n'


keywords = [["Rehearsal"],
            ["Generative Replay"],
            ["Dynamic Architecture"],
            ["Regularization"],
            ["Meta-Learning", "Meta"],
            ["Replay"]]

output_file = os.path.join(folder_name, "Classification_Bibliography.md")
generate_md_file(DB=bib_db,
                 list_classif=keywords,
                 key="keywords",
                 plot_title_fct=plot_keyword_title,
                 filename=output_file,
                 url=repository_url,
                 bibfile=bibfile_name,
                 add_comments=add_comments)


################################### By ID List ####################################

def plot_by_ID_title(ID_name):
    return '\n' + "## Personnal Selection : " + ID_name[0] + '\n'


IDs = [["Lifelong", "Ramapuram17", "hou2018lifelong", "Chen2018Lifelong", "Soltoggio2019Born"],
       ["Generative Replay", "Shin17", "lesort2018generative"]]

output_file = os.path.join(folder_name, "Selection_Bibliography.md")
generate_md_file(DB=bib_db,
                 list_classif=IDs,
                 key="ID",
                 plot_title_fct=plot_by_ID_title,
                 filename=output_file,
                 url=repository_url,
                 bibfile=bibfile_name,
                 add_comments=add_comments)


################################### MY PAPERS ####################################

def plot_my_papers_title(_):
    return '\n' + "## My Papers" '\n'


authors = [["Lesort"]]

output_file = os.path.join(folder_name, "My_Bibliography.md")
generate_md_file(DB=bib_db,
                 list_classif=authors,
                 key="author",
                 plot_title_fct=plot_my_papers_title,
                 filename=output_file,
                 url=repository_url,
                 bibfile=bibfile_name,
                 add_comments=add_comments)
