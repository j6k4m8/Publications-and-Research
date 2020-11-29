cd posters
mkdir -p thumbnails
for f in *.pdf; do convert -thumbnail x300 -background white -alpha remove "$f" "thumbnails/${f%.pdf}.png"; done
cd ..

cd papers
mkdir -p thumbnails
for f in *.pdf; do convert -thumbnail x300 -background white -alpha remove "$f"[0] "thumbnails/${f%.pdf}.png"; done
cd ..

python3 make-readme.py > README.md