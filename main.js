const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  // Define o tamanho da viewport
  await page.setViewport({
    width: 1920,
    height: 6000,
  });

  await page.goto('https://abpinturas.pt');

  // Faz o screenshot
  await page.screenshot({ path: 'screenshot.png' });

  await browser.close();
})();
