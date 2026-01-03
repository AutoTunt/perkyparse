# perkyparse
agent tools for eq browsin

This is a Flask API that fetches a character's class and gear from the Perky Crew CharBrowser, then recommends upgrades from a local SQLite item database.

## Endpoint

POST `/recommend-upgrades`

```json
{
  "characterName": "YourCharName"
}