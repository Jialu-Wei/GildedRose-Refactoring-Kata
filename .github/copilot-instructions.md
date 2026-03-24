# Copilot Instructions

## Project Overview
This is the Gilded Rose Refactoring Kata implemented in Python. The project uses the Strategy design pattern to handle different item update behaviors.

## Architecture
- python/gilded_rose.py — Item class, strategy classes, and GildedRose main class.
- python/tests/test_gilded_rose.py — Unit tests using unittest.
- python/tests/test_gilded_rose_approvals.py — Approval tests.

## Business Rules
- quality is never negative and never exceeds 50 (except Sulfuras, always 80).
- sell_in decreases by 1 each day (except Sulfuras).
- Normal items degrade by 1; after expiry, by 2.
- Aged Brie increases in quality by 1 each day.
- Backstage passes increase by 1 (>10 days), by 2 (6-10 days), by 3 (1-5 days), drop to 0 after concert.
- Conjured items degrade twice as fast as normal items.
- Sulfuras never changes.

## Coding Conventions
- Python 3, PEP 8, unittest for tests.
- Preserve the Strategy pattern. Do NOT revert to nested if/else.
- Do not modify the Item class.
