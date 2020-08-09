const icons = require('./build/index.js')
const assert = require('assert')

assert.strictEqual(icons["GBP"].name, "British pound")
assert.strictEqual(icons["GBP"].symbol, "\u00a3")
const iconStart = "data:image/png;base64,"
assert.strictEqual(icons["GBP"].icon.substr(0, iconStart.length), iconStart)
