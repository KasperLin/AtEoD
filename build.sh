# GitHub Pages deployment requires:
# ./docs directory for html
# ./docs/.nojekyll file for not using jekyll
make html
cp -r build/html/* docs