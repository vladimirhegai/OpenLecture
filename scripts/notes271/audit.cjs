// Render all nine live notes, expand solutions, check math/images, and capture figures.
const fs = require('fs');
const path = require('path');
const { chromium } = require('../../frontend/node_modules/playwright-core');
(async () => {
  const root=__dirname, out=path.join(root,'../../tmp/notes271/ui');
  fs.mkdirSync(out,{recursive:true});
  const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
  const page=await browser.newPage({viewport:{width:1320,height:1000},deviceScaleFactor:1});
  const errors=[], report=[];
  page.on('pageerror',e=>errors.push(e.message));
  page.on('response',r=>{if(r.status()>=400)errors.push(`${r.status()} ${r.url()}`)});
  for(let n=1;n<=9;n++){
    const key=String(n).padStart(2,'0');
    const raw=JSON.parse(fs.readFileSync(path.join(root,'out',`${key}-published.json`),'utf8'));
    const doc=raw.document || raw;
    await page.goto(`http://127.0.0.1:8000/courses/${doc.course_id}/docs/${doc.document_id}`,{waitUntil:'networkidle'});
    await page.locator('.document, .note-page, .blocks').first().waitFor({timeout:1000}).catch(()=>{});
    await page.waitForFunction(()=>document.querySelectorAll('main .katex, .problem').length>0);
    const closed=await page.locator('details:not([open])').count();
    await page.evaluate(()=>document.querySelectorAll('details').forEach(d=>d.open=true));
    await page.waitForFunction(()=>[...document.querySelectorAll('.schematic')].every(f=>f.querySelector('img') || f.classList.contains('broken')));
    const result=await page.evaluate(()=>({
      mathErrors:[...document.querySelectorAll('.katex-error')].map(e=>e.textContent),
      broken:[...document.querySelectorAll('.schematic.broken')].map(e=>e.textContent),
      images:[...document.querySelectorAll('.schematic img')].every(e=>e.complete && e.naturalWidth>0),
      overflow:[...document.querySelectorAll('.katex-display, .mt-eq')].filter(e=>e.scrollWidth>e.clientWidth+3).map(e=>e.textContent),
    }));
    report.push({n,title:doc.title,closedSolutions:closed,...result});
    await page.screenshot({path:path.join(out,`${key}-top.png`)});
    const figures=page.locator('.schematic');
    for(let i=0;i<await figures.count();i++){
      await figures.nth(i).scrollIntoViewIfNeeded();
      await figures.nth(i).screenshot({path:path.join(out,`${key}-figure-${i}.png`)});
    }
    console.log(key,JSON.stringify(result));
  }
  fs.writeFileSync(path.join(out,'audit.json'),JSON.stringify({report,errors},null,2));
  await browser.close();
  if(errors.length || report.some(r=>r.mathErrors.length || r.broken.length || !r.images || r.overflow.length))process.exitCode=1;
})();
