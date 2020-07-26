const icons = require('./build/index.js')
const assert = require('assert')

assert.deepEqual(icons["GBP"], {
  "name": "British pound",
  "symbol": "\u00a3",
  "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAABmklEQVR4nO2Yu07DMBRAjxEvqUViASExwg8AEwMrAxs7A0LiE5jYgN9gYOAPkFj4hLAgsTMxdOMhxCPCDAk0ctKk2A65DT6SJdtN3XvsOn4orTVtYKzpAHwRRKQRRKQRRKQRRKQRRKQRRKTRGpFx2y8qpaoemQZ2gC1gFZhLf+8BuANugCvgMq0DwPpYobW2ShVsAveAHiK9AKfAlFM8NYhsA3FBwJ/A2wCZyLljPYvMA49GkGfAGv2/8QywDhwC1+kz+9JEjg2Jk7KhS1kBOq4iynZyDZjsEUnvAzwBCyRzYGhs4/H9+l3K5CN+KeGCb5HZTL7nue1S6lwQ4xrbztGalT2ISKM1Iq7ryLNR3cnkY5ItSRlds8I6HkcR1xvw3KoqZUFsDFcRZaQs5wWflz3vRBgRaQSRAiaM8ofHtivxKbJolEd297tslG89tl2JT5G9TP4VuPDYdjWezuwbwDv9s/rBn8fjKDIJ7JLsub6vfI5wWOyaunzokdwg/sSB2zm9O6qbxlyz/37TaN0D0mjNiAQRaQQRaXwBRNRkVL2UJc0AAAAASUVORK5CYII="
})
