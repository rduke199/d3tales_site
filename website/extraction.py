import os
import glob
from docx import Document
from pathlib import Path
#import importlib
#import sys
#importlib.reload(sys)
#sys.setdefaultencoding('utf8')

base_path = Path(__file__).resolve().parent.parent
static_path = os.path.join(base_path, 'website', 'static', 'website')

"""
Extract text from text files in text/ directory. 
"""


def get_text(file_name):
    text_path = os.path.join(static_path, 'text', file_name)
    with open(text_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


"""
Extract profile info from directories and files in profiles/ directory
"""


def get_member_image(name, category):
    image_string = "/static/website/profiles/{}/{}/me.png".format(category, name)
    # return os.path.abspath(image_string)
    return image_string


def get_member_university(name, category):
    file_path = os.path.join(static_path, 'profiles', category, name, 'university.txt')
    with open(file_path, "r", encoding='utf-8') as f:
        description = f.read()
    return description


def get_member_about(name, category):
    file_path = os.path.join(static_path, 'profiles', category, name, 'about.txt')
    with open(file_path, "r") as f:
        description = f.read()
    return description


def get_group_website(name, category):
    file_path = os.path.join(static_path, 'profiles', category, name, 'group_website.txt')
    with open(file_path, "r") as f:
        description = f.read()
    return description


def get_members(category):
    file_path = os.path.join(static_path, 'profiles', category)
    os.chdir(file_path)
    members_data = []
    for member in glob.glob("*"):
        try:
            print(member)
            info = {"name": member,
                    "about": get_member_about(member, category),
                    "image": get_member_image(member, category),
                    "university": get_member_university(member, category)
                    }
            members_data.append(info)
            if category == "PIs_SeniorPersonnel":
                info["group_website"] = get_group_website(member, category)
            else:
                pass
            return members_data
        except:
            return None


"""
Extract publication info from publication=/ directory 
"""


def journal_articles():
    document = Document("{}/static/pages/publication/publications.docx".format(base_path))
    paragraphs = document.paragraphs
    articles = []
    for para in paragraphs:
        text = para.text.strip().split("\t")[1]
        citation = text.split("DOI:")[0].strip()
        try:
            doi = text.split("DOI:")[-1].strip()
            d = {"citation": citation, "doi": "https://doi.org/" + doi}
        except:
            d = {"citation": citation}
            pass
        articles.append(d)

    return articles
