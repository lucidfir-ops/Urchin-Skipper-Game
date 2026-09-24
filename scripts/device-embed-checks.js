import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { readFileSync, existsSync, statSync, writeFileSync } from 'node:fs';
import { resolve, extname } from 'node:path';

export async function deviceEmbedChecks(browser) {
  const root = resolve('dist'),
    prefix = '/uploads/device-update/',
    errors = [],
    missing = [];
  const server = createServer((req, res) => {
    const path = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
    if (path === '/favicon.ico') {
      res.writeHead(204).end();
      return;
    }
    if (path === '/play') {
      res.setHeader('Content-Type', 'text/html');
      res.end(
        `<html><body style="margin:0"><iframe allow="fullscreen;autoplay;gamepad" allowfullscreen src="http://localhost:${server.address().port}${prefix}index.html" style="border:0;width:100vw;height:100vh"></iframe></body></html>`,
      );
      return;
    }
    const file = resolve(root, path.slice(prefix.length));
    if (
      !path.startsWith(prefix) ||
      !file.startsWith(root + '/') ||
      !existsSync(file) ||
      !statSync(file).isFile()
    ) {
      missing.push(path);
      res.writeHead(404).end();
      return;
    }
    res.setHeader(
      'Content-Type',
      {
        '.html': 'text/html',
        '.js': 'text/javascript',
        '.css': 'text/css',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.svg': 'image/svg+xml',
      }[extname(file)] || 'application/octet-stream',
    );
    res.end(readFileSync(file));
  });
  await new Promise((done) => server.listen(0, '127.0.0.1', done));
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 }, hasTouch: true });
  page.on('pageerror', (e) => errors.push(e.message));
  try {
    await page.goto(`http://127.0.0.1:${server.address().port}/play`);
    let frame = await page
      .locator('iframe')
      .elementHandle()
      .then((el) => el.contentFrame());
    await frame.waitForFunction(() => window.urchinDebug?.ui);
    await frame.locator('[data-fullscreen]').click();
    await frame.waitForFunction(() => !!document.fullscreenElement);
    await frame.locator('[data-logging]').click();
    await frame.locator('#keyboardFallback').click();
    await frame.getByRole('button', { name: 'Skip day 0 · choose my boat', exact: true }).click();
    await frame.getByRole('button', { name: /Choose Harbour Workhorse/ }).click();
    await frame.locator('[data-action="buy-selected"]').click();
    await frame.locator('[data-action="confirm-purchase"]').click();
    for (let n = 0; n < 4; n++) {
      await frame.locator('[data-action="workshop"]').click();
      await frame
        .getByRole('button', { name: 'Channel Master · controls showcase', exact: true })
        .click();
      await frame.waitForFunction(
        () => urchinDebug.world.career.trainingReplay && !urchinDebug.ui.screen,
      );
      assert.match(await frame.locator('#frankAboard').innerText(), /Channel Master/);
      assert(!/\{(?:pivot|thrust)/.test(await frame.locator('#frankAboard').innerText()));
      await frame.locator('[data-intro="skip"]').click();
      await frame.waitForFunction(() => urchinDebug.ui.screen === 'harbour');
    }
    await frame.evaluate(() => urchinDebug.ui.showTitle());
    await frame.locator('[data-fullscreen]').click();
    await frame.waitForFunction(() => !document.fullscreenElement);
    await page.reload();
    frame = await page
      .locator('iframe')
      .elementHandle()
      .then((el) => el.contentFrame());
    await frame.waitForFunction(() => window.urchinDebug?.ui);
    assert.match(await frame.locator('[data-logging]').innerText(), /ON/);
    await frame.evaluate(() => {
      window.hostUnlockCalls = 0;
      const unlock = screen.orientation.unlock.bind(screen.orientation);
      screen.orientation.unlock = () => {
        window.hostUnlockCalls++;
        return unlock();
      };
    });
    await page.evaluate(() => {
      const launch = document.createElement('button');
      launch.id = 'host-launch';
      launch.textContent = 'Launch embedded game';
      launch.style.cssText = 'position:fixed;top:0;left:0;z-index:99999';
      launch.onclick = () => document.querySelector('iframe').requestFullscreen();
      document.body.append(launch);
    });
    await page.locator('#host-launch').click();
    await page.waitForFunction(() => document.fullscreenElement?.tagName === 'IFRAME');
    await frame.locator('[data-touch-options]').tap();
    await frame.waitForFunction(() => window.hostUnlockCalls > 0);
    await frame.locator('.screen-back').click();
    await page.evaluate(() => document.exitFullscreen());
    for (const viewport of [
      { width: 402, height: 873 },
      { width: 873, height: 402 },
    ]) {
      await page.setViewportSize(viewport);
      // Playwright cannot resize Chromium's native fullscreen window. Resize the
      // host first, then verify host-owned fullscreen at each orientation.
      await page.locator('#host-launch').click();
      await page.waitForFunction(() => document.fullscreenElement?.tagName === 'IFRAME');
      await frame.waitForFunction(
        ({ width, height }) => innerWidth === width && innerHeight === height,
        viewport,
      );
      await page.evaluate(() => document.exitFullscreen());
    }
    await page.locator('#host-launch').evaluate((el) => el.remove());
    await frame.waitForTimeout(300);
    const downloadPromise = page.waitForEvent('download');
    await frame.getByRole('button', { name: 'Download troubleshooting log', exact: true }).click();
    const download = await downloadPromise;
    await download.saveAs('test-results/september20-troubleshooting-download.txt');
    assert.match(
      readFileSync('test-results/september20-troubleshooting-download.txt', 'utf8'),
      /launch: Page loaded/,
    );
    assert.match(
      readFileSync('test-results/september20-troubleshooting-download.txt', 'utf8'),
      /viewport:/,
    );
    await page.screenshot({ path: 'test-results/sep20-embedded-title.png' });
    assert.deepEqual(errors, []);
    assert.deepEqual(missing, []);
    writeFileSync(
      'test-results/sep20-embed.json',
      JSON.stringify(
        {
          errors,
          missing,
          trainingReloads: 4,
          fullscreen: true,
          hostFullscreenInBothOrientations: true,
          logDownload: true,
        },
        null,
        2,
      ),
    );
    console.log(
      'PASS: cross-origin nested hosting, fullscreen in/out, four Channel Master replays, persisted optional log download.',
    );
  } finally {
    await page.close();
    server.close();
    server.closeAllConnections();
  }
}
