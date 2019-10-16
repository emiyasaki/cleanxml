const fs = require('fs');
const es = require('event-stream');

const filename = process.argv[2];
const start = Date.now();
let count = 0;

const ws = fs.createWriteStream(`output${filename}`);
console.log('generating outputfile:', `output${filename}`);
console.log('starting reading file');

fs.createReadStream(filename)
  .pipe(es.split())
  .pipe(
    es
      .mapSync(line => {
        count++;
        let node = `${line}\r\n`;
        if (line.match(/[^ -~\s]+/)) {
        // if (line.match(/\b[0-9A-F]{4}\b/gi)) {
          console.log(`line '${line.trim()}' found - skipping`);
          node = '';
        }
        ws.write(node);
      })
      .on('error', err => {
        console.error('error reading file', err);
        process.exit(1);
        return false;
      })
      .on('end', () => {
        const end = Date.now();
        console.log(`finished reading ${count} lines in ${end - start}ms, closing output file`);
        ws.end();
        return true;
      })
  );
