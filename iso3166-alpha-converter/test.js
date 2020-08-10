const alpha2to3 = require('./build/index.js').alpha2to3
const alpha3to2 = require('./build/index.js').alpha3to2
const assert = require('assert')

assert.strictEqual(alpha2to3["us"], "USA")
assert.strictEqual(alpha3to2["USA"], "us")
Object.keys(alpha2to3).forEach(function(alpha2){
  assert.ok(/^[a-z]{2}$/.test(alpha2))
  assert.ok(/[A-Z]{3}/.test(alpha2to3[alpha2]))
})
Object.keys(alpha3to2).forEach(function(alpha3){
  assert.ok(/^[A-Z]{3}$/.test(alpha3))
  assert.ok(/[a-z]{2}/.test(alpha3to2[alpha3]))
})
