Wynik live codingu z PyLightKrk #2

Mała aplikacja we Flask-u, którą napisaliśmy razem na meetingu ;-)

Jak uruchomić aplikację i się nią pobawić:

1) Upewnić się, że mamy PostgreSql, jeżeli chcesz korzystać z innej bazy nie ma sprawy ;-)
2) Załóż bazę <code>todo</code>, lub jakąkolwiek inną ... grunt to odpowiednio zmienić config w pliku <code>/project/\__init__.py</code>
3) Stwórz virtual_env-a <code>python3 -m venv venv</code>
4) zainstaluj potrzebne paczki <code>pip install -r requirments.txt</code>
5) <code>flask run</code> - uruchomi aplikację
6) <code>flask db init</code> - zainicjalizuje bazę
7) <code>flask db migrate</code> - sprawdzi czy modele się nie zmieniły
8) <code>flask db upgrade</code> - dokona migracji bazy 
9) pobaw się kodem, dopracuj ... jest wiele miejsc, które można tu dopracować jeżeli przysiądzie się na więcej niż 50 min ... czyli tyle w ile ją napisaliśmy na meetingu
