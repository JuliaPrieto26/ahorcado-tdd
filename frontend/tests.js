const {webdriver, Builder, By, Key, until} = require('selenium-webdriver');
var test = require('selenium-webdriver/testing')
const assert = require('assert');

let driver;

describe('PortfolioTests', function() {
  before(function *() {
    driver = new Builder().forBrowser('firefox').build();
  });

  it('01 Drums Access', function() {
    driver.get("https://andreidbr.github.io/JS30/");
    driver.findElement(By.xpath('/html/body/div[2]/div[1]')).click();
    driver.getTitle().then(function(title) {
        assert.equal(title, "JS30: 01 Drums");
    });
  });

  after(() => driver.quit());
});
