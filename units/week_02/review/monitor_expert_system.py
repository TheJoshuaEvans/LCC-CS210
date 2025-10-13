# =========================================================
# Program: Lab 2 - Monitor Expert System
# Author: Trevor Leadon
# Date: October 2025
# Version: 1.0
# IDE: VS Code / IDLE
# Description:
#   A simple expert system using forward chaining to recommend
#   computer monitors based on user preferences.
# =========================================================

import csv

def load_rules(filename):
    rules = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=['IF1', 'IF2', 'THEN', 'GOAL'])
        for row in reader:
            rules.append(row)
    return rules

def forward_chain(facts, rules):
    new_facts = set(facts)
    added = True

    while added:
        added = False
        for rule in rules:
            if rule['IF1'] in new_facts and (not rule['IF2'] or rule['IF2'] in new_facts):
                if rule['THEN'] and rule['THEN'] not in new_facts:
                    new_facts.add(rule['THEN'])
                    added = True
    return new_facts

def main():
    print("=== Monitor Recommendation Expert System ===")
    rules = load_rules('monitor_rules.csv')

    facts = set()
    if input("Do you want a high refresh rate monitor (yes/no)? ").lower() == 'yes':
        facts.add('high_refresh')
    if input("Do you care more about resolution or speed? ").lower() == 'resolution':
        facts.add('high_resolution')
    else:
        facts.add('fast_response')
    if input("Do you want a large monitor (yes/no)? ").lower() == 'yes':
        facts.add('large_screen')
    if input("Are you on a budget (yes/no)? ").lower() == 'yes':
        facts.add('budget')

    results = forward_chain(facts, rules)

    print("\n--- Recommendations ---")
    for fact in results:
        if fact.startswith('recommend'):
            print(f"- {fact.replace('_', ' ')}")
    print("------------------------")

if __name__ == "__main__":
    main()
