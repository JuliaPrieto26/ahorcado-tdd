const { Builder, By, Key, until } = require('selenium-webdriver');
const { expect } = require('chai');

describe('LoginTests', function() {
  const driver = new Builder().forBrowser('firefox').build();

  beforeEach(async () => {
    await driver.get('http://localhost:4200');
    await driver.sleep(1000);
  });

  it('should log in successfully', async () => {
    const nombre = 'Juan'
    let input = await driver.findElement(By.id('nameInput'));
    await input.clear();
    await input.click();
    await input.sendKeys(nombre);
    let boton = await driver.findElement(By.id('ingresarButton'));
    await boton.click();

    await driver.sleep(1000);
    const saludo = await driver.findElement(By.xpath('/html/body/app-root/app-new-game/div/h1')).getText();
    expect(saludo).to.equal('Bienvenido, '+nombre);
  });

  it('should throw invalid characters error', async () => {
    const nombre = "Juan??"
    let input = await driver.findElement(By.id('nameInput'));
    await input.clear();
    await input.click();
    await input.sendKeys(nombre);
    let boton = await driver.findElement(By.id('ingresarButton'));
    await boton.click();
    await driver.sleep(1000);
    const errorMessage = await driver.findElement(By.xpath('/html/body/app-root/app-login/div/p')).getText();
    expect(errorMessage).to.equal('El nombre no debe tener caracteres invalidos');
  });

  it('should throw name should not be more than 30 characters long error', async () => {
    const nombre = "juannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn"
    let input = await driver.findElement(By.id('nameInput'));
    await input.clear();
    await input.click();
    await input.sendKeys(nombre);
    let boton = await driver.findElement(By.id('ingresarButton'));
    await boton.click();
    await driver.sleep(1000);
    const errorMessage = await driver.findElement(By.xpath('/html/body/app-root/app-login/div/p')).getText();
    expect(errorMessage).to.equal('El nombre no debe debe tener mas de 30 caracteres');
  });

  after(async () => driver.quit());
})

describe('Partidas', function() {
  // Testear partidas enteras
})
