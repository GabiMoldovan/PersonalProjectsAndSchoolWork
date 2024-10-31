var express = require('express');
var mysql = require('mysql');
var bodyParser = require('body-parser');
var bcrypt = require('bcrypt');
var app = express();
var port = 3000;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Configurare conexiune la baza de date MySQL
var db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'password',
    database: 'motoshop_db'
});

// Conectare la baza de date MySQL
db.connect(function(err) {
    if (err) {
        throw err;
    }
    console.log('Conectat la baza de date MySQL');
});

// Ruta pentru înregistrare (register)
app.post('/register', function(req, res) {
    var username = req.body.username;
    var email = req.body.email;
    var password = req.body.password;

    bcrypt.hash(password, 10, function(err, hash) {
        if (err) {
            console.log(err);
            res.status(500).send('Eroare la inregistrare');
        } else {
            var user = { username: username, email: email, password: hash };
            // Adăugare utilizator în baza de date
            db.query('INSERT INTO users SET ?', user, function(err, result) {
                if (err) {
                    console.log(err);
                    res.status(500).send('Eroare la inregistrare');
                } else {
                    console.log('Utilizator inregistrat cu succes');
                    res.status(200).send('Utilizator inregistrat cu succes');
                }
            });
        }
    });
});

// Ruta pentru autentificare (login)
app.post('/login', function(req, res) {
    var username = req.body.username;
    var password = req.body.password;

    // Cautare utilizator în baza de date
    db.query('SELECT * FROM users WHERE username = ?', username, function(err, result) {
        if (err) {
            console.log(err);
            res.status(500).send('Eroare la autentificare');
        } else {
            if (result.length > 0) {
                var hashedPassword = result[0].password;

                // Comparare parola introdusa cu parola hash stocata
                bcrypt.compare(password, hashedPassword, function(err, match) {
                    if (err) {
                        console.log(err);
                        res.status(500).send('Eroare la autentificare');
                    } else if (match) {
                        console.log('Autentificare reusita');
                        res.status(200).send('Autentificare reusita');
                    } else {
                        console.log('Autentificare esuata. Parola incorecta.');
                        res.status(401).send('Autentificare esuata. Parolă incorecta.');
                    }
                });
            } else {
                console.log('Autentificare esuata. Utilizator inexistent.');
                res.status(401).send('Autentificare esuata. Utilizator inexistent.');
            }
        }
    });
});

// Pornire server
app.listen(port, function() {
    console.log("Serverul asculta la http://localhost:${port}");
});
