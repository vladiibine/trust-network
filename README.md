# trust-network
first version of o site which allows people to manage their trust in news sources and leaders of opinion

Also, i copied the frontend part from github.com/davezuko/deact-redux-starter-kit ! these starter kits are awesome, I should make some

Install
=======
$ npm install

Compile as static files
=======================
# Will generate a ./dist folder, filled with the static assets to just serve
# This runs linter, tests, cleans dist folder, and compiles
$ npm run deploy:prod
# This just compiles
$ npm run compile

Test
====
$ npm run test

Lint
====
$ npm run lint

Run
===
# This is the original, native way (with built-in http server)
$ npm run dev
# This runs the compiled assets. Port 3000 is important, as it's hardcoded in some assets, and specified in a config file
$ cd ./dist
$ pythom -m SimpleHTTPServer 3000

