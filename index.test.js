const icons = require('./build/index.js')
const assert = require('assert')

assert.strictEqual(icons["GBP"].name, "British pound")
assert.strictEqual(icons["GBP"].symbol, "\u00a3")
assert.strictEqual(icons["GBP"].icon.startsWith("data:image/png;base64,"), true)
