const express = require('express');
const { spawn } = require('child_process');
const app = express();

let chartBase64 = '';
// Middleware untuk file statis
app.use(express.static('public'));

// Route untuk halaman utama
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/views/index.html');
});

// Route untuk mendapatkan gambar pie chart
app.get('/chart', (req, res) => {
    const pythonProcess = spawn('python', ['./generate_chart.py']);
    let data = '';
    pythonProcess.stdout.on('data', (chunk) => {
        data += chunk.toString();
    });
    pythonProcess.on('close', (code) => {
        if (code === 0) {
            chartBase64 = data;
            console.log('Base64 Data:', data); // Cek log ini
            res.send(`<img src="data:image/png;base64,${data}" />`);
        } else {
            res.status(500).send('Error generating chart');
        }
    });
});

// Jalankan server
app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
