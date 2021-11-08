# RSA

Dieses Repository enthält eine Implementation des RSA-Algorithmus in Python. Die Implementation dient nur als Beispiel und vernachlässigt deshalb viele sicherheitskritische Aspekte wie das Padding.

Die Implementation des Algorithmus ist unter [rsa/rsa.py](rsa/rsa.py) zu finden.

## Ausführen des Beispiels

In der Datei [example.py](example.py) ist ein kurzes Beispielprogramm enthalten, das ein Schlüsselpaar generiert und eine Nachricht verschlüsselt. Zur Ausführung des Beispiels muss [Python](https://www.python.org/downloads/) installiert sein.

Die Bibliothek [SymPy](https://www.sympy.org/en/index.html) wird für die Primzahlerzeugung benötigt. Diese kann mit dem Befehl `pip install sympy` installiert werden.

Anschließend kann das Beispielprogramm in der Kommandozeile mit `python example.py` ausgeführt werden.

## Quellen
- `isprime` wird von der Bibliothek [SymPy](https://www.sympy.org/en/index.html) importiert
- `extgcd` ist eine adaptierte Version von https://www.inf.hs-flensburg.de/lang/krypto/algo/euklid-erweitert.htm
- `modinv` ist eine adaptierte Version von https://www.inf.hs-flensburg.de/lang/krypto/grund/inverses-element.htm
