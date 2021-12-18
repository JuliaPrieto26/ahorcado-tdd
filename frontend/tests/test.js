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

describe('WordToGuessTest', function() {

  const driver = new Builder().forBrowser('firefox').build();

  beforeEach(async () => {
    await driver.get('http://localhost:4200/newgame');
    await driver.sleep(1000);
  });

  it('should throw few characters error', async () => {
    const word = 'Ag'
    let input = await driver.findElement(By.id('wordToGuessInput'));
    await input.clear();
    await input.click();
    await input.sendKeys(word);
    let boton = await driver.findElement(By.id('playButton'));
    await boton.click();


    const errorMessage = await driver.findElement(By.xpath('/html/body/app-root/app-new-game/div/p')).getText();
    expect(errorMessage).to.equal('La palabra debe tener al menos 3 caracteres.');
  });

  it('should throw many characters error', async () => {
    const word = 'Agilessssssssssssssssssssssssssssssssssssss'
    let input = await driver.findElement(By.id('wordToGuessInput'));
    await input.clear();
    await input.click();
    await input.sendKeys(word);
    let boton = await driver.findElement(By.id('playButton'));
    await boton.click();


    const errorMessage = await driver.findElement(By.xpath('/html/body/app-root/app-new-game/div/p')).getText();
    expect(errorMessage).to.equal('La palabra no debe tener más de 20 caracteres.');
  });

  it('should throw many characters error', async () => {
    const word = 'Agiles-'
    let input = await driver.findElement(By.id('wordToGuessInput'));
    await input.clear();
    await input.click();
    await input.sendKeys(word);
    let boton = await driver.findElement(By.id('playButton'));
    await boton.click();


    const errorMessage = await driver.findElement(By.xpath('/html/body/app-root/app-new-game/div/p')).getText();
    expect(errorMessage).to.equal('La palabra no debe contener símbolos.');
  });

  after(async () => driver.quit());
});


describe('GameTest', function() {

  const driver = new Builder().forBrowser('firefox').build();

  beforeEach(async () => {
    await driver.get('http://localhost:4200/newgame');
    await driver.sleep(1000);

    const word = 'Agiles'
    let input = await driver.findElement(By.id('wordToGuessInput'));
    await input.clear();
    await input.click();
    await input.sendKeys(word);
    let boton = await driver.findElement(By.id('playButton'));
    await boton.click();
  });

  it('should throw win game', async () => {
    const word = 'Agiles'
    let input = await driver.findElement(By.id('arriesgarInput'));
    await input.clear();
    await input.click();
    await input.sendKeys(word);
    let boton = await driver.findElement(By.id('arriesgarButton'));
    await boton.click();

    await driver.sleep(1000);

    const winGameMassage = await driver.findElement(By.id('resultado')).getText();
    expect(winGameMassage).to.equal('🔥🔥Felicitaciones, ha ganado la partida.');
  });

  it('should throw game over', async () => {
    const word = 'Agile'
    let input = await driver.findElement(By.id('arriesgarInput'));
    await input.clear();
    await input.click();
    await input.sendKeys(word);
    let boton = await driver.findElement(By.id('arriesgarButton'));
    await boton.click();

    await driver.sleep(1000);

    const GameOverMassage = await driver.findElement(By.id('resultado')).getText();
    expect(GameOverMassage).to.equal('😢Ha perdido la partida.');
  });

  it('should keep playig with error', async () => {
    const letter = 'u'
    let input = await driver.findElement(By.id('arriesgarInput'));
    await input.clear();
    await input.click();
    await input.sendKeys(letter);
    let boton = await driver.findElement(By.id('arriesgarButton'));
    await boton.click();

    await driver.sleep(1000);

    const GameOverMassage = await driver.findElement(By.id('cantidad-errores')).getText();
    expect(GameOverMassage).to.equal('❌ Errores: 1');
  });

  it('should keep playig with ', async () => {
    const letter = 'a'
    let input = await driver.findElement(By.id('arriesgarInput'));
    await input.clear();
    await input.click();
    await input.sendKeys(letter);
    let boton = await driver.findElement(By.id('arriesgarButton'));
    await boton.click();

    await driver.sleep(1000);

    const GameOverMassage = await driver.findElement(By.id('cantidad-aciertos')).getText();
    expect(GameOverMassage).to.equal('✅ Letras acertadas: 1');
  });

  after(async () => driver.quit());
});
