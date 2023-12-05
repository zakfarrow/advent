const fs = require('fs')
 
fs.readFile('input.txt', (err, data) => {
    if (err) throw err;
    let raw = data.toString();
    formatRaw(raw);
})

function formatRaw(input) {
    let data = input.replace(/[-’/`~!#*$@_%+=,^&(){}[\]|;:”<>?\\]/g, '£');
    let clean = data.replace(/\n/g, '');
    let arr = [];
    let k = 140;
    for (let i = 0; i <= 140; i++) {
        arr[i] = clean.substring(i*k, (i*k) + k);
    }
    findParts(arr);
}

function findParts(data) {
    let partsCoords = []; 
    for (let i = 0; i <= data.length; i++) {
        if (typeof(data[i]) !== 'undefined' && data[i].includes('£')) {
            var index = data[i].indexOf('£');
            if (data[i][index + 1] != '.') {
                partsCoords.push([i, index + 1]);
            }
            if (data[i][index - 1] != '.') {
                partsCoords.push([i, index - 1]);
            }
            if (data[i - 1][index - 1] != '.') {
                partsCoords.push([i - 1, index - 1]);
            }
            if (data[i - 1][index] != '.') {
                partsCoords.push([i - 1, index]);
            }
            if (data[i - 1][index + 1] != '.') {
                partsCoords.push([i - 1, index + 1]);
            }
            if (data[i + 1][index - 1] != '.') {
                partsCoords.push([i + 1, index - 1]);
            }
            if (data[i + 1][index] != '.') {
                partsCoords.push([i + 1, index]);
            }
            if ([i + 1][index + 1] != '.') {
                partsCoords.push([i + 1, index + 1]);
            }
        }
    }
    console.log(data[0]);
}