

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

def get_md_entry(entry):
    """
    Generate a markdown line for a specific entry
    :param entry: entry dictionary
    :return: markdown string
    """
    md_str = ""
    md_str += "- **" + entry['title'] + "**"

    md_str += ", (" + entry['year'] + ")"

    if 'url' in entry.keys():
        md_str += " [paper](" + entry['url'] + ") "

    md_str += " by *" + keep_last_and_only(entry['author']) + "*"

    md_str += '\n'

    return md_str


def get_md(DB, item, key):
    """

    :param DB: list of dictionary with bibtex
    :param item: list of keywords to search in the DB
    :param key: key to use to search in the DB author/ID/year/keyword...
    :return: a md string with all entries corresponding to the item and keyword
    """

    all_str = ""

    number_of_entries = len(DB)
    for i in range(number_of_entries):
        if key in DB[i].keys():
            if any(elem in DB[i][key] for elem in item):
                all_str += get_md_entry(DB[i])

    return all_str


def generate_md_file(DB, list_classif, key, plot_title_fct, filename):
    """

    :param DB: list of dictionnary with bibtex
    :param list_classif: list with categories we want to put inside md file
    :param key: key allowing to search in the bibtex dictionary author/ID/year/keyword...
    :param plot_title_fct: function to plot category title
    :param filename: name of the markdown file
    :return: nothing
    """

    all_in_one_str = ""

    for item in list_classif:

        str = get_md(DB, item, key)

        if str != "":
            all_in_one_str += plot_title_fct(item)
            all_in_one_str += str

    f = open(filename, "w")
    f.write(all_in_one_str.encode('utf8'))
    f.close()