# -*- coding: utf-8 -*-
import unicodedata
def extract_hash_tags(s):
    return set(part[1:] for part in s.split() if part.startswith('#'))

def extract_mentions(s):
    return set(part[1:] for part in s.split() if part.startswith('@'))

def strip_accents(s):
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))