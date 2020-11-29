import glob

page = """

# Publications & Research



- [Google Scholar](https://scholar.google.com/citations?user=QgJ7CPUAAAAJ&hl=en)
- [ResearchGate](https://www.researchgate.net/scientific-contributions/2132435999_Jordan_Matelsky)
- [ORCID](https://orcid.org/0000-0002-9470-760X)

For a complete CV, see [here](https://jordan.matelsky.com/resume/).

"""

image_template = "<a href='{}'><img src={} width='250' /></a>&nbsp;"

page += "## Papers\n\n"

for paper in glob.glob("papers/thumbnails/*.png"):
    page += image_template.format(
        paper.replace("thumbnails/", "").replace(".png", ".pdf"), paper
    )

page += "\n\n## Posters\n\n"

for poster in glob.glob("posters/thumbnails/*.png"):
    page += image_template.format(
        poster.replace("thumbnails/", "").replace(".png", ".pdf"), poster
    )


print(page)

