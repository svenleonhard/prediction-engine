# Prediction Engine

Die Prediction-Engine realisiert diverse Algorithmen zur Abfahrtsprognose im Karlsruher Verkehrsverbund (KVV). Das Repository ist im Rahmen der Studienarbeit Abfahrtsprognose im ÖPNV enstanden.
Das Projekt ermöglicht das Anaylsieren und Bewerten verschiedener Prognosealgorithmen. Darüber hinaus können mit geringem Aufwand weitere Prognosealgorithmen hinzugefügt werden.
Die Prognosen finden auf Basis einzelner Linien statt. Das bedeutet, dass in jeder Analyse jeweils nur eine Linie isoliert betrachtet wird.
Eine Verwendung der Prognosen ist nur mit der entsprechenden Datengrundlage sinnvoll. Diese kann aus rechtlichen Gründen nicht veröffentlicht werden.
Detailierte Informatioen zu den Prognosealgorithmen finden sich in der Studienarbeit Abfahrtsprognose im ÖPNV.

## Inhalt
[Vorraussetzungen](#vorraussetzungen)

[Installation](#installation)

[Nutzung](#nutzung)

[Implementierte Prognosealgorithmen](#implementierte-prognosealgorithmen)

[Hinzufügen eines neuen Vorhersagemodells](#hinzufügen-eines-neuen-vorhersagemodells)

## Vorraussetzungen
1. Python 3.8.1 oder höher

## Installation
Vor der ersten Prognose muss eine Datenbank mit der Datengrundlage entsprechend der folgenden Anleitung bereitgestellt werden. Anschließend müssen die Abhängigkeiten aus der `requirements.txt` Datei installiert werden.

### Aufsetzen einer eigenen Datenbank auf einem Server oder einem lokalen Computer
1. Installation einer MySQL Datenbank
2. Download der historischen Daten
3. Starten der Datenbank
3. Import der historischen Daten

Ist die Datenbank installiert, müssen die Zugangsdaten hinterlegt werden.
1. Öffnen der Zugangsdaten Datei => `database/credentials.yaml`
2. Eintragen der Zugangsdaten im Block *remote*

## Nutzung
Das Projekt ist dafür gedacht verschiedene Prognosealgorithmen zu analysieren. In der folgenden Anleitung wird beispielhaft erläutert, wie der k-Nächste-Nachbar Algorithmus für die Linie 1 von Durlach nach Oberreut analysiert werden kann

1. Eine Linie für die Prognose wählen. Hierfür werden zwei Informationen benötigt. Zunächst sollte die gewünschte Linien-ID (`Line.line_id`) aus dem Datenbestand der Plattform zur Störungsanalyse entnommen werden. Anschließend muss die zur gewählten Linie passende Linien-Referenz(`line_ref`) aus dem Open Data Paket entommen werden. Das System unterscheidet zwischen `line_id` und `line_id_official`. Bei der `line_id` handelt es sich um die Linien-ID aus der Plattform zu Störungsanaylse. Die `line_id_official` entspricht der Linien-ID wie sie in der TRIAS-Schnittstelle und dem Open DAta Paket des KVVs zu finden ist.
2. Falls die Linie zum ersten Mal gewählt wird, die Fahrten-IDs zur Linie berechnen   
2.1 Stelle sicher, dass die Fahrzeiten der gewählten Linie korrekt sind. Dies kann in der Tabelle TripSections geprüft werden > `SELECT * FROM TripSections WHERE line_id = 18.`   
2.2 Öffne die Quellcodedatei `journey_id_calculation.py`   
2.3 Gebe der Konstanden LINE den Wert der gewählten Linien-ID aus der Plattform zur Störungsanalyse   
2.4 Starte das Skript > `python journey_id_calculation.py`   
3. Öffne die Quellcodedatei `prediction/run_general_knn.py`   
4. Gebe der Konstanden LINE den Wert der gewählten Linien-ID aus der Plattform zur Störungsanalyse   
5. Starte das Skript vom Wurzelverzeichnis > `python prediction/run_general_knn.py`   
6. Die Analyse des Algorithmus läuft. Ist sie beendet, wird ein Bericht auf der Konsole gedruckt.

###Prognosealgorithmen
- k-Nearest-Neighbour Regression > `python prediction/run_general_knn_regression.py`
- k-Nearest-Neighbour Klassifikation> `python prediction/run_general_knn_class.py`
- k-Nearest-Neighbour Eigenentwicklung > `python prediction/rrun_cutsom_knn.py`
- Support Vector Regression > `python prediction/run_svr_regression.py`
- Support Vector Machine (Klassifikation) > `python prediction/run_svm_classification.py`
- Neuonales Netz > `python prediction/run_neural_network.py`
- Kombnierte Ansätze > `python prediction/run_combined.py`

### ML_Service API

Neben der Nutzung eines Skripts besteht die Möglichkeit die ML_Service API zu nutzten. Diese stellt für jeden Prognosealgorithmus einen Methodenaufruf zur Verfügung. Das folgende Beispiel zeigt den Aufruf für den k-Nächsten-Nachbar und der Linien-ID 18 (Linie 1 von Durlach nach Oberreut):

```python
from machine_learning.services.ml_service import MLService
MLService().general_knn_regression(line_id=LINE, line_id_official=LINE_OFFICIAL)
```

- k-Nearest-Neighbour Regression > `MLService().general_knn_regression(line_id, line_id_official)`
- k-Nearest-Neighbour Klassifikation> `MLService().general_knn_class(line_id, line_id_official)`
- k-Nearest-Neighbour Eigenentwicklung > `custom_knn(line_id, line_id_official)`
- Support Vector Regression > `MLService().svr(line_id, line_id_official):`
- Support Vector Machine (Klassifikation) > `MLService().travel_time_class_svm(line_id, line_id_official)`
- Neuonales Netz > `MLService().travel_time_neural_network_for(line_id, line_id_official)`
- Kombnierte Ansätze > `combined_prediction(line_id, line_id_official)`

## Hinzufügen eines neuen Vorhersagemodells

1. Entwicklung eines Prognosealgorithmus.
2. Implementierung der folgenden Schnittstelle (implizit):

```python
class Prognose(object):

    def train(self, eingabe_traingsdaten, ausgabe_traingsdaten)
        # Training des Modells
    
    def predict(self, liste_mit_eingaben):
        # Prognose berechnen
        return lsite_mit_ausgaben
```

3. Prognosealgorithmus im IoC Container hinzufügen => Folgende Codezeilen in die Quellcode Datei `machine_learning/ioc_container.py` einfügen:

```python
# Import der Prognose-Klasse nicht vergessen
from machine_learning.prediction_util import PredictionUtil
from machine_learning.model.report import Report

prognose = providers.Factory(Prognose)
prognose_werkzeug = providers.Factory(PredictionUtil, predictor=prognose, report=Report)
```

4. Methode im ML_Service erstellen
```python
    def prognose(self, line_id):
        self.ioc_container.prediction_util_knn_class().analyse(self.data_loader_travel_time, line_id, line_id_official)
```

5. Die erstellte Methode in einem Skript aufrufen > `MLService().prognose(line_id=18, line_id_official='kvv:21001:E:H')`
