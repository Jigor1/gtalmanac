// usage: node render.js preview 0.5 6.6 ...     -> prev/f_<t>.png
//        node render.js video narration.mp3 [out.mp4]
//        node render.js cover <t> [cover.png]      (no captions)
//        node render.js capcheck                    -> lists caption chunks that wrap to 2 lines
let pw; try { pw = require('playwright'); } catch (e) { pw = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright'); }
const { spawn } = require('child_process'); const { once } = require('events'); const fs = require('fs'); const path = require('path');
const [mode, ...args] = process.argv.slice(2);
(async () => {
  const b = await pw.chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  pg.on('pageerror', e => console.log('PAGEERR:', e.message));
  await pg.goto('file://' + path.resolve('page.html'));
  await pg.waitForFunction(() => window.READY === true, null, { timeout: 30000 });
  if (mode === 'preview') {
    fs.mkdirSync('prev', { recursive: true });
    for (const t of args.map(Number)) { await pg.evaluate(t => render(t), t); await pg.screenshot({ path: `prev/f_${t.toFixed(2)}.png` }); }
  } else if (mode === 'cover') {
    await pg.evaluate(t => render(t, { cover: true }), Number(args[0] || 6.6)); await pg.screenshot({ path: args[1] || 'cover.png' });
  } else if (mode === 'capcheck') {
    const caps = JSON.parse(fs.readFileSync('captions.json')); let bad = 0;
    for (const c of caps) {
      const h = await pg.evaluate(t => { render(t); return document.getElementById('cap').offsetHeight; }, (c.s + c.e) / 2);
      if (h > 130) { bad++; console.log('2 LINES at ' + c.s.toFixed(2) + 's: ' + c.toks.map(k => k.t).join(' ')); }
    }
    console.log(bad ? bad + ' chunk(s) wrap - split them in chunks.txt' : 'captions ok: every chunk fits on one line');
  } else if (mode === 'video') {
    const FPS = 30, DUR = await pg.evaluate(() => window.DUR), N = Math.ceil(DUR * FPS);
    const ff = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-', '-i', args[0],
      '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-r', String(FPS),
      '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-shortest', '-movflags', '+faststart', args[1] || 'out.mp4'], { stdio: ['pipe', 'inherit', 'inherit'] });
    const t0 = Date.now();
    for (let f = 0; f < N; f++) {
      await pg.evaluate(t => render(t), f / FPS);
      const buf = await pg.screenshot({ type: 'jpeg', quality: 95 });
      if (!ff.stdin.write(buf)) await once(ff.stdin, 'drain');
      if (f % 300 === 0) console.log(`frame ${f}/${N} ${((Date.now() - t0) / 1000).toFixed(0)}s`);
    }
    ff.stdin.end(); await once(ff, 'close'); console.log('done', ((Date.now() - t0) / 1000).toFixed(0) + 's');
  }
  await b.close();
})();
