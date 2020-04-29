import os
import bibtexparser


def keep_last_and_only(authors_str):
    """
    This function is dedicated to parse authors, it removes all the "and" but the last and and replace them with ", "
    :param str: string with authors
    :return: string with authors with only one "and"
    """

    last_author = authors_str.split(" and ")[-1]

    without_and = authors_str.replace(" and ", ", ")

    str_ok = without_and.replace(", " + last_author, " and " + last_author)

    return str_ok


def get_bibtex_line(file, ID):
    filename = "bibtex.bib"
    start_line_number = 0
    end_line_number = 0
    with open(filename, encoding="utf-8") as myFile:
        for num, line in enumerate(myFile, 1):

            # first we look for the beginning line
            if start_line_number == 0:
                if (ID in line) and not ("@String" in line):
                    start_line_number = num
            else:  # after finding the start_line_number we go there
                # the last line contains "}"

                # we are at the next entry we stop here, end_line_number have the goof value
                if "@" in line:
                    assert end_line_number > 0
                    break

                if "}" in line:
                    end_line_number = num
    assert end_line_number > 0
    return start_line_number, end_line_number


def create_bib_link(ID, bibfile):
    link = "bibtex.bib"
    start_bib, end_bib = get_bibtex_line(link, ID)

    # bibtex file is one folder upon markdown files
    link = "../" + link
    link += "#L" + str(start_bib) + "-L" + str(end_bib)

    # L66-L73
    return link


def get_md_entry(DB, entry, bibfile, add_comments=True):
    """
    Generate a markdown line for a specific entry
    :param entry: entry dictionary
    :return: markdown string
    """
    md_str = ""
    md_str += "- **" + entry['title'] + "**"

    md_str += ", (" + entry['year'] + ")"

    if 'url' in entry.keys():
        md_str += " [[paper]](" + entry['url'] + ") "

    md_str += " [[bib]](" + create_bib_link(entry['ID'], bibfile) + ") "

    md_str += " by *" + keep_last_and_only(entry['author']) + "*"

    md_str += '\n'

    if add_comments:
        # maybe there is a comment to write
        if entry['ID'].lower() in DB.strings:
            md_str += '``` \n'
            md_str += DB.strings[entry['ID'].lower()]
            md_str += '\n``` \n'

    return md_str


def get_md(DB, item, key, bibfile, add_comments):
    """
    :param DB: list of dictionary with bibtex
    :param item: list of keywords to search in the DB
    :param key: key to use to search in the DB author/ID/year/keyword...
    :return: a md string with all entries corresponding to the item and keyword
    """

    all_str = ""

    list_entry = {}

    number_of_entries = len(DB.entries)
    for i in range(number_of_entries):
        if key in DB.entries[i].keys():
            if any(elem in DB.entries[i][key] for elem in item):
                str_md = get_md_entry(DB, DB.entries[i], add_comments)
                list_entry.update({str_md:DB.entries[i]['year']})


    sorted_tuple_list = sorted(list_entry.items(), reverse=True, key=lambda x: x[1])
    for elem in sorted_tuple_list:
        all_str += elem[0]

    return all_str


# exemple of full url:
# https://github.com/TLESORT/Automatic_Awesome_Bibliography/blob/master/Mardown_Files/Chronological_Bibliography.md#papers-in-2020
def get_outline(list_classif, url, filename, plot_title_fct):
    str_outline = "## Outline \n"

    full_url = os.path.join(url, "blob", "master", filename)

    for item in list_classif:
        name_section = plot_title_fct(item).replace("## ", "")
        name_section = name_section.replace("(", "").replace(")", "") # it seems that title does not like "("
        name_section = name_section.replace(" ", "-").replace("\n", "")
        str_outline += "- [" + name_section + "](" + full_url + "#" + name_section + ')\n'

    return str_outline


def generate_md_file(DB, list_classif, key, plot_title_fct, filename, url, bibfile, add_comments=True):
    """
    This function generqte the full md file from a bibtex database
    :param DB: list of dictionnary with bibtex
    :param list_classif: list with categories we want to put inside md file
    :param key: key allowing to search in the bibtex dictionary author/ID/year/keyword...
    :param plot_title_fct: function to plot category title
    :param filename: name of the markdown file
    :return: nothing
    """

    all_in_one_str = ""

    # this list will only contains item from list_classif found in DB
    outline_list = []

    for item in list_classif:

        str = get_md(DB, item, key, bibfile, add_comments)

        # if there is something in str we keep create a section with a title
        if str != "":
            outline_list.append(item)
            all_in_one_str += plot_title_fct(item)
            all_in_one_str += str

    str_outline = get_outline(outline_list, url, filename, plot_title_fct)

    all_in_one_str = str_outline + all_in_one_str

    path = os.path.join(filename)
    f = open(path, "w")
    f.write(all_in_one_str)
    f.close()
