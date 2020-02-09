

def keep_last_and_only(str):

  last_author = str.split(" and ")[-1]

  without_and = str.replace(" and ", ", ")

  str_ok = without_and.replace(", " + last_author, " and " + last_author)

  return str_ok

def create_rst_entry(entry):

  rst_entry = ""

  rst_entry += "- `\"" + entry['title']

  if 'url' in entry.keys():
    rst_entry += " <" + entry['url'] + ">"

  rst_entry += "`_" + " by " + keep_last_and_only(entry['author'])

  if 'journal' in entry.keys():
    rst_entry += " *" + entry['journal'] + ", " + entry['volume'] + ":" + entry['pages'] +"*"
  elif 'publisher' in entry.keys():
    rst_entry += " *" + entry['publisher'] +"*"

  rst_entry += ", "+ entry['year']  + ". \n"

  return rst_entry


def get_md_entry(entry):
    md_str = ""
    md_str += "- **" + entry['title'] + "**"

    md_str += ", (" + entry['year'] + ")"

    if 'url' in entry.keys():
        md_str += " [paper](" + entry['url'] + ") "

    md_str += " by *" + keep_last_and_only(entry['author']) + "*"

    md_str += '\n'

    return md_str