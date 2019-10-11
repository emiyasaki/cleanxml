# cleanxml
Simple nodejs CLI to strip lines with non printable characters from a large XML file.

It uses `event-stream` to read a line at a time so we won't suffer from memory issues.

Not the fastest solution (it reads and writes an output file of 2M lines in 4s), but it works. Eventually I'll try Python and PowerShell script.

As usual, don't forget to

```javascript
npm install
```

Then, you can 
```javascript
node index [filename]
```
It will create a new file as `output[filename]`