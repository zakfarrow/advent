const fs = require('fs')
 
fs.readFile('data/input3.txt', (err, data) => {
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
    for (let y = 0; y <= data.length; y++) {
        if (typeof(data[y]) !== 'undefined' && data[y].includes('£')) {
            var x = data[y].indexOf('£');
            var curr = data[y - 1][x - 1];
            var partNum = '';
            if (curr != '.') {
                var left = data[y - 1][x - 2];
                var right = data[y - 1][x];
                if (left != '.' || left != '£') {
                    partNum = partNum + left + curr;
                    if (data[y - 1][x - 3] != '.' || data[y - 1][x - 3] != '£') {
                        partNum = data[y - 1][x - 3] + partNum;
                    }
                }
            }
        }
    }
    console.log(partsCoords[0]);
}