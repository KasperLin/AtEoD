# GitHub Pages deployment requires:
# ./docs directory for html
# ./docs/.nojekyll file for not using jekyll
make html
rm -rf docs/*
cp -r build/html/* docs