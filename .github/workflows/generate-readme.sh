cd posters
mkdir -p thumbnails
for f in *.pdf; do gs -dNOPAUSE -dLastPage=1 -sDEVICE=pngalpha -r70 -sOutputFile=thumbnails/${f%.pdf}.png $f; done
#for f in *.pdf; do convert -thumbnail x400 -background white -alpha remove "$f" "thumbnails/${f%.pdf}.png"; done
cd ..

cd papers
mkdir -p thumbnails
for f in *.pdf; do gs -dNOPAUSE -dLastPage=1 -sDEVICE=pngalpha -r70 -sOutputFile=thumbnails/${f%.pdf}.png $f; done
#for f in *.pdf; do convert -thumbnail x400 -background white -alpha remove "$f"[0] "thumbnails/${f%.pdf}.png"; done
cd ..

python3 .github/workflows/make-readme.py > README.md
