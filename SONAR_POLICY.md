# SonarQube Policy — Qualité & Sécurité

## Objectif
Définir une politique DevSecOps claire pour l’utilisation de SonarQube
afin de garantir un niveau de qualité et de sécurité maîtrisé.

---

## Seuils de qualité
- Note minimale acceptée : **B**
- Toute note inférieure bloque le merge
- La dette technique doit être maîtrisée et suivie dans le backlog

---

## Criticité bloquante
Les éléments suivants bloquent automatiquement le pipeline :
- Vulnérabilité critique
- Bug bloquant
- Security hotspot non revu

Les éléments suivants sont informatifs :
- Code smells
- Vulnérabilités mineures

---

## Processus de traitement des alertes
1. Analyse de l’alerte dans SonarQube
2. Création d’une tâche dans le board projet
3. Correction avant merge si bloquant
4. Vérification via CI et SonarQube

---

## Dérogations
- Les dérogations sont possibles uniquement si :
  - Le risque est documenté
  - Le PO et le Security Champion valident
- Aucune dérogation autorisée pour les vulnérabilités critiques

---

## Responsabilités
- Développeurs : correction du code
- QA : validation de la couverture de tests
- Security Champion : arbitrage sécurité
- PO : décision finale sur la livraison
