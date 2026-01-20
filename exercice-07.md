# Exercice 7 — Organisation DevSecOps autour de SonarQube

## Objectif
Définir une organisation claire et partagée autour de SonarQube afin
d’exploiter efficacement les analyses de qualité et de sécurité,
sans créer de friction entre les équipes Dev, Ops, QA et Sécurité.

---

## 1. Rôles et responsabilités autour de SonarQube

| Rôle | Responsabilités liées à SonarQube |
|----|----|
| Développeur | Corriger les code smells, bugs mineurs et dette technique détectés par SonarQube |
| QA | Vérifier que les tests couvrent correctement les zones impactées par les alertes |
| Security Champion | Analyser et arbitrer les security hotspots et vulnérabilités |
| Product Owner (PO) | Arbitrer entre qualité, sécurité et délais de livraison |
| Ops / Intégrateur | Assurer l’intégration de SonarQube dans la CI/CD et le respect des quality gates |

📌 Objectif : chaque type d’alerte a un responsable clair, évitant le flou organisationnel.

---

## 2. Gouvernance SonarQube

### Lecture des rapports
- Code Smells : Développeurs
- Bugs : Développeurs + QA
- Security Hotspots : Security Champion
- Vulnérabilités critiques : Sécurité + PO
- Dette technique globale : PO + Tech Lead

### Décision de blocage
- Les **Quality Gates SonarQube** sont intégrés à la CI
- Le merge est bloqué si :
  - Vulnérabilité critique détectée
  - Bug bloquant
  - Note globale < B

### Seuil de qualité accepté
- Note minimale pour livrer : **B**
- Notes acceptables : A ou B
- Notes refusées : C, D, E

---

## 3. Rituels agiles adaptés DevSecOps

| Rituel | Fréquence | Participants | Objectif |
|----|----|----|----|
| Revue SonarQube | Hebdomadaire | Dev, QA, Security Champion | Identifier et prioriser les alertes critiques |
| Daily | Quotidienne | Dev + PO | Vérifier que les PR passent les quality gates |
| Rétrospective qualité | Mensuelle | Équipe entière | Ajuster règles, seuils et pratiques |
| Revue sécurité | Trimestrielle | SecChampion, Ops, PO | Adapter la politique sécurité |

📌 SonarQube devient un outil de pilotage continu, pas un audit ponctuel.

---

## Conclusion
SonarQube n’est efficace que s’il est accompagné d’une organisation claire,
de règles partagées et de rituels réguliers.  
Cette approche permet d’améliorer la qualité et la sécurité sans ralentir
la livraison.
