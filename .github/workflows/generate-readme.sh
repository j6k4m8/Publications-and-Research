cd posters
mkdir -p thumbnails
for f in *.pdf; do gs -dNOPAUSE -dLastPage=1 -sDEVICE=pngalpha -r70 -sOutputFile=thumbnails/${f%.pdf}.png $f; done
cd ..

cd papers
mkdir -p thumbnails
for f in *.pdf; do gs -dNOPAUSE -dLastPage=1 -sDEVICE=pngalpha -r70 -sOutputFile=thumbnails/${f%.pdf}.png $f; done
cd ..

python3 .github/workflows/make-readme.py > README.md
