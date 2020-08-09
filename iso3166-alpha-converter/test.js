const alpha2to3 = require('./build/index.js').alpha2to3
const alpha3to2 = require('./build/index.js').alpha3to2
const assert = require('assert')

assert.strictEqual(alpha2to3["us"], "USA")
assert.strictEqual(alpha3to2["USA"], "us")
Object.keys(alpha2to3).forEach(alpha2=>{
  assert.match(alpha2, /^[a-z]{2}$/)
  assert.match(alpha2to3[alpha2], /[A-Z]{3}/)
})
Object.keys(alpha3to2).forEach(alpha3=>{
  assert.match(alpha3, /^[A-Z]{3}$/)
  assert.match(alpha3to2[alpha3], /[a-z]{2}/)
})
