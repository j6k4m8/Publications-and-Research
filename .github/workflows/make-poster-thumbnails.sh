for f in ../../posters/*.pdf; do convert -thumbnail x300 -background white -alpha remove "$f" "thumb/${f%.pdf}.png"; done
