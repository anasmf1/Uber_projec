      // Vérifier l'état de l'API
  function checkStatus() {
    fetch('/status')
      .then(response => response.json())
      .then(data => {
        // Affiche le SVG et le message dans la div #testResult
        document.getElementById('testResult').style.display = 'block';
        document.getElementById('testResult').querySelector('h1').textContent = data.message;
      })
      .catch(error => console.error('Error:', error));
  }

      }

      // Fonction pour obtenir une prédiction (si nécessaire pour l'autre partie de votre application)
      function getPrediction() {
        // Récupérer les valeurs des champs d'entrée
        const data = {
            passeng: parseInt(document.getElementById('PASS').value),
            ann: parseInt(document.getElementById('Year').value),
            mois: parseInt(document.getElementById('Month').value),
            jour: parseInt(document.getElementById('Day').value),
            heure: parseInt(document.getElementById('hour').value),
            dist: parseFloat(document.getElementById('distance').value)
        };
    
        // Envoi de la requête POST vers l'API Flask pour la prédiction
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            // Affichage du résultat de la prédiction
            document.getElementById('prediction-result').innerText = "Predicted Fare: $" + data.prediction;
        })
        .catch(error => {
            console.error('Erreur:', error);
            document.getElementById('prediction-result').innerText = "Error: Unable to fetch prediction.";
        });
    }

      // Exemple d'utilisation (un clic sur le bouton vérifier l'état de l'API)
      checkHealth(); // Vérifie l'état de l'API dès le début si nécessaire