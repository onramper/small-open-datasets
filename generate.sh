mkdir -p pages
npm run build
node build/build.js
node build/mergePages.js
npm run build
