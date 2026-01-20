# Security Policy

## Objectif
Ce projet applique une politique DevSecOps visant à détecter et bloquer
l’introduction de vulnérabilités connues dans les dépendances Python.

## Outil utilisé
- pip-audit (audit des dépendances Python via CVE publiques)

## Niveaux de gravité
Les vulnérabilités sont classées selon les niveaux suivants :
- LOW
- MEDIUM
- HIGH
- CRITICAL

## Politique de blocage
- HIGH : ❌ bloquant
- CRITICAL : ❌ bloquant
- LOW / MEDIUM : ⚠️ informatif (à corriger si possible)

Toute dépendance contenant une vulnérabilité HIGH ou CRITICAL
bloque automatiquement le pipeline CI.

## Procédure de correction
1. Identifier la dépendance vulnérable dans le rapport pip-audit
2. Mettre à jour la dépendance vers une version corrigée
3. Vérifier le correctif localement
4. Relancer le pipeline CI

## Responsabilités
- Développeur : mise à jour des dépendances
- SecChampion / équipe sécurité : validation des exceptions éventuelles

## Exceptions
Les exceptions doivent être documentées et justifiées.
Aucune dépendance critique vulnérable ne doit être déployée en production.
