import glob

page = """\
# Publications & Research

<p align=center>
<a href="https://scholar.google.com/citations?user=QgJ7CPUAAAAJ&hl=en"><img src="https://img.shields.io/badge/Google Scholar-4285F4?logo=Google+Scholar&style=for-the-badge&logoColor=black" /></a>
<a href="https://www.researchgate.net/scientific-contributions/2132435999_Jordan_Matelsky"><img src="https://img.shields.io/badge/ResearchGate-00ccbb?logo=ResearchGate&style=for-the-badge&logoColor=black" /></a>
<a href="https://orcid.org/0000-0002-9470-760X"><img src="https://img.shields.io/badge/ORCID-A6CE39?logo=ORCID&style=for-the-badge&logoColor=black" /></a>
</p>

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

