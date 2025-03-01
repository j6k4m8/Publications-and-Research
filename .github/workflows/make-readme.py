import csv
import glob

page = """\
<h1 align=center>Publications & Research</h1>

<p align=center>
<a href="https://scholar.google.com/citations?user=QgJ7CPUAAAAJ&hl=en"><img src="https://img.shields.io/badge/Google Scholar-4285F4?logo=Google+Scholar&style=for-the-badge&logoColor=black" /></a>
<a href="https://www.researchgate.net/scientific-contributions/2132435999_Jordan_Matelsky"><img src="https://img.shields.io/badge/ResearchGate-00ccbb?logo=ResearchGate&style=for-the-badge&logoColor=black" /></a>
<a href="https://orcid.org/0000-0002-9470-760X"><img src="https://img.shields.io/badge/ORCID-A6CE39?logo=ORCID&style=for-the-badge&logoColor=black" /></a>
</p>

For a complete CV, see [here](https://jordan.matelsky.com/resume/).

"""

PAPERS_COLUMN_COUNT = 4  # how many papers to a row
POSTERS_COLUMN_COUNT = 3  # how many posters to a row
TALKS_COLUMN_COUNT = 3  # how many talks to a row

image_template = (
    "<td width='250'><a href='{}'><img src={} /><br /><small>{}</small></a></td>"
)


def extract_details(fpath: str):
    """
    Return year, title, and link.
    """
    fname = fpath.split("/")[-1]
    year = fname.split("_")[0]
    title = " ".join(fname.split("_")[1:]).replace("-", " ").replace(".png", "")
    return (year, title, fpath)


def generate_document_template(fpath):
    year, title, link = extract_details(fpath)
    return image_template.format(
        link.replace("thumbnails/", "").replace(".png", ".pdf"),
        link,
        f"{title} ({year})",
    )


def _is_youtube_link(link_text: str) -> bool:
    """
    Determines if a link is a YouTube link.
    """
    return "youtube.com" in link_text.lower()


def create_thumbnail_for_video(link_text: str) -> str:
    if _is_youtube_link(link_text):
        return (
            f"<img src='http://img.youtube.com/vi/{link_text.split('?v=')[1]}/0.jpg' />"
        )
    return "<img />"


def generate_talk_template(talk_dict):
    """
    The talk dict contains Title,Year,Venue,Link key-vals.
    """
    # we need to generate a thumbnail, link URL, and title:
    title = f"{talk_dict['Title']} ({talk_dict['Venue']} {talk_dict['Year']})"
    link = talk_dict["Link"]
    thumbnail = create_thumbnail_for_video(talk_dict["Link"])

    return f"<td><a href='{link}'>{thumbnail}<br /><small>{title}</small></a></td>"


################################################################################ PAPERS

page += "## Papers\n\n"

papers = sorted(glob.glob("papers/thumbnails/*.png"), reverse=True)

page += "<table>"
for i in range(0, len(papers), PAPERS_COLUMN_COUNT):
    page += (
        "<tr>"
        + "".join(
            [
                generate_document_template(paper)
                for paper in papers[i : min(i + PAPERS_COLUMN_COUNT, len(papers))]
            ]
        )
        + "</tr>"
    )
page += "</table>"

################################################################################ POSTERS

page += "\n\n## Posters\n\n"

posters = sorted(glob.glob("posters/thumbnails/*.png"), reverse=True)

page += "<table>"
for i in range(0, len(posters), POSTERS_COLUMN_COUNT):
    page += (
        "<tr>"
        + "".join(
            [
                generate_document_template(paper)
                for paper in posters[i : min(i + POSTERS_COLUMN_COUNT, len(posters))]
            ]
        )
        + "</tr>"
    )
page += "</table>"

################################################################################ TALKS

page += "\n\n## Talks\n\n"


def read_csv(filename):
    with open(filename, "r") as f:
        file_data = csv.reader(f)
        headers = next(file_data)
        return [dict(zip(headers, i)) for i in file_data]


talks = read_csv("talks/talks.csv")

page += "<table>"
for i in range(0, len(talks), TALKS_COLUMN_COUNT):
    page += (
        "<tr>"
        + "".join(
            [
                generate_talk_template(talk)
                for talk in talks[i : min(i + TALKS_COLUMN_COUNT, len(talks))]
            ]
        )
        + "</tr>"
    )
page += "</table>"


page += """

---

### About this repository

This repository automatically updates this README with thumbnails and links when a PDF is uploaded to the Posters or Papers directories. To make a repo like this for yourself, fork this repository, or add the `.github/workflows` directory to your own project.

"""

print(page)
