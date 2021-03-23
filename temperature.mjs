import EddystoneBeaconScanner from '@abandonware/eddystone-beacon-scanner'


const filter = [
    'dcc49409b98c'  // ID for Microbit
]

app.get('/temp/:temperature', (req, res) => { 
    console.log(req.params.temperature)
  }) //Should send the data to my bot

EddystoneBeaconScanner.on('found', (beacon) => {
    if (filter.join() && !filter.includes(beacon.id)) return
    console.log('Found: ' + beacon.id + ' - ' + beacon.instance);
    
});

EddystoneBeaconScanner.on('lost', (beacon) => {
    if (filter.join() && !filter.includes(beacon.id)) return
    console.log('lost: ' + beacon.id + ' - ' + beacon.instance);
});

EddystoneBeaconScanner.on('updated', (beacon) => {
    if (filter.join() && !filter.includes(beacon.id)) return
    console.log('updated: ' + beacon.id + ' - ' + parseInt(beacon.in 
        stance, 10));     // reads the Microbit sensors and displaying it in termins

});


EddystoneBeaconScanner.startScanning(true)