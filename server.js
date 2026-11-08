const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 3000;
const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.mjs': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.gif': 'image/gif',
  '.woff2': 'font/woff2',
  '.woff': 'font/woff',
  '.ttf': 'font/ttf',
  '.mp4': 'video/mp4',
  '.webm': 'video/webm'
};

const server = http.createServer((req, res) => {
  let reqUrl = decodeURI(req.url.split('?')[0]);

  let filePath = path.join(__dirname, reqUrl);

  // If path doesn't exist, check inside cloned_site/
  if (!fs.existsSync(filePath)) {
    let alt = path.join(__dirname, 'cloned_site', reqUrl);
    if (fs.existsSync(alt)) {
      filePath = alt;
    }
  }

  // Security check
  if (!filePath.startsWith(__dirname)) {
    res.statusCode = 403;
    res.end('Forbidden');
    return;
  }

  fs.stat(filePath, (err, stats) => {
    if (err) {
      console.log(`[404] ${req.url}`);
      res.statusCode = 404;
      res.end(`File not found: ${reqUrl}`);
      return;
    }

    if (stats.isDirectory()) {
      filePath = path.join(filePath, 'index_live.html');
      if (!fs.existsSync(filePath)) {
        filePath = path.join(path.dirname(filePath), 'index.html');
      }
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';

    res.writeHead(200, {
      'Content-Type': contentType,
      'Access-Control-Allow-Origin': '*'
    });

    const readStream = fs.createReadStream(filePath);
    readStream.pipe(res);
  });
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`\n======================================================`);
  console.log(`   OXIS LANDING PAGE SERVER RUNNING`);
  console.log(`   http://localhost:${PORT}/`);
  console.log(`======================================================\n`);
});
